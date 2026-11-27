# Prerequisite and source audit: group B (Calypso, Arkadia, Next Island, Ancient Greece)

Audited 2026-11-26. 24 entries. Final prerequisite status: 6 verified, 11 partial, 7 unknown.

Method: opened every cited URL that could be fetched. Searched the official Entropia Universe forum. Pulled the Entropia Nexus mission records (community database, crowd-sourced) for every matching mission and followed their prerequisite links. "Verified" is used only where a source states the conditions outright. If sources simply describe a mission without naming any gate, the status is "unknown" or "partial", never "verified".

## Sources that could not be read

- **forum.nextisland.com** (Next Island 18.12.0 and 18.12.1 notes, ids N15/N19) does not resolve in DNS. Both files now say so in the source's "supports" field. The Thebes facts that cited them still rest on NI Helper.
- **Reddit** (Iron Road thread, C6) returns HTTP 403 to automated readers. It could not be re-read, and a warning now says so.
- **YouTube** (N8): the title and channel were confirmed through oEmbed, but the video itself was not reviewed. The publisher is corrected to the channel name.
- **arkadiaforum.com** serves an invalid TLS certificate. The pages are still readable and match what is cited.

## Calypso

### calypso-setesh-transport: partial
- Added MindArk staff's Setesh feedback-thread post (forum t/285160, 16 Sep 2025) as source C37. It says the Camp Icarus VTOL to Setesh needs Mentor skill 2+ or a highest combat profession of 5 or lower. Otherwise you fly to Setesh Space Station.
- requirementsText now keeps access apart from eligibility. New avatars get the one-way trip after the Setesh main chain (the Setesh file covers this). The VTOL rule is official. The pilot and station routes have no published rule.
- I did not add a Setesh activity as a prerequisite. It would wrongly block existing Calypso players who travel to Setesh.
- Waypoint fix: copied exactly as the player posted it (`[Setesh, 67634, 68354, 299, skip]`) and now marked verified. The old label "Skip Terminal" was not in the source.
- Diagnostics added, from the "Leaving Setesh again?" thread (Dec 2025 to Mar 2026): Calypso is missing from the Setesh teleporters, the departure NPC only works once, and storage is per planet.
- Unknown: whether the Port Atlantis pilot or the skip terminal has any requirement, and whether the trip can be taken before the chain is finished.

### calypso-interplanetary-travel: verified
- The 18.9.0 notes (28 Jan 2025) and 19.2.0 notes (9 Dec 2025) give every condition: tokens (now 6 or 10), a 150 kg limit, and a Space Thruster to launch yourself, which only works outside PvP areas. No mission or skill is needed.
- Activity unknown added: whether every moon and station link charges the same fare.

### calypso-port-atlantis-chain: unknown
- The 19.12.0 notes (11 Nov 2026) only say a newcomer chain starts in Port Atlantis. Web and forum searches found no start NPC and no requirement.
- Unknowns listed: the start NPC, whether Setesh must be finished first, whether veterans can take it, and whether its "Iron Road" step is the older mission of that name. Nexus has an "Iron Road" record with no details, and players mentioned one in 2016 and 2023.
- Warning added that the Iron Road tip rests on one Reddit post that is currently unreadable.

### calypso-terminal-hunt: unknown
- No source names any requirement. The Nexus records for the hunting categories (for example /missions/5776) are unfinished stubs, so I logged them but did not treat them as evidence.
- **Citation fix:** C12 pointed at post #6, which only says bonus rolls are random. The rolls, the 16 h timer and the waypoint are in **post #7** (Arja, 20 Aug 2025), so the URL and title now point there.
- **Conflict logged:** players and Entropia Codex say 16 h from pickup, while Nexus says 20 h from completion. A warning and an unknown were added. The cooldown value was not changed.

### calypso-argonaut-cave: partial
- **Missing prerequisite found.** A 2017 player post (forum t/268368/30) says a short Argonaut Island chain unlocks this daily. Nexus shows the chain: "Scare Tactics" (Harzol Kenna) → "Argonautical Assassination" (kill 3 Argonaut Leaders) → "Research Recovery (Daily)". This is added as requirementsText, because those missions have no activity entries.
- The official 2017.4.1 content release says the cave is always open, its contents depend on holding the mission, and it is solo-only. A diagnostic was added for this.
- Diagnostic added from the "Research Recovery (daily)" thread (Sep to Oct 2024, with a MindArk staff reply): a frozen Argonaut you cannot hit was cleared by leaving and re-entering the cave, or by re-tagging from range.
- Conflicts logged as unknowns. Target: "50 Argonaut Young" (player) or "50 Argonauts plus 5 pieces of equipment" (Nexus). Timer: 16 h (player) or 20 h from completion (Nexus).
- Unknown: whether the unlock chain survived the 19.2.0 newcomer rebuild, and what comes before Scare Tactics.

### calypso-point-of-origin: partial
- New source: "Help With Fort Lahar Mission Point of Origin" (forum, 15–18 Nov 2026). A player got the mission after finishing a Fort Lahar swamp mission. The door did nothing until 19.12.1, then it worked. The lab can be re-entered, and a box after the boss gives RDI Designs (1,000 are handed in at Fort Medusa for 1 PED of ammo).
- Summary, steps and rewards were updated from this thread. Before, the entry only had the patch line. Two diagnostics were added.
- Unknown: which swamp mission unlocks it, whether a key item is needed, and whether the mission itself repeats.

## Arkadia

### arkadia-travel: verified
- Same official token and thruster rules as Calypso. The 18.9.0 notes were added as A32 for the thruster rule.
- **Correction:** the entry said Kronan "boards" at Celeste Quarry or Twin Peaks. Kronan's "how it works" page says those are where its ticket seller stands, and passengers are then summoned to the ship. The summary and step were reworded to match, and the A2a/A2b supports lines now say which page backs what.

### arkadia-passport: verified
- The Arkadia Archive (updated 24 Aug 2026) and the Nexus record (/missions/4331) agree: hand 10,000 Vibrant Sweat to the Passport Officer, with no earlier mission. The Archive's newcomer guide says the passport is for avatars not born on Arkadia. That settles the old "unconfirmed whether born avatars face the gate" note in requirementsText.
- Warning added: no Planet Arkadia partner page was found, so this rests on two community sources.
- Unknown (activity level): whether Arkadia-born avatars can take it at all, and whether the passport item can be traded.

### arkadia-underground-trip: partial
- Access is sourced: any Arkadia teleporter's dropdown (partner FAQ from 2014, plus an undated firsthand guide that adds Underground teleporters come pre-discovered and may need a download).
- From the Arkadia Archive Sal'Diresh page: Professor Dorne only responds if you carry at least one Arkadian Treasure Map, and entry needs a team (a team of one works). Added as requirementsText and two diagnostics.
- Warning added: access rests on a 2014 FAQ and an undated guide.
- Unknown: whether the Underground Traveller needs the passport.

### arkadia-insignia-hunt: unknown
- No source names a gate. The newcomer guide lists the passport first, but only as a suggested route.
- **Waypoint fix:** the surface Traveller had no waypoint. The cited Daily hunting page shows `[Arkadia, 31185, 9556, 122, Waypoint]`, so it is now added and verified. It is the same spot as the Gatherer's Mysterious Stranger.
- Category payouts (1/2/3 Insignias) were added to the step from the same page.

### arkadia-gatherer: unknown
- One fan page with no requirements stated. A single-source warning was added. The count of items, the reward size and the timer are listed as unknowns.

### arkadia-insignia-mine: unknown
- The Archive and the partner's 19.2.0 notes describe the missions with no gate. Nexus has an ACA newcomer chain ("ACA – Mining Training" and others), but nothing links it to Clive Forester's challenge, so it is listed as an unknown, not added as a prerequisite.

## Next Island

### next-island-travel: verified
- Official token rules, plus Virtualsense's own fee post: the Yamato is 6 PED unless you are Monria- or Toulan-born, own a Virtualsense estate, or have done Toulan Citizenship. This is now in requirementsText.

### next-island-starter-missions: partial
- NI Helper starts the tour with the welcoming NPC and is written for both new avatars and visitors. Nexus lists the beach Hunting (Joe) and Mining (Herbert) missions with no prerequisite (source N26). Step 1 now names the welcoming NPC. The jumpsuit for 50 Animal Hide was added to rewards.
- Unknown: whether non-Next-Island-born avatars (for example those who started on Setesh) still get the gear, and whether the reward is one per account.

### next-island-sebastian-piglets: partial
- Nexus record "Sebastian's Find" (N24): repeatable, 200 piglets, 1,600 chips, no prerequisite. A diagnostic was added from the firsthand guide: not every Mountain Boar counts, but the fenced group did.
- The Enjar guide is about four years old (relative date on the page). Its supports line now says so, and a warning was added.

### next-island-sebastian-screechers: partial
- NI Helper lists the Screecher daily with no "Mission Required" line, while it does list VIP requirements for the other new dailies on the page. That is good but indirect evidence. The partner notes it also cited are unreadable.

### next-island-crystal-hoarder: partial
- Nexus (N25): Hiresh at Kamba Outpost, 100 kills of Cyclops, Arges or Brontes, rewards scaling by target, 20 h from completion, no prerequisite. Entropia Central (via NI Helper) says completing it once is stage 1 of the Resa V.I.P. entry. The summary and step were updated. The kill count and reward values are marked as Nexus-only unknowns, and the timer note now cites both sources. The cooldown kind was left as "unknown".

### next-island-multi-faction: partial
- The Nexus page lists six Juliana hubs, 50 of an activity, and no prerequisite. Step 1 now lists the six hubs. One assignment per day is confirmed by Nexus and the guide.

## Ancient Greece

### ancient-greece-orpheus-cave: verified
- NI Helper gives the conditions (be on Next Island, download Ancient Greece, use the Medium or Large teleporter view). The partner's news page confirms the teleporter is unlocked on arrival. A diagnostic was added for the missing destination. A warning notes the download and map-size steps come from an undated fan guide.

### ancient-greece-falcata: partial
- NI Helper and Nexus (G1, G2) agree on Meeting the Gods → Talk with the Elder → Looking at Distant Pasts, and that it starts at Orpheus' Cave on the Ancient Greece side. Step 1 now says where it starts. A diagnostic was added: talk to Penthesilea twice before Creon.
- **Conflict logged:** Nexus says to talk to the Haruspex Elder *before* Meeting the Gods, but NI Helper puts the Elder after it. This is left as an unknown.
- Entropia Central's item page shows trade-chat listings for the Falcata (TT+5 to TT+10 through Nov 2026), which suggests it is tradeable. This is recorded as an unknown, not a fact.

### ancient-greece-islander-pursuit: verified
- Next Island's own 18.4.0 notes (on the partner news page) say two Thebes NPCs offer the Islander quest, open to everyone including True Islanders. The only requirement is being in Thebes. The N7 supports line was updated.

### ancient-greece-key-fragments: unknown
- NI Helper names Alexandra and her options. On the same page it says "all SVIP missions need the five V.I.P.s and Becoming an Islander", but it is unclear whether that covers the Thebes NPCs. This is listed as the main unknown.
- Diagnostic added: the 500-Asterion "Daily Asterion Hunt" at Tanzanite View is a different mission and needs Haruspex V.I.P. (Nexus, G5).
- Warning added: the partner notes it cites are unreadable.

### ancient-greece-nots: unknown
- Same SVIP ambiguity as above, and the same unreadable partner notes. No other source was found.

### ancient-greece-gorgon: partial
- **Missing prerequisite found.** NI Helper and Nexus (G3, G4) put "Find Batiatus" (from the Haruspex Elder at Orpheus' Cave) before Deliver Us from the Dark Queen. Step 1 and requirementsText now say this, and also list the Vellum, Blood of the Gods and Block Chisel hand-ins.
- Warning added: do not abandon the mission or sell the Block Chisel blueprint, because both are given only once.
- Three diagnostics added: the Shade missions are not offered, the blueprint is lost, and Vellum only drops from creatures named exactly "Cyclops".
- Unknown: entry requirements for the 18.12.0 dungeons and key route, because those partner notes are unreadable.

## Not done

- No game check was possible. Nothing here has been confirmed in game.
- The other entries in these four files were not audited and are still "unreviewed".
- No cooldown values were changed. Timer conflicts are recorded as warnings and unknowns only.
