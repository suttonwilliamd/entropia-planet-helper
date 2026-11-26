"""Status (done / cooling down / blocked / available) and ranking of activities."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from .data import STAGES
from .store import Progress

WEIGHTS = {"normal": (0.40, 0.35, 0.25), "budget": (0.25, 0.55, 0.20)}
CONFIDENCE_FACTOR = {"high": 1.0, "medium": 0.85, "low": 0.6}

AVAILABLE, COOLDOWN, BLOCKED, DONE = "available", "cooldown", "blocked", "done"


@dataclass
class Status:
    state: str
    ready_at: datetime | None = None     # for cooldown with a known time
    missing: tuple[str, ...] = ()        # unmet prerequisite ids
    note: str = ""


def next_fixed_reset(after: datetime, utc_hour: int) -> datetime:
    after = after.astimezone(timezone.utc)
    candidate = after.replace(hour=utc_hour, minute=0, second=0, microsecond=0)
    if candidate <= after:
        candidate += timedelta(days=1)
    return candidate


def status_of(act: dict, progress: Progress, now: datetime) -> Status:
    missing = tuple(p for p in act.get("_blocking", act["prerequisites"]) if not progress.ever_done(p))
    cd = act["cooldown"]
    kind = cd["kind"]
    last = progress.last_done(act["id"])
    if progress.ever_done(act["id"]):
        if kind == "once":
            return Status(DONE, note="Completed (one-time).")
        if last is not None:
            if kind == "rolling":
                ready = last + timedelta(hours=float(cd["hours"]))
                if now < ready:
                    return Status(COOLDOWN, ready_at=ready,
                                  note=f"Rolling {cd['hours']:g} h from when you marked it done.")
            elif kind == "fixed-reset":
                if "resetUtcHour" in cd:
                    ready = next_fixed_reset(last, cd["resetUtcHour"])
                    if now < ready:
                        return Status(COOLDOWN, ready_at=ready,
                                      note=f"Resets daily at {cd['resetUtcHour']:02d}:00 UTC.")
                else:
                    return Status(COOLDOWN, note="Fixed reset; press 'Ready again' once it has reset in game.")
            elif kind == "unknown":
                return Status(COOLDOWN, note="Reset timing unknown; press 'Ready again' when the game offers it.")
    if missing:
        return Status(BLOCKED, missing=missing)
    return Status(AVAILABLE)


def score_of(act: dict, user_stage: str, budget_mode: bool = False) -> tuple[float, str]:
    wv, wb, we = WEIGHTS["budget" if budget_mode else "normal"]
    s = act["score"]
    base = (wv * s["value"] + wb * s["budget"] + we * s["effort"]) / 5
    conf = CONFIDENCE_FACTOR[act["confidence"]]
    u, a = STAGES.index(user_stage), STAGES.index(act["stage"])
    if a == u:
        stage_mult, stage_txt = 1.10, "matches your stage (+10%)"
    elif a < u:
        stage_mult, stage_txt = 1.0, "earlier stage, still useful"
    else:
        stage_mult = max(0.25, 1 - 0.25 * (a - u))
        stage_txt = f"{a - u} stage(s) ahead of you (-{round((1 - stage_mult) * 100)}%)"
    total = round(base * conf * stage_mult * 100, 1)
    why = (f"value {s['value']}/5 x{wv:.2f}, budget {s['budget']}/5 x{wb:.2f}, quickness {s['effort']}/5 x{we:.2f}"
           f" -> {base * 100:.0f}; confidence {act['confidence']} (x{conf}); {stage_txt}. Score {total}.")
    return total, why


def ranked(acts: list[dict], progress: Progress, user_stage: str, budget_mode: bool,
           now: datetime | None = None) -> list[tuple[dict, Status, float, str]]:
    """All activities with status and score, best first; available ones before the rest."""
    now = now or datetime.now(timezone.utc)
    order = {AVAILABLE: 0, COOLDOWN: 1, BLOCKED: 2, DONE: 3}
    rows = []
    for act in acts:
        st = status_of(act, progress, now)
        sc, why = score_of(act, user_stage, budget_mode)
        rows.append((act, st, sc, why))
    rows.sort(key=lambda r: (order[r[1].state], -r[2], r[0]["title"].lower()))
    return rows
