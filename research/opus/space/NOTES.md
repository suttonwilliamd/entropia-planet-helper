# Research notes: space, crossworld, setesh (and the destination census)

Researcher: Opus research child, working in research/opus/space/. All pages were accessed on 2026-11-26. This was desk research only. I did no in-game checks.

## Method
- **Official news.** MindArk's news from Nov 2025 to Nov 2026 came in full through Steam's public news API for app 3642750 (`api.steampowered.com/ISteamNews/GetNewsForApp`), about 100 posts. The official account/news pages and Steam announcement pages are rendered with JavaScript, so the API was the reliable route. The JSON files cite the steamstore "externalpost" URLs. Those redirect to the Steam announcement for the same post.
- **Older official notes and forum threads.** Release notes from 18.9.0 to 19.2.0 and the player threads were read through the Entropia Universe Forum's JSON API (Discourse). The forum mirrors the official notes as "Bertha_Bot" posts, and MindArk staff posts are flagged as STAFF.
- **Official beginner's guides.** be.entropiauniverse.com serves an expired TLS certificate. I read the pages with curl in read-only mode. They are undated, and the space guide is partly stale.
- **The lead's cross-check URL.** account.entropiauniverse.com/news/pages/2025/11/04/5561 was fetched and confirms the 19.1.1 notes. It is now cited in space.json as S1911A.
- **Community sources.** These came from forum threads, the featurebase "Space Mining Guide", thehowlingmine.com (run by NEVERDIE Studios, the Howling Mine operator, and promotional in tone), entropiahub.com (a fan space map), and Ripcraze. For Ripcraze, I read its cooldown table and points of interest from the site's public JavaScript bundle.
- **Videos.** Two YouTube videos were found, but I did not watch them. I cite neither in the JSON:
  - "How to get to Setesh and acquire the SET-P1 Civilian Sidearm", channel avarupter, published 2025-09-30.
  - "Entropia Universe- The Setesh breakdown", channel MissWatson221B, published 2025-10-30.

## Confirmed (official, 2025-11 to 2026-11)
- **Setesh is live.** It has been the starter moon since 19.0.0 (2025-09-16) and replaced Thule. Fixes and changes to Setesh content shipped in 19.10.1 (Vivo S10 now 2 PED TT) and 19.12.0 (Small Iron after Cliffchaser Run). 19.5.3 fixed a bug that sent some new accounts to Thule instead.
- **Token teleports.** Station-to-station costs 6 tokens and planet-to-planet costs 10 (19.2.0, 2025-12-09). The 150 kg cap and the free station-to-planet teleport date from 18.9.0. 19.11.0 fixed teleports that did not consume tokens.
- **Free intro ship.** The Howling Mine tutorial gives a FREE ship (19.1.1, 2025-11-04, two official copies). The Pioneer Mining Ship is a different thing: it is material-gated, and you must bring materials for its parts (Howling Mine Update, 2025-01-28). space.json keeps them as two separate entries with explicit requirements, as the build lead asked.
- **Space mining changes.** ND asteroids sit outside the lootable zone (19.1.0) and got a Codex challenge (19.2.0). Combat buffs no longer apply to space mining (19.1.0). The 19.5.0 rebalance made some materials space-only, and laser blueprints come from the Howling Mine vendor.
- **Space map and warp.** The space map was reworked (19.10.1). Mothership guest lists now need the guest's consent (19.10.1). Warp fixes shipped in 19.10.6.
- **New Horizons Bonus Track.** It runs from 2026-10-20 08:15 UTC to 2027-01-01 00:00 UTC. It has 60 ranks, then repeatable ranks, and a shared pool of 500,000 Unreal Tokens.
- **Mayhem in 2026.**
  - Easter: 31 Mar to 13 Apr.
  - Summer: 16 Jun to 25 Aug.
  - Halloween: 30 Oct to 13 Nov.
  - Merry Mayhem 2025 ran 10 Dec 2025 to 15 Jan 2026.
  - Merry Mayhem 2026 had not been announced as of 2026-11-26.
  - Tokens are non-tradable. Items bought from the Mayhem traders are tradable.
- **Recruit a Colonist (19.5.0).** The recruit gets +25% skill gain for 7 days. The recruiter gets +10% for 24 hours plus tiered rewards.
- **Unreal Engine 5.** The client is "scheduled for release before Christmas 2026" (MindArk, 2026-08-30).

## Contradictions and how I resolved them
- **Token costs.** It was 15 tokens in Jan 2025 and in Jun 2025 (18.15.1). The newest official numbers, 6 and 10 from 19.2.0, are used. A Dec 2025 player guide still quoted a 15-to-10 change, which is consistent with this.
- **Getting to Setesh as an existing player.**
  - A Sep 2025 MindArk preview said existing players can travel "at any time without the requirements Thule had".
  - The staff feedback thread from the same day says the Camp Icarus VTOL needs Mentor skill 2+ or a highest combat profession of 5 or lower.
  - Players in Mar 2026 use a shuttle pilot near the Port Atlantis teleporter.
  - All three routes are listed, with a warning.
- **Teleporting from a station to its planet.** The official space guide (undated, old) says the trip is one-way and that some teleports cost 17.5 PED. The 2025 release notes supersede this: station to own planet is free. The guide is marked as partly outdated.
- **Scottium.** Older guides say Scottium comes only from M-types in the lootable Howling Mine belt. 19.1.0 added ND asteroids with Scottium outside that zone, at a lower yield according to the operator's guide. One Nov 2026 player claims M-types now also spawn in safe space near Rocktropia. That claim is unconfirmed and flagged.
- **Setesh skip-terminal waypoint.** I copy the forum's exact text: `[Setesh, 67634, 68354, 299, skip]`. Sol's calypso.md uses the same coordinates with the name "Skip Terminal". The coordinates agree.

## Stale or low-confidence items
- **Possibly stale (Jan 2025, about 22 months old, not re-confirmed).** These are the Contractor dailies, Pioneer ship mission steps, Space Pirates and Outlaw Zones. Each is marked "possibly stale".
- **Howling Mine Employer job pay.** The figures (about 2 PED per job, "resets every 24 hours") come from the operator's promotional site. I modelled the cooldown as a rolling 24 hours, with a note that the source does not say when the timer starts.
- **Genesis Star and Contractor daily timers.** These are not published, so the cooldown is set to "unknown".
- **General daily timers.** They are personal and start when you finish. Lengths vary (16, 20, 21, 23, 24 or 168 hours). This comes only from community trackers (Ripcraze bundle data, forum threads from 2017 and 2025). Confidence is medium.
- **Station waypoints.** They come from an undated fan map. The Howling Mine entry there (`79228, 79228`) looks malformed, so I left it out.
- **Teleportation Token price.** The only price is one Jun 2025 player remark (about 80 PED for 15 tokens). I gave no PED estimate.

## Coverage gaps
- **Codex rules.** No official current page gives rank counts or reward categories. The official beginner page covers only the basics, so I kept it to that.
- **Mentor program.** There is no current official source (only a 2011 press release), so I left it out of the JSON.
- **Setesh missions.** I found no full walkthrough. Mission names come from release notes. The order and rewards of many side missions are unknown.
- **Lars.** The post on the fishing NPC Lars does not say which camp he is at.
- **No visual checks.** No in-game or video confirmation was done. All waypoints come only from cited text.

## Sources (URL – published – accessed 2026-11-26)
Official (MindArk; Steam mirror base is https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/ followed by the ID):
- 19.12.1 Patch Notes – 1849458702692934 – 2026-11-17
- 19.12.0 Release Notes – 1849192144178196 – 2026-11-11
- Halloween Mayhem 2026 – 1847286114035889 – 2026-10-23
- 19.11.0 Release Notes – 1846651706694218 – 2026-10-20
- 19.10.6 Release Notes – 1846651706673572 – 2026-10-14
- Locate and Eliminate RX Units: Unreal Edition – 1844115010503642 – 2026-09-22
- 19.10.1 Release Notes – 1843481262704136 – 2026-09-15
- Tier Boost Weekend! – 1842846814452418 – 2026-09-07
- The Next Era Starts Here – 1842212951307426 – 2026-08-30
- 19.9.0 Release Notes – 1836506165545261 – 2026-06-24
- SUMMER MAYHEM 2026 – 1834602721201100 – 2026-06-09
- 19.8.1 Release Notes – 1833968530899769 – 2026-06-02
- 19.7.0 Release Notes – 1832065502823359 – 2026-05-12
- 19.6.1 Release Notes – 1830163047267983 – 2026-04-21
- Fishing & Cooking LIVE – 1830163047254349 – 2026-04-15
- 19.5.3 Patch Notes – 1828441623111530 – 2026-03-31
- Major Update: 19.5.0 Release Notes – 1827626365765242 – 2026-03-24
- EBN News Bulletin: Cargo Commandeered Close to Calypso – 1827626365758969 – 2026-03-20
- Easter Mayhem 2026 – 1827626365756949 – 2026-03-20
- Mayhem Vendor Restock and Additions – 1825093633193935 – 2026-02-23
- Dev Blog: The Road to Unreal Engine 5 – 1823825466509297 – 2026-02-10
- 19.2.0 Release Notes – 1818118366184963 – 2025-12-09
- Merry Mayhem 2025 – 1818118366175542 – 2025-12-05
- Steam news index (API): https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=3642750&count=100 – n/a
- 19.1.1 Release Notes (account news): https://account.entropiauniverse.com/news/pages/2025/11/04/5561 – 2025-11-04

Official release notes on the forum (https://forum.entropiauniverse.com/t/ followed by the ID):
- 287741 (19.1.1) – 2025-11-04
- 283998 (19.1.0) – 2025-10-28
- 284406 (19.0.2) – 2025-09-23
- 287878 (19.0.0) – 2025-09-16
- 280474 (18.15.1) – 2025-06-17
- 287506 (18.9.0) – 2025-01-28
- 279066 (New Space Features) – 2025-01-28
- 283421 (Howling Mine Update) – 2025-01-28
- 285160 (Setesh feedback thread, staff opening post) – 2025-09-16
- 286750 (Hunt the Thing, MindArk reply) – 2025-02-03

Official guides (undated):
- https://be.entropiauniverse.com/entropia-universe/beginners-guide/space-guide/
- https://be.entropiauniverse.com/entropia-universe/beginners-guide/transportation/
- https://be.entropiauniverse.com/entropia-universe/beginners-guide/skill-rewards/

Mirror of official text:
- https://www.entropiamuseum.com/news/view/upcoming-update-new-onboarding-experience/ – 2025-09-03

Operator / partner (NEVERDIE Studios):
- https://www.thehowlingmine.com/ – undated
- https://www.thehowlingmine.com/guides/Asteroid-mining-101 – 2026-02-17

Community guides and tools:
- https://entropiauniverse.featurebase.app/help/articles/8086562-space-mining-guide – about early 2026 ("9 months ago")
- https://entropiahub.com/entropia-universe-space-map/ – undated
- https://entropiahub.com/news/ – undated (Toulan monthly event)
- https://ripcraze.com/ and /daily (bundle data) – undated
- https://playentropiauniverse.com/setesh – undated. Checked, but it is generic, so not cited.

Forum player threads (https://forum.entropiauniverse.com/t/ followed by the ID):
- 853745 – 2026-11-14
- 853753 – 2026-11-15
- 255780 – 2026-11-11 (post date)
- 853118 – 2026-10-17
- 283905 – 2025-10-18 (later posts to 2026-10)
- 852247 – 2026-09-08
- 852091 – 2026-09-01
- 287028 – 2026-08-04
- 851340 – 2026-07-23
- 288022 – 2026-03-23
- 281409 – 2026-03-01
- 283276 – 2026-03-01
- 284691 – 2026-01-30
- 288277 – 2025-12-29
- 280672 – 2025-12-26
- 284073 – 2025-12-07
- 285688 – 2025-12-05
- 287410 – 2025-09-16
- 287662 – 2025-02-15
- 283088 – 2025-02-11
- 269168 – 2021-06-04 (edited later)
- 247866 – 2017-03-19

## Blocks
- **Steam announcement pages.** These render with JavaScript, so WebFetch got empty bodies. I used the Steam news API instead.
- **Official Bulletin URLs.** entropiauniverse.com/bulletin/... URLs return 404 since the Jan 2026 website overhaul.
- **be.entropiauniverse.com.** The certificate is expired. I read the pages with curl in read-only mode.
- **entropiaplayer.com/wiki/codex.** It redirects to a forum homepage with no Codex content.
