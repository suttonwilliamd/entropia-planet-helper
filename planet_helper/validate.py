"""Command-line validator: python -m planet_helper.validate FILE_OR_DIR [...]"""
from __future__ import annotations

import sys
from pathlib import Path

from .data import load_dataset, load_file


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if not args:
        args = [str(Path(__file__).resolve().parent.parent / "data" / "planets")]
    failed = False
    for arg in args:
        p = Path(arg)
        if p.is_dir():
            ds = load_dataset(p)
            reports = ds.reports
        else:
            reports = [load_file(p)[1]]
        for rep in reports:
            status = "OK " if rep.ok else "BAD"
            print(f"{status} {rep.path}  ({len(rep.errors)} errors, {len(rep.warnings)} warnings)")
            for e in rep.errors:
                print(f"   error: {e}")
            for w in rep.warnings:
                print(f"   warn:  {w}")
            failed |= not rep.ok
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
