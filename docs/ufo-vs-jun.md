# UFO vs [JUN] — matchup analysis and attack plan

Generated 2026-10-15 from scouted garrisons (`garrison.csv`, `enemy-JUN.csv`).

## Who is stronger

| | UFO | [JUN] |
|---|---|---|
| Garrison power | 72.33B | 48.84B |
| Squads ≥ 1B / ≥ 2B | 13 / 0 | 3 / 0 |
| Strongest squad | 1.49B | 1.41B |
| Stars on board | 210 | 190 |
| Layout | front-heavy (strength at the fronts): core 6.45B, middle 29.24B, fronts 36.63B | front-heavy (strength at the fronts): core 8.88B, middle 16.85B, fronts 23.10B |
| Squads the other side cannot kill (60% floor) | 0: none | 0: none |

### Per stronghold

| Stronghold | UFO power · ★ · Warden | [JUN] power · ★ · Warden | attacks for us to clear | attacks for them to clear |
|---|---|---|---|---|
| 1 (Empowered) | 6.45B · 63★ · Panda S1 388M | 8.88B · 57★ · Frank1119 S1 974M | ~91 | ~101 |
| 2 (Advanced) | 14.68B · 42★ · Leoder S1 1.49B | 8.71B · 38★ · xsharman S1 1.08B | ~91 | ~261 |
| 3 (Advanced) | 14.57B · 42★ · Ms Get Down S1 1.33B | 8.14B · 38★ · Franka S1 813M | ~91 | ~267 |
| 4 (Primitive) | 12.27B · 21★ · Team JackBiscuit S1 1.32B | 8.67B · 19★ · xsharman S2 850M | ~91 | ~167 |
| 5 (Primitive) | 12.20B · 21★ · Chytras S1 1.29B | 7.33B · 19★ · Boss_ S1 1.41B | ~115 | ~161 |
| 6 (Primitive) | 12.16B · 21★ · Nibbler S1 1.24B | 7.10B · 19★ · Boss_ S2 1.04B | ~91 | ~149 |

## Simulation

Same model as our own plan (`sim.py`): path unlocking, win chance rising with power ratio, in-game morale rule, coordinated and greedy attacker behaviours, 8 runs. Columns are attacks landed per squad (each side has 10; sleep and waste push the real number down).

| Attacks landed per squad | 3 | 4 | 5 | 6 | 8 |
|---|---|---|---|---|---|
| Stars [JUN] loses when UFO attacks (of 190) | 105 / 107 | 131 / 131 | 166 / 150 | 186 / 186 | 190 / 190 |
| Stars UFO loses when [JUN] attacks (of 210) | 27 / 27 | 35 / 36 | 38 / 42 | 61 / 48 | 92 / 74 |

**Verdict: UFO is favoured: at equal activity we keep more Stars than they do.** Ceiling for UFO: 190★ of 190 (the rest sits on unkillable squads).

## Attack plan for UFO

Rules for every attack: hit only the current phase's stronghold (a half-cleared stronghold unlocks nothing); hit only targets you beat outright — your power ≥ 1.07× theirs at their current morale; a lost attack is only useful as a planned bait; use attempts as they restore (1 per squad every 2 h).

### Phase 1 — open the map: clear Stronghold 4

Opens Stronghold 2; the cheapest front at ~91 attacks for 19★. Warden xsharman S2 (850M, 6 Hearts) needs attackers over 909M — no baiting needed.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| xsharman S2 (W) | 4 | 850M | 2 | ≥ 909M (18 of ours) | 6 |
| Conan S2 | 4 | 661M | 1 | ≥ 707M (31 of ours) | 5 |
| Cpt Bluesaurus S1 | 4 | 585M | 1 | ≥ 626M (40 of ours) | 5 |
| Shinichi S1 | 4 | 567M | 1 | ≥ 606M (42 of ours) | 5 |
| De82So S1 | 4 | 563M | 1 | ≥ 602M (43 of ours) | 5 |
| 543 S1 | 4 | 562M | 1 | ≥ 601M (43 of ours) | 5 |
| Marshall_Mitch S1 | 4 | 549M | 1 | ≥ 587M (44 of ours) | 5 |
| Lina S1 | 4 | 505M | 1 | ≥ 540M (52 of ours) | 5 |
| Count S2 | 4 | 479M | 1 | ≥ 512M (58 of ours) | 5 |
| 哈囉！我是喵紙醬 S1 | 4 | 477M | 1 | ≥ 510M (58 of ours) | 5 |
| Bethioio S2 | 4 | 461M | 1 | ≥ 493M (67 of ours) | 5 |
| Samanović S1 | 4 | 431M | 1 | ≥ 461M (75 of ours) | 5 |
| BaeY S1 | 4 | 430M | 1 | ≥ 460M (77 of ours) | 5 |
| Apple S1 | 4 | 371M | 1 | ≥ 397M (100 of ours) | 5 |
| Pipimi S1 | 4 | 348M | 1 | ≥ 372M (103 of ours) | 5 |
| Fletch S1 | 4 | 307M | 1 | ≥ 328M (109 of ours) | 5 |
| justin_adilyn S1 | 4 | 288M | 1 | ≥ 308M (112 of ours) | 5 |
| Emerald S2 | 4 | 238M | 1 | ≥ 255M (118 of ours) | 5 |

### Phase 2 — farm the cheap 2★ squads in Stronghold 2

17 squads worth 2★ each that 12+ of our squads beat outright: ~85 attacks for 34★. Best Stars-per-attack on their board. Leave their whales alone for now.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| FrankBella S1 | 2 | 817M | 2 | ≥ 874M (20 of ours) | 5 |
| Franka S2 | 2 | 643M | 2 | ≥ 688M (31 of ours) | 5 |
| Taran S1 | 2 | 637M | 2 | ≥ 681M (34 of ours) | 5 |
| frankaa S1 | 2 | 606M | 2 | ≥ 649M (39 of ours) | 5 |
| Amy95 S1 | 2 | 583M | 2 | ≥ 624M (40 of ours) | 5 |
| Amy99 S1 | 2 | 545M | 2 | ≥ 583M (47 of ours) | 5 |
| Milbert 高艾伯 S1 | 2 | 498M | 2 | ≥ 532M (54 of ours) | 5 |
| Amy95 S2 | 2 | 493M | 2 | ≥ 527M (54 of ours) | 5 |
| Amy99 S2 | 2 | 492M | 2 | ≥ 526M (54 of ours) | 5 |
| Tonycoutri S1 | 2 | 458M | 2 | ≥ 490M (69 of ours) | 5 |
| Minsom7 S1 | 2 | 417M | 2 | ≥ 446M (81 of ours) | 5 |
| Abalas S1 | 2 | 335M | 2 | ≥ 358M (106 of ours) | 5 |
| Mali3056 S1 | 2 | 307M | 2 | ≥ 329M (109 of ours) | 5 |
| Frank1123 S2 | 2 | 261M | 2 | ≥ 279M (116 of ours) | 5 |
| iynnn S2 | 2 | 240M | 2 | ≥ 257M (118 of ours) | 5 |
| John Snow S1 | 2 | 199M | 2 | ≥ 213M (120 of ours) | 5 |
| Len Len S2 | 2 | 105M | 2 | ≥ 112M (120 of ours) | 5 |

### Phase 3 — clear Strongholds 5 and 6

115 + 91 attacks for 38★. Wardens: Boss_ S1 (1.41B, needs ≥ 1.51B), Boss_ S2 (1.04B, needs ≥ 1.11B).

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| Boss_ S1 (W) | 5 | 1.41B | 2 | ≥ 1.51B (0 of ours) | 30 |
| Bethioio S1 | 5 | 578M | 1 | ≥ 618M (41 of ours) | 5 |
| biagio S2 | 5 | 517M | 1 | ≥ 553M (51 of ours) | 5 |
| Ange672 S2 | 5 | 487M | 1 | ≥ 521M (55 of ours) | 5 |
| Milbert 高艾伯 S2 | 5 | 463M | 1 | ≥ 495M (66 of ours) | 5 |
| Samanović S2 | 5 | 415M | 1 | ≥ 444M (81 of ours) | 5 |
| Cleoats S1 | 5 | 410M | 1 | ≥ 438M (84 of ours) | 5 |
| 哈囉！我是喵紙醬 S2 | 5 | 392M | 1 | ≥ 419M (91 of ours) | 5 |
| Dona S1 | 5 | 358M | 1 | ≥ 383M (101 of ours) | 5 |
| BaeY S2 | 5 | 344M | 1 | ≥ 368M (104 of ours) | 5 |
| Bagheera S1 | 5 | 332M | 1 | ≥ 355M (106 of ours) | 5 |
| Bagheera S2 | 5 | 318M | 1 | ≥ 340M (107 of ours) | 5 |
| Fletch S2 | 5 | 313M | 1 | ≥ 335M (107 of ours) | 5 |
| 烤糖蕎麥凍桂花青 S1 | 5 | 306M | 1 | ≥ 327M (109 of ours) | 5 |
| Pipimi S2 | 5 | 278M | 1 | ≥ 298M (114 of ours) | 5 |
| Ambie S1 | 5 | 187M | 1 | ≥ 200M (120 of ours) | 5 |
| Ambie S2 | 5 | 184M | 1 | ≥ 197M (120 of ours) | 5 |
| July S1 | 5 | 43M | 1 | ≥ 46M (120 of ours) | 5 |
| Boss_ S2 (W) | 6 | 1.04B | 2 | ≥ 1.11B (8 of ours) | 6 |
| FrankBella S2 | 6 | 630M | 1 | ≥ 674M (36 of ours) | 5 |
| Count S1 | 6 | 553M | 1 | ≥ 592M (44 of ours) | 5 |
| De82So S2 | 6 | 517M | 1 | ≥ 553M (51 of ours) | 5 |
| Shinichi S2 | 6 | 480M | 1 | ≥ 514M (58 of ours) | 5 |
| 543 S2 | 6 | 469M | 1 | ≥ 502M (63 of ours) | 5 |
| Ninja Wolf S2 | 6 | 460M | 1 | ≥ 492M (69 of ours) | 5 |
| Cpt Bluesaurus S2 | 6 | 443M | 1 | ≥ 474M (72 of ours) | 5 |
| Cleoats S2 | 6 | 374M | 1 | ≥ 400M (98 of ours) | 5 |
| Dona S2 | 6 | 329M | 1 | ≥ 352M (106 of ours) | 5 |
| Apple S2 | 6 | 326M | 1 | ≥ 348M (106 of ours) | 5 |
| mohamed amine S1 | 6 | 278M | 1 | ≥ 297M (114 of ours) | 5 |
| mohamed amine S2 | 6 | 266M | 1 | ≥ 285M (115 of ours) | 5 |
| justin_adilyn S2 | 6 | 263M | 1 | ≥ 282M (116 of ours) | 5 |
| iynnn S1 | 6 | 262M | 1 | ≥ 280M (116 of ours) | 5 |
| 烤糖蕎麥凍桂花青 S2 | 6 | 221M | 1 | ≥ 236M (120 of ours) | 5 |
| John Snow S2 | 6 | 154M | 1 | ≥ 165M (120 of ours) | 5 |
| July S2 | 6 | 38M | 1 | ≥ 41M (120 of ours) | 5 |

### Phase 3b — cheap 2★ squads newly reachable in Stronghold 3

18 squads, ~91 attacks for 36★.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| Franka S1 (W) | 3 | 813M | 4 | ≥ 870M (20 of ours) | 6 |
| Frank1119 S2 | 3 | 804M | 2 | ≥ 861M (21 of ours) | 5 |
| Mad Max11084 S1 | 3 | 672M | 2 | ≥ 719M (30 of ours) | 5 |
| Taran S2 | 3 | 595M | 2 | ≥ 636M (39 of ours) | 5 |
| Marshall_Mitch S2 | 3 | 517M | 2 | ≥ 553M (51 of ours) | 5 |
| Pixy S2 | 3 | 493M | 2 | ≥ 528M (54 of ours) | 5 |
| Lina S2 | 3 | 489M | 2 | ≥ 523M (54 of ours) | 5 |
| frankaa S2 | 3 | 477M | 2 | ≥ 510M (58 of ours) | 5 |
| Tonycoutri S2 | 3 | 451M | 2 | ≥ 482M (71 of ours) | 5 |
| Korgo S1 | 3 | 413M | 2 | ≥ 442M (81 of ours) | 5 |
| Korgo S2 | 3 | 393M | 2 | ≥ 421M (91 of ours) | 5 |
| Pacorete S1 | 3 | 362M | 2 | ≥ 388M (101 of ours) | 5 |
| Pacorete S2 | 3 | 345M | 2 | ≥ 369M (104 of ours) | 5 |
| Minsom7 S2 | 3 | 328M | 2 | ≥ 351M (106 of ours) | 5 |
| Abalas S2 | 3 | 308M | 2 | ≥ 330M (109 of ours) | 5 |
| Mali3056 S2 | 3 | 285M | 2 | ≥ 305M (113 of ours) | 5 |
| Emerald S1 | 3 | 239M | 2 | ≥ 256M (118 of ours) | 5 |
| Len Len S1 | 3 | 157M | 2 | ≥ 168M (120 of ours) | 5 |

### Phase 4 — mid 2★ targets in Strongholds 2 and 3

1 squads that 3–11 of our squads beat outright, or that need a bait or two: ~6 attacks for 2★.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| xsharman S1 (W) | 2 | 1.08B | 4 | ≥ 1.15B (8 of ours) | 6 |

### Phase 6 — if Stronghold 2 is fully cleared (~91 attacks): farm Stronghold 1

18 squads worth 3★ that we beat outright or nearly: ~91 attacks for 57★. Their Stronghold 1 can be zeroed.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| Frank1119 S1 (W) | 1 | 974M | 6 | ≥ 1.04B (11 of ours) | 6 |
| Conan S1 | 1 | 801M | 3 | ≥ 857M (21 of ours) | 5 |
| James_Hu S1 | 1 | 681M | 3 | ≥ 729M (27 of ours) | 5 |
| James_Hu S2 | 1 | 611M | 3 | ≥ 653M (39 of ours) | 5 |
| Mad Max11084 S2 | 1 | 602M | 3 | ≥ 644M (39 of ours) | 5 |
| Ange672 S1 | 1 | 551M | 3 | ≥ 589M (44 of ours) | 5 |
| Pixy S1 | 1 | 549M | 3 | ≥ 587M (44 of ours) | 5 |
| biagio S1 | 1 | 541M | 3 | ≥ 579M (48 of ours) | 5 |
| Ninja Wolf S1 | 1 | 532M | 3 | ≥ 569M (49 of ours) | 5 |
| Johnny S1 | 1 | 448M | 3 | ≥ 479M (71 of ours) | 5 |
| Johnny S2 | 1 | 426M | 3 | ≥ 456M (77 of ours) | 5 |
| khaled sndbad@66 S1 | 1 | 426M | 3 | ≥ 456M (78 of ours) | 5 |
| khaled sndbad@66 S2 | 1 | 372M | 3 | ≥ 398M (99 of ours) | 5 |
| Frank1123 S1 | 1 | 320M | 3 | ≥ 343M (107 of ours) | 5 |
| Богдан S2 | 1 | 289M | 3 | ≥ 310M (112 of ours) | 5 |
| Богдан S1 | 1 | 263M | 3 | ≥ 281M (116 of ours) | 5 |
| Ahmed 313 S1 | 1 | 256M | 3 | ≥ 274M (116 of ours) | 5 |
| Ahmed 313 S2 | 1 | 239M | 3 | ≥ 255M (118 of ours) | 5 |

## Roles

| UFO squad | Power | Beats outright up to | Role |
|---|---|---|---|
| Leoder S1 (SH2) | 1.49B | 1.39B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Ms Get Down S1 (SH3) | 1.33B | 1.24B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Team JackBiscuit S1 (SH4) | 1.32B | 1.23B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Chytras S1 (SH5) | 1.29B | 1.20B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Nibbler S1 (SH6) | 1.24B | 1.15B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Fangs of Maple S1 (SH2) | 1.22B | 1.14B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Raggylug S1 (SH3) | 1.21B | 1.13B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Leoder S2 (SH3) | 1.18B | 1.10B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Interstellar S1 (SH2) | 1.07B | 1.00B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Fangs of Maple S2 (SH2) | 1.06B | 991M | Finisher — save attempts for baited whales; don't spend them on fronts |
| Ms Get Down S2 (SH3) | 1.06B | 990M | Finisher — save attempts for baited whales; don't spend them on fronts |
| Raggylug S2 (SH3) | 1.03B | 961M | Finisher — save attempts for baited whales; don't spend them on fronts |
| Nibbler S2 (SH2) | 1.01B | 946M | Finisher — save attempts for baited whales; don't spend them on fronts |
| Team JackBiscuit S2 (SH2) | 999M | 934M | Heavy hitter — front Wardens and the 600–750M squads |
| Chytras S2 (SH3) | 981M | 917M | Heavy hitter — front Wardens and the 600–750M squads |
| LE RAT CANAM S1 (SH3) | 980M | 916M | Heavy hitter — front Wardens and the 600–750M squads |
| Awares S1 (SH2) | 949M | 887M | Heavy hitter — front Wardens and the 600–750M squads |
| Shaka S1 (SH2) | 947M | 885M | Heavy hitter — front Wardens and the 600–750M squads |
| Siren Katt S1 (SH3) | 881M | 823M | Heavy hitter — front Wardens and the 600–750M squads |
| Paulo" S1 (SH3) | 874M | 817M | Heavy hitter — front Wardens and the 600–750M squads |
| Interstellar S2 (SH2) | 861M | 804M | Heavy hitter — front Wardens and the 600–750M squads |
| LE RAT CANAM S2 (SH2) | 839M | 784M | Heavy hitter — front Wardens and the 600–750M squads |
| Greys S1 (SH3) | 837M | 782M | Heavy hitter — front Wardens and the 600–750M squads |
| PsyPat S1 (SH4) | 795M | 743M | Heavy hitter — front Wardens and the 600–750M squads |
| Japip S1 (SH5) | 782M | 731M | Heavy hitter — front Wardens and the 600–750M squads |
| Ghost Rider S1 (SH6) | 781M | 730M | Heavy hitter — front Wardens and the 600–750M squads |
| Ghost Rider S2 (SH6) | 734M | 686M | Heavy hitter — front Wardens and the 600–750M squads |
| Shaka S2 (SH5) | 727M | 680M | Heavy hitter — front Wardens and the 600–750M squads |
| MAJD MAJD S1 (SH4) | 720M | 673M | Heavy hitter — front Wardens and the 600–750M squads |
| Siren Katt S2 (SH4) | 720M | 673M | Heavy hitter — front Wardens and the 600–750M squads |
| Awares S2 (SH5) | 710M | 663M | Heavy hitter — front Wardens and the 600–750M squads |
| PsyPat S2 (SH6) | 686M | 641M | Line hitter — fronts and the cheap 2★ farm |
| Obsession S1 (SH6) | 686M | 641M | Line hitter — fronts and the cheap 2★ farm |
| Paulo" S2 (SH5) | 683M | 638M | Line hitter — fronts and the cheap 2★ farm |
| Wrath S1 (SH4) | 679M | 634M | Line hitter — fronts and the cheap 2★ farm |
| Reddyvetty S1 (SH4) | 678M | 634M | Line hitter — fronts and the cheap 2★ farm |
| Peter S1 (SH5) | 662M | 619M | Line hitter — fronts and the cheap 2★ farm |
| Middletonia S1 (SH6) | 661M | 618M | Line hitter — fronts and the cheap 2★ farm |
| Lina S1 (SH6) | 655M | 612M | Line hitter — fronts and the cheap 2★ farm |
| GHØSTFACE S1 (SH5) | 634M | 593M | Line hitter — fronts and the cheap 2★ farm |
| Greys S2 (SH4) | 624M | 583M | Line hitter — fronts and the cheap 2★ farm |
| Lina S2 (SH4) | 608M | 569M | Line hitter — fronts and the cheap 2★ farm |
| Japip S2 (SH5) | 604M | 564M | Line hitter — fronts and the cheap 2★ farm |
| Middletonia S2 (SH6) | 599M | 560M | Line hitter — fronts and the cheap 2★ farm |
| Obsession S2 (SH6) | 585M | 547M | Line hitter — fronts and the cheap 2★ farm |
| #3174joemama S1 (SH5) | 585M | 546M | Line hitter — fronts and the cheap 2★ farm |
| Peter S2 (SH4) | 583M | 545M | Line hitter — fronts and the cheap 2★ farm |
| MAJD MAJD S2 (SH4) | 579M | 541M | Line hitter — fronts and the cheap 2★ farm |
| Reddyvetty S2 (SH5) | 572M | 535M | Line hitter — fronts and the cheap 2★ farm |
| Count Phoenicula S1 (SH6) | 568M | 531M | Line hitter — fronts and the cheap 2★ farm |
| Jesse S1 (SH6) | 554M | 518M | Line hitter — fronts and the cheap 2★ farm |
| #3174joemama S2 (SH5) | 550M | 514M | Line hitter — fronts and the cheap 2★ farm |
| Junho S1 (SH4) | 539M | 504M | Line hitter — fronts and the cheap 2★ farm |
| ~SHADAI~ S1 (SH4) | 538M | 503M | Line hitter — fronts and the cheap 2★ farm |
| Lord_Kris S1 (SH5) | 523M | 488M | Line hitter — fronts and the cheap 2★ farm |
| Lord Kempington S1 (SH6) | 520M | 486M | Line hitter — fronts and the cheap 2★ farm |
| Count Phoenicula S2 (SH6) | 518M | 484M | Line hitter — fronts and the cheap 2★ farm |
| Tosha S1 (SH5) | 514M | 480M | Line hitter — fronts and the cheap 2★ farm |
| SANCAK S1 (SH4) | 507M | 474M | Line hitter — fronts and the cheap 2★ farm |
| Wrath S2 (SH4) | 505M | 472M | Line hitter — fronts and the cheap 2★ farm |
| ESPARTACO S1 (SH5) | 503M | 470M | Line hitter — fronts and the cheap 2★ farm |
| GHØSTFACE S2 (SH6) | 503M | 470M | Line hitter — fronts and the cheap 2★ farm |
| RADA S1 (SH6) | 503M | 470M | Line hitter — fronts and the cheap 2★ farm |
| Junho S2 (SH5) | 500M | 467M | Line hitter — fronts and the cheap 2★ farm |
| Arwres S1 (SH4) | 498M | 466M | Line hitter — fronts and the cheap 2★ farm |
| Patti S1 (SH4) | 498M | 465M | Line hitter — fronts and the cheap 2★ farm |
| Tosha S2 (SH5) | 494M | 461M | Line hitter — fronts and the cheap 2★ farm |
| ESPARTACO S2 (SH6) | 493M | 461M | Line hitter — fronts and the cheap 2★ farm |
| İbrahim S1 (SH6) | 492M | 460M | Line hitter — fronts and the cheap 2★ farm |
| ~SHADAI~ S2 (SH5) | 488M | 456M | Line hitter — fronts and the cheap 2★ farm |
| Sanimales S1 (SH4) | 485M | 453M | Line hitter — fronts and the cheap 2★ farm |
| LMX S1 (SH4) | 476M | 445M | Line hitter — fronts and the cheap 2★ farm |
| Arwres S2 (SH5) | 474M | 443M | Line hitter — fronts and the cheap 2★ farm |
| Lord_Kris S2 (SH6) | 469M | 439M | Line hitter — fronts and the cheap 2★ farm |
| LMX S2 (SH6) | 466M | 435M | Line hitter — fronts and the cheap 2★ farm |
| 8SMITTY8 S1 (SH5) | 460M | 430M | Line hitter — fronts and the cheap 2★ farm |
| Lord of North S1 (SH4) | 460M | 430M | Line hitter — fronts and the cheap 2★ farm |
| Sanimales S2 (SH4) | 456M | 426M | Line hitter — fronts and the cheap 2★ farm |
| Dobbinater S1 (SH5) | 453M | 423M | Line hitter — fronts and the cheap 2★ farm |
| Jesse S2 (SH6) | 451M | 422M | Line hitter — fronts and the cheap 2★ farm |
| jojo le rigolo S1 (SH2) | 449M | 420M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Patti S2 (SH3) | 442M | 413M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| RADA S2 (SH3) | 441M | 413M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| İbrahim S2 (SH2) | 440M | 412M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Lord Kempington S2 (SH2) | 438M | 409M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Dobbinater S2 (SH3) | 433M | 405M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Lord of North S2 (SH3) | 431M | 403M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| المهندسة S1 (SH2) | 429M | 401M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| chefinha S1 (SH2) | 427M | 399M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| jojo le rigolo S2 (SH3) | 423M | 396M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| 8SMITTY8 S2 (SH3) | 421M | 394M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| SNOW X JOKER S1 (SH2) | 419M | 391M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Denara S1 (SH2) | 409M | 382M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Freefall S1 (SH3) | 409M | 382M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| SANCAK S2 (SH3) | 408M | 381M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Doxter S1 (SH2) | 408M | 381M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Yarden S1 (SH2) | 404M | 378M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Freefall S2 (SH3) | 403M | 377M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| المهندسة S2 (SH3) | 399M | 373M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| chefinha S2 (SH2) | 397M | 371M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Panda S1 (SH1) | 388M | 362M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Manabeille S1 (SH1) | 377M | 352M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Manabeille S2 (SH1) | 376M | 351M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| #3174Crazy S1 (SH1) | 370M | 346M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Doxter S2 (SH1) | 366M | 342M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| SNOW X JOKER S2 (SH1) | 365M | 341M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Denara S2 (SH1) | 345M | 323M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Yarden S2 (SH1) | 335M | 313M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| #3174Crazy S2 (SH1) | 331M | 309M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Anunnaki S1 (SH1) | 325M | 304M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Celestis S1 (SH1) | 324M | 303M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Gang&ter S1 (SH1) | 316M | 295M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Celestis S2 (SH1) | 308M | 288M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Panda S2 (SH1) | 299M | 279M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| capy bara S1 (SH1) | 291M | 272M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Benson S1 (SH1) | 285M | 266M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| capy bara S2 (SH1) | 274M | 256M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Anunnaki S2 (SH1) | 274M | 256M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Gang&ter S2 (SH1) | 255M | 238M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Benson S2 (SH1) | 251M | 234M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
