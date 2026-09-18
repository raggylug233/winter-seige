# SIN vs [LIT] — matchup analysis and attack plan

Generated 2026-09-18 from scouted garrisons (`friendly-SIN.csv`, `enemy-LIT.csv`).

## Who is stronger

| | SIN | [LIT] |
|---|---|---|
| Garrison power | 65.00B | 62.64B |
| Squads ≥ 1B / ≥ 2B | 2 / 0 | 4 / 1 |
| Strongest squad | 1.24B | 2.18B |
| Stars on board | 210 | 210 |
| Layout | front-heavy (strength at the fronts): core 12.14B, middle 21.17B, fronts 31.69B | front-heavy (strength at the fronts): core 14.25B, middle 20.99B, fronts 27.40B |
| Squads the other side cannot kill (60% floor) | 0: none | 1: KnackeredNoggin S1 2.18B (SH1) |

### Per stronghold

| Stronghold | SIN power · ★ · Warden | [LIT] power · ★ · Warden | attacks for us to clear | attacks for them to clear |
|---|---|---|---|---|
| 1 (Empowered) | 12.14B · 63★ · (blank) S1 1.24B | 14.25B · 63★ · KnackeredNoggin S1 2.18B | never (unkillable squad) | ~86 |
| 2 (Advanced) | 9.79B · 42★ · ⊶GuGu⊷ S1 1.01B | 10.25B · 42★ · Ary S2 963M | ~86 | ~81 |
| 3 (Advanced) | 11.38B · 42★ · FedeC S1 959M | 10.74B · 42★ · KnackeredNoggin S2 1.91B | ~111 | ~81 |
| 4 (Primitive) | 10.85B · 21★ · Kloss S1 924M | 9.00B · 21★ · Hornet S1 712M | ~81 | ~81 |
| 5 (Primitive) | 11.89B · 21★ · Hassikkome S1 963M | 9.20B · 21★ · Ndi Ari S1 780M | ~81 | ~81 |
| 6 (Primitive) | 8.95B · 21★ · Rebel S1 810M | 9.20B · 21★ · Ary S1 1.22B | ~101 | ~81 |

## Simulation

Same model as our own plan (`sim.py`): path unlocking, win chance rising with power ratio, in-game morale rule, coordinated and greedy attacker behaviours, 8 runs. Columns are attacks landed per squad (each side has 10; sleep and waste push the real number down).

| Attacks landed per squad | 3 | 4 | 5 | 6 | 8 |
|---|---|---|---|---|---|
| Stars [LIT] loses when SIN attacks (of 210) | 84 / 110 | 107 / 137 | 152 / 159 | 194 / 198 | 200 / 200 |
| Stars SIN loses when [LIT] attacks (of 210) | 98 / 97 | 131 / 134 | 161 / 154 | 163 / 167 | 207 / 208 |

**Verdict: Too close to call at equal activity — whoever uses more of their attacks wins.** Ceiling for SIN: 204★ of 210 (the rest sits on unkillable squads).

## Attack plan for SIN

Rules for every attack: hit only the current phase's stronghold (a half-cleared stronghold unlocks nothing); hit only targets you beat outright — your power ≥ 1.07× theirs at their current morale; a lost attack is only useful as a planned bait; use attempts as they restore (1 per squad every 2 h).

### Phase 1 — open the map: clear Stronghold 5

Opens both 2 and 3; not the very cheapest front, but worth it for the double unlock at ~81 attacks for 21★. Warden Ndi Ari S1 (780M, 5 Hearts) needs attackers over 835M — no baiting needed.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| Ndi Ari S1 (W) | 5 | 780M | 2 | ≥ 835M (8 of ours) | 5 |
| Gettitt S2 | 5 | 759M | 1 | ≥ 813M (8 of ours) | 4 |
| Learnman S1 | 5 | 634M | 1 | ≥ 678M (17 of ours) | 4 |
| JzM S1 | 5 | 570M | 1 | ≥ 610M (30 of ours) | 4 |
| Learnman S2 | 5 | 529M | 1 | ≥ 566M (40 of ours) | 4 |
| leelee S2 | 5 | 513M | 1 | ≥ 549M (47 of ours) | 4 |
| Gεrα Rεy S1 | 5 | 497M | 1 | ≥ 532M (54 of ours) | 4 |
| Atreyu S2 | 5 | 496M | 1 | ≥ 531M (55 of ours) | 4 |
| Sabri22 S1 | 5 | 488M | 1 | ≥ 523M (56 of ours) | 4 |
| Dao S2 | 5 | 488M | 1 | ≥ 522M (56 of ours) | 4 |
| LIN S1 | 5 | 478M | 1 | ≥ 511M (58 of ours) | 4 |
| Pyob S2 | 5 | 466M | 1 | ≥ 498M (61 of ours) | 4 |
| JzM S2 | 5 | 451M | 1 | ≥ 483M (68 of ours) | 4 |
| Reyyy S2 | 5 | 436M | 1 | ≥ 466M (74 of ours) | 4 |
| Gεrα Rεy S2 | 5 | 399M | 1 | ≥ 427M (88 of ours) | 4 |
| 肥來了 S2 | 5 | 393M | 1 | ≥ 421M (90 of ours) | 4 |
| SoftieDriftie S2 | 5 | 335M | 1 | ≥ 358M (116 of ours) | 4 |
| User1234 S2 | 5 | 239M | 1 | ≥ 256M (120 of ours) | 4 |
| little ol' me S2 | 5 | 144M | 1 | ≥ 154M (120 of ours) | 4 |
| Splinter S2 | 5 | 105M | 1 | ≥ 112M (120 of ours) | 4 |

### Phase 2 — farm the cheap 2★ squads in Strongholds 2 and 3

36 squads worth 2★ each that 12+ of our squads beat outright: ~144 attacks for 72★. Best Stars-per-attack on their board. Leave their whales alone for now.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| breta S1 | 2 | 693M | 2 | ≥ 742M (12 of ours) | 4 |
| Simba S1 | 2 | 684M | 2 | ≥ 732M (13 of ours) | 4 |
| Hachiman S1 | 2 | 632M | 2 | ≥ 676M (17 of ours) | 4 |
| Merlino S1 | 2 | 629M | 2 | ≥ 673M (17 of ours) | 4 |
| MuEzZa S2 | 2 | 622M | 2 | ≥ 666M (19 of ours) | 4 |
| ঔ×° Queen B °× S2 | 2 | 610M | 2 | ≥ 652M (20 of ours) | 4 |
| Abby2 S1 | 2 | 533M | 2 | ≥ 571M (40 of ours) | 4 |
| Merlino S2 | 2 | 509M | 2 | ≥ 544M (47 of ours) | 4 |
| E °°Liz°° S1 | 2 | 502M | 2 | ≥ 537M (54 of ours) | 4 |
| Softly Calmly S2 | 2 | 475M | 2 | ≥ 509M (59 of ours) | 4 |
| Sabri22 S2 | 2 | 430M | 2 | ≥ 460M (78 of ours) | 4 |
| Sand Ra S1 | 2 | 378M | 2 | ≥ 404M (101 of ours) | 4 |
| ShadowGhostJoint S1 | 2 | 342M | 2 | ≥ 366M (112 of ours) | 4 |
| InsideOut S1 | 2 | 336M | 2 | ≥ 360M (116 of ours) | 4 |
| Kelbo S1 | 2 | 314M | 2 | ≥ 336M (118 of ours) | 4 |
| Penguin Naj S2 | 2 | 313M | 2 | ≥ 334M (118 of ours) | 4 |
| Sea S1 | 2 | 306M | 2 | ≥ 328M (119 of ours) | 4 |
| Phantom Thief S1 | 2 | 246M | 2 | ≥ 263M (120 of ours) | 4 |
| Bay S1 | 3 | 608M | 2 | ≥ 651M (20 of ours) | 4 |
| Ndi Ari S2 | 3 | 604M | 2 | ≥ 647M (21 of ours) | 4 |
| ᖷ Bкᖷ S2 | 3 | 593M | 2 | ≥ 635M (22 of ours) | 4 |
| breta S2 | 3 | 551M | 2 | ≥ 590M (34 of ours) | 4 |
| Md0909 S2 | 3 | 543M | 2 | ≥ 581M (36 of ours) | 4 |
| Softly Calmly S1 | 3 | 537M | 2 | ≥ 575M (40 of ours) | 4 |
| Canine S1 | 3 | 480M | 2 | ≥ 514M (58 of ours) | 4 |
| Tania S1 | 3 | 469M | 2 | ≥ 501M (61 of ours) | 4 |
| NIHAKU° S2 | 3 | 455M | 2 | ≥ 487M (67 of ours) | 4 |
| Yahya07 S2 | 3 | 450M | 2 | ≥ 482M (68 of ours) | 4 |
| Abby2 S2 | 3 | 445M | 2 | ≥ 476M (70 of ours) | 4 |
| E °°Liz°° S2 | 3 | 410M | 2 | ≥ 439M (86 of ours) | 4 |
| Sand Ra S2 | 3 | 380M | 2 | ≥ 407M (100 of ours) | 4 |
| smol zeo ໒· S2 | 3 | 345M | 2 | ≥ 369M (112 of ours) | 4 |
| InsideOut S2 | 3 | 331M | 2 | ≥ 355M (117 of ours) | 4 |
| ShadowGhostJoint S2 | 3 | 320M | 2 | ≥ 342M (118 of ours) | 4 |
| Kelbo S2 | 3 | 283M | 2 | ≥ 303M (119 of ours) | 4 |
| Phantom Thief S2 | 3 | 215M | 2 | ≥ 230M (120 of ours) | 4 |

### Phase 3 — clear Strongholds 4 and 6

81 + 101 attacks for 42★. Wardens: Hornet S1 (712M, needs ≥ 762M), Ary S1 (1.22B, needs ≥ 1.31B).

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| Hornet S1 (W) | 4 | 712M | 2 | ≥ 762M (11 of ours) | 5 |
| Glooorz S1 | 4 | 671M | 1 | ≥ 718M (14 of ours) | 4 |
| leelee S1 | 4 | 614M | 1 | ≥ 657M (20 of ours) | 4 |
| Dao S1 | 4 | 571M | 1 | ≥ 611M (30 of ours) | 4 |
| Reyyy S1 | 4 | 554M | 1 | ≥ 592M (34 of ours) | 4 |
| Pyob S1 | 4 | 544M | 1 | ≥ 582M (35 of ours) | 4 |
| Hachiman S2 | 4 | 532M | 1 | ≥ 569M (40 of ours) | 4 |
| MuEzZa S1 | 4 | 510M | 1 | ≥ 546M (47 of ours) | 4 |
| Lia Alya S1 | 4 | 477M | 1 | ≥ 510M (58 of ours) | 4 |
| kajol S2 | 4 | 467M | 1 | ≥ 500M (61 of ours) | 4 |
| aliee S2 | 4 | 454M | 1 | ≥ 486M (68 of ours) | 4 |
| 肥來了 S1 | 4 | 444M | 1 | ≥ 476M (72 of ours) | 4 |
| Wasp S1 | 4 | 433M | 1 | ≥ 463M (76 of ours) | 4 |
| Nath S1 | 4 | 415M | 1 | ≥ 444M (85 of ours) | 4 |
| Canine S2 | 4 | 401M | 1 | ≥ 429M (88 of ours) | 4 |
| Sollazza S2 | 4 | 370M | 1 | ≥ 396M (104 of ours) | 4 |
| User1234 S1 | 4 | 277M | 1 | ≥ 297M (119 of ours) | 4 |
| Sea S2 | 4 | 241M | 1 | ≥ 258M (120 of ours) | 4 |
| little ol' me S1 | 4 | 175M | 1 | ≥ 187M (120 of ours) | 4 |
| Splinter S1 | 4 | 139M | 1 | ≥ 149M (120 of ours) | 4 |
| Ary S1 (W) | 6 | 1.22B | 2 | ≥ 1.31B (0 of ours) | 25 |
| NIHAKU° S1 | 6 | 596M | 1 | ≥ 638M (22 of ours) | 4 |
| aliee S1 | 6 | 525M | 1 | ≥ 562M (41 of ours) | 4 |
| Nomad S2 | 6 | 513M | 1 | ≥ 549M (47 of ours) | 4 |
| Simba S2 | 6 | 509M | 1 | ≥ 545M (47 of ours) | 4 |
| Sollazza S1 | 6 | 488M | 1 | ≥ 522M (56 of ours) | 4 |
| LIN S2 | 6 | 455M | 1 | ≥ 487M (67 of ours) | 4 |
| SUPER Szeee S2 | 6 | 448M | 1 | ≥ 479M (69 of ours) | 4 |
| Lia Alya S2 | 6 | 440M | 1 | ≥ 471M (74 of ours) | 4 |
| Evil Bunny S1 | 6 | 429M | 1 | ≥ 459M (79 of ours) | 4 |
| Nath S2 | 6 | 412M | 1 | ≥ 441M (85 of ours) | 4 |
| SoftieDriftie S1 | 6 | 405M | 1 | ≥ 434M (86 of ours) | 4 |
| Penguin Naj S1 | 6 | 399M | 1 | ≥ 427M (88 of ours) | 4 |
| Blueberry S2 | 6 | 389M | 1 | ≥ 417M (93 of ours) | 4 |
| Tania S2 | 6 | 388M | 1 | ≥ 415M (95 of ours) | 4 |
| Wasp S2 | 6 | 346M | 1 | ≥ 370M (112 of ours) | 4 |
| Sparrow S1 | 6 | 341M | 1 | ≥ 365M (113 of ours) | 4 |
| ঔ×°Persephone°× S1 | 6 | 322M | 1 | ≥ 344M (118 of ours) | 4 |
| Sparrow S2 | 6 | 312M | 1 | ≥ 334M (118 of ours) | 4 |
| ঔ×°Persephone°× S2 | 6 | 260M | 1 | ≥ 278M (120 of ours) | 4 |

### Phase 4 — mid 2★ targets in Strongholds 2 and 3

2 squads that 3–11 of our squads beat outright, or that need a bait or two: ~8 attacks for 4★.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| Fury S2 | 2 | 729M | 2 | ≥ 780M (11 of ours) | 4 |
| TLE_Nick S2 | 3 | 817M | 2 | ≥ 875M (6 of ours) | 4 |

### Phase 5 — only with leftover attempts: the hard 2★ targets

2 squads that need several baits per Heart before a top squad can finish: ~45 attacks for 8★. Poor value.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| Ary S2 (W) | 2 | 963M | 4 | ≥ 1.03B (1 of ours) | 10 |
| KnackeredNoggin S2 (W) | 3 | 1.91B | 4 | ≥ 2.04B (0 of ours) | 35 |

### Phase 6 — if Stronghold 2 is fully cleared (~86 attacks): farm Stronghold 1

18 squads worth 3★ that we beat outright or nearly: ~72 attacks for 54★. Their Stronghold 1 Warden is unkillable, so it can never be zeroed.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| Gettitt S1 | 1 | 897M | 3 | ≥ 960M (4 of ours) | 4 |
| Fury S1 | 1 | 894M | 3 | ≥ 957M (5 of ours) | 4 |
| ঔ×° Queen B °× S1 | 1 | 808M | 3 | ≥ 865M (6 of ours) | 4 |
| Alizarin Crimson S1 | 1 | 717M | 3 | ≥ 767M (11 of ours) | 4 |
| ᖷ Bкᖷ S1 | 1 | 678M | 3 | ≥ 725M (14 of ours) | 4 |
| Md0909 S1 | 1 | 661M | 3 | ≥ 708M (15 of ours) | 4 |
| Atreyu S1 | 1 | 639M | 3 | ≥ 683M (17 of ours) | 4 |
| Nomad S1 | 1 | 608M | 3 | ≥ 651M (20 of ours) | 4 |
| Glooorz S2 | 1 | 595M | 3 | ≥ 636M (22 of ours) | 4 |
| Hornet S2 | 1 | 579M | 3 | ≥ 619M (27 of ours) | 4 |
| SUPER Szeee S1 | 1 | 553M | 3 | ≥ 592M (34 of ours) | 4 |
| Alizarin Crimson S2 | 1 | 551M | 3 | ≥ 589M (34 of ours) | 4 |
| Bay S2 | 1 | 497M | 3 | ≥ 532M (54 of ours) | 4 |
| Yahya07 S1 | 1 | 495M | 3 | ≥ 529M (55 of ours) | 4 |
| kajol S1 | 1 | 485M | 3 | ≥ 519M (57 of ours) | 4 |
| smol zeo ໒· S1 | 1 | 476M | 3 | ≥ 509M (59 of ours) | 4 |
| Blueberry S1 | 1 | 440M | 3 | ≥ 471M (74 of ours) | 4 |
| Evil Bunny S2 | 1 | 425M | 3 | ≥ 454M (83 of ours) | 4 |

## Roles

| SIN squad | Power | Beats outright up to | Role |
|---|---|---|---|
| (blank) S1 (SH1) | 1.24B | 1.16B | Finisher — save attempts for baited whales; don't spend them on fronts |
| ⊶GuGu⊷ S1 (SH2) | 1.01B | 942M | Finisher — save attempts for baited whales; don't spend them on fronts |
| (blank) S2 (SH1) | 981M | 917M | Heavy hitter — front Wardens and the 600–750M squads |
| Hassikkome S1 (SH5) | 963M | 900M | Heavy hitter — front Wardens and the 600–750M squads |
| FedeC S1 (SH3) | 959M | 896M | Heavy hitter — front Wardens and the 600–750M squads |
| Kloss S1 (SH4) | 924M | 864M | Heavy hitter — front Wardens and the 600–750M squads |
| ⊶GuGu⊷ S2 (SH2) | 839M | 784M | Heavy hitter — front Wardens and the 600–750M squads |
| eneny S1 (SH5) | 836M | 781M | Heavy hitter — front Wardens and the 600–750M squads |
| Rebel S1 (SH6) | 810M | 757M | Heavy hitter — front Wardens and the 600–750M squads |
| kr1dm S1 (SH1) | 807M | 754M | Heavy hitter — front Wardens and the 600–750M squads |
| Kloss S2 (SH4) | 806M | 753M | Heavy hitter — front Wardens and the 600–750M squads |
| Hassikkome S2 (SH5) | 752M | 703M | Heavy hitter — front Wardens and the 600–750M squads |
| FedeC S2 (SH3) | 737M | 689M | Heavy hitter — front Wardens and the 600–750M squads |
| Dziadek S1 (SH3) | 732M | 684M | Heavy hitter — front Wardens and the 600–750M squads |
| Narcotics S1 (SH1) | 713M | 666M | Heavy hitter — front Wardens and the 600–750M squads |
| elvs S1 (SH1) | 696M | 650M | Line hitter — fronts and the cheap 2★ farm |
| iain Frost S1 (SH4) | 690M | 645M | Line hitter — fronts and the cheap 2★ farm |
| Toad S1 (SH5) | 670M | 626M | Line hitter — fronts and the cheap 2★ farm |
| Rebel S2 (SH3) | 668M | 624M | Line hitter — fronts and the cheap 2★ farm |
| LordTheGreatest S1 (SH3) | 657M | 614M | Line hitter — fronts and the cheap 2★ farm |
| TMBSHROOM S1 (SH1) | 650M | 607M | Line hitter — fronts and the cheap 2★ farm |
| Hunger4More S1 (SH3) | 638M | 596M | Line hitter — fronts and the cheap 2★ farm |
| Lime Knight S1 (SH5) | 631M | 589M | Line hitter — fronts and the cheap 2★ farm |
| Kookie S1 (SH5) | 630M | 589M | Line hitter — fronts and the cheap 2★ farm |
| Andrez S1 (SH4) | 629M | 587M | Line hitter — fronts and the cheap 2★ farm |
| Pipeline S1 (SH5) | 626M | 586M | Line hitter — fronts and the cheap 2★ farm |
| Kitto Katto S1 (SH4) | 624M | 583M | Line hitter — fronts and the cheap 2★ farm |
| kr1dm S2 (SH5) | 618M | 578M | Line hitter — fronts and the cheap 2★ farm |
| AlexWinter S1 (SH3) | 616M | 576M | Line hitter — fronts and the cheap 2★ farm |
| ItsAllemao S1 (SH1) | 612M | 572M | Line hitter — fronts and the cheap 2★ farm |
| GaTTo S1 (SH4) | 608M | 568M | Line hitter — fronts and the cheap 2★ farm |
| eneny S2 (SH5) | 602M | 563M | Line hitter — fronts and the cheap 2★ farm |
| Aira S1 (SH3) | 602M | 562M | Line hitter — fronts and the cheap 2★ farm |
| Dziadek S2 (SH5) | 601M | 561M | Line hitter — fronts and the cheap 2★ farm |
| Darkzeeko S1 (SH1) | 585M | 546M | Line hitter — fronts and the cheap 2★ farm |
| Tanmay S1 (SH3) | 581M | 543M | Line hitter — fronts and the cheap 2★ farm |
| LordTheGreatest S2 (SH1) | 581M | 543M | Line hitter — fronts and the cheap 2★ farm |
| elvs S2 (SH1) | 580M | 542M | Line hitter — fronts and the cheap 2★ farm |
| Garlicmushroom S1 (SH5) | 579M | 541M | Line hitter — fronts and the cheap 2★ farm |
| Xena S1 (SH4) | 578M | 540M | Line hitter — fronts and the cheap 2★ farm |
| David Hasselhoff S1 (SH5) | 562M | 526M | Line hitter — fronts and the cheap 2★ farm |
| R¥NO S1 (SH4) | 556M | 520M | Line hitter — fronts and the cheap 2★ farm |
| Šaturdaÿ S1 (SH6) | 552M | 516M | Line hitter — fronts and the cheap 2★ farm |
| Alpinacolada S1 (SH2) | 552M | 516M | Line hitter — fronts and the cheap 2★ farm |
| Toad S2 (SH1) | 552M | 516M | Line hitter — fronts and the cheap 2★ farm |
| iain Frost S2 (SH4) | 551M | 515M | Line hitter — fronts and the cheap 2★ farm |
| GaTTo S2 (SH2) | 549M | 513M | Line hitter — fronts and the cheap 2★ farm |
| MBG S1 (SH1) | 544M | 508M | Line hitter — fronts and the cheap 2★ farm |
| Narcotics S2 (SH3) | 543M | 508M | Line hitter — fronts and the cheap 2★ farm |
| TMBSHROOM S2 (SH5) | 539M | 504M | Line hitter — fronts and the cheap 2★ farm |
| Edo S1 (SH4) | 539M | 504M | Line hitter — fronts and the cheap 2★ farm |
| Andrez S2 (SH6) | 538M | 503M | Line hitter — fronts and the cheap 2★ farm |
| Milord S1 (SH1) | 538M | 502M | Line hitter — fronts and the cheap 2★ farm |
| Pipeline S2 (SH5) | 537M | 502M | Line hitter — fronts and the cheap 2★ farm |
| AlexWinter S2 (SH3) | 532M | 497M | Line hitter — fronts and the cheap 2★ farm |
| Katemush S1 (SH5) | 528M | 493M | Line hitter — fronts and the cheap 2★ farm |
| Hunger4More S2 (SH2) | 520M | 486M | Line hitter — fronts and the cheap 2★ farm |
| huam41 S1 (SH4) | 517M | 483M | Line hitter — fronts and the cheap 2★ farm |
| Kookie S2 (SH3) | 509M | 476M | Line hitter — fronts and the cheap 2★ farm |
| Edo S2 (SH1) | 505M | 472M | Line hitter — fronts and the cheap 2★ farm |
| Chu S1 (SH5) | 503M | 470M | Line hitter — fronts and the cheap 2★ farm |
| Aira S2 (SH2) | 498M | 465M | Line hitter — fronts and the cheap 2★ farm |
| LaCrazyLicorne S1 (SH3) | 497M | 465M | Line hitter — fronts and the cheap 2★ farm |
| Kitto Katto S2 (SH2) | 497M | 465M | Line hitter — fronts and the cheap 2★ farm |
| Tanmay S2 (SH3) | 496M | 464M | Line hitter — fronts and the cheap 2★ farm |
| Katemush S2 (SH3) | 489M | 457M | Line hitter — fronts and the cheap 2★ farm |
| Lime Knight S2 (SH6) | 489M | 457M | Line hitter — fronts and the cheap 2★ farm |
| Darkzeeko S2 (SH4) | 486M | 454M | Line hitter — fronts and the cheap 2★ farm |
| David Hasselhoff S2 (SH6) | 481M | 450M | Line hitter — fronts and the cheap 2★ farm |
| ItsAllemao S2 (SH2) | 479M | 447M | Line hitter — fronts and the cheap 2★ farm |
| Šaturdaÿ S2 (SH2) | 476M | 445M | Line hitter — fronts and the cheap 2★ farm |
| °°CABRILIK°° S2 (SH6) | 476M | 444M | Line hitter — fronts and the cheap 2★ farm |
| MBG S2 (SH2) | 474M | 443M | Line hitter — fronts and the cheap 2★ farm |
| Xena S2 (SH6) | 471M | 441M | Line hitter — fronts and the cheap 2★ farm |
| Alpinacolada S2 (SH1) | 465M | 435M | Line hitter — fronts and the cheap 2★ farm |
| Milord S2 (SH1) | 463M | 433M | Line hitter — fronts and the cheap 2★ farm |
| Ferfecir S2 (SH3) | 462M | 431M | Line hitter — fronts and the cheap 2★ farm |
| Rochus0815 S1 (SH5) | 461M | 431M | Line hitter — fronts and the cheap 2★ farm |
| °°CABRILIK°° S1 (SH4) | 459M | 429M | Line hitter — fronts and the cheap 2★ farm |
| Old_Viking S1 (SH4) | 457M | 427M | Line hitter — fronts and the cheap 2★ farm |
| @MONEY@ S1 (SH1) | 457M | 427M | Line hitter — fronts and the cheap 2★ farm |
| R¥NO S2 (SH6) | 456M | 426M | Line hitter — fronts and the cheap 2★ farm |
| Ferfecir S1 (SH2) | 455M | 426M | Line hitter — fronts and the cheap 2★ farm |
| LaCrazyLicorne S2 (SH4) | 452M | 422M | Line hitter — fronts and the cheap 2★ farm |
| huam41 S2 (SH4) | 449M | 420M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| itzdk420 S1 (SH2) | 441M | 412M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Stesha S1 (SH2) | 433M | 404M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Ania 2000 S1 (SH5) | 430M | 401M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| tay S1 (SH2) | 423M | 395M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| JBV S1 (SH6) | 421M | 394M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Cui S1 (SH4) | 420M | 392M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Garlicmushroom S2 (SH6) | 418M | 390M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Jelly S2 (SH3) | 418M | 390M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Ania 2000 S2 (SH5) | 416M | 389M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| winter_ S1 (SH3) | 415M | 388M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| 犬醉雨 S1 (SH3) | 415M | 388M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| 犬醉雨 S2 (SH3) | 410M | 384M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| gusdyds7 S1 (SH1) | 410M | 384M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Jelly S1 (SH4) | 410M | 383M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| JBV S2 (SH6) | 408M | 381M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| YꙨM S1 (SH2) | 405M | 378M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Cui S2 (SH5) | 402M | 376M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| MaD_MaN S1 (SH6) | 401M | 374M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Klaus_jr S1 (SH6) | 397M | 371M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| itzdk420 S2 (SH2) | 395M | 369M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Chu S2 (SH6) | 392M | 367M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| HouShroom :o S1 (SH6) | 391M | 366M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Rochus0815 S2 (SH6) | 388M | 362M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Türk Devleti S1 (SH1) | 378M | 353M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| LordOfSurvival S1 (SH6) | 375M | 351M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Stesha S2 (SH1) | 374M | 350M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| @MONEY@ S2 (SH2) | 373M | 349M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| gusdyds7 S2 (SH2) | 366M | 342M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| MaD_MaN S2 (SH6) | 364M | 341M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| tay S2 (SH6) | 363M | 339M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Old_Viking S2 (SH6) | 361M | 337M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Thiago Casarini S1 (SH4) | 355M | 332M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Андрюха S1 (SH4) | 345M | 323M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Türk Devleti S2 (SH2) | 331M | 309M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| dul S1 (SH2) | 280M | 262M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
