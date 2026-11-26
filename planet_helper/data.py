"""Load and validate destination data files (see docs/DATA_SCHEMA.md)."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

SCHEMA_VERSION = 1
PLANET_KINDS = {"planet", "moon", "space", "instance", "event", "special"}
PLANET_STATUS = {"active", "seasonal", "inactive", "unverified"}
SOURCE_KINDS = {"official", "official-forum", "wiki", "community-guide", "forum", "video"}
ACTIVITY_TYPES = {"unlock", "mission-chain", "mission", "daily", "repeatable", "event", "travel", "skill", "tip"}
STAGES = ("arrival", "early", "mid", "late")
MARKUP = {"none", "low", "medium", "high", "unknown"}
CURRENCY_USE = {"earned", "spent", "kept"}
COOLDOWN_KINDS = {"none", "once", "rolling", "fixed-reset", "unknown"}
CONFIDENCE = {"high", "medium", "low"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
WAYPOINT_RE = re.compile(r"^\[[^,\[\]]+(,\s*-?\d+(\.\d+)?){3}(,[^\[\]]*)?\]$")


@dataclass
class Report:
    path: str
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def _req(obj: dict, key: str, typ, where: str, rep: Report, allow_none: bool = False):
    if key not in obj:
        rep.errors.append(f"{where}: missing '{key}'")
        return None
    val = obj[key]
    if val is None and allow_none:
        return None
    if not isinstance(val, typ) or (typ is int and isinstance(val, bool)):
        rep.errors.append(f"{where}: '{key}' should be {getattr(typ, '__name__', typ)}")
        return None
    return val


def _enum(val, allowed, where: str, key: str, rep: Report):
    if val is not None and val not in allowed:
        rep.errors.append(f"{where}: '{key}'={val!r} not in {sorted(allowed)}")


def _str_list(obj: dict, key: str, where: str, rep: Report) -> list:
    val = _req(obj, key, list, where, rep)
    if val is None:
        return []
    for i, v in enumerate(val):
        if not isinstance(v, str) or not v.strip():
            rep.errors.append(f"{where}: {key}[{i}] must be a non-empty string")
    return val


def validate_doc(doc, path: str = "<memory>") -> Report:
    rep = Report(path)
    if not isinstance(doc, dict):
        rep.errors.append("top level must be an object")
        return rep
    if doc.get("schemaVersion") != SCHEMA_VERSION:
        rep.errors.append(f"schemaVersion must be {SCHEMA_VERSION}")

    planet = _req(doc, "planet", dict, "file", rep) or {}
    pid = _req(planet, "id", str, "planet", rep)
    if pid and not ID_RE.match(pid):
        rep.errors.append(f"planet: id {pid!r} must be a lowercase slug")
    _req(planet, "name", str, "planet", rep)
    _enum(_req(planet, "kind", str, "planet", rep), PLANET_KINDS, "planet", "kind", rep)
    _req(planet, "parent", str, "planet", rep, allow_none=True)
    _enum(_req(planet, "status", str, "planet", rep), PLANET_STATUS, "planet", "status", rep)
    _req(planet, "summary", str, "planet", rep)
    _req(planet, "howToReach", str, "planet", rep)
    lr = _req(planet, "lastReviewed", str, "planet", rep)
    if lr and not DATE_RE.match(lr):
        rep.errors.append("planet: lastReviewed must be YYYY-MM-DD")
    _str_list(planet, "warnings", "planet", rep)
    planet_srcs = _str_list(planet, "sourceIds", "planet", rep)

    sources = _req(doc, "sources", list, "file", rep) or []
    src_ids: set[str] = set()
    for i, s in enumerate(sources):
        w = f"sources[{i}]"
        if not isinstance(s, dict):
            rep.errors.append(f"{w}: must be an object")
            continue
        sid = _req(s, "id", str, w, rep)
        if sid:
            if sid in src_ids:
                rep.errors.append(f"{w}: duplicate source id {sid!r}")
            src_ids.add(sid)
        _req(s, "title", str, w, rep)
        url = _req(s, "url", str, w, rep)
        if url and not url.startswith(("https://", "http://")):
            rep.errors.append(f"{w}: url must be http(s)")
        _req(s, "publisher", str, w, rep)
        _enum(_req(s, "kind", str, w, rep), SOURCE_KINDS, w, "kind", rep)
        pub = _req(s, "published", str, w, rep, allow_none=True)
        if pub and not DATE_RE.match(pub):
            rep.errors.append(f"{w}: published must be YYYY-MM-DD or null")
        acc = _req(s, "accessed", str, w, rep)
        if acc and not DATE_RE.match(acc):
            rep.errors.append(f"{w}: accessed must be YYYY-MM-DD")
        _req(s, "supports", str, w, rep)

    def check_src_refs(ids, where):
        for sid in ids:
            if sid not in src_ids:
                rep.errors.append(f"{where}: unknown source id {sid!r}")

    check_src_refs(planet_srcs, "planet")
    if not planet_srcs:
        rep.errors.append("planet: needs at least one sourceId")

    acts = _req(doc, "activities", list, "file", rep) or []
    act_ids: set[str] = set()
    for i, a in enumerate(acts):
        w = f"activities[{i}]"
        if not isinstance(a, dict):
            rep.errors.append(f"{w}: must be an object")
            continue
        aid = _req(a, "id", str, w, rep)
        if aid:
            w = f"activity {aid}"
            if not ID_RE.match(aid):
                rep.errors.append(f"{w}: id must be a lowercase slug")
            if aid in act_ids:
                rep.errors.append(f"{w}: duplicate activity id")
            act_ids.add(aid)
        _req(a, "title", str, w, rep)
        _enum(_req(a, "type", str, w, rep), ACTIVITY_TYPES, w, "type", rep)
        _enum(_req(a, "stage", str, w, rep), set(STAGES), w, "stage", rep)
        _req(a, "summary", str, w, rep)
        _str_list(a, "steps", w, rep)
        _str_list(a, "rewards", w, rep)
        _str_list(a, "prerequisites", w, rep)
        _str_list(a, "requirementsText", w, rep)
        cost = _req(a, "cost", dict, w, rep) or {}
        pe = cost.get("pedEstimate") if cost else None
        if cost:
            if "pedEstimate" not in cost:
                rep.errors.append(f"{w}: cost missing 'pedEstimate'")
            elif pe is not None and (not isinstance(pe, (int, float)) or isinstance(pe, bool) or pe < 0):
                rep.errors.append(f"{w}: cost.pedEstimate must be a non-negative number or null")
            _req(cost, "text", str, f"{w} cost", rep)
            _enum(_req(cost, "markup", str, f"{w} cost", rep), MARKUP, w, "cost.markup", rep)
            _req(cost, "markupNote", str, f"{w} cost", rep)
        for j, c in enumerate(_req(a, "currencies", list, w, rep) or []):
            cw = f"{w} currencies[{j}]"
            if not isinstance(c, dict):
                rep.errors.append(f"{cw}: must be an object")
                continue
            _req(c, "name", str, cw, rep)
            _enum(_req(c, "use", str, cw, rep), CURRENCY_USE, cw, "use", rep)
            _req(c, "note", str, cw, rep)
        _req(a, "limits", str, w, rep)
        cd = _req(a, "cooldown", dict, w, rep) or {}
        if cd:
            kind = _req(cd, "kind", str, f"{w} cooldown", rep)
            _enum(kind, COOLDOWN_KINDS, w, "cooldown.kind", rep)
            hours = cd.get("hours")
            if kind == "rolling" and (not isinstance(hours, (int, float)) or isinstance(hours, bool) or hours <= 0):
                rep.errors.append(f"{w}: rolling cooldown needs positive 'hours'")
            if "resetUtcHour" in cd:
                h = cd["resetUtcHour"]
                if kind != "fixed-reset" or not isinstance(h, int) or isinstance(h, bool) or not 0 <= h <= 23:
                    rep.errors.append(f"{w}: resetUtcHour must be 0-23 on a fixed-reset cooldown")
            _req(cd, "resetNote", str, f"{w} cooldown", rep)
        for j, loc in enumerate(_req(a, "locations", list, w, rep) or []):
            lw = f"{w} locations[{j}]"
            if not isinstance(loc, dict):
                rep.errors.append(f"{lw}: must be an object")
                continue
            _req(loc, "label", str, lw, rep)
            wp = _req(loc, "waypoint", str, lw, rep, allow_none=True)
            verified = _req(loc, "verified", bool, lw, rep)
            lsrc = _str_list(loc, "sourceIds", lw, rep)
            check_src_refs(lsrc, lw)
            if wp and not WAYPOINT_RE.match(wp.strip()):
                rep.errors.append(f"{lw}: waypoint {wp!r} is not like [Planet, x, y, z, Name]")
            if verified and not wp:
                rep.errors.append(f"{lw}: verified=true needs a waypoint")
            if verified and not lsrc:
                rep.errors.append(f"{lw}: verified waypoint needs sourceIds")
            if wp and not verified:
                rep.warnings.append(f"{lw}: waypoint given but not verified")
        score = _req(a, "score", dict, w, rep) or {}
        for k in ("value", "budget", "effort"):
            v = _req(score, k, int, f"{w} score", rep) if score else None
            if v is not None and not 1 <= v <= 5:
                rep.errors.append(f"{w}: score.{k} must be 1-5")
        if score:
            _req(score, "rationale", str, f"{w} score", rep)
        _enum(_req(a, "confidence", str, w, rep), CONFIDENCE, w, "confidence", rep)
        srcs = _str_list(a, "sourceIds", w, rep)
        if not srcs:
            rep.errors.append(f"{w}: needs at least one sourceId (no source = no entry)")
        check_src_refs(srcs, w)
        _str_list(a, "warnings", w, rep)
        lv = _req(a, "lastVerified", str, w, rep)
        if lv and not DATE_RE.match(lv):
            rep.errors.append(f"{w}: lastVerified must be YYYY-MM-DD")
        _str_list(a, "tags", w, rep)

    for a in acts:
        if isinstance(a, dict) and isinstance(a.get("prerequisites"), list):
            for p in a["prerequisites"]:
                if p == a.get("id"):
                    rep.errors.append(f"activity {a.get('id')}: lists itself as prerequisite")
                elif isinstance(p, str) and p not in act_ids:
                    rep.warnings.append(f"activity {a.get('id')}: prerequisite {p!r} not in this file (must exist in another file)")
    return rep


def load_file(path: Path) -> tuple[dict | None, Report]:
    try:
        doc = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        rep = Report(str(path))
        rep.errors.append(f"cannot read JSON: {exc}")
        return None, rep
    rep = validate_doc(doc, str(path))
    stem = Path(path).stem
    pid = doc.get("planet", {}).get("id") if isinstance(doc, dict) and isinstance(doc.get("planet"), dict) else None
    if pid and pid != stem:
        rep.errors.append(f"planet id {pid!r} must match file name {stem!r}")
    return doc, rep


@dataclass
class Dataset:
    planets: dict[str, dict]           # id -> planet doc
    activities: dict[str, dict]        # activity id -> activity (with '_planet' key)
    reports: list[Report]

    @property
    def errors(self) -> list[str]:
        return [f"{r.path}: {e}" for r in self.reports for e in r.errors]


def load_dataset(data_dir: Path) -> Dataset:
    """Load every valid planet file. Invalid files are skipped and reported, never half-loaded."""
    planets: dict[str, dict] = {}
    activities: dict[str, dict] = {}
    reports: list[Report] = []
    for path in sorted(Path(data_dir).glob("*.json")):
        doc, rep = load_file(path)
        reports.append(rep)
        if doc is None or not rep.ok:
            continue
        pid = doc["planet"]["id"]
        clash = [a["id"] for a in doc["activities"] if a["id"] in activities]
        if pid in planets or clash:
            rep.errors.append(f"duplicate planet/activity ids across files: {pid if pid in planets else clash}")
            continue
        planets[pid] = doc
        for a in doc["activities"]:
            activities[a["id"]] = {**a, "_planet": pid}
    for act in activities.values():
        for p in act["prerequisites"]:
            if p not in activities:
                rep = next(r for r in reports if Path(r.path).stem == act["_planet"])
                rep.errors.append(f"activity {act['id']}: prerequisite {p!r} does not exist in any file")
    return Dataset(planets, activities, reports)
