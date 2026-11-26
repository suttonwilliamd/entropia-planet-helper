# Cyrene research log (output id: `cyrene`)

Researcher: Opus 5.5 research child. Access date for everything below: 2026-11-26.

## What I checked

1. **Official sources**
   - `planetcyrene.com`: `http://planetcyrene.com` returns **410 Gone**. `https://www.planetcyrene.com` only shows "Apache is functioning normally". Wayback shows it was a redirect in 2024-2025. No usable official partner site any more.
   - `cyreneforum.com` (the Cyrene team's official forum, where "Kris | Cyrene" posted VU notes): **the live domain now shows a GoDaddy-style parking page** (`/lander`). Wayback snapshots from 2026-05 still hold the forum. The last homepage snapshot shows a "Forum downtime/maintenance" thread (id 9494), which was never archived. Snapshots from 2026-08 onward already show the parking page. I read these Cyrene VU notes from Wayback copies: 2025-04-01, 2025-06-10, 2025-10-07 (plus dev replies), 2025-12-09 and 2026-03-31. The Spring 2026 preview thread was only archived as the parking page.
   - MindArk release notes: `be.entropiauniverse.com` has an expired TLS certificate, and `www.entropiauniverse.com/bulletin/release-notes/` returns 404. Instead I used **MindArk's Steam news feed** for app 3642750 (official announcements API), which includes Planet Cyrene sections in 19.8.0 (2026-05-19), 19.9.0 (2026-06-24), 19.10.3 (2026-09-22), 19.10.6 (2026-10-14) and 19.11.0 (2026-10-20). 19.12.x (Nov 2026) has no Cyrene section. The 18.9.0 notes (2025-01-28) on account.entropiauniverse.com cover interplanetary token teleports.
   - The SteamDB patch-note pages returned 403. I used the Steam API instead.
2. **CyreneDream** (cyrenedream.org, the community guide): I read about 50 pages through its WordPress JSON API, which also gives each page's created/modified dates. I extracted the copy-waypoints from the page HTML (`data-copy` attributes) so they match exactly.
3. **Corroboration**
   - Entropia Nexus API (teleporters and locations for Cyrene).
   - Entropia Codex Cyrene page (newcomer daily rotation).
   - Entropia Universe Forum TToken guide (Dec 2025).
   - Entropia Central Cyrene guide (updated 2026-08-13; secondary, used only to spot contradictions).
   - Entropia Museum VU list (via WebFetch summary; matched the Steam notes).

## Confirmed (official, 2025-2026)

- **A.R.C. Prestige** opened 2025-04-01. You talk to Cait at the top floor of A.R.C. HQ, and the keycard is paid with Cyrene Mission Tokens plus A.R.C. Badges.
  - Golem portal and new Amos/Saphira missions: June 2025.
  - Vlanwing/Protocore missions, and A.R.C. Tier 4 moved into Prestige with the A.R.C. Adept armor for Shrapnel: Dec 2025.
  - Thunderous instance with a weekly droplet mission for Assassinator owners: Mar 2026. The weekly mission was fixed in May 2026.
  - Undersea Folken repeatable: June 2026.
  - Bi-weekly Mang Chang / Rhino Beetle missions: Sept 2026.
- **Zyn Rucksack**: Modified (2025-06), Augmented (2025-10), Perfected (2026-06).
- **H.E.A.R.T.**: Rank X added in 2025-06.
- **Stable Turrelion Assassinator**: Imperium faction requirement cut from 20,000 to 8,000 (2025-06). Attachment terminals above Kwarn TP (2026-03); you must choose one of Coat, Sight, Scope or Amp at a time. Components marked rare (2026-06).
- **High-level limited amps** (Zorra's Blessed Laser, Hyden's Unstable BLP): added 2025-10 through Rory at A.R.C. HQ and Frankie at Kwarn. TT value raised and turn-ins changed in 2025-12.
- **Weapon cubes** can be sold to the TT (2026-03).
- **Team instances** raised from 6 to 12 players (2026-06).
- **Texture NPCs** (Ben Keery, Kayde Barnes, Hoban Statsk) got new blueprint rewards in every VU from 2025-04 to 2026-09. Texture Tutor Jyor'den's TPM daily was added in 2026-09.
- **The Hub** removes implants; 19.11.0 (2026-10) fixed implant buffs that stayed active afterwards.
- **Known issues**, repeated in every Cyrene note from 2025-04 to 2026-09:
  - support weapons are not working properly (a platform issue);
  - vehicles use default sounds;
  - the Brown Beetle rank-5 supplementary mission is broken;
  - A.R.C. blueprint book quality ratings are wrong.
- **Mining Iron Challenge**: a player in the Oct 2025 VU thread reported that it stops after rank 4. The Cyrene dev (Kris) said they would look into it. I found no fix note.

## Contradictions and judgement calls

- **Faction vendors.** Entropia Central says they are paid only in badges. CyreneDream's Vendors and Voucher pages show the Hub A.R.C. terminals take Shrapnel and Limited Weapon Cubes, and only *check* that you carry 200+ badges. I went with CyreneDream (more detailed, firsthand) and flagged the conflict.
- **Teleporter count.** CyreneDream lists 36. Entropia Nexus lists 37 and adds the "Rookie Training Area" teleporter. Nexus also calls one of them "Ngu Volcano Island Lookout Teleporter" where CyreneDream has "Ngu Volcano". Both are recorded.
- **Paneleon Hunter Jameson cooldown.** 21h on CyreneDream's Repeatable Missions page, 24h on its Sweating page. I used 21h and added a warning.
- **Crystal Pede Tempo Manager.** It was moved away from the water in Oct 2025. CyreneDream's waypoint for it may predate the move, so I did not include it.
- **Teleportation Token cost.** The official launch cost was 15 tokens (Jan 2025). Players reported 10 per planet trip (Dec 2025/Jan 2026), and one reply says 6 for station-to-station. No official note of the change was found, so the cost is marked low confidence.
- **Arrival point.** No current source names Cyrene's space-station teleport destination. A Cloudflare-pages "definitive guide" mirror claims new players arrive at "Sky Labs (the orbiting space station)". Sky Labs is actually an on-planet teleporter at altitude 958. That site's provenance is unknown, so I did not use it. The `cyrene-travel-getting-there` activity is marked low confidence.
- **Rana Haven / Z.R.Q. buff cooldown.** CyreneDream lists these under "Daily Buff Missions" without a timer, so I used `unknown`.

## Possibly stale (CyreneDream page last modified more than 18 months ago and not re-confirmed)

- One Time Missions (2023-12): A.R.C. Academy rewards, starter missions, faction one-offs, Esther, Test of Faith, salvage hunts and Miner's Paradise.
- Zorra's HK (2022-10)
- Psyche Master (2023-01)
- Mazeweaver (2023-01)
- Tanhok (2024-02)
- Zyn'viathan (2024-02)
- Rana Haven (2023-12)
- MOB Instances (2023-11)
- Teleporters (2024-06): cross-checked against Nexus, so treated as current.
- Vendors (2022-10)
- Neff (2023-02)

Some of these are indirectly re-confirmed by newer official notes. For example, the A.R.C. Academy and Esther missions are listed as Prestige entry checks in 2025, and Selbor's trainee kit re-trade appears in the 2025-06 notes.

## Coverage gaps

- No official newcomer walkthrough exists for Cyrene. The Academy chain and the newcomer rotation are taken from CyreneDream and Entropia Codex.
- I did not verify current market prices or markup for tokens, badges, Zyn'viathan coins or Lazidol parts.
- These are not described in detail:
  - Tanhok weapon choices;
  - Hub vendor prices;
  - the Prestige keycard purchase steps;
  - Perfected rucksack recipe numbers;
  - the Summer 2026 / Sept 2026 mission numbers (kill counts) for the new Prestige missions.
- I did not watch any YouTube videos. A "Nightmare Nexus 2026 on Cyrene" video appeared in search, but I relied on MindArk's 19.10.3 note ("later in October") for timing.
- The live Cyrene Discord (the current home of announcements) cannot be read without logging in.
- The Hub is folded into `cyrene.json` as a tip, not a separate destination file.

## Sources (URL - published - accessed)

| Id | Title | URL | Published / last modified | Accessed |
|---|---|---|---|---|
| CD-REP | CyreneDream: Repeatable Missions | https://cyrenedream.org/daily-missions | created 2022-09-04, modified 2026-02-16 | 2026-11-26 |
| CD-ONE | CyreneDream: One Time Missions | https://cyrenedream.org/one-time-missions | modified 2023-12-09 | 2026-11-26 |
| CD-TP | CyreneDream: Teleporters | https://cyrenedream.org/teleporters | modified 2024-06-27 | 2026-11-26 |
| CD-PRES | CyreneDream: A.R.C. Prestige | https://cyrenedream.org/a-r-c-prestige | created 2025-04-01, modified 2026-02-12 | 2026-11-26 |
| CD-HUB | CyreneDream: HUB | https://cyrenedream.org/hub | modified 2025-07-25 | 2026-11-26 |
| CD-ZORRA | CyreneDream: Zorra's HK Epic | https://cyrenedream.org/zorra | modified 2022-10-22 | 2026-11-26 |
| CD-TANHOK | CyreneDream: Tanhok Ambassador Epic | https://cyrenedream.org/tanhok-epic | modified 2024-02-22 | 2026-11-26 |
| CD-ZYNV | CyreneDream: The Zyn'viathan Epic | https://cyrenedream.org/the-zynviathan-epic | modified 2024-02-27 | 2026-11-26 |
| CD-UTA | CyreneDream: Unstable Turrelion Assassinator Epic | https://cyrenedream.org/uta-epic | modified 2026-02-24 | 2026-11-26 |
| CD-STA | CyreneDream: Stable Turrelion Assassinator Epic | https://cyrenedream.org/stable-turrelion-assassinator-epic | modified 2025-08-19 | 2026-11-26 |
| CD-HEART | CyreneDream: Refurbished H.E.A.R.T. FAP | https://cyrenedream.org/refurbished-h-e-a-r-t-fap | modified 2025-06-18 | 2026-11-26 |
| CD-PSY | CyreneDream: Zyn'Tukano Psyche Master | https://cyrenedream.org/zyntukano-psyche-master | modified 2023-01-18 | 2026-11-26 |
| CD-RANA | CyreneDream: Rana Haven | https://cyrenedream.org/rana-haven | modified 2023-12-14 | 2026-11-26 |
| CD-ZRQ | CyreneDream: Robot Base Z.R.Q. | https://cyrenedream.org/robot-base-z-r-q | modified 2025-12-11 | 2026-11-26 |
| CD-MAZE | CyreneDream: Mazeweaver | https://cyrenedream.org/mazeweaver | modified 2023-01-15 | 2026-11-26 |
| CD-RANGER | CyreneDream: Imperium Ranger Info | https://cyrenedream.org/imperium-ranger-info | modified 2025-01-25 | 2026-11-26 |
| CD-VEND | CyreneDream: Vendors | https://cyrenedream.org/vendors | modified 2022-10-24 | 2026-11-26 |
| CD-SNOW | CyreneDream: Imperium Snow Base | https://cyrenedream.org/imperium-snow-base | modified 2026-10-08 | 2026-11-26 |
| CD-RUCK | CyreneDream: Zyn Rucksack Basic | https://cyrenedream.org/zyn-rucksack | modified 2024-09-15 | 2026-11-26 |
| CD-RUCKP | CyreneDream: Zyn Rucksack Perfected | https://cyrenedream.org/zyn-rucksack-perfected | created 2026-08-02, modified 2026-10-15 | 2026-11-26 |
| CD-SWEAT | CyreneDream: Sweating | https://cyrenedream.org/sweating | modified 2024-12-03 | 2026-11-26 |
| CD-VOUCH | CyreneDream: A.R.C. Tier 1 Limited Weapon Voucher | https://cyrenedream.org/a-r-c-weapon-vouchers | modified 2024-01-18 | 2026-11-26 |
| CD-AMPS | CyreneDream: Limited Amps | https://cyrenedream.org/limited-amps | modified 2025-12-10 | 2026-11-26 |
| CD-INST | CyreneDream: MOB Instances | https://cyrenedream.org/mob-instances | modified 2023-11-29 | 2026-11-26 |
| CD-ROY | CyreneDream: Roy Vulker's Armor | https://cyrenedream.org/roy-vulkers-armor | modified 2025-11-08 | 2026-11-26 |
| CD-NEFF | CyreneDream: Neff's Stim Pack | https://cyrenedream.org/neffs-stim-pack | modified 2023-02-28 | 2026-11-26 |
| CD-W25 | CyreneDream: Winter 2025 | https://cyrenedream.org/winter-2025 | modified 2025-12-16 | 2026-11-26 |
| CD-S26 | CyreneDream: Spring 2026 | https://cyrenedream.org/spring-2026 | modified 2026-04-01 | 2026-11-26 |
| CF-2504 | Planet Cyrene April 1st, 2025 VU Notes (Wayback) | http://web.archive.org/web/2026/https://cyreneforum.com/threads/planet-cyrene-april-1st-2025-vu-notes.9313/ | 2025-04-01 | 2026-11-26 |
| CF-2506 | Planet Cyrene June 10th, 2025 VU Notes (Wayback) | http://web.archive.org/web/2026/https://cyreneforum.com/threads/planet-cyrene-june-10th-2025-vu-notes.9344/ | 2025-06-10 | 2026-11-26 |
| CF-2510 | Planet Cyrene October 7th, 2025 VU Notes (Wayback) | http://web.archive.org/web/2026/https://cyreneforum.com/threads/planet-cyrene-october-7th-2025-vu-notes.9407/ | 2025-10-07 | 2026-11-26 |
| CF-2512 | Planet Cyrene December 9th, 2025 VU Notes (Wayback) | http://web.archive.org/web/20260517062716/https://cyreneforum.com/threads/planet-cyrene-december-9th-2025-vu-notes.9449/ | 2025-12-09 | 2026-11-26 |
| CF-2603 | Planet Cyrene March 31, 2026 VU Notes (Wayback) | http://web.archive.org/web/2026/https://cyreneforum.com/threads/planet-cyrene-march-31-2026-vu-notes.9484/ | 2026-03-31 | 2026-11-26 |
| MA-1890 | Entropia Universe 18.9.0 Release Notes | https://account.entropiauniverse.com/news/pages/2025/01/28/8564/index.xml | 2025-01-28 | 2026-11-26 |
| MA-1980 | 19.8.0 Release Notes (MindArk, Steam) | https://store.steampowered.com/news/app/3642750/view/1832700592800388 | 2026-05-19 | 2026-11-26 |
| MA-1990 | 19.9.0 Release Notes (MindArk, Steam) | https://store.steampowered.com/news/app/3642750/view/1836506165545261 | 2026-06-24 | 2026-11-26 |
| MA-19103 | 19.10.3 Release Notes (MindArk, Steam) | https://store.steampowered.com/news/app/3642750/view/1844115010503532 | 2026-09-22 | 2026-11-26 |
| MA-19110 | 19.11.0 Release Notes (MindArk, Steam) | https://store.steampowered.com/news/app/3642750/view/1846651706694218 | 2026-10-20 | 2026-11-26 |
| MA-UE5 | Unreal Engine 5: The Future of Entropia Universe is Coming Soon | https://store.steampowered.com/news/app/3642750/view/1841579228669629 | 2026-08-21 | 2026-11-26 |
| NX-TP | Entropia Nexus teleporters (Cyrene) | https://api.entropianexus.com/teleporters?Planet=Cyrene | n/a | 2026-11-26 |
| EC-CY | Entropia Codex: Planet Cyrene | https://www.entropiacodex.com/planets/planet-cyrene/ | n/a (c) 2026 | 2026-11-26 |
| EF-TT | Small guide to TTokens & Howling Mine Missions (Entropia Universe Forum) | https://forum.entropiauniverse.com/t/small-guide-to-ttokens-howling-mine-missions/280672 | 2025-12-26 | 2026-11-26 |
| ECN-CY | Entropia Central: Cyrene guide | https://www.entropiacentral.com/guides/planets/cyrene | 2026-08-13 | 2026-11-26 |

### Also consulted, not cited in JSON

- Entropia Museum VU list (https://www.entropiamuseum.com/vu): matched the MindArk 19.10.3 and 19.10.6 notes.
- Wayback CDX listings of cyreneforum.com thread titles: used to confirm Snow Base runs in Apr, Jul and Sep 2025; dates not used in the JSON.
- eux-9mx.pages.dev "Planet Cyrene — The Definitive Guide": unknown provenance, looks like a mirror. Rejected.
- SteamDB patch notes: blocked (403).
- be.entropiauniverse.com: certificate expired.
