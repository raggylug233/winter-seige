# SIN vs [HoT] — matchup analysis and attack plan

Generated 2026-10-16 from scouted garrisons (`friendly-SIN-1015.csv`, `enemy-HoT.csv`).

## Who is stronger

| | SIN | [HoT] |
|---|---|---|
| Garrison power | 69.00B | 60.38B |
| Squads ≥ 1B / ≥ 2B | 5 / 0 | 10 / 0 |
| Strongest squad | 1.34B | 1.58B |
| Stars on board | 210 | 208 |
| Layout | front-heavy (strength at the fronts): core 12.88B, middle 21.75B, fronts 34.36B | front-heavy (strength at the fronts): core 11.08B, middle 19.72B, fronts 29.58B |
| Squads the other side cannot kill (60% floor) | 0: none | 0: none |

### Per stronghold

| Stronghold | SIN power · ★ · Warden | [HoT] power · ★ · Warden | attacks for us to clear | attacks for them to clear |
|---|---|---|---|---|
| 1 (Empowered) | 12.88B · 63★ · (blank) S1 1.34B | 11.08B · 63★ · Falcon S1 1.58B | ~212 | ~107 |
| 2 (Advanced) | 11.43B · 42★ · GuGu S1 1.16B | 9.35B · 42★ · BRWDKS S1 1.43B | ~188 | ~101 |
| 3 (Advanced) | 10.33B · 42★ · FrankenKloss S1 979M | 10.37B · 42★ · Nneo HoT S1 1.37B | ~167 | ~101 |
| 4 (Primitive) | 9.87B · 21★ · eneny S1 991M | 9.54B · 21★ · MAzEN S2 1.29B | ~155 | ~101 |
| 5 (Primitive) | 12.24B · 21★ · FedeC S1 1.07B | 9.90B · 20★ · Falcon S2 1.21B | ~132 | ~101 |
| 6 (Primitive) | 12.25B · 21★ · Count Hassicula S1 1.07B | 10.13B · 20★ · END S1 1.33B | ~181 | ~101 |

## Simulation

Same model as our own plan (`sim.py`): path unlocking, win chance rising with power ratio, in-game morale rule, coordinated and greedy attacker behaviours, 8 runs. Columns are attacks landed per squad (each side has 10; sleep and waste push the real number down).

| Attacks landed per squad | 3 | 4 | 5 | 6 | 8 |
|---|---|---|---|---|---|
| Stars [HoT] loses when SIN attacks (of 208) | 43 / 52 | 77 / 84 | 91 / 123 | 102 / 137 | 146 / 194 |
| Stars SIN loses when [HoT] attacks (of 210) | 59 / 59 | 87 / 87 | 112 / 114 | 135 / 137 | 154 / 155 |

**Verdict: Too close to call at equal activity — whoever uses more of their attacks wins.** Ceiling for SIN: 208★ of 208 (the rest sits on unkillable squads).

## Attack plan for SIN

Rules for every attack: hit only the current phase's stronghold (a half-cleared stronghold unlocks nothing); hit only targets you beat outright — your power ≥ 1.07× theirs at their current morale; a lost attack is only useful as a planned bait; use attempts as they restore (1 per squad every 2 h).

### Phase 1 — open the map: clear Stronghold 5

Opens both 2 and 3; the cheapest front at ~132 attacks for 20★. Warden Falcon S2 (1.21B, 6 Hearts) needs attackers over 1.29B after baiting (~42 attacks).

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| Falcon S2 (W) | 5 | 1.21B | 2 | ≥ 1.29B (1 of ours) | 42 |
| Nneo farm HoT S1 | 5 | 707M | 1 | ≥ 756M (14 of ours) | 5 |
| LuckeyCZ S2 | 5 | 689M | 1 | ≥ 737M (17 of ours) | 5 |
| Iban le terible S2 | 5 | 670M | 1 | ≥ 717M (19 of ours) | 5 |
| Sunat S1 | 5 | 628M | 1 | ≥ 672M (26 of ours) | 5 |
| Evernight Sun S2 | 5 | 600M | 1 | ≥ 642M (30 of ours) | 5 |
| VikkiLi S1 | 5 | 599M | 1 | ≥ 641M (30 of ours) | 5 |
| chickenjockey S2 | 5 | 592M | 1 | ≥ 634M (33 of ours) | 5 |
| Lord Basquegrand S1 | 5 | 560M | 1 | ≥ 600M (45 of ours) | 5 |
| mhm S2 | 5 | 549M | 1 | ≥ 587M (47 of ours) | 5 |
| Lord Basquegrand S2 | 5 | 457M | 1 | ≥ 489M (79 of ours) | 5 |
| Cold Patriot S1 | 5 | 456M | 1 | ≥ 488M (80 of ours) | 5 |
| cb659 S1 | 5 | 453M | 1 | ≥ 484M (81 of ours) | 5 |
| cb659 S2 | 5 | 436M | 1 | ≥ 467M (82 of ours) | 5 |
| Bluemoon S1 | 5 | 374M | 1 | ≥ 400M (101 of ours) | 5 |
| Cuddleshad13 S2 | 5 | 354M | 1 | ≥ 379M (106 of ours) | 5 |
| RavenOfGod S2 | 5 | 286M | 1 | ≥ 306M (117 of ours) | 5 |
| FlorLarsLou S1 | 5 | 247M | 1 | ≥ 264M (120 of ours) | 5 |
| LittleFalcon S2 | 5 | 42M | 1 | ≥ 45M (120 of ours) | 5 |

### Phase 2 — farm the cheap 2★ squads in Strongholds 2 and 3

37 squads worth 2★ each that 12+ of our squads beat outright: ~185 attacks for 74★. Best Stars-per-attack on their board. Leave their whales alone for now.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| Iban le terible S1 | 2 | 825M | 2 | ≥ 883M (12 of ours) | 5 |
| Bishoy S2 | 2 | 550M | 2 | ≥ 589M (46 of ours) | 5 |
| Ahmed Wafaey S1 | 2 | 532M | 2 | ≥ 569M (55 of ours) | 5 |
| robetovich S1 | 2 | 516M | 2 | ≥ 552M (56 of ours) | 5 |
| Honeydaddy S1 | 2 | 504M | 2 | ≥ 539M (61 of ours) | 5 |
| Aria Shah S1 | 2 | 444M | 2 | ≥ 475M (81 of ours) | 5 |
| Honeydaddy S2 | 2 | 431M | 2 | ≥ 461M (85 of ours) | 5 |
| 猫咪喵喵叫 S1 | 2 | 423M | 2 | ≥ 453M (87 of ours) | 5 |
| Wil S1 | 2 | 324M | 2 | ≥ 347M (113 of ours) | 5 |
| Wil S2 | 2 | 313M | 2 | ≥ 335M (113 of ours) | 5 |
| Banana bond S2 | 2 | 309M | 2 | ≥ 330M (115 of ours) | 5 |
| Lee S2 | 2 | 300M | 2 | ≥ 321M (116 of ours) | 5 |
| WOSoholic S2 | 2 | 293M | 2 | ≥ 314M (116 of ours) | 5 |
| RAJAFARMhot S1 | 2 | 291M | 2 | ≥ 312M (116 of ours) | 5 |
| RAJAFARMhot S2 | 2 | 237M | 2 | ≥ 254M (120 of ours) | 5 |
| fm4vxll S2 | 2 | 207M | 2 | ≥ 221M (120 of ours) | 5 |
| TaFiK FARMhot S1 | 2 | 201M | 2 | ≥ 216M (120 of ours) | 5 |
| GOTA S1 | 2 | 99M | 2 | ≥ 106M (120 of ours) | 5 |
| MUSTAFA S1 | 3 | 810M | 2 | ≥ 867M (12 of ours) | 5 |
| VOLYA S1 | 3 | 760M | 2 | ≥ 813M (13 of ours) | 5 |
| Evernight Sun S1 | 3 | 691M | 2 | ≥ 739M (17 of ours) | 5 |
| VOLYA S2 | 3 | 675M | 2 | ≥ 722M (19 of ours) | 5 |
| chickenjockey S1 | 3 | 653M | 2 | ≥ 698M (22 of ours) | 5 |
| mhm S1 | 3 | 560M | 2 | ≥ 599M (45 of ours) | 5 |
| Sunat S2 | 3 | 549M | 2 | ≥ 588M (47 of ours) | 5 |
| VikkiLi S2 | 3 | 541M | 2 | ≥ 579M (50 of ours) | 5 |
| LoneWolf S1 | 3 | 531M | 2 | ≥ 568M (55 of ours) | 5 |
| Ahmed Wafaey S2 | 3 | 480M | 2 | ≥ 513M (67 of ours) | 5 |
| Cold Patriot S2 | 3 | 441M | 2 | ≥ 472M (81 of ours) | 5 |
| robetovich S2 | 3 | 428M | 2 | ≥ 458M (86 of ours) | 5 |
| Cuddleshad13 S1 | 3 | 369M | 2 | ≥ 395M (103 of ours) | 5 |
| Jameson S2 | 3 | 321M | 2 | ≥ 344M (113 of ours) | 5 |
| Harshdeep Singh S2 | 3 | 316M | 2 | ≥ 338M (113 of ours) | 5 |
| 猫咪喵喵叫 S2 | 3 | 297M | 2 | ≥ 318M (116 of ours) | 5 |
| Rehan Ali S2 | 3 | 203M | 2 | ≥ 217M (120 of ours) | 5 |
| Rehan Ali S1 | 3 | 189M | 2 | ≥ 202M (120 of ours) | 5 |
| TaFiK FARMhot S2 | 3 | 184M | 2 | ≥ 197M (120 of ours) | 5 |

### Phase 3 — clear Strongholds 4 and 6

155 + 181 attacks for 41★. Wardens: MAzEN S2 (1.29B, needs ≥ 1.38B), END S1 (1.33B, needs ≥ 1.42B).

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| MAzEN S2 (W) | 4 | 1.29B | 2 | ≥ 1.38B (0 of ours) | 60 |
| aiku S2 | 4 | 869M | 1 | ≥ 929M (8 of ours) | 5 |
| TaFiKhot S1 | 4 | 732M | 1 | ≥ 784M (13 of ours) | 5 |
| Rajahot S1 | 4 | 639M | 1 | ≥ 684M (25 of ours) | 5 |
| Rajahot S2 | 4 | 537M | 1 | ≥ 575M (50 of ours) | 5 |
| liskh S1 | 4 | 496M | 1 | ≥ 531M (65 of ours) | 5 |
| Aria Shah S2 | 4 | 495M | 1 | ≥ 530M (65 of ours) | 5 |
| LoneWolf S2 | 4 | 485M | 1 | ≥ 518M (67 of ours) | 5 |
| Killer S2 | 4 | 482M | 1 | ≥ 515M (67 of ours) | 5 |
| liskh S2 | 4 | 477M | 1 | ≥ 510M (68 of ours) | 5 |
| KimBacktou S1 | 4 | 424M | 1 | ≥ 454M (87 of ours) | 5 |
| Lord Tichondrius S1 | 4 | 424M | 1 | ≥ 453M (87 of ours) | 5 |
| Five S2 | 4 | 409M | 1 | ≥ 437M (92 of ours) | 5 |
| ELNEGRO S1 | 4 | 398M | 1 | ≥ 426M (96 of ours) | 5 |
| Lord Tichondrius S2 | 4 | 370M | 1 | ≥ 396M (103 of ours) | 5 |
| KimBacktou S2 | 4 | 331M | 1 | ≥ 354M (110 of ours) | 5 |
| RavenOfGod S1 | 4 | 301M | 1 | ≥ 322M (116 of ours) | 5 |
| fm4vxll S1 | 4 | 242M | 1 | ≥ 259M (120 of ours) | 5 |
| Poseidon S1 | 4 | 85M | 1 | ≥ 91M (120 of ours) | 5 |
| LittleFalcon S1 | 4 | 55M | 1 | ≥ 59M (120 of ours) | 5 |
| END S1 (W) | 6 | 1.33B | 2 | ≥ 1.42B (0 of ours) | 66 |
| aiku S1 | 6 | 1.17B | 1 | ≥ 1.25B (1 of ours) | 30 |
| LuckeyCZ S1 | 6 | 868M | 1 | ≥ 929M (8 of ours) | 5 |
| Nando S1 | 6 | 756M | 1 | ≥ 809M (13 of ours) | 5 |
| TaFiKhot S2 | 6 | 641M | 1 | ≥ 686M (25 of ours) | 5 |
| Nando S2 | 6 | 630M | 1 | ≥ 674M (26 of ours) | 5 |
| MUSTAFA S2 | 6 | 625M | 1 | ≥ 668M (27 of ours) | 5 |
| Killer S1 | 6 | 541M | 1 | ≥ 579M (50 of ours) | 5 |
| Five S1 | 6 | 465M | 1 | ≥ 497M (76 of ours) | 5 |
| RedJacks S1 | 6 | 456M | 1 | ≥ 488M (79 of ours) | 5 |
| RedJacks S2 | 6 | 410M | 1 | ≥ 439M (91 of ours) | 5 |
| ELNEGRO S2 | 6 | 388M | 1 | ≥ 416M (97 of ours) | 5 |
| Bluemoon S2 | 6 | 379M | 1 | ≥ 405M (101 of ours) | 5 |
| Jameson S1 | 6 | 368M | 1 | ≥ 394M (103 of ours) | 5 |
| GoGoGo 3180 S1 | 6 | 363M | 1 | ≥ 389M (105 of ours) | 5 |
| GoGoGo 3180 S2 | 6 | 294M | 1 | ≥ 314M (116 of ours) | 5 |
| FlorLarsLou S2 | 6 | 220M | 1 | ≥ 235M (120 of ours) | 5 |
| GOTA S2 | 6 | 161M | 1 | ≥ 172M (120 of ours) | 5 |
| Poseidon S2 | 6 | 74M | 1 | ≥ 79M (120 of ours) | 5 |

### Phase 5 — only with leftover attempts: the hard 2★ targets

3 squads that need several baits per Heart before a top squad can finish: ~170 attacks for 10★. Poor value.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| BRWDKS S1 (W) | 2 | 1.43B | 4 | ≥ 1.53B (0 of ours) | 78 |
| Nneo HoT S2 | 2 | 1.12B | 2 | ≥ 1.20B (1 of ours) | 20 |
| Nneo HoT S1 (W) | 3 | 1.37B | 4 | ≥ 1.47B (0 of ours) | 72 |

### Phase 6 — if Stronghold 3 is fully cleared (~167 attacks): farm Stronghold 1

17 squads worth 3★ that we beat outright or nearly: ~85 attacks for 51★. Their Stronghold 1 can be zeroed.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| MAzEN S1 | 1 | 949M | 3 | ≥ 1.02B (4 of ours) | 5 |
| Kamal R S1 | 1 | 672M | 3 | ≥ 719M (19 of ours) | 5 |
| Bishoy S1 | 1 | 620M | 3 | ≥ 663M (27 of ours) | 5 |
| Kamal R S2 | 1 | 593M | 3 | ≥ 635M (33 of ours) | 5 |
| Nneo farm HoT S2 | 1 | 528M | 3 | ≥ 565M (55 of ours) | 5 |
| Banana bond S1 | 1 | 422M | 3 | ≥ 451M (87 of ours) | 5 |
| ARM S1 | 1 | 402M | 3 | ≥ 430M (94 of ours) | 5 |
| Yukon Cornelius S1 | 1 | 392M | 3 | ≥ 420M (97 of ours) | 5 |
| Mo7med S1 | 1 | 375M | 3 | ≥ 401M (101 of ours) | 5 |
| ARM S2 | 1 | 368M | 3 | ≥ 394M (103 of ours) | 5 |
| Mo7med S2 | 1 | 355M | 3 | ≥ 380M (106 of ours) | 5 |
| Yukon Cornelius S2 | 1 | 337M | 3 | ≥ 361M (109 of ours) | 5 |
| WOSoholic S1 | 1 | 331M | 3 | ≥ 354M (110 of ours) | 5 |
| Lee S1 | 1 | 320M | 3 | ≥ 343M (113 of ours) | 5 |
| Harshdeep Singh S1 | 1 | 320M | 3 | ≥ 342M (113 of ours) | 5 |
| Mic S1 | 1 | 218M | 3 | ≥ 233M (120 of ours) | 5 |
| Mic S2 | 1 | 183M | 3 | ≥ 196M (120 of ours) | 5 |

## Roles

| SIN squad | Power | Beats outright up to | Role |
|---|---|---|---|
| (blank) S1 (SH1) | 1.34B | 1.25B | Finisher — save attempts for baited whales; don't spend them on fronts |
| GuGu S1 (SH2) | 1.16B | 1.08B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Count Hassicula S1 (SH6) | 1.07B | 1.00B | Finisher — save attempts for baited whales; don't spend them on fronts |
| FedeC S1 (SH5) | 1.07B | 1.00B | Finisher — save attempts for baited whales; don't spend them on fronts |
| (blank) S2 (SH1) | 1.00B | 937M | Finisher — save attempts for baited whales; don't spend them on fronts |
| eneny S1 (SH4) | 991M | 926M | Heavy hitter — front Wardens and the 600–750M squads |
| FrankenKloss S1 (SH3) | 979M | 915M | Heavy hitter — front Wardens and the 600–750M squads |
| GuGu S2 (SH2) | 970M | 907M | Heavy hitter — front Wardens and the 600–750M squads |
| FedeC S2 (SH6) | 912M | 852M | Heavy hitter — front Wardens and the 600–750M squads |
| Count Hassicula S2 (SH6) | 906M | 847M | Heavy hitter — front Wardens and the 600–750M squads |
| Dziadzilla S1 (SH4) | 895M | 837M | Heavy hitter — front Wardens and the 600–750M squads |
| kr1dm S1 (SH6) | 890M | 832M | Heavy hitter — front Wardens and the 600–750M squads |
| FrankenKloss S2 (SH5) | 858M | 802M | Heavy hitter — front Wardens and the 600–750M squads |
| WARMachine S1 (SH5) | 769M | 718M | Heavy hitter — front Wardens and the 600–750M squads |
| iain Frost S1 (SH1) | 756M | 707M | Heavy hitter — front Wardens and the 600–750M squads |
| Dziadzilla S2 (SH5) | 755M | 706M | Heavy hitter — front Wardens and the 600–750M squads |
| elvs S1 (SH4) | 742M | 693M | Heavy hitter — front Wardens and the 600–750M squads |
| eneny S2 (SH5) | 727M | 680M | Heavy hitter — front Wardens and the 600–750M squads |
| ScareKlaus S1 (SH5) | 725M | 678M | Heavy hitter — front Wardens and the 600–750M squads |
| GreatestPumpkin S1 (SH1) | 706M | 660M | Heavy hitter — front Wardens and the 600–750M squads |
| TMB O'Lantern S1 (SH1) | 705M | 659M | Heavy hitter — front Wardens and the 600–750M squads |
| GaTTo S1 (SH1) | 699M | 654M | Line hitter — fronts and the cheap 2★ farm |
| Pipeline S1 (SH2) | 693M | 648M | Line hitter — fronts and the cheap 2★ farm |
| kr1dm S2 (SH1) | 693M | 648M | Line hitter — fronts and the cheap 2★ farm |
| Aqua_kookie S1 (SH2) | 686M | 641M | Line hitter — fronts and the cheap 2★ farm |
| Kitto Katto S1 (SH1) | 677M | 632M | Line hitter — fronts and the cheap 2★ farm |
| Pumpkin Knight S1 (SH6) | 669M | 626M | Line hitter — fronts and the cheap 2★ farm |
| AlexWinter S1 (SH5) | 661M | 618M | Line hitter — fronts and the cheap 2★ farm |
| Hunger4Brains S1 (SH5) | 656M | 613M | Line hitter — fronts and the cheap 2★ farm |
| ItsAllemao S1 (SH1) | 651M | 608M | Line hitter — fronts and the cheap 2★ farm |
| Elderberry TI S1 (SH5) | 641M | 599M | Line hitter — fronts and the cheap 2★ farm |
| David Hasselhoff S1 (SH6) | 637M | 596M | Line hitter — fronts and the cheap 2★ farm |
| Tanmay S1 (SH6) | 637M | 596M | Line hitter — fronts and the cheap 2★ farm |
| Šaturdaÿ S1 (SH3) | 631M | 590M | Line hitter — fronts and the cheap 2★ farm |
| GreatestPumpkin S2 (SH3) | 627M | 586M | Line hitter — fronts and the cheap 2★ farm |
| bygor666 S1 (SH5) | 619M | 578M | Line hitter — fronts and the cheap 2★ farm |
| MBG S1 (SH1) | 616M | 576M | Line hitter — fronts and the cheap 2★ farm |
| Kate S1 (SH2) | 616M | 576M | Line hitter — fronts and the cheap 2★ farm |
| elvs S2 (SH4) | 616M | 576M | Line hitter — fronts and the cheap 2★ farm |
| Edo S1 (SH1) | 616M | 576M | Line hitter — fronts and the cheap 2★ farm |
| Xena S1 (SH4) | 614M | 574M | Line hitter — fronts and the cheap 2★ farm |
| iain Frost S2 (SH5) | 607M | 567M | Line hitter — fronts and the cheap 2★ farm |
| Elderberry TI S2 (SH5) | 604M | 564M | Line hitter — fronts and the cheap 2★ farm |
| GaTTo S2 (SH3) | 601M | 562M | Line hitter — fronts and the cheap 2★ farm |
| Pina S1 (SH1) | 600M | 561M | Line hitter — fronts and the cheap 2★ farm |
| HEADLESS R¥NO S1 (SH6) | 596M | 557M | Line hitter — fronts and the cheap 2★ farm |
| ScareKlaus S2 (SH6) | 588M | 549M | Line hitter — fronts and the cheap 2★ farm |
| Kate S2 (SH2) | 587M | 548M | Line hitter — fronts and the cheap 2★ farm |
| TMB O'Lantern S2 (SH6) | 581M | 543M | Line hitter — fronts and the cheap 2★ farm |
| Milord S1 (SH3) | 580M | 542M | Line hitter — fronts and the cheap 2★ farm |
| Edo S2 (SH2) | 574M | 537M | Line hitter — fronts and the cheap 2★ farm |
| Pipeline S2 (SH2) | 574M | 537M | Line hitter — fronts and the cheap 2★ farm |
| bygor666 S2 (SH6) | 572M | 535M | Line hitter — fronts and the cheap 2★ farm |
| huam41 S1 (SH4) | 572M | 535M | Line hitter — fronts and the cheap 2★ farm |
| AlexWinter S2 (SH5) | 569M | 532M | Line hitter — fronts and the cheap 2★ farm |
| Aqua_kookie S2 (SH1) | 558M | 522M | Line hitter — fronts and the cheap 2★ farm |
| Hunger4Brains S2 (SH5) | 550M | 514M | Line hitter — fronts and the cheap 2★ farm |
| WARMachine S2 (SH2) | 543M | 507M | Line hitter — fronts and the cheap 2★ farm |
| Chu S1 (SH3) | 543M | 507M | Line hitter — fronts and the cheap 2★ farm |
| Kitto Katto S2 (SH3) | 543M | 507M | Line hitter — fronts and the cheap 2★ farm |
| LaCrazyLicorne S1 (SH3) | 540M | 505M | Line hitter — fronts and the cheap 2★ farm |
| Šaturdaÿ S2 (SH6) | 534M | 499M | Line hitter — fronts and the cheap 2★ farm |
| Tanmay S2 (SH6) | 534M | 499M | Line hitter — fronts and the cheap 2★ farm |
| Pina S2 (SH2) | 534M | 499M | Line hitter — fronts and the cheap 2★ farm |
| David Hasselhoff S2 (SH6) | 531M | 497M | Line hitter — fronts and the cheap 2★ farm |
| MBG S2 (SH4) | 522M | 488M | Line hitter — fronts and the cheap 2★ farm |
| Pumpkin Knight S2 (SH3) | 521M | 487M | Line hitter — fronts and the cheap 2★ farm |
| itzdk420 S1 (SH6) | 512M | 478M | Line hitter — fronts and the cheap 2★ farm |
| Ferfecir S2 (SH2) | 506M | 473M | Line hitter — fronts and the cheap 2★ farm |
| Rochus0815 S1 (SH1) | 506M | 472M | Line hitter — fronts and the cheap 2★ farm |
| Ferfecir S1 (SH1) | 504M | 471M | Line hitter — fronts and the cheap 2★ farm |
| MORCABRI S1 (SH1) | 504M | 471M | Line hitter — fronts and the cheap 2★ farm |
| ItsAllemao S2 (SH3) | 504M | 471M | Line hitter — fronts and the cheap 2★ farm |
| huam41 S2 (SH4) | 502M | 469M | Line hitter — fronts and the cheap 2★ farm |
| Milord S2 (SH3) | 501M | 468M | Line hitter — fronts and the cheap 2★ farm |
| MORCABRI S2 (SH1) | 497M | 465M | Line hitter — fronts and the cheap 2★ farm |
| Xena S2 (SH4) | 497M | 465M | Line hitter — fronts and the cheap 2★ farm |
| HEADLESS R¥NO S2 (SH6) | 497M | 465M | Line hitter — fronts and the cheap 2★ farm |
| @MONEY@ S1 (SH3) | 491M | 459M | Line hitter — fronts and the cheap 2★ farm |
| LaCrazyLicorne S2 (SH1) | 488M | 456M | Line hitter — fronts and the cheap 2★ farm |
| Stesha S1 (SH2) | 486M | 455M | Line hitter — fronts and the cheap 2★ farm |
| 犬醉雨 S1 (SH3) | 468M | 438M | Line hitter — fronts and the cheap 2★ farm |
| Cursed Viking S1 (SH6) | 466M | 436M | Line hitter — fronts and the cheap 2★ farm |
| Ania 2000 S1 (SH2) | 465M | 435M | Line hitter — fronts and the cheap 2★ farm |
| itzdk420 S2 (SH3) | 464M | 434M | Line hitter — fronts and the cheap 2★ farm |
| Ania 2000 S2 (SH2) | 461M | 430M | Line hitter — fronts and the cheap 2★ farm |
| JBV S2 (SH2) | 457M | 427M | Line hitter — fronts and the cheap 2★ farm |
| 犬醉雨 S2 (SH3) | 451M | 422M | Line hitter — fronts and the cheap 2★ farm |
| Cui S1 (SH2) | 449M | 420M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| MaD_WereWolF S1 (SH5) | 449M | 420M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| HouShroom :o S1 (SH4) | 441M | 412M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Thund3r_N4 S1 (SH2) | 438M | 410M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Thund3r_N4 S2 (SH2) | 431M | 403M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| JBV S1 (SH4) | 431M | 402M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Cui S2 (SH5) | 429M | 401M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Stesha S2 (SH3) | 428M | 400M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Spooky Vee S1 (SH4) | 421M | 393M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| @MONEY@ S2 (SH3) | 415M | 388M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| MaD_WereWolF S2 (SH5) | 409M | 382M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Thiago Casarini S1 (SH2) | 408M | 382M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Rochus0815 S2 (SH1) | 408M | 382M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Thiago Casarini S2 (SH3) | 398M | 372M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| LordOfSurvival S1 (SH5) | 398M | 372M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Chu S2 (SH6) | 392M | 366M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| I'm EM S1 (SH2) | 389M | 364M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| LordOfSurvival S2 (SH4) | 385M | 360M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| jxjsjxjxj S1 (SH5) | 376M | 351M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Spooky Vee S2 (SH6) | 375M | 350M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Cursed Viking S2 (SH5) | 367M | 343M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Lavine121 S1 (SH1) | 356M | 332M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Sumqayit S1 (SH4) | 351M | 328M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| HouShroom :o S2 (SH4) | 351M | 328M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| I'm EM S2 (SH6) | 350M | 327M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| jxjsjxjxj S2 (SH4) | 335M | 313M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Sumqayit S2 (SH3) | 333M | 311M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Stormwind S1 (SH4) | 325M | 304M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Lavine121 S2 (SH3) | 308M | 287M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Hakuji_Akaza S1 (SH4) | 300M | 280M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| Stormwind S2 (SH4) | 292M | 273M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
| saransh45 S1 (SH4) | 287M | 269M | Cleanup / bait — squads under your threshold; bait duty on whales when called |
