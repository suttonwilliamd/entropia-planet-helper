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
        finally:
            root.destroy()


if __name__ == "__main__":
    unittest.main()
