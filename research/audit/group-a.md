# Prerequisite and source-quality audit, group A

Date: 2026-11-26. Files: aris.json, cyrene.json, space.json, crossworld.json, setesh.json (only the listed entries).
Every listed entry now has a real `prereqInfo` and `lastVerified` 2026-11-26.

Result: 26 entries. 5 verified, 20 partial, 1 unknown.

## Source problems found (all files)

- **be.entropiauniverse.com has an expired TLS certificate** (checked 2026-11-26). This covers the ARIS launch post (S1) and the official beginner guides (space guide, transportation, Codex/skill rewards). The pages still load if you skip the certificate check, and their content backs what they are cited for. I added a note to each of those sources' `supports`.
- **cyreneforum.com is now a parked domain.** It redirects to a domain-parking page. The old `web.archive.org/web/2026/...` links go to the newest 2026 capture, and for the 7 Oct 2025 notes (CF-2510) that capture is the parking page. I pinned CF-2510 to the 15 Jan 2026 capture and CF-2506 to the 15 Feb 2026 capture. Both were re-read and back their claims.
  - **For the lead:** CF-2512 (9 Dec 2025 notes, cited by entries outside my list) probably has the same problem. Its newest capture (9 Aug 2026, www host) has the parking-page fingerprint. A good capture exists from 17 May 2026. I did not touch it. CF-2504 and CF-2603 have no parked capture so far.
- **The Entropia Nexus teleporter URL ignores its Planet filter** (NX-TP). It returns every planet, 37 of them tagged Cyrene. The data is right, so I only noted this in `supports`.
- **The store.steampowered.com news links are rendered by JavaScript** (MA-1980 and similar). I checked their text through Steam's public news API instead. MA-1980 (19.8.0) backs the H.E.A.R.T. Stage 9 clarification.
- **YouTube sources** (ARIS S50-S52, Setesh YTAXE*): I checked the titles, dates and descriptions only. I did not re-watch the videos.
- **README test:** `tests/test_data.py::test_readme_cites_every_source_url` fails. 18 URLs I added are missing from README.md, plus URLs from other agents' files. README is outside my files; the lead should regenerate it with `scripts/gen_readme_sources.py`. My new URLs are listed at the end of this log.

## ARIS (aris.json)

New sources: ASPACE (official space guide), ACODEX (official Codex guide), ATTG (Dec 2025 player token guide). All URLs already appear elsewhere in the data.

- **aris-travel-by-ship: partial.** The official space guide says only a Sleipnir or Quad-Wing with a Space Thruster can leave a planet, or you ride with someone. The station-to-planet teleport is free (18.9.0). A launch-day player had to download ARIS and restart the client (forum, 7 May 2025). I made the ship requirement more precise and added a "not showing in space" diagnostic. I also added a warning: launch-day players were told to fly at the moon itself, but 19.2.0 (9 Dec 2025) added collision to ARIS in space, so aim for the station. Unknown: whether the station teleporter to ARIS has any other gate.
- **aris-planet-teleport-tokens: partial.** Official: main landing teleporter, 10 tokens since 19.2.0, 150 kg limit since 18.9.0. Players (Dec 2025-Jan 2026) say the 150 kg limit still applies and that crafting tokens needs some crafting level; I added that to the requirements. Unknown: whether you must have visited ARIS first, and whether MindArk itself still applies 150 kg to planet-to-planet jumps.
- **aris-ironhaven-orientation: partial.** Being on ARIS is the only requirement any source gives. The talk order (representative, then General Ashfall) comes from a May 2025 video. I added a warning that it may have changed, and a "no sound" diagnostic: the launch-day workaround, plus the 19.12.0 sound-memory fix.
- **aris-codex: verified.** The official Codex guide says a challenge unlocks on your first kill, and 18.14.2 says ARIS uses the same formula as everywhere else. Content fix: the old warning blamed unsourced "player reports". I reworded it to the official fact: until 19.12.1 (17 Nov 2026) the new southern challenges did not count toward the Meta challenge, and the progress is added back at login.

## Cyrene (cyrene.json)

New sources: six Entropia Nexus mission records (NX-ACAD, NX-ONE, NX-DAILY, NX-TOK, NX-HEART, NX-TEMPO). Nexus is crowd-sourced, so each is labelled that way. I used it to corroborate CyreneDream. Its "no prerequisites" is never treated as proof.

- **cyrene-teleporter-network: partial.** You only need to be on Cyrene and reach each teleporter. Added a warning: the list rests on a fan page last edited June 2024 (over 18 months old) and an undated database. Unknown: whether any teleporter is locked behind a mission or rank.
- **cyrene-arc-academy: partial.** Nexus gives the chain order (01 has no prerequisite, then 01 to 06, and the optional knife and finder missions only after 06). Added a diagnostic for that. Content fix: the old warning said nothing newer confirmed the Academy. In fact, the Cyrene notes of 10 Jun 2025 (Selbor re-trade) and CyreneDream's Prestige page (12 Feb 2026, "A.R.C. Academy!" achievement) show it still runs. I reworded the warning; the 2023 reward list is still unconfirmed.
- **cyrene-starter-one-offs: partial.** Added two sourced requirements:
  - Hollingsworth needs Captain Doan's "Help the Cap'n" (CyreneDream and Nexus).
  - Nexus lists "Trial By Fire" from the Drill Instructor as the prerequisite for "Gathering Parts". It sits at the end of an older-looking "Cyrene New Arrival" chain (In The Shadows, Getting Battle Ready, Trial By Fire). Whether that is the same as Academy 06 "Trial by fire!" is unknown.

  Added diagnostics for both, and a warning that the entry rests on a Dec 2023 fan page plus an undated database.
- **cyrene-arc-faction-dailies: partial.** CyreneDream (16 Feb 2026) lists requirements where they exist (for example, Stage 2 needs 200 badges) and lists none for these. Nexus lists none either. Nexus says the 21 h timer runs from completion; I added that to the reset note. Added a "fan sources only" warning.
- **cyrene-token-dailies: partial.** Nexus lists a separate one-time "Find the Auraforger" mission. Whether it gates the Auraforging daily is unknown. The Auraforging step was not backed by CyreneDream, so I added Nexus as its source. Entropia Codex says you must stay in the gathering area; added to the requirements. The sources disagree on the Auraforging timer (24 h vs 21 h); noted in a warning.
- **cyrene-heart-fap: partial.** You start with Medical Tech Orandius, and each rank needs the previous FAP repaired and handed in (CyreneDream, last edited June 2025). Rank X work starts with Lazarus (Cyrene notes, 10 Jun 2025). Added that requirement and an upgrade diagnostic.
- **cyrene-tempo-trials: partial.** No requirement is listed anywhere. Nexus matches the counts and timers. The citation fix (CF-2510) is described above. Added a "fan sources only" warning.

## Space (space.json)

No new sources. I re-read all the cited release notes and guides.

- **space-station-to-planet-free: partial.** Content fix: the summary said you can never teleport from a planet up to a station. That came from the Jan 2025 "New Space Features" post, but 18.15.1 (17 Jun 2025) lets the main landing teleporters of listed planets reach any station for tokens. I corrected the summary and added a warning. Unknown: whether you need that planet's landing teleporter registered.
- **space-teleportation-tokens: partial.** I listed the official requirements (6 or 10 tokens, 150 kg, main landing teleporter) and the player note on the crafting level. I also noted a nuance from the 19.2.0 notes: station-to-station jumps were 10 tokens just before that patch, not 15. Unknown: whether destinations must have been visited before, the exact crafting level, and whether tokens can be looted in space.
- **space-launch-to-space: verified.** 18.9.0: thruster equipped, outside PvP areas. The space guide: only the Sleipnir and Quad-Wing can make the crossing. The requirements list now says this, including that the free tutorial ship qualifies.
- **space-howling-mine-free-ship: partial.** Official: the tutorial is at the Howling Mine. A player guide (26 Dec 2025) puts the NPC at the Howling Mine Teleporter, reached by walking in from the docks. I sharpened the location label, without coordinates, and added diagnostics for finding the NPC and for running out of fuel. Unknown: whether it is limited to new avatars, avatars without a ship, or one per avatar.
- **space-howling-mine-hub: verified.** It is on the official token list, and 18.9.0 says the terminal area needs no thruster (the secondary entrance does). Added both to the requirements.
- **space-genstar-dailies: partial.** Official: Genesis Star dailies are at all stations. Players: up the stairs, one daily per day, a TT laser works. Added the ship and laser requirement. Unknown: any level gate, and what the hunting dailies need.

## Cross-world (crossworld.json)

New sources: the 19.6.0 thread staff reply (F1960T), 19.6.1 notes (F1961), a player post on where Lars is (FLARS), and a player post on Halloween Annihilation (FHALL).

- **crossworld-codex-basics: verified.** The official guide: a challenge unlocks on the first kill. Unknown: which creature groups still have no Codex entry.
- **crossworld-recruit-a-colonist: partial.** Official 19.5.0: you are linked when you create the account through the link, and the rewards start at "Trained status". Unknown: what "Trained status" means, and whether an account can be linked after it is created.
- **crossworld-new-horizons-bonus-track: verified.** The 19.11.0 text was re-read: points come automatically from decay and ammo, and you claim from the HUD or your account page. It runs from 20 Oct 2026 08:15 UTC to 1 Jan 2027 00:00 UTC. No other condition is stated.
- **crossworld-jul-snarg-hunt: partial.** Merry Mayhem 2025 rules: start it with Santa's Little Helper by the Port Atlantis teleporter, once per avatar ever. Added a diagnostic. Unknown: the 2026 rules. Merry Mayhem 2026 was not announced on Steam or the forum as of 26 Nov 2026.
- **crossworld-fishing-start: partial.** Content fix: Lars's location was only "at the camp". A MindArk staff reply (15 Apr 2026) names the Port Atlantis fishing camp, and a player (29 Apr 2026) puts it north-east of Port Atlantis by a campfire. 19.6.1 (21 Apr 2026) removed skill requirements that had wrongly been put on the Baitfishing Rod. Added a diagnostic for not getting the rod, using the staff advice (check inventory, relog, Compact). Unknown: whether the Spool Cell trade blocks the rod (one player says yes, staff say the missions work).
- **crossworld-mayhem-calendar: partial.** You can enter while an event runs, through the Global Events list or event NPCs on Calypso. In Summer 2026 each stage unlocked the next. Content fix: the Annihilation step now says Merry 2025 and Easter 2026 had it, and the Halloween 2026 post has no Annihilation track (a player asked MindArk about this on 24 Oct 2026). Unknown: level gates, and whether Halloween Survival stages must be cleared in order.

## Setesh (setesh.json)

New sources:
- FJOEL1: player feedback post, 3 Oct 2025.
- FMEL: MindArk staff reply, 18 Sep 2025.
- FWHAT: player post, 8 Aug 2026.
- FFISH9 and FFISH111: fishing player posts, 16-17 Apr 2026.
- F1960: 19.6.0 thread.

The lead's six entries are unchanged (checked by comparing the file before and after).

- **setesh-savannah-survey: partial.**
  - Giver: Specialist Mel at Outpost Hunraqan, confirmed by MindArk staff.
  - A player (Oct 2025) says the 3 surveys need a Genesis Star Rookie Finder (L), which veterans may lack and the trade terminal doesn't sell. Added to the requirements with a diagnostic.
  - A Jan 2026 video calls it "Survey the Savannah" and shows it after "To Hunraqan".
  - Removed an old warning about a "Dec 2025 player" getting the mission without probes or a finder. I could not trace it to any cited or findable source.
  - Added a thin-evidence warning.
  - Unknown: whether a main-chain mission must come first, where newcomers get the finder, and rewards for Thule veterans.
- **setesh-trader-joel-daily: partial.**
  - Mission name, objective and rewards from one player (Oct 2025): "Fetch: Robot Component Residue", 100 residue for oil, ammo, a Blazer and a Nova fragment.
  - Waypoint `[Setesh, 67819, 68112, 268, Joel]`, posted by a player on 8 Aug 2026. Marked verified because the cited post shows that exact waypoint. An Oct 2025 post gives nearly the same spot.
  - Added that 19.6.0 stopped hand-in objectives being negotiated.
  - Confidence raised from low to medium, because the mission's existence is official and two player posts (one from Aug 2026) agree on it. The 24 h timer still comes only from a fan tool and players.
- **setesh-fishing-starter-gear: unknown.** Only one official sentence says this mission exists. No source names the giver, the mission, or its prerequisites. Recorded as unknowns:
  - A newcomer did "about 10 missions" before learning to fish, which hints it comes later in a chain.
  - An unconfirmed claim that Lars's Spool Cell exchange affects it.
  - A launch-day report of not being able to fish after finishing it.

  Added a warning that the entry rests on one official line and scattered player remarks.

## Blocked or not done

- The forum search rate-limited me once (HTTP 429). I retried more slowly and finished.
- No source anywhere names the Setesh fishing mission or its giver.
- I did not re-watch the videos.
- No sites were blocked otherwise.

## New source URLs not yet in README

- cyrene: the two re-pinned Wayback URLs for CF-2506 and CF-2510, and api.entropianexus.com/missions/6236, 4586, 6063, 6106, 4590, 5502.
- crossworld: forum t/287175/17, t/287339, t/288221, t/853251.
- setesh: forum t/285160/105, t/285160/29, t/what-to-do-in-satesh/851608, t/284171/9, t/286671/111, t/287175.
