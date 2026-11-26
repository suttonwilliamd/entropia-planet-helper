"""Entry point: python -m planet_helper [--planet aris] [--check]"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .data import load_dataset
from .store import Progress, default_profile_dir

DEFAULT_DATA = Path(__file__).resolve().parent.parent / "data" / "planets"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="entropia-planet-helper", description="Offline guide to the best next "
                                 "unlocks, missions and dailies on each Entropia Universe destination.")
    ap.add_argument("--planet", help="destination id to open first, e.g. aris (you can switch in the app)")
    ap.add_argument("--data-dir", type=Path, default=DEFAULT_DATA, help="folder of destination JSON files")
    ap.add_argument("--profile-dir", type=Path, default=None,
                    help=f"where progress is saved (default {default_profile_dir()})")
    ap.add_argument("--check", action="store_true", help="load and validate everything, print a summary, no window")
    ap.add_argument("--version", action="version", version=__version__)
    args = ap.parse_args(argv)

    ds = load_dataset(args.data_dir)
    planet = args.planet.lower() if args.planet else None
    if planet and planet not in ds.planets:
        print(f"Unknown destination {args.planet!r}. Known: {', '.join(sorted(ds.planets))}", file=sys.stderr)
        return 2

    if args.check:
        for pid in sorted(ds.planets):
            doc = ds.planets[pid]
            print(f"{pid:18} {doc['planet']['status']:10} {len(doc['activities']):3} activities "
                  f"{len(doc['sources']):3} sources  reviewed {doc['planet']['lastReviewed']}")
        for err in ds.errors:
            print("ERROR", err)
        if not ds.planets:
            print("ERROR no destination files loaded")
        start = planet or ("aris" if "aris" in ds.planets else None)
        print(f"startup destination: {start}")
        return 1 if ds.errors or not ds.planets else 0

    for err in ds.errors:
        print("data error (file skipped):", err, file=sys.stderr)
    from .app import run  # imported late so --check works without a display
    run(ds, Progress(args.profile_dir), planet)
    return 0


if __name__ == "__main__":
    sys.exit(main())
