"""Checks on the real shipped data and the real entry point."""
import io
import subprocess
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from planet_helper.__main__ import main
from planet_helper.data import load_dataset

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "planets"


class RealDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ds = load_dataset(DATA)

    def test_all_files_valid_and_loaded(self):
        self.assertEqual(self.ds.errors, [])
        self.assertEqual(len(self.ds.planets), len(list(DATA.glob("*.json"))))
        self.assertGreaterEqual(len(self.ds.planets), 5)

    def test_aris_is_present_and_substantial(self):
        aris = self.ds.planets["aris"]
        self.assertEqual(aris["planet"]["name"].upper(), "ARIS")
        self.assertGreaterEqual(len(aris["activities"]), 5)

    def test_every_activity_has_dated_http_source(self):
        for pid, doc in self.ds.planets.items():
            srcs = {s["id"]: s for s in doc["sources"]}
            for a in doc["activities"]:
                self.assertTrue(a["sourceIds"], a["id"])
                for sid in a["sourceIds"]:
                    self.assertTrue(srcs[sid]["url"].startswith("http"), (pid, sid))
                    self.assertTrue(srcs[sid]["accessed"], (pid, sid))

    def test_readme_cites_every_source_url(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        missing = [s["url"] for d in self.ds.planets.values() for s in d["sources"] if s["url"] not in readme]
        self.assertEqual(missing, [])
        res = subprocess.run([sys.executable, str(ROOT / "scripts" / "gen_readme_sources.py"), "--check"],
                             capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)


class SetP1AdjustedTests(unittest.TestCase):
    """The entry William's friend needed: the confirmed dependency and the stuck-player path."""

    @classmethod
    def setUpClass(cls):
        cls.ds = load_dataset(DATA)
        cls.act = cls.ds.activities["setesh-set-p1-adjusted"]
        cls.srcs = {s["id"]: s for s in cls.ds.planets["setesh"]["sources"]}

    def test_cliffchaser_run_dependency_is_official_and_blocking(self):
        import tempfile
        from datetime import datetime, timezone
        from planet_helper.ranking import AVAILABLE, BLOCKED, status_of
        from planet_helper.store import Progress
        self.assertEqual(self.act["prerequisites"], ["setesh-cliffchaser-run"])
        pi = self.act["prereqInfo"]
        self.assertIn("forum.entropiauniverse.com/t/entropia-universe-19-12-0-release-notes/853664",
                      " ".join(self.srcs[s]["url"] for s in pi["sourceIds"]))
        self.assertTrue(pi["unknowns"])                       # Thule etc. stated as unknown, not guessed
        now = datetime(2026, 11, 26, tzinfo=timezone.utc)
        with tempfile.TemporaryDirectory() as d:
            p = Progress(Path(d))
            self.assertEqual(status_of(self.act, p, now).state, BLOCKED)
            p.mark_done("setesh-cliffchaser-run", now)
            self.assertEqual(status_of(self.act, p, now).state, AVAILABLE)

    def test_diagnostics_and_pins(self):
        symptoms = " ".join(d["symptom"] for d in self.act["diagnostics"]).lower()
        for needed in ("paul", "already have", "leave setesh", "thule"):
            self.assertIn(needed, symptoms)
        self.assertFalse(any(l["verified"] for l in self.act["locations"]))      # Nexus pin is not in-game verified
        chain = self.ds.activities["setesh-a-new-arrival-chain"]
        self.assertTrue(all(l["waypoint"] is None for l in chain["locations"]))  # no Harkov pin (sources disagree)
        raw = (DATA / "setesh.json").read_text(encoding="utf-8")
        self.assertNotIn("69257", raw)

    def test_old_small_iron_progress_carries_over(self):
        self.assertEqual(self.ds.former_ids.get("setesh-cliffchaser-small-iron"), "setesh-set-p1-adjusted")


class EntryPointTests(unittest.TestCase):
    def test_exact_aris_entry_point_in_check_mode(self):
        out = io.StringIO()
        with redirect_stdout(out):
            code = main(["--planet", "aris", "--check"])
        self.assertEqual(code, 0, out.getvalue())
        self.assertIn("startup destination: aris", out.getvalue())

    def test_module_launch_offline_subprocess(self):
        # Same command the shortcut runs (python instead of pythonw), in check mode.
        res = subprocess.run([sys.executable, "-m", "planet_helper", "--planet", "aris", "--check"],
                             cwd=ROOT, capture_output=True, text=True, timeout=60)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)

    def test_gui_opens_on_aris(self):
        import tempfile
        import tkinter as tk
        from planet_helper.app import PlanetHelperApp
        from planet_helper.store import Progress
        try:
            root = tk.Tk()
        except tk.TclError as exc:
            self.skipTest(f"no display: {exc}")
        root.withdraw()
        try:
            with tempfile.TemporaryDirectory() as tmp:
                prog = Progress(Path(tmp))
                prog.set_setting("planet", "calypso")          # a saved choice must not beat the flag
                app = PlanetHelperApp(root, load_dataset(DATA), prog, "aris")
                self.assertEqual(app.planet.get(), "aris")
                self.assertIn("ARIS", root.title().upper())
                self.assertTrue(app.tree.get_children())
                for pid in app.planet_ids:                       # every destination renders
                    app.planet_box.current(app.planet_ids.index(pid))
                    app._pick_planet()
                    app.view.set("Everything")
                    app.refresh()
                    self.assertEqual(len(app.tree.get_children()), len(app.ds.planets[pid]["activities"]), pid)
                    app.show_about()                                 # destination cautions + sources render
                    text = app.detail.get("1.0", "end")
                    for w in app.ds.planets[pid]["planet"]["warnings"]:
                        self.assertIn(w[:40], text)
                # William's path: Destination Setesh -> Show Everything -> search "gun" -> SET-P1 entry
                app.planet_box.current(app.planet_ids.index("setesh"))
                app._pick_planet()
                app.view.set("Everything")
                app.query.set("gun")
                self.assertIn("setesh-set-p1-adjusted", app.tree.get_children())
                app.tree.selection_set("setesh-set-p1-adjusted")
                app.show_detail()
                text = app.detail.get("1.0", "end")
                for needed in ("Stuck? Check these in order", "Cliffchaser Run", "Partly known", "Not known yet"):
                    self.assertIn(needed, text)
                self.assertEqual(app.tree.set("setesh-set-p1-adjusted", "status"), "Blocked")
        finally:
            root.destroy()


if __name__ == "__main__":
    unittest.main()
