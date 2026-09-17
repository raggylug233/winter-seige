# Comparison: our plan vs Gemini's plan

Compared 2026-09-17 on all 112 squads. Gemini's plan ("Winter Siege - Balanced Deployment Plan") was transcribed from its rendered table. Its four extra squads (Mai ♡ ×2, CANSæRBæRæ ×2; names de-mangled from `Mai â™¡` and `CANSĂŚRBĂŚRĂ`) have been added to `data/squads.csv` with the powers it listed.

## The three plans

- **Gemini:** round-robin by power rank across all six strongholds, so every stronghold gets an even slice of the roster: one ~1.1B+ Warden, a couple of 900M+ squads, and 6–8 squads under 400M. Leaves SH1 at 19/20 and SH2/SH3 at 19/20.
- **Balanced (Gemini's idea, fixed):** one whale Warden per stronghold as Gemini has it, but SH1–3 filled to 20, the empty slots at the fronts, the next 18 strongest in SH2/SH3, mid squads at the fronts and the weakest 19 around the SH1 Warden. Built as `balanced.html`.
- **Ours (front-wardens):** the two biggest squads anchor SH2/SH3, the next three are the front Wardens, then the same grading. Built as `index.html`. This came out of the comparison: Gemini's whale-Warden-at-every-front idea is right, its whale Warden in SH1 is not.

## Structure

| Stronghold | Ours: squads / ★ / power / ≥900M / <400M | Balanced | Gemini |
|---|---|---|---|
| 1 (Empowered) | 20 / 63★ / 4.8B / 0 / 20 | 20 / 63★ / 5.9B / 1 / 19 | 19 / 60★ / 9.5B / 2 / 8 |
| 2 (Advanced) | 20 / 42★ / 12.8B / 5 / 10 | 20 / 42★ / 12.3B / 4 / 10 | 19 / 40★ / 10.3B / 3 / 7 |
| 3 (Advanced) | 20 / 42★ / 12.5B / 5 / 10 | 20 / 42★ / 12.2B / 5 / 10 | 19 / 40★ / 10.0B / 2 / 7 |
| 4 (Primitive) | 18 / 19★ / 9.7B / 1 / 1 | 18 / 19★ / 9.6B / 1 / 2 | 19 / 20★ / 9.8B / 2 / 7 |
| 5 (Primitive) | 17 / 18★ / 9.3B / 1 / 0 | 17 / 18★ / 9.2B / 1 / 0 | 18 / 19★ / 9.4B / 2 / 6 |
| 6 (Primitive) | 17 / 18★ / 9.3B / 1 / 0 | 17 / 18★ / 9.2B / 1 / 0 | 18 / 19★ / 9.5B / 2 / 6 |
| **Total** | **202★** | **202★** | **198★** |

## Simulation (path gating, `sim.py`, stars lost)

Coordinated / greedy attacker, at 3 · 4 · 5 attacks landed per enemy squad:

| Enemy | Ours | Balanced | Gemini |
|---|---|---|---|
| ×0.85 | **42/39 · 62/45 · 91/48** | 42/40 · 64/45 · 91/48 | 60/46 · 78/51 · 104/70 |
| ×1.0 | **47/67 · 87/81 · 109/102** | 47/68 · 88/136 · 110/154 | 72/89 · 99/131 · 136/150 |
| ×1.15 | **56/126 · 99/153 · 169/186** | 60/124 · 101/152 · 169/186 | 85/118 · 142/142 · 181/180 |

Why Gemini's original loses: it forfeits 4★ to empty high-value slots, spreads 8 sub-400M squads into 3★ slots and 14 into 2★ slots where they die in 4–5 attacks each, and its explanation overstates the toll ("15–30 attacks per stronghold" is the cost of one whale, and only against an equal enemy). Its two good ideas — a whale Warden at every front, and balanced fronts — are kept in ours.

Why the balanced version still loses to ours against an equal greedy enemy (136 vs 81 at 4 attacks): the whale in SH1 doesn't protect the 19 weak squads around him. Once a front and an Advanced stronghold are down, those 57★ go in ~100 attacks whether Leoder is there or not, and Leoder is worth more as a front Warden.

## Where each squad goes

Warden marked ★W.

| # | Player | Squad | Power | Ours | Balanced | Gemini |
|---|---|---|---|---|---|---|
| 1 | Leoder | S1 | 1.41B | SH2 ★W | SH1 ★W | SH1 ★W |
| 2 | Ms Get Down | S1 | 1.18B | SH3 ★W | SH2 ★W | SH2 ★W |
| 3 | Chytras | S1 | 1.16B | SH4 ★W | SH3 ★W | SH3 ★W |
| 4 | Raggylug | S1 | 1.15B | SH5 ★W | SH4 ★W | SH4 ★W |
| 5 | Leoder | S2 | 1.14B | SH6 ★W | SH5 ★W | SH2 |
| 6 | Team hala kahiki | S1 | 1.12B | SH2 | SH6 ★W | SH5 ★W |
| 7 | Nibbler | S1 | 1.10B | SH3 | SH2 | SH6 ★W |
| 8 | Nibbler | S2 | 1.07B | SH3 | SH3 | SH3 |
| 9 | Interstellar | S1 | 1.02B | SH2 | SH3 | SH4 |
| 10 | Chytras | S2 | 958M | SH2 | SH2 | SH6 |
| 11 | Raggylug | S2 | 956M | SH3 | SH2 | SH1 |
| 12 | Ms Get Down | S2 | 935M | SH3 | SH3 | SH2 |
| 13 | Team hala kahiki | S2 | 923M | SH2 | SH3 | SH5 |
| 14 | Awares | S1 | 892M | SH2 | SH2 | SH3 |
| 15 | Interstellar | S2 | 833M | SH3 | SH2 | SH4 |
| 16 | Katnanas | S1 | 817M | SH3 | SH3 | SH5 |
| 17 | Shaka | S1 | 813M | SH2 | SH3 | SH6 |
| 18 | Mai ♡ | S1 | 790M | SH2 | SH2 | SH1 |
| 19 | Paulo" | S1 | 768M | SH3 | SH2 | SH2 |
| 20 | PsyPat | S1 | 690M | SH3 | SH3 | SH3 |
| 21 | MAJD MAJD | S1 | 686M | SH2 | SH3 | SH4 |
| 22 | Sassy | S1 | 680M | SH2 | SH2 | SH5 |
| 23 | Katnanas | S2 | 671M | SH3 | SH2 | SH6 |
| 24 | Awares | S2 | 660M | SH4 | SH3 | SH1 |
| 25 | Ananas | S1 | 654M | SH5 | SH4 | SH2 |
| 26 | Shaka | S2 | 644M | SH6 | SH5 | SH3 |
| 27 | Greys | S1 | 641M | SH6 | SH6 | SH4 |
| 28 | Sassy | S2 | 641M | SH5 | SH6 | SH5 |
| 29 | Mai ♡ | S2 | 626M | SH4 | SH5 | SH6 |
| 30 | CANSæRBæRæ | S1 | 624M | SH4 | SH4 | SH6 |
| 31 | Middletonia | S1 | 613M | SH5 | SH4 | SH2 |
| 32 | Reddyvetty | S1 | 606M | SH6 | SH5 | SH3 |
| 33 | Paulo" | S2 | 604M | SH6 | SH6 | SH4 |
| 34 | Lina | S1 | 597M | SH5 | SH6 | SH5 |
| 35 | PsyPat | S2 | 594M | SH4 | SH5 | SH6 |
| 36 | Japip | S1 | 587M | SH4 | SH4 | SH1 |
| 37 | Wrath | S1 | 574M | SH5 | SH4 | SH2 |
| 38 | Ananas | S2 | 571M | SH6 | SH5 | SH3 |
| 39 | Middletonia | S2 | 548M | SH6 | SH6 | SH4 |
| 40 | Lina | S2 | 536M | SH5 | SH6 | SH5 |
| 41 | MAJD MAJD | S2 | 531M | SH4 | SH5 | SH6 |
| 42 | Reddyvetty | S2 | 530M | SH4 | SH4 | SH1 |
| 43 | Greys | S2 | 525M | SH5 | SH4 | SH2 |
| 44 | Phoe Iago | S1 | 520M | SH6 | SH5 | SH3 |
| 45 | Kaptain Kurt | S1 | 517M | SH6 | SH6 | SH4 |
| 46 | ~SHADAI~ | S1 | 496M | SH5 | SH6 | SH5 |
| 47 | CANSæRBæRæ | S2 | 495M | SH4 | SH5 | SH1 |
| 48 | Kaptain Kurt | S2 | 483M | SH4 | SH4 | SH1 |
| 49 | Japip | S2 | 480M | SH5 | SH4 | SH2 |
| 50 | Phoe Iago | S2 | 479M | SH6 | SH5 | SH3 |
| 51 | ESPARTACO | S1 | 473M | SH6 | SH6 | SH4 |
| 52 | Lord_Kris | S1 | 466M | SH5 | SH6 | SH5 |
| 53 | ESPARTACO | S2 | 462M | SH4 | SH5 | SH6 |
| 54 | Wrath | S2 | 461M | SH4 | SH4 | SH1 |
| 55 | Patti | S1 | 458M | SH5 | SH4 | SH2 |
| 56 | Lord of North | S1 | 453M | SH6 | SH5 | SH3 |
| 57 | LMX | S1 | 446M | SH6 | SH6 | SH4 |
| 58 | Jesse | S1 | 441M | SH5 | SH6 | SH5 |
| 59 | Sanimales | S1 | 436M | SH4 | SH5 | SH6 |
| 60 | LMX | S2 | 435M | SH4 | SH4 | SH1 |
| 61 | ~SHADAI~ | S2 | 433M | SH5 | SH4 | SH2 |
| 62 | madam mimin | S1 | 433M | SH6 | SH5 | SH3 |
| 63 | Patti | S2 | 422M | SH6 | SH6 | SH4 |
| 64 | Dobbinater | S1 | 415M | SH5 | SH6 | SH5 |
| 65 | chefinha | S1 | 415M | SH4 | SH5 | SH6 |
| 66 | Lord of North | S2 | 415M | SH4 | SH4 | SH1 |
| 67 | RADA | S1 | 414M | SH5 | SH4 | SH2 |
| 68 | 8SMITTY8 | S1 | 413M | SH6 | SH5 | SH3 |
| 69 | Dobbinater | S2 | 409M | SH6 | SH6 | SH4 |
| 70 | SNOW X JOKER | S1 | 407M | SH5 | SH6 | SH5 |
| 71 | Sanimales | S2 | 402M | SH4 | SH5 | SH6 |
| 72 | Lord_Kris | S2 | 399M | SH4 | SH4 | SH1 |
| 73 | RADA | S2 | 396M | SH2 | SH4 | SH2 |
| 74 | Doxter | S1 | 386M | SH3 | SH2 | SH3 |
| 75 | madam mimin | S2 | 383M | SH3 | SH3 | SH4 |
| 76 | Freefall | S1 | 373M | SH2 | SH3 | SH5 |
| 77 | chefinha | S2 | 369M | SH2 | SH2 | SH6 |
| 78 | 8SMITTY8 | S2 | 366M | SH3 | SH2 | SH1 |
| 79 | المهندسة | S1 | 359M | SH3 | SH3 | SH2 |
| 80 | Jesse | S2 | 358M | SH2 | SH3 | SH3 |
| 81 | المهندسة | S2 | 355M | SH2 | SH2 | SH4 |
| 82 | SNOW X JOKER | S2 | 352M | SH3 | SH2 | SH5 |
| 83 | effylyt | S1 | 349M | SH3 | SH3 | SH6 |
| 84 | Freefall | S2 | 339M | SH2 | SH3 | SH1 |
| 85 | Manabeille | S1 | 338M | SH2 | SH2 | SH2 |
| 86 | Panda | S1 | 337M | SH3 | SH2 | SH3 |
| 87 | Manabeille | S2 | 333M | SH3 | SH3 | SH4 |
| 88 | Happy | S1 | 328M | SH2 | SH3 | SH5 |
| 89 | Carlitos__ | S1 | 321M | SH2 | SH2 | SH6 |
| 90 | effylyt | S2 | 320M | SH3 | SH2 | SH1 |
| 91 | Doxter | S2 | 305M | SH3 | SH3 | SH2 |
| 92 | Carlitos__ | S2 | 305M | SH2 | SH3 | SH3 |
| 93 | Happy | S2 | 298M | SH1 ★W | SH2 | SH4 |
| 94 | Celestis | S1 | 288M | SH1 | SH1 | SH5 |
| 95 | Celestis | S2 | 278M | SH1 | SH1 | SH6 |
| 96 | Cassss | S1 | 278M | SH1 | SH1 | SH1 |
| 97 | Panda | S2 | 273M | SH1 | SH1 | SH2 |
| 98 | Gang&ter | S1 | 272M | SH1 | SH1 | SH3 |
| 99 | Anunnaki | S1 | 266M | SH1 | SH1 | SH4 |
| 100 | capy bara | S1 | 260M | SH1 | SH1 | SH5 |
| 101 | Cassss | S2 | 259M | SH1 | SH1 | SH6 |
| 102 | Benson | S1 | 247M | SH1 | SH1 | SH6 |
| 103 | capy bara | S2 | 243M | SH1 | SH1 | SH2 |
| 104 | Anunnaki | S2 | 230M | SH1 | SH1 | SH3 |
| 105 | Gang&ter | S2 | 229M | SH1 | SH1 | SH4 |
| 106 | Danii | S1 | 228M | SH1 | SH1 | SH5 |
| 107 | Benson | S2 | 227M | SH1 | SH1 | SH1 |
| 108 | Lily blue | S1 | 215M | SH1 | SH1 | SH1 |
| 109 | Lily blue | S2 | 210M | SH1 | SH1 | SH2 |
| 110 | Danii | S2 | 184M | SH1 | SH1 | SH3 |
| 111 | Elysian | S1 | 156M | SH1 | SH1 | SH4 |
| 112 | Elysian | S2 | 149M | SH1 | SH1 | SH1 |
