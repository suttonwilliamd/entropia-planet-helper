import copy
import io
import json
import socket
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

from planet_helper.__main__ import main
from planet_helper.data import load_dataset, validate_doc
from planet_helper.ranking import AVAILABLE, BLOCKED, COOLDOWN, DONE, ranked, score_of, status_of
from planet_helper.store import Progress

FIX = Path(__file__).parent / "fixtures" / "planets"
ALPHA = json.loads((FIX / "alpha.json").read_text(encoding="utf-8"))
NOW = datetime(2026, 11, 26, 12, 0, tzinfo=timezone.utc)


def errors_after(mutate):
    doc = copy.deepcopy(ALPHA)
    mutate(doc)
    return validate_doc(doc).errors


class SchemaTests(unittest.TestCase):
    def test_fixture_is_valid(self):
        self.assertEqual(validate_doc(ALPHA).errors, [])

    def test_rejects_uncited_and_broken_citations(self):
        self.assertTrue(any("needs at least one sourceId" in e
                            for e in errors_after(lambda d: d["activities"][0].update(sourceIds=[]))))
        self.assertTrue(any("unknown source id" in e
                            for e in errors_after(lambda d: d["activities"][0].update(sourceIds=["S9"]))))
        self.assertTrue(any("url must be http" in e
                            for e in errors_after(lambda d: d["sources"][0].update(url="file:///c:/x"))))

    def test_waypoint_rules(self):
        def bad_format(d):
            d["activities"][0]["locations"][0]["waypoint"] = "Alpha 100 200"
        def verified_without_source(d):
            d["activities"][0]["locations"][0]["sourceIds"] = []
        self.assertTrue(any("not like" in e for e in errors_after(bad_format)))
        self.assertTrue(any("needs sourceIds" in e for e in errors_after(verified_without_source)))

    def test_enum_scores_and_cooldowns(self):
        self.assertTrue(errors_after(lambda d: d["activities"][0].update(stage="endgame")))
        self.assertTrue(errors_after(lambda d: d["activities"][0]["score"].update(value=9)))
        self.assertTrue(any("rolling cooldown needs" in e for e in
                            errors_after(lambda d: d["activities"][2]["cooldown"].update(hours=None))))
        self.assertTrue(errors_after(lambda d: d["activities"][0].update(prerequisites=["alpha-start"])))

    def test_dataset_reports_dangling_cross_file_prereq(self):
        with tempfile.TemporaryDirectory() as tmp:
            beta = json.loads((FIX / "beta.json").read_text(encoding="utf-8"))
            Path(tmp, "beta.json").write_text(json.dumps(beta), encoding="utf-8")
            ds = load_dataset(Path(tmp))
            self.assertTrue(any("does not exist in any file" in e for e in ds.errors))

    def test_invalid_file_is_skipped_not_half_loaded(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "alpha.json").write_text(json.dumps(ALPHA), encoding="utf-8")
            Path(tmp, "broken.json").write_text("{not json", encoding="utf-8")
            ds = load_dataset(Path(tmp))
            self.assertEqual(list(ds.planets), ["alpha"])
            self.assertTrue(ds.errors)


class RankingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.p = Progress(Path(self.tmp.name))
        self.ds = load_dataset(FIX)
        self.acts = {a["id"]: a for a in self.ds.activities.values()}

    def tearDown(self):
        self.tmp.cleanup()

    def test_prerequisites_block_until_done_even_across_planets(self):
        self.assertEqual(status_of(self.acts["alpha-next"], self.p, NOW).state, BLOCKED)
        self.assertEqual(status_of(self.acts["beta-cross"], self.p, NOW).missing, ("alpha-start",))
        self.p.mark_done("alpha-start", NOW)
        self.assertEqual(status_of(self.acts["alpha-start"], self.p, NOW).state, DONE)
        self.assertEqual(status_of(self.acts["alpha-next"], self.p, NOW).state, AVAILABLE)
        self.assertEqual(status_of(self.acts["beta-cross"], self.p, NOW).state, AVAILABLE)

    def test_rolling_cooldown_and_ready_again(self):
        a = self.acts["alpha-daily"]
        self.p.mark_done(a["id"], NOW)
        st = status_of(a, self.p, NOW + timedelta(hours=19))
        self.assertEqual((st.state, st.ready_at), (COOLDOWN, NOW + timedelta(hours=20)))
        self.assertEqual(status_of(a, self.p, NOW + timedelta(hours=20)).state, AVAILABLE)
        self.p.mark_done(a["id"], NOW)
        self.p.ready_again(a["id"])
        self.assertEqual(status_of(a, self.p, NOW).state, AVAILABLE)
        self.assertTrue(self.p.ever_done(a["id"]))  # still satisfies prerequisites

    def test_fixed_utc_reset(self):
        a = self.acts["alpha-fixed"]
        self.p.mark_done(a["id"], NOW)  # 12:00 UTC -> resets next 00:00 UTC
        st = status_of(a, self.p, NOW + timedelta(hours=11))
        self.assertEqual(st.ready_at, datetime(2026, 11, 27, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(status_of(a, self.p, NOW + timedelta(hours=12)).state, AVAILABLE)

    def test_order_and_explanations(self):
        rows = ranked(list(self.acts.values()), self.p, "arrival", False, NOW)
        self.assertEqual(rows[0][0]["id"], "alpha-start")       # best value, available
        states = [r[1].state for r in rows]
        self.assertEqual(states, sorted(states, key=[AVAILABLE, COOLDOWN, BLOCKED, DONE].index))
        late, _ = score_of(self.acts["alpha-late"], "arrival")
        late_here, why = score_of(self.acts["alpha-late"], "late")
        self.assertLess(late, late_here)                         # stage penalty
        self.assertIn("confidence low", why)
        cheap = self.acts["alpha-start"]
        self.assertGreater(score_of(self.acts["alpha-late"], "late", False)[0],
                           score_of(self.acts["alpha-late"], "late", True)[0])  # budget mode punishes pricey
        self.assertEqual(score_of(cheap, "arrival", True)[0], score_of(cheap, "arrival", False)[0])


class PersistenceTests(unittest.TestCase):
    def test_round_trip_and_settings(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Progress(Path(tmp))
            p.mark_done("alpha-start", NOW)
            p.set_setting("planet", "alpha")
            q = Progress(Path(tmp))
            self.assertEqual(q.last_done("alpha-start"), NOW)
            self.assertEqual(q.settings["planet"], "alpha")
            q.undo("alpha-start")
            self.assertFalse(Progress(Path(tmp)).ever_done("alpha-start"))
            self.assertEqual([f.name for f in Path(tmp).iterdir()], ["progress.json"])  # no temp files left

    def test_corrupt_file_is_kept_aside_not_deleted(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "progress.json").write_text("{oops", encoding="utf-8")
            p = Progress(Path(tmp))
            self.assertEqual(p.records, {})
            self.assertTrue(p.recovered_from and p.recovered_from.read_text(encoding="utf-8") == "{oops")


class EntryPointTests(unittest.TestCase):
    def run_main(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = main(list(args))
        return code, out.getvalue() + err.getvalue()

    def test_check_and_unknown_planet(self):
        code, out = self.run_main("--data-dir", str(FIX), "--check")
        self.assertEqual(code, 0, out)
        self.assertIn("alpha", out)
        code, out = self.run_main("--data-dir", str(FIX), "--planet", "nowhere")
        self.assertEqual(code, 2)

    def test_gui_builds_offline_switches_planets_and_persists(self):
        import tkinter as tk
        from planet_helper.app import PlanetHelperApp

        def no_network(*a, **k):
            raise AssertionError("network access attempted")

        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(socket, "socket", no_network), \
                mock.patch.object(socket, "create_connection", no_network):
            try:
                root = tk.Tk()
            except tk.TclError as exc:
                self.skipTest(f"no display: {exc}")
            root.withdraw()  # never shown: no focus stealing
            try:
                progress = Progress(Path(tmp))
                app = PlanetHelperApp(root, load_dataset(FIX), progress, "beta")
                self.assertEqual(app.planet.get(), "beta")
                self.assertIn("Beta Fixture", root.title())
                app.planet_box.current(app.planet_ids.index("alpha"))
                app._pick_planet()
                self.assertEqual(app.tree.selection()[0], "alpha-start")   # top-ranked first
                app.mark_done()
                self.assertTrue(Progress(Path(tmp)).ever_done("alpha-start"))
                self.assertEqual(Progress(Path(tmp)).settings["planet"], "alpha")
                app.query.set("daily")
                self.assertTrue(all("daily" in iid for iid in app.tree.get_children()))
                app.query.set("")
                app.view.set("Done")
                app.refresh()
                self.assertEqual(app.tree.get_children(), ("alpha-start",))
            finally:
                root.destroy()


if __name__ == "__main__":
    unittest.main()
