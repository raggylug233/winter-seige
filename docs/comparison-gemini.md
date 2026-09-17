# Comparison: our plan vs Gemini's plan

Compared 2026-09-17. Gemini's plan ("Winter Siege - Balanced Deployment Plan") was transcribed from its rendered table; it lists 112 squads, including Mai ×2 and "CANSĂŚRBĂŚRĂ" ×2 that are not in our screenshots, so both plans are compared on the 108 squads we have. Several names in Gemini's output are mojibake (e.g. `Ø§Ù„Ù…Ù‡Ù†Ø¯Ø³Ø©` for المهندسة, `LÃ¯na`, `ðŸ"RADA`).

## How each plan is built

- **Gemini:** round-robin by power rank across all six strongholds (rank 1 → SH1, 2 → SH2, 3 → SH3, 4 → SH4, … repeating), so every stronghold gets an even slice of the whole roster: one ~1.1B+ Warden, a couple of 900M+ squads, and 6–8 squads under 400M. On our 108 squads that leaves SH1 at 17/20 and SH2/SH3 at 19/20.
- **Ours:** graded by what the enemy can reach. Ranks 1–20 split across SH2/SH3, ranks 21–68 balanced across the three fronts, ranks 69–88 fill SH2/SH3, the weakest 20 in SH1. SH1–3 full, the 12 empty slots at the fronts.

## Structure

| Stronghold | Ours: squads / ★ / power / ≥900M / <400M | Gemini: squads / ★ / power / ≥900M / <400M |
|---|---|---|
| 1 (Empowered) | 20 / 63★ / 4.8B / 0 / 20 | 17 / 54★ / 8.2B / 2 / 8 |
| 2 (Advanced) | 20 / 42★ / 13.4B / 7 / 10 | 19 / 40★ / 10.3B / 3 / 7 |
| 3 (Advanced) | 20 / 42★ / 13.2B / 6 / 10 | 19 / 40★ / 10.0B / 2 / 7 |
| 4 (Primitive) | 16 / 17★ / 8.2B / 0 / 1 | 19 / 20★ / 9.8B / 2 / 7 |
| 5 (Primitive) | 16 / 17★ / 8.1B / 0 / 0 | 18 / 19★ / 9.4B / 2 / 6 |
| 6 (Primitive) | 16 / 17★ / 8.2B / 0 / 0 | 16 / 17★ / 8.2B / 2 / 6 |
| **Total** | **198★** | **190★** (200★ with its 4 extra squads) |

## Simulation (path gating, our simulator, stars lost of 198 / 190)

Coordinated / greedy attacker, by attacks landed per enemy squad:

| Enemy | Plan | 3 | 4 | 5 |
|---|---|---|---|---|
| ×0.85 | ours | 44 / 56 | 66 / 69 | 88 / 93 |
| ×0.85 | Gemini | 58 / 45 | 77 / 51 | 100 / 81 |
| ×1.0 | ours | 48 / 65 | 88 / 94 | 114 / 111 |
| ×1.0 | Gemini | 72 / 93 | 96 / 124 | 139 / 144 |
| ×1.15 | ours | 60 / 124 | 99 / 151 | 167 / 182 |
| ×1.15 | Gemini | 80 / 114 | 137 / 135 | 173 / 173 |

## Where each squad goes

Warden marked with ★W. Rows where both plans agree are marked =.

| # | Player | Squad | Power | Ours | Gemini | |
|---|---|---|---|---|---|---|
| 1 | Leoder | S1 | 1.41B | SH2 ★W | SH1 ★W |  |
| 2 | Ms Get Down | S1 | 1.18B | SH3 ★W | SH2 ★W |  |
| 3 | Chytras | S1 | 1.16B | SH3 | SH3 ★W | = |
| 4 | Raggylug | S1 | 1.15B | SH2 | SH4 ★W |  |
| 5 | Leoder | S2 | 1.14B | SH2 | SH2 | = |
| 6 | Team hala kahiki | S1 | 1.12B | SH3 | SH5 ★W |  |
| 7 | Nibbler | S1 | 1.10B | SH3 | SH6 ★W |  |
| 8 | Nibbler | S2 | 1.07B | SH2 | SH3 |  |
| 9 | Interstellar | S1 | 1.02B | SH2 | SH4 |  |
| 10 | Chytras | S2 | 958M | SH3 | SH6 |  |
| 11 | Raggylug | S2 | 956M | SH3 | SH1 |  |
| 12 | Ms Get Down | S2 | 935M | SH2 | SH2 | = |
| 13 | Team hala kahiki | S2 | 923M | SH2 | SH5 |  |
| 14 | Awares | S1 | 892M | SH3 | SH3 | = |
| 15 | Interstellar | S2 | 833M | SH3 | SH4 |  |
| 16 | Katnanas | S1 | 817M | SH2 | SH5 |  |
| 17 | Shaka | S1 | 813M | SH2 | SH6 |  |
| 18 | Paulo" | S1 | 768M | SH3 | SH2 |  |
| 19 | PsyPat | S1 | 690M | SH3 | SH3 | = |
| 20 | MAJD MAJD | S1 | 686M | SH2 | SH4 |  |
| 21 | Sassy | S1 | 680M | SH4 ★W | SH5 |  |
| 22 | Katnanas | S2 | 671M | SH5 ★W | SH6 |  |
| 23 | Awares | S2 | 660M | SH6 ★W | SH1 |  |
| 24 | Ananas | S1 | 654M | SH6 | SH2 |  |
| 25 | Shaka | S2 | 644M | SH5 | SH3 |  |
| 26 | Greys | S1 | 641M | SH4 | SH4 | = |
| 27 | Sassy | S2 | 641M | SH4 | SH5 |  |
| 28 | Middletonia | S1 | 613M | SH5 | SH2 |  |
| 29 | Reddyvetty | S1 | 606M | SH6 | SH3 |  |
| 30 | Paulo" | S2 | 604M | SH6 | SH4 |  |
| 31 | Lina | S1 | 597M | SH5 | SH5 | = |
| 32 | PsyPat | S2 | 594M | SH4 | SH6 |  |
| 33 | Japip | S1 | 587M | SH4 | SH1 |  |
| 34 | Wrath | S1 | 574M | SH5 | SH2 |  |
| 35 | Ananas | S2 | 571M | SH6 | SH3 |  |
| 36 | Middletonia | S2 | 548M | SH6 | SH4 |  |
| 37 | Lina | S2 | 536M | SH5 | SH5 | = |
| 38 | MAJD MAJD | S2 | 531M | SH4 | SH6 |  |
| 39 | Reddyvetty | S2 | 530M | SH4 | SH1 |  |
| 40 | Greys | S2 | 525M | SH5 | SH2 |  |
| 41 | Phoe Iago | S1 | 520M | SH6 | SH3 |  |
| 42 | Kaptain Kurt | S1 | 517M | SH6 | SH4 |  |
| 43 | ~SHADAI~ | S1 | 496M | SH5 | SH5 | = |
| 44 | Kaptain Kurt | S2 | 483M | SH4 | SH1 |  |
| 45 | Japip | S2 | 480M | SH4 | SH2 |  |
| 46 | Phoe Iago | S2 | 479M | SH5 | SH3 |  |
| 47 | ESPARTACO | S1 | 473M | SH6 | SH4 |  |
| 48 | Lord_Kris | S1 | 466M | SH6 | SH5 |  |
| 49 | ESPARTACO | S2 | 462M | SH5 | SH6 |  |
| 50 | Wrath | S2 | 461M | SH4 | SH1 |  |
| 51 | Patti | S1 | 458M | SH4 | SH2 |  |
| 52 | Lord of North | S1 | 453M | SH5 | SH3 |  |
| 53 | LMX | S1 | 446M | SH6 | SH4 |  |
| 54 | Jesse | S1 | 441M | SH6 | SH5 |  |
| 55 | Sanimales | S1 | 436M | SH5 | SH6 |  |
| 56 | LMX | S2 | 435M | SH4 | SH1 |  |
| 57 | ~SHADAI~ | S2 | 433M | SH4 | SH2 |  |
| 58 | madam mimin | S1 | 433M | SH5 | SH3 |  |
| 59 | Patti | S2 | 422M | SH6 | SH4 |  |
| 60 | Dobbinater | S1 | 415M | SH6 | SH5 |  |
| 61 | chefinha | S1 | 415M | SH5 | SH6 |  |
| 62 | Lord of North | S2 | 415M | SH4 | SH1 |  |
| 63 | RADA | S1 | 414M | SH4 | SH2 |  |
| 64 | 8SMITTY8 | S1 | 413M | SH5 | SH3 |  |
| 65 | Dobbinater | S2 | 409M | SH6 | SH4 |  |
| 66 | SNOW X JOKER | S1 | 407M | SH6 | SH5 |  |
| 67 | Sanimales | S2 | 402M | SH5 | SH6 |  |
| 68 | Lord_Kris | S2 | 399M | SH4 | SH1 |  |
| 69 | RADA | S2 | 396M | SH2 | SH2 | = |
| 70 | Doxter | S1 | 386M | SH3 | SH3 | = |
| 71 | madam mimin | S2 | 383M | SH3 | SH4 |  |
| 72 | Freefall | S1 | 373M | SH2 | SH5 |  |
| 73 | chefinha | S2 | 369M | SH2 | SH6 |  |
| 74 | 8SMITTY8 | S2 | 366M | SH3 | SH1 |  |
| 75 | المهندسة | S1 | 359M | SH3 | SH2 |  |
| 76 | Jesse | S2 | 358M | SH2 | SH3 |  |
| 77 | المهندسة | S2 | 355M | SH2 | SH4 |  |
| 78 | SNOW X JOKER | S2 | 352M | SH3 | SH5 |  |
| 79 | effylyt | S1 | 349M | SH3 | SH6 |  |
| 80 | Freefall | S2 | 339M | SH2 | SH1 |  |
| 81 | Manabeille | S1 | 338M | SH2 | SH2 | = |
| 82 | Panda | S1 | 337M | SH3 | SH3 | = |
| 83 | Manabeille | S2 | 333M | SH3 | SH4 |  |
| 84 | Happy | S1 | 328M | SH2 | SH5 |  |
| 85 | Carlitos__ | S1 | 321M | SH2 | SH6 |  |
| 86 | effylyt | S2 | 320M | SH3 | SH1 |  |
| 87 | Doxter | S2 | 305M | SH3 | SH2 |  |
| 88 | Carlitos__ | S2 | 305M | SH2 | SH3 |  |
| 89 | Happy | S2 | 298M | SH1 ★W | SH4 |  |
| 90 | Celestis | S1 | 288M | SH1 | SH5 |  |
| 91 | Celestis | S2 | 278M | SH1 | SH6 |  |
| 92 | Cassss | S1 | 278M | SH1 | SH1 | = |
| 93 | Panda | S2 | 273M | SH1 | SH2 |  |
| 94 | Gang&ter | S1 | 272M | SH1 | SH3 |  |
| 95 | Anunnaki | S1 | 266M | SH1 | SH4 |  |
| 96 | capy bara | S1 | 260M | SH1 | SH5 |  |
| 97 | Cassss | S2 | 259M | SH1 | SH6 |  |
| 98 | Benson | S1 | 247M | SH1 | SH6 |  |
| 99 | capy bara | S2 | 243M | SH1 | SH2 |  |
| 100 | Anunnaki | S2 | 230M | SH1 | SH3 |  |
| 101 | Gang&ter | S2 | 229M | SH1 | SH4 |  |
| 102 | Danii | S1 | 228M | SH1 | SH5 |  |
| 103 | Benson | S2 | 227M | SH1 | SH1 | = |
| 104 | Lily blue | S1 | 215M | SH1 | SH1 | = |
| 105 | Lily blue | S2 | 210M | SH1 | SH2 |  |
| 106 | Danii | S2 | 184M | SH1 | SH3 |  |
| 107 | Elysian | S1 | 156M | SH1 | SH4 |  |
| 108 | Elysian | S2 | 149M | SH1 | SH1 | = |
