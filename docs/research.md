# Winter Siege: mechanics and deployment research

Compiled 2026-09-16 and updated for the September 2026 rule change. Official documentation is still thin; the in-game Help Center section has no articles yet.

## Sources
- Shield WOS, "How to play Winter Siege": https://www.youtube.com/watch?v=oWejV9-RCXo (shows the in-game rule screens)
- Shield WOS, "Winter Siege Best Formation and Hero Setup": https://www.youtube.com/watch?v=-BipzXf2ySQ
- https://www.mone.gg/blog/whiteout-survival/winter-siege-guide.html
- https://www.treyexgaming.com/whiteout-survival-winter-siege-guide-wardens-formation/
- https://www.topuplive.com/news/whiteout-survival-winter-siege-guide.html
- Century Games update notes: https://www.centurygames.com/whiteout-survival-wos-update/
- Avoid topuplist.com's guide. It confuses Winter Siege with Fortress Battles.

## What our own screenshots show
The guides describe 4 strongholds with 30 squads each. Our battlefield is different:

| Item | Our game (screenshots) | Guides |
|---|---|---|
| Strongholds | **6**: #1 Empowered, #2–3 Advanced, #4–6 Primitive | 4 (1 Empowered, 3 Primitive) |
| Garrison cap | **Top 20 squads** per stronghold | Warden + top 29 (30 total) |
| Stars per normal squad | Empowered **3**, Advanced **2**, Primitive **1** (from the stronghold headers) | Empowered 3, Primitive 1; Warden ×2 |
| Hearts shown | 4 on every squad (no Wardens appointed yet) | 4 normal, 5 Warden (after the Sept 2026 change) |
| Squads signed up | 120 (60 players × 2) as of 2026-09-17; Mai ♡ and CANSæRBæRæ were added from Gemini's list, not from our screenshots; LE RAT CANAM, Luckynanas, Arwres and Gemini signed up after the plan was applied | — |

Map paths (from the "Switch Garrison Stronghold" screen): 4→2, 5→2, 5→3, 6→3, then 2→1 and 3→1. Stronghold 1 is the core, 2 and 3 are the middle ring, and 4, 5 and 6 are the front.

Total slots: 6 × 20 = 120, and we have 120 squads, so the board is exactly full.

Maximum Stars if every slot is filled (normal squads only): Empowered 20 × 3 = 60, Advanced 2 × 20 × 2 = 80, Primitive 3 × 20 × 1 = 60, for 200 in total. Wardens are presumably worth double (6, 4 and 2 Stars). That's confirmed for Empowered and Primitive, and inferred for Advanced.

## Rules we're treating as confirmed
- **Format:** our alliance against one other alliance. Preparation runs Wednesday–Thursday, Scouting on Friday (lineups visible, no stats), Battle on Saturday. Setups lock when Preparation ends.
- **Squads (in-game rules screen, `screenshots/rules4-how-to-play.png`):** each Chief sets up 2 and garrisons them in any friendly stronghold; the same squads attack in the Battle Phase. At the end of Preparation a set number of the most powerful squads in each stronghold form its garrison and add Stars; squads not selected can still attack. In the Scout Phase you can view the enemy garrison formations. In the Battle Phase you pick any squad in an unlocked enemy stronghold to attack.
- **Fights:** each attack is one squad against one defending squad. No troops are lost.
- **Hearts:** a defender loses 1 Heart per lost defense. At 0 Hearts, the stronghold loses all of that squad's Stars at once. Normal squads have **4 Hearts** and Wardens **5** (see the rule change below).
- **Scoring:** see the rule change below.
- **Gating (in-game rules screen, `screenshots/rules1.png`):** "all defender squads garrisoning the current stronghold must be defeated in order for your forces to attack the next connected strongholds." Connections from the map: 4→2, 5→2 and 3, 6→3, 2→1, 3→1. So the enemy clears one front, then the Advanced stronghold behind it, then Stronghold 1.
- **Morale (defenders only, in-game rules screen, `screenshots/rules2.png`):**
  - A defender's stats are its stats at lock time × its morale.
  - Each defender victory costs −10% morale while morale is above 80%, and −5% at or below 80%. **Morale stops falling at 60%** (the creator videos said 35%; the in-game text says 60%).
  - Losing a Heart resets morale to 100%. Attacker morale is always 100%.
- **Bonuses that don't apply:** hero gear exclusive skills, territory buffs, state or President buffs, Frost Dragon, and city bonuses.
- **Attack attempts (in-game rules screen):** each squad starts with 3 and gets 1 restored every 2 hours, at most 7 restored, so 10 per squad and 20 per player. Injured troops recover after every battle. Squads set up by a Chief who leaves during the Battle Phase are retained.

## Rule change (announced about 2026-09-10)
Sources: Tonton Gaming, "Is Winter Siege now a FAIR battle? They FIXED it!" (https://www.youtube.com/watch?v=NfQpHMjFco0, 2026-09-10) and "Winter Siege Recap" (https://www.youtube.com/watch?v=GF9OpXP-iGo, 2026-09-14); WOS Strategy Lab (https://www.youtube.com/watch?v=uDJjrh021wk, 2026-09-13).

1. **New win conditions, checked in this order:**
   1. The first side to reduce the enemy to **0 Stars wins immediately**. (Previously both sides could be zeroed and power decided the result.)
   2. If neither side is zeroed, the side with **more Stars left** wins.
   3. If Stars tie, the side with **higher total power among surviving troops** in its strongholds wins.
   4. If that also ties, the side whose Stars were reduced to that number **later** wins.
   5. Special case (in-game rules screen, `screenshots/rules5-result.png`): if both sides have the same Stars before the Battle Phase *and* the same after it, both sides lose.
2. **Hearts:** normal squads go from **3 to 4**. Wardens stay at **5** (3 + 2 extra).
3. **Tier and matchmaking:** your starting tier now comes from your Alliance Championship tier, so the event is matched by AC tier instead of raw power. A loss earns +0 tier progress, a win +1, and a win streak more.

What this means for us:
- Taking all of the enemy's Stars is now a real way to win, so the speed of the attack matters as much as the defense.
- Surviving power is the tiebreaker, so strong squads that never lose all their Hearts still count at the end.
- The extra Heart makes every garrisoned squad harder to remove, so a deep garrison (many squads) is worth more than before.

## The Warden
- R4/R5 appoint 1 Warden per stronghold during Preparation.
- The Warden has **no aura and no garrison-wide skills**. It just carries double Stars and **one more Heart than a normal squad (5 vs 4)**.
- Developer tip: make the strongest squad in each stronghold its Warden. Some guides say the Warden must be among that stronghold's top 5 squads.
- The core Warden matters most, because it holds the most Stars in one place.

## Strategy notes
- **Placement:** two schools of thought.
  - (a) Put the strongest squads in the core; it holds the most Stars.
  - (b) Make the front strongholds hard to clear, so the enemy never reaches the core.
  - Hybrid: one top player as Warden on each stronghold, and the next-strongest squads in the core.
- **Gating:** the enemy only needs to clear **one** front stronghold. A weak front stronghold is therefore the breach point, so keep the front evenly matched.
- **Morale baiting:** the enemy will send weak squads to drain a strong defender's morale, then finish it with a strong one. A stronghold with many mid-strength defenders takes many attempts to clear.
- **Formations (first-run advice):**
  - Weak lancer gear: 49/24/9 with Mia or Molly.
  - Weak marksman gear: 60/40 with Greg, Alonso or Bradley.
  - Heavy spenders: 50/20/30 or 40/20/40.
  - Since the same squad attacks and defends, prefer hybrid setups.
- **During the battle:** coordinate targets first, use battle reports to read enemy stats (scouting shows none), and attack enemies of similar power.
