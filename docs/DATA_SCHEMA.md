# Entropia Planet Helper — data schema (v1)

One JSON file per destination in `data/planets/<id>.json` (UTF-8, no comments).
Research drafts may live under `research/` in the same shape and are merged by the build lead.
Validate any file with:

```
python -m planet_helper.validate data/planets/aris.json
```

## Ground rules

- Every activity must cite at least one source in `sourceIds`. No source = no entry.
- Write in your own words. Do not paste mission text, guides or images. Short names, numbers and waypoint coordinates are fine.
- A guess is never a fact. If something is unconfirmed, set `confidence: "low"` and say why in `warnings`.
- Waypoints: copy them exactly as the source gives them, e.g. `[ARIS, 12345, 67890, 100, Waypoint]`.
  `verified: true` only if a cited source shows that exact waypoint. Otherwise leave `waypoint: null` and describe the place in `label`.
- Prices in PED. TT = the trade-terminal value. Markup = what players pay above TT. Never promise profit.
- Dates are `YYYY-MM-DD`. `published` is the source's own date (null if none shown); `accessed` is when you read it.

## Shape

```json
{
  "schemaVersion": 1,
  "planet": {
    "id": "aris",                       // lowercase slug, matches file name
    "name": "ARIS",
    "kind": "planet",                   // planet | moon | space | instance | event | special
    "parent": null,                      // e.g. "rocktropia" for Hunt The THING
    "status": "active",                 // active | seasonal | inactive | unverified
    "summary": "Plain-language overview, 1-3 sentences.",
    "howToReach": "How a player gets there (ship, teleporter, ticket...).",
    "lastReviewed": "2026-11-26",
    "warnings": ["Anything stale, contradictory or risky."],
    "sourceIds": ["S1"]
  },
  "sources": [
    {
      "id": "S1",                       // unique within the file
      "title": "Exact page title",
      "url": "https://...",
      "publisher": "MindArk (official)",
      "kind": "official",               // official | official-forum | wiki | community-guide | forum | video
      "published": "2025-04-09",        // or null
      "accessed": "2026-11-26",
      "supports": "What this source backs up, in one line."
    }
  ],
  "activities": [
    {
      "id": "aris-example-chain",       // globally unique, prefix with planet id
      "title": "Short name",
      "type": "mission-chain",          // unlock | mission-chain | mission | daily | repeatable | event | travel | skill | tip
      "stage": "early",                 // arrival | early | mid | late
      "summary": "What it is and why it matters, plain language.",
      "steps": ["Concrete step 1", "Step 2"],
      "rewards": ["What you get (item, skill, unlock, PED value if known)"],
      "prerequisites": ["other-activity-id"],   // ids that must be completed first (same or other file)
      "requirementsText": ["Non-activity requirements, e.g. 'Level 20 in Laser Weaponry'"],
      "cost": {
        "pedEstimate": 0,               // number or null if unknown
        "text": "What you spend (ammo, decay, tickets).",
        "markup": "unknown",            // none | low | medium | high | unknown
        "markupNote": ""
      },
      "currencies": [
        { "name": "Some token", "use": "earned", "note": "kept / spent / earned and what for" }
      ],                                // use: earned | spent | kept
      "limits": "Caps, one-time only, per-account limits...",
      "cooldown": {
        "kind": "rolling",              // none | once | rolling | fixed-reset | unknown
        "hours": 24,                    // for rolling; null otherwise
        "resetNote": "Exactly what the source says about when it resets."
      },
      "locations": [
        { "label": "Mission giver name / place", "waypoint": null, "verified": false, "sourceIds": ["S1"] }
      ],
      "score": {
        "value": 4,                     // 1-5 long-term benefit to the player
        "budget": 5,                    // 1-5 (5 = cheap / free)
        "effort": 3,                    // 1-5 (5 = quick)
        "rationale": "Why these scores, in one or two sentences."
      },
      "confidence": "medium",           // high | medium | low
      "sourceIds": ["S1"],
      "warnings": [],
      "lastVerified": "2026-11-26",
      "tags": ["beginner", "hunting"]
    }
  ]
}
```

## Cooldown meaning in the app

- `once`: completed for good once ticked.
- `rolling`: becomes available again `hours` after the moment *you* mark it done in the app (the app cannot see the game).
- `fixed-reset`: resets at a fixed time described in `resetNote`; the app shows the note and lets you clear it manually. If the note gives a UTC hour like `00:00 UTC`, put `"resetUtcHour": 0` in the cooldown object and the app will reset it automatically.
- `unknown`: tracked as done until you clear it.

## Ranking (how the app orders "next actions")

score = (0.40·value + 0.35·budget + 0.25·effort) / 5 × confidence factor (high 1.0, medium 0.85, low 0.6),
then adjusted for the stage you picked (same stage +10%, one stage earlier +0%, later stages −25% per step).
Activities with unmet prerequisites go to "Blocked" (prerequisites of type `travel` are shown but never block); ones on cooldown go to "Cooling down"; completed one-time items are hidden.
"Budget mode" swaps the weights to 0.25/0.55/0.20.
