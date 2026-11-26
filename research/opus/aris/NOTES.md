# ARIS research log (research/opus/aris)

Researcher: Opus 5.5 research child. Reviewed 2026-11-26. One output file: `aris.json` (31 activities).

## Why one file, not several
Breakwater (the southern continent) and Misty Island (a Land Area reached through a southern mission) sit on the same ARIS map, use the same currency (Hyperion Daily Vouchers), and are unlocked by missions that start on ARIS. A separate destination would split prerequisite chains across files for no gain, so I kept them in `aris.json` as `mid`-stage activities tagged `breakwater` / `land-area`. If the build lead wants a sub-destination later, the ids `aris-breakwater-*`, `aris-sketh-incursion`, `aris-qay-sekku-missions`, `aris-south-instances`, `aris-missing-scientists-south` and `aris-misty-island` move cleanly.

## What ARIS is (confirmed)
- A moon orbiting Calypso that MindArk also calls a "full-fledged planet" and "the sixth planet". Released 7 May 2025 in VU 18.14.0 (S1, S3). The teaser on 2025-04-09 (S2) announced it "in the coming weeks".
- Run by **Hyperion Enterprises**, a new Planet Partner. Its forum account (John_Archer_Hyperion) says it is a new company based in Sweden, started for this project, unrelated to other player groups, with a "more light-weight" partnership than other partners (S20, post #73). "John Archer" is a fictional CEO persona; the poster is a real person (S20 #13). Omegaton is the in-lore sponsor (S1). The developer says ARIS was built with the regular world editor, not the Genesis Probe (S20 #191).
- Lore name: "Autonomous Robot Invasion System" (S1, CEO letter). Entropia Hub calls it "Asteroid Revival Initiative Station". That conflicts with the official letter, so I did not use it.
- Main settlement Ironhaven. Steelrise was announced as a future second outpost (S1). Entropia Nexus lists a "Steelrise" outpost at 35947, 19632 (S43), but no release note confirms it opened, so I left it out of the activities.
- Design rules: no flying vehicles, no Mindforce teleport (fully blocked since 18.15.0), toxic water, ground vehicles allowed (S1, S6). Since 19.3.0 the ocean is safe for boats and ships (S10).

## Status / last 6 months (all official)
- 19.7.0 (2026-05-12): first anniversary, Lure MF chip, Dr. Vera Santis psionic division, Energy Matter revamp with 3 ARIS resources, fishing camp, Altar rebuilt and activated 13 May 13:00 CET, Personal Pharmatron 103/106/109/120, Vaults S-3/S-6 built but inactive.
- 19.8.0 (2026-05-19) / 19.8.1 (2026-06-02): boss rebalances, S9 WARDEN buff fix, altar boss name fix.
- 19.10.1 (2026-09-15): faster doors in ARIS daily robot instances.
- 19.10.3 (2026-09-22): Bonnie and Fenton moved outside the main building; **anniversary missions can no longer be started** (in-progress ones can be finished, no deadline).
- 19.11.0 (2026-10-20): fixed interplanetary teleports that did not consume Teleportation Tokens.
- **19.12.0 (2026-11-11): biggest ARIS update since launch.** Southern continent and Breakwater (travel with Nora Gretz or find your own way); Vaults S3/S6/S9 active (at least 2 players); new mining discoveries; **selected hunting dailies replaced by weekly missions** with choice of difficulty and random target, and already-accepted dailies can still be completed; research and sample missions now include the south; Hyperion armor restocked.
- 19.12.1 (2026-11-17): Vault Emergency Exits (**Access Fragments already used are not returned**); fixed weekly hunting contribution values and rewards; Nora arrival points moved to solid ground; new codex challenges added to meta retroactively; "ARIS - The Incursion Resurgent" and "ARIS - A Fresh Breath" can now be active at the same time.
- No release after 19.12.1 was listed in the official forum category as of 2026-11-26.
- Verdict: **active**, and changing fast right now.

## Build-lead acceptance cross-check (2026-11-26)
I re-checked both forum pages myself (S15, S16):
- 19.12.0: Breakwater via Nora Gretz or your own way. Covered in `aris-breakwater-access` (summary and warnings).
- 19.12.0: S3/S6/S9 need at least two players. Covered in `aris-vaults-coop` (summary, requirementsText, warnings).
- 19.12.0: selected hunting dailies replaced by weeklies; already-accepted dailies can still be completed, but you cannot take them again. Covered in `aris-hyperion-hunting-contract` warnings (cooldown kind rolling 168 h).
- 19.12.1: used Access Fragments are not refunded at emergency exits. Covered in `aris-vaults-coop` warnings and its currency note (`Access Fragment`, use `spent`).

## Key numbers and where they come from
- Planet-to-planet teleport: added 18.15.1 at 15 Teleporter Tokens, from the main landing teleporter. ARIS is on the list (S7). Lowered to 10 in 19.2.0 (S9). Interplanetary station teleport launched in 18.9.0 with a 150 kg limit, and token blueprints are sold at the Space Mining Terminal (S17).
  - **Contradiction:** players in May 2025 (S20, S23) and a March 2026 video (S50) call the ARIS-to-Calypso teleport free. The 19.11.0 fix (S14) suggests some teleports were wrongly not charging. The app text says to assume 10 tokens.
- Cooldowns, all from the Ripcraze tracker bundle (S40, app v2.6.12): Samples 168 h; Hyperion Hunting Contract 168 h; Juston Breakwater Field Contract 168 h; Daily Mining 16 h; Daily Crafting 16 h; Elara Vox 20 h; all 8 northern instances 20 h; 3 southern instances 20 h; Tonathan AI 24 h; Qay Field Repairs 24 h, Machine Intelligence 168 h, Mutation Samples 24 h, Unstable Minds 168 h.
  - **Official cooldown rule:** instance cooldown triggers on boss death or voluntary exit (18.14.3, S4). You cannot log in inside a dungeon that is on cooldown, and you can rerun after a crash (19.0.2, S8).
  - No source says whether mission timers start at accept or at completion. Entropia Nexus records "CooldownStartsOn: Accept" for Calypso AI dailies, but it has no ARIS missions. I modelled all of them as `rolling` and stated this uncertainty in `resetNote`.
- Voucher rewards: Samples 2; Hunting Contract 4/8/12; Juston 3/7/11; Mining 1; Crafting 1; south instances 1 each; Tonathan 1 (all S40). One-time missions per a player list (S21 #47): Scientists 10, Scrapheap 10, Ultimate Threat 30, Taming the Wilds 10, Extinguishing the Flames 10 (corroborated by S51).
  - **Conflict:** samples were "Daily Samples" in official 18.14.4 notes and in videos through March 2026. Now they are weekly per S40 and a player on 2026-11-18 (S27 #57). The official 19.12.0 notes do not say "weekly" for samples. I marked it medium confidence.
  - **Unconfirmed:** a player says 19.12.0 removed the voucher from the easiest robot instance (S27 #40). I kept the claim as a warning.
- Hyperion armor (S22, May 2025 player table; corroborated by S52 video and S51): 80 vouchers per base piece plus padding and fabric per slot; each upgrade is 2 pieces + 10 catalysts. Mixed-set rule is official (S8). The developer says vendor stock is capped and restocks (S23); restocked in 19.12.0 (S15).
- Blueprint unlocks: 30 vouchers + 2 PED each, 7 blueprints (S22, corroborated by S51 and S50).
- Voucher "value": players quote about 3 PED per voucher (Aug 2025, S51) and a "pull" at 150-250 PED (2025-2026; S22 thread, S50). Recorded only as markup notes, never as a promise.

## Waypoints
- I copied the bracket part exactly and dropped the leading "/wp " because the validator regex requires the string to start with "[".
- Three planet labels appear in sources: "Planet ARIS" (Entropia Hub), "Aris" (Ripcraze) and "ARIS" (in-game copies on the forum). Planet warnings tell players to switch to ARIS if a paste fails.
- Teleporter coordinates were cross-checked: Entropia Hub (S42) against Entropia Nexus (S43) against Ripcraze (S41). All agree within about 10 m.
- Southern teleporters (Breakwater Landing, Stillwater, Farpoint) are known only as coordinates from the Ripcraze map bundle, so `waypoint: null` and the coordinates go in the label.

## Possibly stale (older than about 18 months or not re-confirmed)
- Nothing on ARIS is older than 19 months. Items from mid-2025 that were not re-confirmed after the 19.12.0 economy change: the armor cost table, blueprint costs, the one-time mission voucher amounts, AI-daily cost reports (Oct 2025) and Scrapheap spawn spots.
- The chemistry chain (S25, Dec 2025) rests on one player post.

## Coverage gaps
- How to get Access Fragments; vault rewards and cooldowns.
- The exact Nora Gretz travel chain and its cost. Only player estimates exist (about 150 PED, S27 #27). A "Frontier Pass" was asked about by one player and is unconfirmed.
- What the southern story missions ("The Incursion Resurgent", "A Fresh Breath") and the Southern Expedition scientists reward.
- Altar mechanics and rewards after the May 2026 rebuild.
- Cryo Lab daily cooldown; Dr. Vera Santis mission details; Lure chip details.
- The name of the 18.15.0 "south tip of Ironhaven island" outpost teleporter.
- Teleportation Token PED price.

## Blocks and failures
- be.entropiauniverse.com has an expired TLS certificate. WebFetch failed, so I read the pages with curl (certificate check skipped; content is public news).
- EntropiaWiki (entropiawiki.com and www.) did not respond (connection failed, HTTP 000). No EntropiaWiki data was used.
- Entropia Nexus has no ARIS missions ("No missions configured yet"; the public API returned 0 ARIS missions out of 2,130). I used only its location data.
- The official forum search rate-limited me once. I waited and retried.
- YouTube captions could not be fetched directly. I got transcripts through DeepAPI. The Vault S9 video (9yWMPDJy-Kk) had no transcript, so it was not used.
- Reddit: web searches returned no relevant r/EntropiaUniverse ARIS threads.
- Found but not used: eux-9mx.pages.dev "ARIS Moon Guide" (unverifiable, looks generated) and Entropia Hub's blog post (its claims are covered better elsewhere). The EarnPED video (MKoJm9KWe3M, 2025-07-26) was read but adds nothing beyond S51/S52.

## Full source list (published, accessed)
| Id | Source | URL | Published | Accessed |
|---|---|---|---|---|
| S1 | Introducing Planet ARIS (MindArk) | https://be.entropiauniverse.com/news/2025/05/07/Introducing-Planet-ARIS/index.xml | 2025-05-07 | 2026-11-26 |
| S2 | The Expansion of Entropia Universe (MindArk) | https://be.entropiauniverse.com/news/2025/04/09/The-Expansion-of-Entropia-Universe/ | 2025-04-09 | 2026-11-26 |
| S3 | 18.14.0 Release Notes | https://account.entropiauniverse.com/news/pages/2025/05/07/0658/index.xml | 2025-05-07 | 2026-11-26 |
| S18 | 18.14.2 Release Notes | https://account.entropiauniverse.com/news/pages/2025/05/09/1140/index.xml | 2025-05-09 | 2026-11-26 |
| S4 | 18.14.3 Release Notes | https://account.entropiauniverse.com/news/pages/2025/05/13/2476/index.xml | 2025-05-13 | 2026-11-26 |
| S5 | 18.14.4 Release Notes | https://account.entropiauniverse.com/news/pages/2025/05/22/2980/index.xml | 2025-05-22 | 2026-11-26 |
| S6 | 18.15.0 Release Notes | https://account.entropiauniverse.com/news/pages/2025/06/10/9692/index.xml | 2025-06-10 | 2026-11-26 |
| S7 | 18.15.1 Release Notes | https://account.entropiauniverse.com/news/pages/2025/06/17/5160/index.xml | 2025-06-17 | 2026-11-26 |
| S17 | 18.9.0 Release Notes | https://account.entropiauniverse.com/news/pages/2025/01/28/8564/index.xml | 2025-01-28 | 2026-11-26 |
| S8 | 19.0.2 Release Notes | https://account.entropiauniverse.com/news/pages/2025/09/23/9650/index.xml | 2025-09-23 | 2026-11-26 |
| S9 | 19.2.0 Release Notes | https://account.entropiauniverse.com/news/pages/2025/12/09/3273/index.xml | 2025-12-09 | 2026-11-26 |
| S10 | 19.3.0 Release Notes | https://account.entropiauniverse.com/news/pages/2026/01/27/7397/index.xml | 2026-01-27 | 2026-11-26 |
| S11 | 19.7.0 Release Notes | https://account.entropiauniverse.com/news/pages/2026/05/12/2619/index.xml | 2026-05-12 | 2026-11-26 |
| S12 | 19.8.0 Release Notes | https://account.entropiauniverse.com/news/pages/2026/05/19/6532/index.xml | 2026-05-19 | 2026-11-26 |
| S19 | 19.10.0 Release Notes (forum) | https://forum.entropiauniverse.com/t/entropia-universe-19-10-0-release-notes/852226 | 2026-09-08 | 2026-11-26 |
| S13 | 19.10.3 Release Notes (forum) | https://forum.entropiauniverse.com/t/entropia-universe-19-10-3-release-notes/852635 | 2026-09-22 | 2026-11-26 |
| S14 | 19.11.0 Release Notes (forum) | https://forum.entropiauniverse.com/t/entropia-universe-19-11-0-release-notes/853170 | 2026-10-20 | 2026-11-26 |
| S15 | 19.12.0 Release Notes (forum) | https://forum.entropiauniverse.com/t/entropia-universe-19-12-0-release-notes/853664 | 2026-11-11 | 2026-11-26 |
| S16 | 19.12.1 Release Notes (forum) | https://forum.entropiauniverse.com/t/entropia-universe-19-12-1-release-notes/853808 | 2026-11-17 | 2026-11-26 |
| S20 | Welcome to ARIS! (forum) | https://forum.entropiauniverse.com/t/welcome-to-aris/282924 | 2025-05-07 | 2026-11-26 |
| S31 | ARIS Daily missions and AI daily missions + rewards | https://forum.entropiauniverse.com/t/aris-daily-missions-and-ai-daily-missions-rewards/287943 | 2025-05-09 | 2026-11-26 |
| S23 | New Hyperion Armour upgrade question | https://forum.entropiauniverse.com/t/new-hyperion-armour-upgrade-question/287953 | 2025-05-12 | 2026-11-26 |
| S21 | Operation: Scrapheap [Spoiler Alert] | https://forum.entropiauniverse.com/t/operation-scrapheap-spoiler-alert/287845 | 2025-05-15 | 2026-11-26 |
| S22 | Hyperion Armor Series | https://forum.entropiauniverse.com/t/hyperion-armor-series/289203 | 2025-05-31 | 2026-11-26 |
| S32 | Strange Altar | https://forum.entropiauniverse.com/t/strange-altar/286895 | 2025-07-03 | 2026-11-26 |
| S24 | ARIS Daily AI | https://forum.entropiauniverse.com/t/aris-daily-ai/282745 | 2025-10-07 | 2026-11-26 |
| S25 | Aris new missions infos & new chemist profession questline | https://forum.entropiauniverse.com/t/aris-new-missions-infos-new-chemist-profession-questline/282633 | 2025-12-19 | 2026-11-26 |
| S26 | 19.12.0 ARIS Release Feedback | https://forum.entropiauniverse.com/t/19-12-0-aris-release-feedback/853662 | 2026-11-11 | 2026-11-26 |
| S27 | 19.12.0 ARIS Release Issues | https://forum.entropiauniverse.com/t/19-12-0-aris-release-issues/853663 | 2026-11-11 | 2026-11-26 |
| S28 | [SPOILER ALERT] ARIS Breakwater secrets | https://forum.entropiauniverse.com/t/spoiler-alert-aris-breakwater-secrets/853687 | 2026-11-12 | 2026-11-26 |
| S29 | Misty Island - home of the Veilback | https://forum.entropiauniverse.com/t/misty-island-home-of-the-veilback/853747 | 2026-11-15 | 2026-11-26 |
| S30 | Misty Island Land Grab - Feedback | https://forum.entropiauniverse.com/t/misty-island-land-grab-feedback/853820 | 2026-11-17 | 2026-11-26 |
| S40 | Ripcraze ARIS Daily Missions Tracker | https://ripcraze.com/?type=daily&planet=aris | n/a | 2026-11-26 |
| S41 | Ripcraze Maps (ARIS map data) | https://ripcraze.com/map | n/a | 2026-11-26 |
| S42 | Entropia Hub Planet ARIS hub | https://entropiahub.com/aris/ | n/a | 2026-11-26 |
| S43 | Entropia Nexus ARIS map | https://entropianexus.com/maps/aris | n/a | 2026-11-26 |
| S50 | "Entroipa  Aris daily mission guide", Old Bloke Gaming (YouTube) | https://www.youtube.com/watch?v=OeobyRKnmNs | 2026-03-20 | 2026-11-26 |
| S51 | "ARIS GUIDE FOR NEWCOMERS", @Artanis_Hr (YouTube) | https://www.youtube.com/watch?v=UCv54WRu1KI | 2025-08-03 | 2026-11-26 |
| S52 | "Getting started on A.R.I.S - Entropia Universe", @BladeofAkire (YouTube) | https://www.youtube.com/watch?v=atjpUkg126s | 2025-05-09 | 2026-11-26 |

Also read, not cited in JSON: the full official release-note archive embedded in https://account.entropiauniverse.com/news/ (18.12–19.9, all ARIS sections checked) and https://be.entropiauniverse.com/bulletin/release-notes (to 19.10.0); 19.9.1, 19.9.2, 19.10.0 hotfix, 19.10.1 hotfix, 19.10.4–19.10.6 forum notes (no ARIS content beyond what is listed); forum threads 287959, 850437, 287137, 287837; EarnPED video MKoJm9KWe3M (2025-07-26).
