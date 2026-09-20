# Us vs [AoA] — matchup analysis and attack plan

Generated 2026-09-20 from scouted garrisons (`garrison.csv`, `enemy.csv`).

## Who is stronger

| | Us | [AoA] |
|---|---|---|
| Garrison power | 65.15B | 73.26B |
| Squads ≥ 1B / ≥ 2B | 9 / 0 | 17 / 4 |
| Strongest squad | 1.41B | 2.44B |
| Stars on board | 210 | 210 |
| Layout | front-heavy (strength at the fronts): core 7.01B, middle 25.58B, fronts 32.56B | middle-heavy (strength in Strongholds 2 and 3): core 19.92B, middle 29.55B, fronts 23.79B |
| Squads the other side cannot kill (60% floor) | 0: none | 0: none |

### Per stronghold

| Stronghold | Us power · ★ · Warden | [AoA] power · ★ · Warden | attacks for us to clear | attacks for them to clear |
|---|---|---|---|---|
| 1 (Empowered) | 7.01B · 63★ · Team FishBiscuit S1 576M | 19.92B · 63★ · NoSoup4u S1 2.44B | ~192 | ~81 |
| 2 (Advanced) | 12.97B · 42★ · Leoder S1 1.41B | 14.75B · 42★ · Camille Khan S2 2.41B | ~152 | ~81 |
| 3 (Advanced) | 12.62B · 42★ · Ms Get Down S1 1.18B | 14.80B · 42★ · NoSoup4u S2 2.03B | ~148 | ~81 |
| 4 (Primitive) | 10.74B · 21★ · Chytras S1 1.16B | 7.45B · 21★ · Macsen S2 828M | ~81 | ~81 |
| 5 (Primitive) | 10.96B · 21★ · Raggylug S1 1.15B | 8.75B · 21★ · jinx S1 770M | ~81 | ~81 |
| 6 (Primitive) | 10.86B · 21★ · Leoder S2 1.14B | 7.59B · 21★ · Mistyy S1 816M | ~81 | ~81 |

## Simulation

Same model as our own plan (`sim.py`): path unlocking, win chance rising with power ratio, in-game morale rule, coordinated and greedy attacker behaviours, 8 runs. Columns are attacks landed per squad (each side has 10; sleep and waste push the real number down).

| Attacks landed per squad | 3 | 4 | 5 | 6 | 8 |
|---|---|---|---|---|---|
| Stars [AoA] loses when Us attacks (of 210) | 85 / 94 | 118 / 123 | 133 / 133 | 138 / 139 | 139 / 139 |
| Stars Us loses when [AoA] attacks (of 210) | 111 / 111 | 140 / 139 | 169 / 169 | 195 / 196 | 210 / 210 |

**Verdict: AoA is favoured: at equal activity they keep more Stars. Us wins only by out-attacking them.** Ceiling for Us: 210★ of 210 (the rest sits on unkillable squads).

## Attack plan for Us

Rules for every attack: hit only the current phase's stronghold (a half-cleared stronghold unlocks nothing); hit only targets you beat outright — your power ≥ 1.07× theirs at their current morale; a lost attack is only useful as a planned bait; use attempts as they restore (1 per squad every 2 h).

### Phase 1 — open the map: clear Stronghold 5

Opens both 2 and 3; not the very cheapest front, but worth it for the double unlock at ~81 attacks for 21★. Warden jinx S1 (770M, 5 Hearts) needs attackers over 824M — no baiting needed.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| jinx S1 (W) | 5 | 770M | 2 | ≥ 824M (15 of ours) | 5 |
| Sara S1 | 5 | 717M | 1 | ≥ 767M (19 of ours) | 4 |
| Mistyy S2 | 5 | 714M | 1 | ≥ 764M (19 of ours) | 4 |
| The Nutz S2 | 5 | 650M | 1 | ≥ 695M (20 of ours) | 4 |
| Canary S2 | 5 | 603M | 1 | ≥ 646M (27 of ours) | 4 |
| Redeemer S2 | 5 | 585M | 1 | ≥ 626M (30 of ours) | 4 |
| ninjapro S1 | 5 | 585M | 1 | ≥ 626M (31 of ours) | 4 |
| Sengana S1 | 5 | 509M | 1 | ≥ 545M (44 of ours) | 4 |
| ninjapro S2 | 5 | 508M | 1 | ≥ 543M (44 of ours) | 4 |
| Flaus S2 | 5 | 467M | 1 | ≥ 500M (53 of ours) | 4 |
| Kris_ S2 | 5 | 379M | 1 | ≥ 405M (83 of ours) | 4 |
| Twinkle S1 | 5 | 359M | 1 | ≥ 385M (89 of ours) | 4 |
| Big S1 | 5 | 310M | 1 | ≥ 332M (104 of ours) | 4 |
| MallyPally S2 | 5 | 300M | 1 | ≥ 321M (106 of ours) | 4 |
| Tiny Dancer S1 | 5 | 297M | 1 | ≥ 318M (107 of ours) | 4 |
| POINTLESS S2 | 5 | 288M | 1 | ≥ 309M (107 of ours) | 4 |
| LordXama S2 | 5 | 202M | 1 | ≥ 216M (120 of ours) | 4 |
| Андрей 1988 S2 | 5 | 183M | 1 | ≥ 196M (120 of ours) | 4 |
| Frost King S2 | 5 | 183M | 1 | ≥ 196M (120 of ours) | 4 |
| Flestz S1 | 5 | 137M | 1 | ≥ 147M (120 of ours) | 4 |

### Phase 2 — farm the cheap 2★ squads in Strongholds 2 and 3

31 squads worth 2★ each that 12+ of our squads beat outright: ~124 attacks for 62★. Best Stars-per-attack on their board. Leave their whales alone for now.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| fadher pablo S1 | 2 | 734M | 2 | ≥ 785M (18 of ours) | 4 |
| Mopeyvader S1 | 2 | 716M | 2 | ≥ 766M (19 of ours) | 4 |
| jinx S2 | 2 | 605M | 2 | ≥ 647M (27 of ours) | 4 |
| chapo the frog S2 | 2 | 593M | 2 | ≥ 634M (30 of ours) | 4 |
| Ari6 S2 | 2 | 579M | 2 | ≥ 619M (32 of ours) | 4 |
| I Am Groot S2 | 2 | 571M | 2 | ≥ 611M (33 of ours) | 4 |
| ssh12345 S1 | 2 | 537M | 2 | ≥ 574M (41 of ours) | 4 |
| MUD S2 | 2 | 533M | 2 | ≥ 570M (43 of ours) | 4 |
| Charlie S2 | 2 | 509M | 2 | ≥ 544M (44 of ours) | 4 |
| Danny S2 | 2 | 497M | 2 | ≥ 531M (45 of ours) | 4 |
| ssh12345 S2 | 2 | 491M | 2 | ≥ 525M (47 of ours) | 4 |
| Memily S1 | 2 | 485M | 2 | ≥ 519M (50 of ours) | 4 |
| MiniCanary S2 | 2 | 478M | 2 | ≥ 512M (51 of ours) | 4 |
| BizarreStar S2 | 2 | 294M | 2 | ≥ 315M (107 of ours) | 4 |
| KayRenae S2 | 2 | 274M | 2 | ≥ 293M (111 of ours) | 4 |
| Mostafa fathy S2 | 2 | 264M | 2 | ≥ 282M (112 of ours) | 4 |
| Deadly_Kilt S1 | 3 | 696M | 2 | ≥ 745M (20 of ours) | 4 |
| OTTOMAN S2 | 3 | 682M | 2 | ≥ 730M (20 of ours) | 4 |
| I Am Groot S1 | 3 | 670M | 2 | ≥ 716M (20 of ours) | 4 |
| Mopeyvader S2 | 3 | 664M | 2 | ≥ 710M (20 of ours) | 4 |
| Charlie S1 | 3 | 601M | 2 | ≥ 643M (28 of ours) | 4 |
| fadher pablo S2 | 3 | 589M | 2 | ≥ 630M (30 of ours) | 4 |
| MiniCanary S1 | 3 | 581M | 2 | ≥ 622M (32 of ours) | 4 |
| SKC250902 S1 | 3 | 492M | 2 | ≥ 527M (47 of ours) | 4 |
| Memily S2 | 3 | 448M | 2 | ≥ 480M (57 of ours) | 4 |
| Burnt Sosig S1 | 3 | 422M | 2 | ≥ 451M (67 of ours) | 4 |
| Luiz S2 | 3 | 411M | 2 | ≥ 440M (69 of ours) | 4 |
| LINDA S1 | 3 | 405M | 2 | ≥ 433M (71 of ours) | 4 |
| 精氣神 S2 | 3 | 398M | 2 | ≥ 426M (73 of ours) | 4 |
| Luiz S1 | 3 | 354M | 2 | ≥ 379M (90 of ours) | 4 |
| LINDA S2 | 3 | 330M | 2 | ≥ 353M (98 of ours) | 4 |

### Phase 3 — clear Strongholds 4 and 6

81 + 81 attacks for 42★. Wardens: Macsen S2 (828M, needs ≥ 886M), Mistyy S1 (816M, needs ≥ 873M).

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| Macsen S2 (W) | 4 | 828M | 2 | ≥ 886M (14 of ours) | 5 |
| Canary S1 | 4 | 737M | 1 | ≥ 789M (18 of ours) | 4 |
| Redeemer S1 | 4 | 674M | 1 | ≥ 721M (20 of ours) | 4 |
| Flaus S1 | 4 | 574M | 1 | ≥ 615M (32 of ours) | 4 |
| Kris_ S1 | 4 | 532M | 1 | ≥ 569M (43 of ours) | 4 |
| 내가 왕이다 S1 | 4 | 402M | 1 | ≥ 431M (73 of ours) | 4 |
| Twinkle S2 | 4 | 383M | 1 | ≥ 409M (81 of ours) | 4 |
| Burnt Sosig S2 | 4 | 378M | 1 | ≥ 405M (83 of ours) | 4 |
| 내가 왕이다 S2 | 4 | 371M | 1 | ≥ 397M (86 of ours) | 4 |
| Eagle's Eye S1 | 4 | 331M | 1 | ≥ 355M (98 of ours) | 4 |
| MallyPally S1 | 4 | 319M | 1 | ≥ 341M (100 of ours) | 4 |
| KayRenae S1 | 4 | 292M | 1 | ≥ 312M (107 of ours) | 4 |
| Kalenian S1 | 4 | 251M | 1 | ≥ 268M (116 of ours) | 4 |
| badgarfield S2 | 4 | 212M | 1 | ≥ 227M (120 of ours) | 4 |
| LordXama S1 | 4 | 212M | 1 | ≥ 227M (120 of ours) | 4 |
| tom_ S1 | 4 | 208M | 1 | ≥ 222M (120 of ours) | 4 |
| Frost King S1 | 4 | 199M | 1 | ≥ 213M (120 of ours) | 4 |
| Андрей 1988 S1 | 4 | 191M | 1 | ≥ 204M (120 of ours) | 4 |
| KingRama27 S2 | 4 | 190M | 1 | ≥ 203M (120 of ours) | 4 |
| tom_ S2 | 4 | 171M | 1 | ≥ 183M (120 of ours) | 4 |
| Mistyy S1 (W) | 6 | 816M | 2 | ≥ 873M (14 of ours) | 5 |
| OTTOMAN S1 | 6 | 795M | 1 | ≥ 851M (14 of ours) | 4 |
| Ari6 S1 | 6 | 695M | 1 | ≥ 743M (20 of ours) | 4 |
| Sara S2 | 6 | 582M | 1 | ≥ 623M (32 of ours) | 4 |
| Deadly_Kilt S2 | 6 | 547M | 1 | ≥ 586M (39 of ours) | 4 |
| Sengana S2 | 6 | 456M | 1 | ≥ 488M (55 of ours) | 4 |
| SKC250902 S2 | 6 | 432M | 1 | ≥ 463M (62 of ours) | 4 |
| Eagle's Eye S2 | 6 | 302M | 1 | ≥ 324M (105 of ours) | 4 |
| BizarreStar S1 | 6 | 296M | 1 | ≥ 317M (107 of ours) | 4 |
| Tiny Dancer S2 | 6 | 288M | 1 | ≥ 308M (107 of ours) | 4 |
| 국방부장관 S1 | 6 | 285M | 1 | ≥ 305M (109 of ours) | 4 |
| 臻龍太子 S1 | 6 | 274M | 1 | ≥ 293M (111 of ours) | 4 |
| badgarfield S1 | 6 | 260M | 1 | ≥ 278M (112 of ours) | 4 |
| Mostafa fathy S1 | 6 | 254M | 1 | ≥ 272M (116 of ours) | 4 |
| 臻龍太子 S2 | 6 | 251M | 1 | ≥ 269M (116 of ours) | 4 |
| 국방부장관 S2 | 6 | 243M | 1 | ≥ 260M (118 of ours) | 4 |
| Big S2 | 6 | 238M | 1 | ≥ 255M (119 of ours) | 4 |
| Kalenian S2 | 6 | 236M | 1 | ≥ 253M (119 of ours) | 4 |
| KingRama27 S1 | 6 | 198M | 1 | ≥ 212M (120 of ours) | 4 |
| MiniMerida1981 S2 | 6 | 144M | 1 | ≥ 154M (120 of ours) | 4 |

### Phase 4 — mid 2★ targets in Strongholds 2 and 3

2 squads that 3–11 of our squads beat outright, or that need a bait or two: ~8 attacks for 4★.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| Junior S2 | 3 | 1.06B | 2 | ≥ 1.13B (5 of ours) | 4 |
| Tdancer2 S2 | 3 | 892M | 2 | ≥ 954M (11 of ours) | 4 |

### Phase 5 — only with leftover attempts: the hard 2★ targets

7 squads that need several baits per Heart before a top squad can finish: ~168 attacks for 18★. Poor value.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| Camille Khan S2 (W) | 2 | 2.41B | 4 | ≥ 2.58B (0 of ours) | 40 |
| Megs S1 | 2 | 1.71B | 2 | ≥ 1.83B (0 of ours) | 28 |
| Weebins S1 | 2 | 1.32B | 2 | ≥ 1.41B (0 of ours) | 12 |
| ShadowX S2 | 2 | 1.15B | 2 | ≥ 1.23B (1 of ours) | 8 |
| NoSoup4u S2 (W) | 3 | 2.03B | 4 | ≥ 2.18B (0 of ours) | 40 |
| Peanut Hamper S1 | 3 | 1.78B | 2 | ≥ 1.91B (0 of ours) | 28 |
| Junior S1 | 3 | 1.29B | 2 | ≥ 1.38B (1 of ours) | 12 |

### Phase 6 — if Stronghold 3 is fully cleared (~148 attacks): farm Stronghold 1

14 squads worth 3★ that we beat outright or nearly: ~56 attacks for 42★. Their Stronghold 1 can be zeroed.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| SAIF S1 | 1 | 1.07B | 3 | ≥ 1.14B (4 of ours) | 4 |
| Weebins S2 | 1 | 1.03B | 3 | ≥ 1.11B (6 of ours) | 4 |
| Tdancer2 S1 | 1 | 1.03B | 3 | ≥ 1.10B (7 of ours) | 4 |
| SAIF S2 | 1 | 850M | 3 | ≥ 910M (13 of ours) | 4 |
| The Nutz S1 | 1 | 839M | 3 | ≥ 897M (13 of ours) | 4 |
| chapo the frog S1 | 1 | 780M | 3 | ≥ 835M (14 of ours) | 4 |
| Danny S1 | 1 | 655M | 3 | ≥ 701M (20 of ours) | 4 |
| Meryl S1 | 1 | 641M | 3 | ≥ 685M (23 of ours) | 4 |
| MUD S1 | 1 | 608M | 3 | ≥ 651M (27 of ours) | 4 |
| Lioness S1 | 1 | 504M | 3 | ≥ 540M (44 of ours) | 4 |
| Meryl S2 | 1 | 488M | 3 | ≥ 522M (48 of ours) | 4 |
| Lioness S2 | 1 | 474M | 3 | ≥ 507M (52 of ours) | 4 |
| 精氣神 S1 | 1 | 462M | 3 | ≥ 494M (55 of ours) | 4 |
| POINTLESS S1 | 1 | 345M | 3 | ≥ 370M (92 of ours) | 4 |

## Roles

| Us squad | Power | Beats outright up to | Role |
|---|---|---|---|
| Leoder S1 (SH2) | 1.41B | 1.31B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Ms Get Down S1 (SH3) | 1.18B | 1.11B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Chytras S1 (SH4) | 1.16B | 1.08B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Raggylug S1 (SH5) | 1.15B | 1.07B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Leoder S2 (SH6) | 1.14B | 1.07B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Team hala kahiki S1 (SH2) | 1.12B | 1.05B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Nibbler S1 (SH3) | 1.10B | 1.03B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Nibbler S2 (SH3) | 1.07B | 1.00B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Interstellar S1 (SH2) | 1.02B | 952M | Finisher — save attempts for baited whales; don't spend them on fronts |
| Chytras S2 (SH2) | 958M | 895M | Heavy hitter — front Wardens and the 600–750M squads |
| Raggylug S2 (SH3) | 956M | 894M | Heavy hitter — front Wardens and the 600–750M squads |
| Ms Get Down S2 (SH3) | 935M | 874M | Heavy hitter — front Wardens and the 600–750M squads |
| Team hala kahiki S2 (SH2) | 923M | 862M | Heavy hitter — front Wardens and the 600–750M squads |
| Awares S1 (SH2) | 892M | 834M | Heavy hitter — front Wardens and the 600–750M squads |
| Interstellar S2 (SH3) | 833M | 779M | Heavy hitter — front Wardens and the 600–750M squads |
| Katnanas S1 (SH3) | 817M | 763M | Heavy hitter — front Wardens and the 600–750M squads |
| Shaka S1 (SH2) | 813M | 760M | Heavy hitter — front Wardens and the 600–750M squads |
| Mai ♡ S1 (SH2) | 790M | 738M | Heavy hitter — front Wardens and the 600–750M squads |
| Paulo" S1 (SH3) | 768M | 717M | Heavy hitter — front Wardens and the 600–750M squads |
| LE RAT CANAM S2 (SH5) | 764M | 714M | Heavy hitter — front Wardens and the 600–750M squads |
| LE RAT CANAM S1 (SH6) | 692M | 646M | Line hitter — fronts and the cheap 2★ farm |
| PsyPat S1 (SH3) | 690M | 645M | Line hitter — fronts and the cheap 2★ farm |
| MAJD MAJD S1 (SH2) | 686M | 642M | Line hitter — fronts and the cheap 2★ farm |
| Sassy S1 (SH2) | 680M | 635M | Line hitter — fronts and the cheap 2★ farm |
| Katnanas S2 (SH3) | 671M | 627M | Line hitter — fronts and the cheap 2★ farm |
| Awares S2 (SH4) | 660M | 617M | Line hitter — fronts and the cheap 2★ farm |
| Ananas S1 (SH5) | 654M | 611M | Line hitter — fronts and the cheap 2★ farm |
| Shaka S2 (SH6) | 644M | 602M | Line hitter — fronts and the cheap 2★ farm |
| Greys S1 (SH6) | 641M | 599M | Line hitter — fronts and the cheap 2★ farm |
| Sassy S2 (SH5) | 641M | 599M | Line hitter — fronts and the cheap 2★ farm |
| Mai ♡ S2 (SH4) | 626M | 585M | Line hitter — fronts and the cheap 2★ farm |
| CANSæRBæRæ S1 (SH4) | 624M | 583M | Line hitter — fronts and the cheap 2★ farm |
| Middletonia S1 (SH5) | 613M | 573M | Line hitter — fronts and the cheap 2★ farm |
| Reddyvetty S1 (SH6) | 606M | 566M | Line hitter — fronts and the cheap 2★ farm |
| Paulo" S2 (SH6) | 604M | 564M | Line hitter — fronts and the cheap 2★ farm |
| Luckynanas S1 (SH4) | 601M | 561M | Line hitter — fronts and the cheap 2★ farm |
| Lina S1 (SH5) | 597M | 558M | Line hitter — fronts and the cheap 2★ farm |
| PsyPat S2 (SH4) | 594M | 555M | Line hitter — fronts and the cheap 2★ farm |
| Japip S1 (SH4) | 587M | 548M | Line hitter — fronts and the cheap 2★ farm |
| Team FishBiscuit S1 (SH1) | 576M | 538M | Line hitter — fronts and the cheap 2★ farm |
| Meg S1 (SH1) | 575M | 538M | Line hitter — fronts and the cheap 2★ farm |
| Wrath S1 (SH5) | 574M | 536M | Line hitter — fronts and the cheap 2★ farm |
| Ananas S2 (SH6) | 571M | 533M | Line hitter — fronts and the cheap 2★ farm |
| Middletonia S2 (SH6) | 548M | 513M | Line hitter — fronts and the cheap 2★ farm |
| Lina S2 (SH5) | 536M | 501M | Line hitter — fronts and the cheap 2★ farm |
| MAJD MAJD S2 (SH4) | 531M | 496M | Line hitter — fronts and the cheap 2★ farm |
| Reddyvetty S2 (SH4) | 530M | 496M | Line hitter — fronts and the cheap 2★ farm |
| Greys S2 (SH5) | 525M | 491M | Line hitter — fronts and the cheap 2★ farm |
| Luckynanas S2 (SH5) | 521M | 487M | Line hitter — fronts and the cheap 2★ farm |
| Phoe Iago S1 (SH6) | 520M | 486M | Line hitter — fronts and the cheap 2★ farm |
| Kaptain Kurt S1 (SH6) | 517M | 483M | Line hitter — fronts and the cheap 2★ farm |
| Meg S2 (SH1) | 510M | 477M | Line hitter — fronts and the cheap 2★ farm |
| SANCAK S1 (SH2) | 503M | 470M | Line hitter — fronts and the cheap 2★ farm |
| ~SHADAI~ S1 (SH5) | 496M | 464M | Line hitter — fronts and the cheap 2★ farm |
| CANSæRBæRæ S2 (SH4) | 495M | 463M | Line hitter — fronts and the cheap 2★ farm |
| Arwres S1 (SH6) | 486M | 454M | Line hitter — fronts and the cheap 2★ farm |
| Kaptain Kurt S2 (SH4) | 483M | 452M | Line hitter — fronts and the cheap 2★ farm |
| Japip S2 (SH5) | 480M | 448M | Line hitter — fronts and the cheap 2★ farm |
| Phoe Iago S2 (SH6) | 479M | 447M | Line hitter — fronts and the cheap 2★ farm |
| ESPARTACO S1 (SH6) | 473M | 442M | Line hitter — fronts and the cheap 2★ farm |
| Lord_Kris S1 (SH5) | 466M | 435M | Line hitter — fronts and the cheap 2★ farm |
| İbrahim S1 (SH1) | 465M | 434M | Line hitter — fronts and the cheap 2★ farm |
| ESPARTACO S2 (SH4) | 462M | 432M | Line hitter — fronts and the cheap 2★ farm |
| Wrath S2 (SH4) | 461M | 431M | Line hitter — fronts and the cheap 2★ farm |
| Team FishBiscuit S2 (SH1) | 459M | 429M | Line hitter — fronts and the cheap 2★ farm |
| Patti S1 (SH5) | 458M | 428M | Line hitter — fronts and the cheap 2★ farm |
| Lord of North S1 (SH6) | 453M | 424M | Line hitter — fronts and the cheap 2★ farm |
| LMX S1 (SH6) | 446M | 416M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Jesse S1 (SH5) | 441M | 412M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Sanimales S1 (SH4) | 436M | 408M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| LMX S2 (SH4) | 435M | 407M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| ~SHADAI~ S2 (SH5) | 433M | 405M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| madam mimin S1 (SH6) | 433M | 405M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Arwres S2 (SH4) | 425M | 397M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Patti S2 (SH6) | 422M | 395M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| İbrahim S2 (SH1) | 417M | 390M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Dobbinater S1 (SH5) | 415M | 388M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| chefinha S1 (SH4) | 415M | 388M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Lord of North S2 (SH4) | 415M | 388M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| RADA S1 (SH5) | 414M | 387M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| 8SMITTY8 S1 (SH6) | 413M | 386M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Dobbinater S2 (SH6) | 409M | 382M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| SNOW X JOKER S1 (SH5) | 407M | 380M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| SANCAK S2 (SH3) | 405M | 378M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Sanimales S2 (SH4) | 402M | 376M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Lord_Kris S2 (SH4) | 399M | 373M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| RADA S2 (SH2) | 396M | 370M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Doxter S1 (SH3) | 386M | 361M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Gemini S1 (SH5) | 385M | 360M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| madam mimin S2 (SH3) | 383M | 358M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| #3174Den S1 (SH1) | 373M | 349M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Freefall S1 (SH2) | 373M | 348M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| chefinha S2 (SH2) | 369M | 345M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| 8SMITTY8 S2 (SH3) | 366M | 342M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Gemini S2 (SH6) | 364M | 340M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| المهندسة S1 (SH3) | 359M | 336M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Jesse S2 (SH2) | 358M | 335M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| المهندسة S2 (SH2) | 355M | 332M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| SNOW X JOKER S2 (SH3) | 352M | 329M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| effylyt S1 (SH3) | 349M | 326M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Freefall S2 (SH2) | 339M | 317M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Manabeille S1 (SH2) | 338M | 316M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Panda S1 (SH3) | 337M | 315M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Manabeille S2 (SH3) | 333M | 311M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Happy S1 (SH2) | 328M | 306M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Carlitos__ S1 (SH2) | 321M | 300M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| effylyt S2 (SH3) | 320M | 299M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Doxter S2 (SH1) | 305M | 285M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Carlitos__ S2 (SH1) | 305M | 285M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| #3174Den S2 (SH1) | 303M | 284M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Happy S2 (SH1) | 298M | 279M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Celestis S1 (SH1) | 288M | 269M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Celestis S2 (SH1) | 278M | 260M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Cassss S1 (SH1) | 278M | 259M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Panda S2 (SH1) | 273M | 255M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Gang&ter S1 (SH1) | 272M | 255M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Anunnaki S1 (SH1) | 266M | 249M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| capy bara S1 (SH1) | 260M | 243M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Cassss S2 (SH1) | 259M | 242M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Benson S1 (SH1) | 247M | 231M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
