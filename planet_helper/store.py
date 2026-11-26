"""Local-only progress storage. One JSON file in the user's profile folder; nothing leaves the machine."""
from __future__ import annotations

import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

STORE_VERSION = 1


def default_profile_dir() -> Path:
    env = os.environ.get("EPH_PROFILE_DIR")
    if env:
        return Path(env)
    base = os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Local")
    return Path(base) / "entropia-planet-helper"


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat(timespec="seconds")


class Progress:
    """Per-activity record: {"last": iso-UTC or None, "count": int}.

    - count > 0 means "done at least once" (satisfies prerequisites).
    - last is the moment the user last marked it done; cooldowns run from it.
    - "Ready again" clears last but keeps count. "Undo" removes the record entirely.
    """

    def __init__(self, profile_dir: Path | None = None):
        self.dir = Path(profile_dir) if profile_dir else default_profile_dir()
        self.path = self.dir / "progress.json"
        self.records: dict[str, dict] = {}
        self.settings: dict = {}
        self.recovered_from: Path | None = None
        self._load()

    def _load(self) -> None:
        if not self.path.exists():
            return
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
            if not isinstance(raw, dict) or not isinstance(raw.get("done", {}), dict):
                raise ValueError("unexpected layout")
            self.records = {
                k: {"last": v.get("last"), "count": int(v.get("count", 1))}
                for k, v in raw.get("done", {}).items()
                if isinstance(v, dict)
            }
            self.settings = raw.get("settings", {}) if isinstance(raw.get("settings"), dict) else {}
        except (OSError, ValueError, TypeError, AttributeError):
            # Keep the damaged file for the user instead of deleting it, then start clean.
            backup = self.path.with_name(f"progress.corrupt-{utcnow():%Y%m%d-%H%M%S}.json")
            try:
                os.replace(self.path, backup)
                self.recovered_from = backup
            except OSError:
                pass
            self.records, self.settings = {}, {}

    def save(self) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        payload = {"version": STORE_VERSION, "done": self.records, "settings": self.settings}
        fd, tmp = tempfile.mkstemp(prefix="progress.", suffix=".tmp", dir=self.dir)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                json.dump(payload, fh, indent=2, sort_keys=True)
            os.replace(tmp, self.path)
        except BaseException:
            try:
                os.unlink(tmp)
            except OSError:
                pass
            raise

    # --- queries -------------------------------------------------------
    def ever_done(self, activity_id: str) -> bool:
        return self.records.get(activity_id, {}).get("count", 0) > 0

    def last_done(self, activity_id: str) -> datetime | None:
        last = self.records.get(activity_id, {}).get("last")
        if not last:
            return None
        try:
            dt = datetime.fromisoformat(last)
        except ValueError:
            return None
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)

    # --- mutations (each saves immediately) ------------------------------
    def mark_done(self, activity_id: str, when: datetime | None = None) -> None:
        rec = self.records.setdefault(activity_id, {"last": None, "count": 0})
        rec["last"] = _iso(when or utcnow())
        rec["count"] += 1
        self.save()

    def ready_again(self, activity_id: str) -> None:
        if activity_id in self.records:
            self.records[activity_id]["last"] = None
            self.save()

    def undo(self, activity_id: str) -> None:
        if self.records.pop(activity_id, None) is not None:
            self.save()

    def set_setting(self, key: str, value) -> None:
        if self.settings.get(key) != value:
            self.settings[key] = value
            self.save()
