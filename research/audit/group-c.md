# Audit group C: prerequisites and source quality

Reviewed 2026-11-26. Files: rocktropia, hell, secret-island, monria, dsec-9, toulan.
31 entries audited: **7 verified, 24 partial, 0 unknown**. Every entry now has a `prereqInfo` note, cited sources and, where needed, `unknowns`, short `diagnostics` and source warnings. No ids were changed and no entries were deleted.

## Method

- Opened every cited URL except one dead PDF (see below). MindArk release notes were read as raw first posts on the official forum, plus the account.entropiauniverse.com news pages for 18.9.0, 18.15.1 and 18.15.2.
- Checked the Entropia Nexus API (mission list, mission details, locations, search) for every audited mission and NPC. Nexus is crowd-sourced, so it is cited as kind "wiki". Each entry says when Nexus is the only source.
- Note on dates: since the forum moved (2026-06-01), threads posted before then show that date on every post. Source `published` dates in the data keep the original post dates.

## Source problems found (all files)

- **Monria 2025 directory PDF** (monria S25): HTTP 404 on two tries. Its `supports` text now says so. No audited entry relies on it alone.
- **Monria Guide to Everything PDF** (monria S9): it opens and the text can be extracted. Earlier notes treated it as unchecked. Its footer says 2024. It gives the hub teleporter waypoints, now used in monria-claim-hubs.
- **ROCKtropia 19.12.1 notes** (rocktropia S5): read straight from the official forum this time, not the Nexus mirror. `supports` updated.
- **Nexus teleporter pages** (rocktropia S22, hell H5): the waypoints are now confirmed by the Nexus API as well as the page text.
- **Token travel to ROCKtropia**: 18.15.1 (2025-06-17) listed it as broken. 18.15.2 (2025-07-01) fixed "interplanetary teleports usability" but does not name ROCKtropia. No later note says it was fixed. Added 18.15.2 and 19.2.0 as official sources in the ROCKtropia file.
- **Stale guides contradicted by newer official notes**: EntropiaCentral's ROCKtropia guide (updated 2026-08-13) and the Entropia Codex beginner page both say ROCKtropia has no Codex. The 19.12.0 notes (2026-11-11) supersede them. A warning was added to rocktropia-codex.
- **Secret Island** activity data still rests on a 2022 blog, a 2015 forum thread and undated fan pages. Warnings saying so were added to the travel and return entries.
- **Virtualsense sources** are mostly from 2019 to 2024. The DSEC-9 navigation guide was last edited 2026-09-21, and the event posts from Oct/Nov 2026 confirm the routes are still current.

## ROCKtropia

**rocktropia-travel-getting-there**: partial.
Official: you travel by token from a planet's main landing teleporter, it costs 10 tokens since 19.2.0, and the limit is 150 kg. Added a requirement to leave Setesh first, plus two diagnostics (overweight; Setesh sends you to Calypso). Updated the currency note to cite 19.2.0.
Unknown: whether token travel to ROCKtropia works today (no official fix), and the direct Setesh shuttle that rocktropia.com claims.

**rocktropia-ai-war-daily**: partial.
Every source (DailyEntropia Aug 2026, Entropia Codex, JoinEntropia, Nexus mission 5741) describes taking it straight from the recruiter. Nexus lists no prerequisite missions. Added the ROCKtropia travel step as a non-blocking prerequisite. Added diagnostics for "no AI spawn" (19.12.1 restored spawns near the moved Vixens) and "ran out of mission ammo" (one player's workaround).
Unknown: whether anything else is needed (no source says so outright), when the timer starts, and which weapon is supplied.

**rocktropia-cellphone-errand**: partial.
EntropiaCentral (Aug 2026) and JoinEntropia both start the errand at Big Boy with nothing before it. Both copy the 2016 community guide. Added two diagnostics: there is no tracker, so keep the NPC order; after the glam ingot, head east toward Try.
Unknown: hidden requirements, and whether the errand still works after 19.12.0 changed quest texts.

**rocktropia-codex**: partial.
19.12.0 says nothing is needed beyond hunting. Added a warning that older community guides deny the Codex exists. Added a diagnostic for the Codex display and claim bug that players reported in the 19.12.0 thread (no official fix noted).

**rocktropia-claimable-plots**: partial.
Official: plot tokens drop in loot and are used for plots near Club NEVERDIE. Added a diagnostic: players report that some plots have too few building points for the new homes (Nov 2026).
Unknown: how a token is redeemed, any extra condition, tradeability, number of plots, and drop rate.

**rocktropia-bar-job-hourly**: partial. **Prerequisite added.**
Nexus (missions 4346 and 5748) lists Alia's one-time "The bar Fly" (pick up 30 kegs at the Beer Garden) as required first. This was added as requirementsText, because no such activity exists in the data. Steps and reward were corrected from Nexus: 20 Thugs or Hustlers, reward a ROCKtropia Gold Coin. Previously the reward was "not stated". Rewrote the warning: this entry rests only on an undated guide and Nexus.
Unknown: the cooldown (the guide says hourly; Nexus gives none). Nexus also lists "Motorhead Madness" (kill 30 Motorheads) as unlocked by The bar Fly. It was not added as a new entry.

## HELL

**hell-travel-club-hell**: verified.
Players (Feb and Oct 2026) and a blog describe the same access: pick HELL in the drop-down of any ROCKtropia teleporter. No tokens are needed on ROCKtropia or Secret Island. Added requirementsText (be on ROCKtropia or Secret Island; the first visit downloads extra files).

**hell-halloween-zombie-kong**: verified.
The organiser's Oct 2026 post sets no entry conditions. Added unknowns: whether it runs again in 2027, and the loot pool.

**hell-monthly-global-competition**: verified (entry rules).
The thread's rules say who can enter and how. Added an unknown and rewrote the warning: the single source's latest round is March 2026, over 8 months old, and no later round was found.

**hell-legacy-missions**: partial.
Nexus shows each stage needs the previous one (Hackathon I→II; Little Devil I→II→III). Added that as requirementsText. Cited Nexus for Duty Calls (kill Kong) and The Great AI War (kill Virus Kong or Kong).
Unknown: whether 19.12.0's "ROCKtropia hunting chains" rule covers HELL and the ore Mining Raid chains. Nexus lists only five ore raid chains (Belkar, Blausariam, Iron, Lysterium, Zinc), so the other five ore names in older guides are unconfirmed. Nexus still uses the old "Horny" creature name.

**hell-key-instances**: partial.
Each instance needs a Hell Key, which is used up on entry, and is solo only (fan page and blog). Nexus confirms Hell Keys I to X exist.
Unknown: which tier opens which instance, any other unlock, entrance waypoints in HELL coordinates, and cooldown. Added a warning that the sources are undated, with no 2025-2026 reports.

## Secret Island

**secret-island-token-teleport**: partial.
19.2.0 confirms the route. The waypoint was missing; it is now set to NI Helper's exact Club NEVERDIE waypoint, matching Nexus location 347 (verified). Added 18.9.0 as the source for the 150 kg limit.
Unknown: token cost, whether you must have registered the teleporter first, and whether you can leave the same way.

**secret-island-travel-there**: partial.
Added two diagnostics from the 2022 blog: she offers the mission only if you carry a Rotten Banana (not a Bunch), and she works once per hour. Added a stale-source warning.

**secret-island-return-cnd-banana**: partial.
Unknown: the one-hour wait (one fan page only), and whether the token teleport works outbound. Added a stale-source warning.

**secret-island-gorilla-kill-points**: partial.
Nexus (mission 4743, "Hunt Things I (Gorillas)") places Archibald on Secret Island. This resolves the old "which Club NEVERDIE" doubt, and the warning was rewritten. Added the kill-point thresholds 3,200 / 6,400 / 12,800 / 25,600 from Nexus and EntropiaCentral.
Unknown: whether the 19.12.0 stop applies to Secret Island chains.

**secret-island-element-temples**: partial.
Requirement: a matching Sacred skull (2022 blog).
Unknown: which creatures drop the Fire and Forest skulls, whether Mogwas's hint is required, whether earlier Antidote steps must come first, and the temple waypoints. JoinEntropia prints them with the wrong area name.

## Monria

**monria-claim-hubs**: verified.
The partner guide (2024) says how each teleporter is obtained. DSEC Forensics is given; the Mining and Military camps must be collected; the cave teleporters up to Shub Cavern are reached by fighting through on foot, with no vehicles or teleport chips. Added verified waypoints from that guide for Forensics, Mining Camp, Military Camp and Shub Cavern. Previously they had none. Added the Nexus "3 Hub" teleporter for Monria Hub, marked unverified. Added a warning that the guide is from 2024 and the 2025 directory is dead.

**monria-get-there**: partial.
Spelled out Yamato sign-up and the free-travel groups from the partner fee thread: Monrian or Toulan born, estate owners at Monria, DSEC9 or Toulan, and Toulan citizens. Added Kronan's 01:25 request deadline.
Unknown: a token link to Monria, and whether the Yamato is back to normal after September 2026.

**monria-to-dsec-9**: verified.
Added a staff-sourced diagnostic: DSEC9 is hidden lower in the drop-down, so scroll it (Oct 2024). Noted that this entry duplicates dsec-9-enter-from-monria.

## DSEC-9

**dsec-9-enter-from-monria**: verified. Same route sources and the same drop-down diagnostic.

**dsec-9-mountain-of-madness-route**: verified. The partner guide was last edited Sep 2026. The beginner-chain walkthrough assumes this route is done first.

**dsec-9-welcome-to-the-dark-side**: partial.
The partner guide says everyone can do the chain and needs a sweating tool. The walkthrough assumes the Lotus teleporter and the Mountain area are unlocked; that was added as requirementsText. Added the staff reply to a Monrian-born newcomer (2023) as a source, and a route diagnostic.
Unknown: whether the mining step supplies a finder and probes.

**dsec-9-frustrated-local**: partial.
The mission thread (Apr/Jun 2025) lists no requirement.
Unknown: whether the beginner chain must come first, and teaming (players were unsure in June 2026).

**dsec-9-church-hunt / dsec-9-church-mine**: partial.
Partner guides: the Worshipper stage is open from the start; more opens at 150 Elder Tributes. Nexus lists the Shrine tribute missions with 16 h timers and no prerequisites. Added a finder and probes, and Initiate rank for the weekly, to the mining entry. Added a diagnostic: a contract held at the Toulan Church blocks taking it here.
Unknown: whether the beginner chain, which sends you to the Church, must be finished first.

## Toulan

**toulan-get-there**: partial. Same travel details as Monria. Unknown: a token link to Toulan.

**toulan-ahlan-wedding-ring**: partial. **Conflict recorded.**
Staff (2021) call it the one beginner mission open to everyone. The 2021 visitor guide starts with Salam and Bilal before Ahlan. This conflict is left as an unknown. Added diagnostics: relog if the ring does not update (Aug 2026 player, confirmed by staff), and talk to Salam and Bilal if Ahlan offers nothing.

**toulan-born-starter-chain**: partial. **Eligibility corrected and expanded.**
Toulan-born means the avatar was created on Toulan (the Toulan_Player tag) or is Monrian-born. New from the official Nov 2026 event notice: finishing the Toulan Citizenship Mission makes you eligible for Toulan Born missions. Added a player-reported reward (2 PED Universal Ammo at Labiba, Jun 2026). Added diagnostics: no team loot; at Faiza, step 7 needs the 20 TabTab Teeth (a skip option exists); the ring needs a relog.
Unknown: how much of the chain citizens can do, and redoing it after the old open version.

**toulan-nawacore-mk1**: partial.
Partner post (Dec 2020): visitors hunt 100 TabTab or pay 10,000 Vibrant Sweat; Toulan-born get it on arrival. Nexus mission 4532 agrees and lists no prerequisites. Added the NawaCore Agent waypoint from Nexus (unverified). Added a warning that the detailed source is from 2020.

**toulan-worship-elder-gods-start**: partial.
The Church guides mention no condition.
Unknown: whether a NawaCore is needed (the daily list says hunting dailies need one), and how a visitor first gets the Pit North teleporter. Added the shared-contract diagnostic.

**toulan-thana-mini**: partial.
Added a finder and probes. A Feb 2024 player adds Drilling or Surveying as reward choices for the 500-point version; noted in the reward text.
Unknown: whether a NawaCore is needed, and whether both contracts can be held at once.

## Still open (most important)

1. Whether token travel to ROCKtropia, Monria or Toulan exists and works now (no official confirmation).
2. Whether 19.12.0's end of new hunting chains covers HELL and Secret Island chains.
3. The visitor path to Ahlan's Wedding Ring (direct, or after Salam and Bilal).
4. Whether Toulan's Church and Thana contracts need a NawaCore.
5. How ROCKtropia plot tokens are redeemed.
6. Any first-hand Secret Island report newer than 2022.

Blocked sources: none, apart from the dead 2025 Monria directory PDF. The account.entropiauniverse.com news page timed out once in Python but loaded with curl.
