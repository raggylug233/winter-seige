# Winter Siege deployment plan — briefing for review

This document summarises a squad-deployment plan for the Whiteout Survival **Winter Siege** event so that another model (or person) can check the reasoning, challenge it, or propose a better plan on the same facts. Everything below comes from in-game screenshots taken 2026-09-16/17, the in-game Rules Overview, and a simulation whose assumptions are stated. Where something is an assumption rather than a rule, it says so.

Repository with the data, generator and simulator: https://github.com/stevenbower/hieroglyphics (live page: https://stevenbower.github.io/hieroglyphics/).

## 1. The battlefield (from our screenshots — differs from every public guide)

Public guides and creator videos describe 4 strongholds with 30 squads each. Our battlefield has **6 strongholds with 20 squads each**:

| Stronghold | Tier | Stars per normal squad | Stars per Warden |
|---|---|---|---|
| 1 | Empowered | 3 | 6 |
| 2, 3 | Advanced | 2 | 4 (assumed double; confirmed for the other tiers) |
| 4, 5, 6 | Primitive | 1 | 2 |

Map connections (from the "Switch Garrison Stronghold" screen): **4 → 2, 5 → 2 and 3, 6 → 3, then 2 → 1 and 3 → 1.** Strongholds 4/5/6 are the front, 2/3 the middle ring, 1 the core.

## 2. Rules (verbatim substance of the in-game Rules Overview)

- **Squads.** Each Chief sets up 2 squads and garrisons them in any friendly stronghold. The same squads attack in the Battle Phase. A hero can be in only one of a player's two squads.
- **Garrison selection.** When Preparation ends, a set number (20) of the most powerful squads in each stronghold form its garrison and add Stars. Squads not selected can still attack. R4/R5 can move any member's squads and appoint one Warden per stronghold (from that stronghold's top 5). Everything locks at the end of Thursday UTC.
- **Hearts.** A normal squad has 4 Hearts, a Warden 5. Each defensive defeat removes 1 Heart. When all Hearts are gone the squad is defeated and its stronghold loses that squad's Stars. Stars are lost only then — a squad with 1 Heart left still counts fully.
- **Unlocking.** "All defender squads garrisoning the current stronghold must be defeated in order for your forces to attack the next connected strongholds." So an attacker must fully clear one front to attack the Advanced stronghold(s) it connects to, and fully clear an Advanced stronghold to attack Stronghold 1.
- **Morale (defenders only).** Squad stats = stats at lock × morale. Morale starts at 100% and drops with each *defender victory*: −10% while above 80%, −5% at or below 80%, **floor 60%**. Losing a Heart resets morale to 100%. Attacker morale is always 100%.
- **Attack attempts.** Each squad starts with 3 and gets 1 restored every 2 hours, at most 7 restored → 10 per squad, 20 per player. Injured troops recover after every battle; no troops are lost.
- **Result.** The alliance that reduces the other side to 0 Stars first wins. Otherwise, more remaining Stars wins. If tied, higher total troop power among surviving squads in strongholds wins. If still tied, the side that reached that number of Stars later wins. If both sides have equal Stars before *and* after the Battle Phase, both lose.
- **Bonuses that do not apply:** city combat bonuses, state positions, President skills, territory buffs, Frost Dragon titles, hero exclusive-gear *skills* (the gear's stats do count). Pet skills are on by default.
- **Sparring.** Once all enemy strongholds are at 0 Stars, further attacks are sparring and change nothing.

## 3. The roster

112 squads from 56 players, sorted by power. Top 20 range 1.41B–690M; ranks 21–60 range 680M–450M; ranks 61–112 range 450M–149M. Nine squads are ≥1B. Full list: `data/squads.csv` in the repository. Four squads (Mai ♡ ×2, CANSæRBæRæ ×2) were taken from a Gemini-produced plan and are unverified in-game.

## 4. How we reasoned about it

1. **An attacker maximises Stars per attack.** A weak squad dies in 4–5 attacks wherever it is. A squad stronger than most enemy attackers has to be baited down first: with the 60% floor, roughly 15–30 attacks for a 1B+ squad against an equal enemy, and it cannot be killed at all by an enemy whose best squad is under 60% of its power.
2. **Therefore weak squads belong where a squad is worth 1★** (the fronts), or behind gates (Stronghold 1, which requires a front *and* an Advanced stronghold to be fully cleared first). Weak squads in 2★/3★ slots are the enemy's best targets.
3. **Strength is a toll, and it only counts on the path the enemy takes.** Under path unlocking the enemy picks one front, so strength spread across the three fronts is one-third efficient; strength in the Advanced ring is one-half efficient; Stronghold 1 is on every path but is reached after 60★ are already gone.
4. **The front Warden is the exception.** It is the one squad that *must* be killed (five times) before the Advanced ring opens. A whale there is the most expensive gate on the map, and an enemy that can't bait it down never gets past the fronts.
5. **Fill every high-value slot.** An empty slot in Stronghold 1 forfeits 3★ before the battle starts; the empty slots should be at the fronts.
6. **Against a much stronger enemy, layout stops mattering.** If their top squads beat ours outright, nothing we garrison is a toll and only the Heart count on the path slows them; every layout loses 130–190★ once they land 4+ attacks per squad. Placement decides close matchups.
7. **With 10 attacks per squad (~1,120 per side) and ~500 Hearts on the board, a full wipe is possible in principle**, so the "first to zero" rule makes attack throughput on battle day matter as much as the layout.

## 5. The simulation

`sim.py` in the repository. The enemy is our own roster scaled by a power factor (0.85, 1.0, 1.15). It respects the unlock paths; an attack wins with probability sigmoid(6 · ln(attacker power / (defender power × morale))); the attacker uses the weakest squad with ≥60% win chance, or baits with its weakest squad when none can win; morale follows the in-game rule; each enemy squad has N attacks and eliminated squads keep attacking. Two attacker behaviours: **coordinated** (commit to the cheapest stronghold to clear, then the next on the path) and **greedy** (always the best Stars-per-expected-attack target reachable). 16 runs per cell. Output is Stars lost (of 202) at 3 · 4 · 5 attacks landed per enemy squad (they have 10; sleep and wasted attacks reduce the real number), written coordinated/greedy.

| Layout | ×0.85 enemy | equal enemy | ×1.15 enemy |
|---|---|---|---|
| **front-wardens (chosen)** | 42/39 · 62/45 · 91/48 | 47/67 · 87/81 · 109/102 | 56/126 · 99/153 · 169/186 |
| graded (same but no whale front Wardens) | 50/58 · 66/72 · 91/88 | 49/68 · 89/95 · 110/113 | 58/126 · 102/154 · 170/186 |
| balanced (one whale Warden in every stronghold incl. SH1, then graded) | 42/40 · 64/45 · 91/48 | 47/68 · 88/136 · 110/154 | 60/124 · 101/152 · 169/186 |
| Gemini's original (round-robin by rank over all six) | 60/46 · 78/51 · 104/70 | 72/89 · 99/131 · 136/150 | 85/118 · 142/142 · 181/180 |
| strongest 20 in SH1, next 40 in 2/3, weakest at fronts | — | 84/97 · 118/127 · 154/155 | 94/106 · 140/141 · 170/175 |
| fortress: strongest 48 at the fronts, weakest in SH1 | — | 60/138 · 174/191 (3/4/5) | — |

Known limitations of the model: power is used as a proxy for combat strength (no troop-type counters, formations or hero skills); the enemy is a scaled mirror of us; attacker behaviour is one of two simple policies; results have run-to-run noise of roughly ±10★.

## 6. The chosen plan ("front-wardens")

Rule: sort by power. Ranks 1–2 are the Wardens of Strongholds 2 and 3. Ranks 3–5 are the Wardens of Strongholds 4, 5 and 6. Ranks 6–23 go to 2/3 (snake draft, 9 each). Ranks 24–72 go to the fronts (snake draft, 16–17 each, where the 8 empty slots land). Ranks 73–92 top up 2/3 (10 each). Ranks 93–112 go to Stronghold 1. Total 202★.

### Stronghold 4 (Primitive, 1★ per squad, Warden 2★) — 18/20 squads, 19★, 9.71B

**Chytras S1 1.16B (Warden)**, Awares S2 660M, Mai ♡ S2 626M, CANSæRBæRæ S1 624M, PsyPat S2 594M, Japip S1 587M, MAJD MAJD S2 531M, Reddyvetty S2 530M, CANSæRBæRæ S2 495M, Kaptain Kurt S2 483M, ESPARTACO S2 462M, Wrath S2 461M, Sanimales S1 436M, LMX S2 435M, chefinha S1 415M, Lord of North S2 415M, Sanimales S2 402M, Lord_Kris S2 399M

### Stronghold 5 (Primitive, 1★ per squad, Warden 2★) — 17/20 squads, 18★, 9.29B

**Raggylug S1 1.15B (Warden)**, Ananas S1 654M, Sassy S2 641M, Middletonia S1 613M, Lina S1 597M, Wrath S1 574M, Lina S2 536M, Greys S2 525M, ~SHADAI~ S1 496M, Japip S2 480M, Lord_Kris S1 466M, Patti S1 458M, Jesse S1 441M, ~SHADAI~ S2 433M, Dobbinater S1 415M, RADA S1 414M, SNOW X JOKER S1 407M

### Stronghold 6 (Primitive, 1★ per squad, Warden 2★) — 17/20 squads, 18★, 9.32B

**Leoder S2 1.14B (Warden)**, Shaka S2 644M, Greys S1 641M, Reddyvetty S1 606M, Paulo" S2 604M, Ananas S2 571M, Middletonia S2 548M, Phoe Iago S1 520M, Kaptain Kurt S1 517M, Phoe Iago S2 479M, ESPARTACO S1 473M, Lord of North S1 453M, LMX S1 446M, madam mimin S1 433M, Patti S2 422M, 8SMITTY8 S1 413M, Dobbinater S2 409M

### Stronghold 2 (Advanced, 2★ per squad, Warden 4★) — 20/20 squads, 42★, 12.77B

**Leoder S1 1.41B (Warden)**, Team hala kahiki S1 1.12B, Interstellar S1 1.02B, Chytras S2 958M, Team hala kahiki S2 923M, Awares S1 892M, Shaka S1 813M, Mai ♡ S1 790M, MAJD MAJD S1 686M, Sassy S1 680M, RADA S2 396M, Freefall S1 373M, chefinha S2 369M, Jesse S2 358M, المهندسة S2 355M, Freefall S2 339M, Manabeille S1 338M, Happy S1 328M, Carlitos__ S1 321M, Carlitos__ S2 305M

### Stronghold 3 (Advanced, 2★ per squad, Warden 4★) — 20/20 squads, 42★, 12.52B

**Ms Get Down S1 1.18B (Warden)**, Nibbler S1 1.10B, Nibbler S2 1.07B, Raggylug S2 956M, Ms Get Down S2 935M, Interstellar S2 833M, Katnanas S1 817M, Paulo" S1 768M, PsyPat S1 690M, Katnanas S2 671M, Doxter S1 386M, madam mimin S2 383M, 8SMITTY8 S2 366M, المهندسة S1 359M, SNOW X JOKER S2 352M, effylyt S1 349M, Panda S1 337M, Manabeille S2 333M, effylyt S2 320M, Doxter S2 305M

### Stronghold 1 (Empowered, 3★ per squad, Warden 6★) — 20/20 squads, 63★, 4.79B

**Happy S2 298M (Warden)**, Celestis S1 288M, Celestis S2 278M, Cassss S1 278M, Panda S2 273M, Gang&ter S1 272M, Anunnaki S1 266M, capy bara S1 260M, Cassss S2 259M, Benson S1 247M, capy bara S2 243M, Anunnaki S2 230M, Gang&ter S2 229M, Danii S1 228M, Benson S2 227M, Lily blue S1 215M, Lily blue S2 210M, Danii S2 184M, Elysian S1 156M, Elysian S2 149M

## 7. What it is worse at, honestly

- Against an enemy that walks through the wall (≈15%+ stronger), the 19 weak squads in Stronghold 1 give up 57★ in ~100 attacks. Every layout loses 130–190★ against such an enemy, so this is accepted.
- Three 1.1B+ squads are worth 2★ each at the fronts instead of 3★/6★ in Stronghold 1. Those extra Stars only exist if the enemy reaches Stronghold 1.
- The plan assumes Advanced Wardens are worth 4★ and that a Warden must merely be in its stronghold's top 5 (every Warden here is its stronghold's top squad).

## 8. Questions a reviewer could usefully answer

1. Is there a layout that beats front-wardens against an equal enemy in the simulation above without giving up its advantage against a weaker one? (Candidate ideas: which ranks become front Wardens; how many strong squads the Advanced ring needs; whether Stronghold 1 should hold mid squads instead of the weakest.)
2. Does anything in the in-game rules contradict the model — in particular the claim that a front cannot be cleared without killing its Warden, and that Stronghold 1 needs a full Advanced clear first?
3. Are there battle-day tactics (attack order, bait assignment, timing of the 2-hourly restores) that change which defensive layout is best?
