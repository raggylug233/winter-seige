# VKR vs [Asy] — matchup analysis and attack plan

Generated 2026-09-20 from scouted garrisons (`friendly-VKR.csv`, `enemy-ASY.csv`).

## Who is stronger

| | VKR | [Asy] |
|---|---|---|
| Garrison power | 84.62B | 67.77B |
| Squads ≥ 1B / ≥ 2B | 9 / 0 | 5 / 1 |
| Strongest squad | 1.65B | 2.16B |
| Stars on board | 210 | 209 |
| Layout | front-heavy (strength at the fronts): core 14.85B, middle 27.26B, fronts 42.51B | front-heavy (strength at the fronts): core 15.64B, middle 21.62B, fronts 30.51B |
| Squads the other side cannot kill (60% floor) | 0: none | 0: none |

### Per stronghold

| Stronghold | VKR power · ★ · Warden | [Asy] power · ★ · Warden | attacks for us to clear | attacks for them to clear |
|---|---|---|---|---|
| 1 (Empowered) | 14.85B · 63★ · Peppermint S1 1.63B | 15.64B · 63★ · SireJoe S1 2.16B | ~114 | ~86 |
| 2 (Advanced) | 12.42B · 42★ · Rollo S1 1.51B | 10.59B · 42★ · SireJoe S2 1.84B | ~96 | ~81 |
| 3 (Advanced) | 14.83B · 42★ · Mushroom S1 1.65B | 11.03B · 42★ · Entropy S2 1.43B | ~86 | ~86 |
| 4 (Primitive) | 14.88B · 21★ · Schamser S1 1.34B | 10.09B · 21★ · Elara S2 778M | ~81 | ~81 |
| 5 (Primitive) | 14.24B · 21★ · Mushroom S2 1.35B | 10.50B · 21★ · 熊熊遇見Don冬米糕 S1 872M | ~81 | ~81 |
| 6 (Primitive) | 13.39B · 21★ · Schamser S2 1.13B | 9.92B · 20★ · Elara S1 978M | ~77 | ~81 |

## Simulation

Same model as our own plan (`sim.py`): path unlocking, win chance rising with power ratio, in-game morale rule, coordinated and greedy attacker behaviours, 8 runs. Columns are attacks landed per squad (each side has 10; sleep and waste push the real number down).

| Attacks landed per squad | 3 | 4 | 5 | 6 | 8 |
|---|---|---|---|---|---|
| Stars [Asy] loses when VKR attacks (of 209) | 94 / 125 | 131 / 157 | 190 / 193 | 204 / 203 | 209 / 209 |
| Stars VKR loses when [Asy] attacks (of 210) | 39 / 41 | 71 / 72 | 89 / 103 | 133 / 140 | 156 / 156 |

**Verdict: VKR is favoured: at equal activity we keep more Stars than they do.** Ceiling for VKR: 209★ of 209 (the rest sits on unkillable squads).

## Attack plan for VKR

Rules for every attack: hit only the current phase's stronghold (a half-cleared stronghold unlocks nothing); hit only targets you beat outright — your power ≥ 1.07× theirs at their current morale; a lost attack is only useful as a planned bait; use attempts as they restore (1 per squad every 2 h).

### Phase 1 — open the map: clear Stronghold 5

Opens both 2 and 3; not the very cheapest front, but worth it for the double unlock at ~81 attacks for 21★. Warden 熊熊遇見Don冬米糕 S1 (872M, 5 Hearts) needs attackers over 933M — no baiting needed.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| 熊熊遇見Don冬米糕 S1 (W) | 5 | 872M | 2 | ≥ 933M (14 of ours) | 5 |
| └_ノ ȧm KεLσ ツ S2 | 5 | 812M | 1 | ≥ 868M (19 of ours) | 4 |
| Saafiya S1 | 5 | 725M | 1 | ≥ 776M (26 of ours) | 4 |
| 熊熊遇見Don冬米糕 S2 | 5 | 707M | 1 | ≥ 756M (30 of ours) | 4 |
| Fresh302 S2 | 5 | 686M | 1 | ≥ 734M (35 of ours) | 4 |
| Saafiya S2 | 5 | 638M | 1 | ≥ 683M (47 of ours) | 4 |
| Titus Pullo S2 | 5 | 565M | 1 | ≥ 604M (75 of ours) | 4 |
| FARQD S2 | 5 | 559M | 1 | ≥ 598M (76 of ours) | 4 |
| la reine S2 | 5 | 551M | 1 | ≥ 589M (78 of ours) | 4 |
| lewa968 S2 | 5 | 515M | 1 | ≥ 551M (94 of ours) | 4 |
| Dennypaypy S1 | 5 | 483M | 1 | ≥ 517M (106 of ours) | 4 |
| pomp S1 | 5 | 482M | 1 | ≥ 515M (107 of ours) | 4 |
| legkrut S1 | 5 | 446M | 1 | ≥ 477M (117 of ours) | 4 |
| Lufubustpika S2 | 5 | 427M | 1 | ≥ 457M (119 of ours) | 4 |
| Boudicca S1 | 5 | 380M | 1 | ≥ 406M (120 of ours) | 4 |
| Nope S2 | 5 | 364M | 1 | ≥ 390M (120 of ours) | 4 |
| bread crust S1 | 5 | 342M | 1 | ≥ 366M (120 of ours) | 4 |
| Sirius S2 | 5 | 340M | 1 | ≥ 364M (120 of ours) | 4 |
| veritas S1 | 5 | 315M | 1 | ≥ 337M (120 of ours) | 4 |
| bread crust S2 | 5 | 290M | 1 | ≥ 310M (120 of ours) | 4 |

### Phase 2 — farm the cheap 2★ squads in Strongholds 2 and 3

38 squads worth 2★ each that 12+ of our squads beat outright: ~152 attacks for 76★. Best Stars-per-attack on their board. Leave their whales alone for now.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| 'BembangHalo2' S1 | 2 | 716M | 2 | ≥ 766M (28 of ours) | 4 |
| ㅛ ·ĒĹ· ㅛ S1 | 2 | 595M | 2 | ≥ 637M (55 of ours) | 4 |
| 千ǔεGσ ツᵃᵏˢ S2 | 2 | 575M | 2 | ≥ 616M (66 of ours) | 4 |
| MiniWoF S1 | 2 | 520M | 2 | ≥ 557M (92 of ours) | 4 |
| A░L░F░H░D░ S1 | 2 | 517M | 2 | ≥ 553M (93 of ours) | 4 |
| adel S2 | 2 | 503M | 2 | ≥ 539M (97 of ours) | 4 |
| SandersX S1 | 2 | 493M | 2 | ≥ 528M (103 of ours) | 4 |
| ㅛ ·ĒĹ· ㅛ S2 | 2 | 485M | 2 | ≥ 519M (106 of ours) | 4 |
| Baby Weeeeeeeeee S2 | 2 | 461M | 2 | ≥ 494M (112 of ours) | 4 |
| Krakatok S2 | 2 | 440M | 2 | ≥ 471M (118 of ours) | 4 |
| Nope S1 | 2 | 439M | 2 | ≥ 470M (118 of ours) | 4 |
| Bunny ഗ് S2 | 2 | 422M | 2 | ≥ 451M (120 of ours) | 4 |
| Cary S2 | 2 | 403M | 2 | ≥ 432M (120 of ours) | 4 |
| t3o S2 | 2 | 369M | 2 | ≥ 395M (120 of ours) | 4 |
| yosuf to S2 | 2 | 368M | 2 | ≥ 394M (120 of ours) | 4 |
| SandersX S2 | 2 | 368M | 2 | ≥ 394M (120 of ours) | 4 |
| veritas S2 | 2 | 365M | 2 | ≥ 390M (120 of ours) | 4 |
| zooo S2 | 2 | 362M | 2 | ≥ 387M (120 of ours) | 4 |
| ꙄNAKE S2 | 2 | 345M | 2 | ≥ 369M (120 of ours) | 4 |
| Zhuo Fan S2 | 3 | 756M | 2 | ≥ 809M (23 of ours) | 4 |
| WeaponsOfFury S2 | 3 | 674M | 2 | ≥ 722M (39 of ours) | 4 |
| ༄Angel༄ S2 | 3 | 651M | 2 | ≥ 697M (42 of ours) | 4 |
| Weeeeeeeeeė S2 | 3 | 643M | 2 | ≥ 688M (45 of ours) | 4 |
| Petr the Greate S2 | 3 | 620M | 2 | ≥ 664M (50 of ours) | 4 |
| ༄Applɛ༄ S1 | 3 | 529M | 2 | ≥ 566M (90 of ours) | 4 |
| jerry S1 | 3 | 510M | 2 | ≥ 546M (96 of ours) | 4 |
| WizardOrchid S2 | 3 | 507M | 2 | ≥ 543M (96 of ours) | 4 |
| lewa968 S1 | 3 | 491M | 2 | ≥ 525M (104 of ours) | 4 |
| Death Angel S2 | 3 | 486M | 2 | ≥ 520M (106 of ours) | 4 |
| Iron King S2 | 3 | 483M | 2 | ≥ 517M (106 of ours) | 4 |
| A░L░F░H░D░ S2 | 3 | 474M | 2 | ≥ 507M (108 of ours) | 4 |
| Roro Moon ^ᴥ^ S2 | 3 | 450M | 2 | ≥ 482M (117 of ours) | 4 |
| MiniWoF S2 | 3 | 430M | 2 | ≥ 460M (118 of ours) | 4 |
| yosuf to S1 | 3 | 428M | 2 | ≥ 458M (119 of ours) | 4 |
| legkrut S2 | 3 | 404M | 2 | ≥ 433M (120 of ours) | 4 |
| Sirius S1 | 3 | 394M | 2 | ≥ 422M (120 of ours) | 4 |
| Albi S1 | 3 | 365M | 2 | ≥ 391M (120 of ours) | 4 |
| Miss Green S1 | 3 | 307M | 2 | ≥ 329M (120 of ours) | 4 |

### Phase 3 — clear Strongholds 4 and 6

81 + 77 attacks for 41★. Wardens: Elara S2 (778M, needs ≥ 833M), Elara S1 (978M, needs ≥ 1.05B).

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| Elara S2 (W) | 4 | 778M | 2 | ≥ 833M (21 of ours) | 5 |
| Titus Pullo S1 | 4 | 703M | 1 | ≥ 753M (30 of ours) | 4 |
| la reine S1 | 4 | 697M | 1 | ≥ 745M (32 of ours) | 4 |
| Nikoś S1 | 4 | 663M | 1 | ≥ 709M (40 of ours) | 4 |
| 熊熊遇見桑 S1 | 4 | 641M | 1 | ≥ 686M (45 of ours) | 4 |
| SashaGreat S2 | 4 | 619M | 1 | ≥ 663M (50 of ours) | 4 |
| 'BembangHalo2' S2 | 4 | 619M | 1 | ≥ 662M (50 of ours) | 4 |
| Lufubustpika S1 | 4 | 549M | 1 | ≥ 587M (79 of ours) | 4 |
| 熊熊遇見桑 S2 | 4 | 525M | 1 | ≥ 561M (90 of ours) | 4 |
| Krakatok S1 | 4 | 487M | 1 | ≥ 521M (104 of ours) | 4 |
| Bunny ഗ് S1 | 4 | 471M | 1 | ≥ 504M (110 of ours) | 4 |
| ༄Applɛ༄ S2 | 4 | 465M | 1 | ≥ 498M (112 of ours) | 4 |
| Nymphadora S2 | 4 | 432M | 1 | ≥ 462M (118 of ours) | 4 |
| 小新b S1 | 4 | 410M | 1 | ≥ 438M (120 of ours) | 4 |
| pomp S2 | 4 | 393M | 1 | ≥ 420M (120 of ours) | 4 |
| 小新b S2 | 4 | 375M | 1 | ≥ 401M (120 of ours) | 4 |
| Joe Black S1 | 4 | 350M | 1 | ≥ 374M (120 of ours) | 4 |
| bread crumb S1 | 4 | 309M | 1 | ≥ 331M (120 of ours) | 4 |
| Bean S2 | 4 | 304M | 1 | ≥ 326M (120 of ours) | 4 |
| Reina S2 | 4 | 299M | 1 | ≥ 320M (120 of ours) | 4 |
| Elara S1 (W) | 6 | 978M | 2 | ≥ 1.05B (8 of ours) | 5 |
| Fresh302 S1 | 6 | 845M | 1 | ≥ 904M (17 of ours) | 4 |
| SashaGreat S1 | 6 | 733M | 1 | ≥ 784M (26 of ours) | 4 |
| Lennon123 S2 | 6 | 581M | 1 | ≥ 622M (59 of ours) | 4 |
| SrNoa S1 | 6 | 570M | 1 | ≥ 610M (69 of ours) | 4 |
| WizardOrchid S1 | 6 | 567M | 1 | ≥ 607M (70 of ours) | 4 |
| Nymphadora S1 | 6 | 540M | 1 | ≥ 578M (86 of ours) | 4 |
| Nikoś S2 | 6 | 520M | 1 | ≥ 557M (92 of ours) | 4 |
| Cary S1 | 6 | 511M | 1 | ≥ 547M (95 of ours) | 4 |
| jerry S2 | 6 | 465M | 1 | ≥ 498M (112 of ours) | 4 |
| t3o S1 | 6 | 465M | 1 | ≥ 497M (112 of ours) | 4 |
| SrNoa S2 | 6 | 461M | 1 | ≥ 494M (112 of ours) | 4 |
| Bean S1 | 6 | 418M | 1 | ≥ 447M (120 of ours) | 4 |
| Dennypaypy S2 | 6 | 411M | 1 | ≥ 439M (120 of ours) | 4 |
| ꙄNAKE S1 | 6 | 398M | 1 | ≥ 426M (120 of ours) | 4 |
| zooo S1 | 6 | 383M | 1 | ≥ 410M (120 of ours) | 4 |
| Emre S1 | 6 | 379M | 1 | ≥ 405M (120 of ours) | 4 |
| Emre S2 | 6 | 359M | 1 | ≥ 385M (120 of ours) | 4 |
| Joe Black S2 | 6 | 336M | 1 | ≥ 359M (120 of ours) | 4 |

### Phase 5 — only with leftover attempts: the hard 2★ targets

2 squads that need several baits per Heart before a top squad can finish: ~30 attacks for 8★. Poor value.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| SireJoe S2 (W) | 2 | 1.84B | 4 | ≥ 1.97B (0 of ours) | 20 |
| Entropy S2 (W) | 3 | 1.43B | 4 | ≥ 1.53B (2 of ours) | 10 |

### Phase 6 — if Stronghold 3 is fully cleared (~86 attacks): farm Stronghold 1

18 squads worth 3★ that we beat outright or nearly: ~72 attacks for 54★. Their Stronghold 1 can be zeroed.

| Target | SH | Power | ★ | Beat outright by | Est. attacks |
|---|---|---|---|---|---|
| └_ノ ȧm KεLσ ツ S1 | 1 | 1.00B | 3 | ≥ 1.07B (8 of ours) | 4 |
| Zhuo Fan S1 | 1 | 984M | 3 | ≥ 1.05B (8 of ours) | 4 |
| WeaponsOfFury S1 | 1 | 832M | 3 | ≥ 891M (18 of ours) | 4 |
| Weeeeeeeeeė S1 | 1 | 801M | 3 | ≥ 857M (20 of ours) | 4 |
| ༄Angel༄ S1 | 1 | 793M | 3 | ≥ 849M (21 of ours) | 4 |
| Sahᴮᴵᴸᴸʸ S1 | 1 | 716M | 3 | ≥ 766M (28 of ours) | 4 |
| Petr the Greate S1 | 1 | 699M | 3 | ≥ 748M (32 of ours) | 4 |
| FARQD S1 | 1 | 660M | 3 | ≥ 706M (42 of ours) | 4 |
| 千ǔεGσ ツᵃᵏˢ S1 | 1 | 642M | 3 | ≥ 687M (45 of ours) | 4 |
| Lennon123 S1 | 1 | 639M | 3 | ≥ 684M (46 of ours) | 4 |
| Death Angel S1 | 1 | 616M | 3 | ≥ 659M (50 of ours) | 4 |
| Iron King S1 | 1 | 599M | 3 | ≥ 641M (55 of ours) | 4 |
| adel S1 | 1 | 576M | 3 | ≥ 616M (65 of ours) | 4 |
| Sahᴮᴵᴸᴸʸ S2 | 1 | 563M | 3 | ≥ 602M (76 of ours) | 4 |
| Roro Moon ^ᴥ^ S1 | 1 | 536M | 3 | ≥ 573M (88 of ours) | 4 |
| Baby Weeeeeeeeee S1 | 1 | 525M | 3 | ≥ 562M (90 of ours) | 4 |
| Reina S1 | 1 | 315M | 3 | ≥ 337M (120 of ours) | 4 |
| Boudicca S2 | 1 | 309M | 3 | ≥ 331M (120 of ours) | 4 |

## Roles

| VKR squad | Power | Beats outright up to | Role |
|---|---|---|---|
| Mushroom S1 (SH3) | 1.65B | 1.54B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Peppermint S1 (SH1) | 1.63B | 1.52B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Rollo S1 (SH2) | 1.51B | 1.41B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Peppermint S2 (SH3) | 1.43B | 1.33B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Mushroom S2 (SH5) | 1.35B | 1.26B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Schamser S1 (SH4) | 1.34B | 1.26B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Rollo S2 (SH1) | 1.33B | 1.24B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Schamser S2 (SH6) | 1.13B | 1.06B | Finisher — save attempts for baited whales; don't spend them on fronts |
| Schnitzel Ninja S1 (SH4) | 1.01B | 945M | Finisher — save attempts for baited whales; don't spend them on fronts |
| Tayxo S1 (SH1) | 994M | 929M | Heavy hitter — front Wardens and the 600–750M squads |
| Chaky S2 (SH4) | 971M | 907M | Heavy hitter — front Wardens and the 600–750M squads |
| 3C SPCX S1 (SH2) | 957M | 895M | Heavy hitter — front Wardens and the 600–750M squads |
| Micky S1 (SH1) | 954M | 892M | Heavy hitter — front Wardens and the 600–750M squads |
| FMC S1 (SH5) | 936M | 875M | Heavy hitter — front Wardens and the 600–750M squads |
| ExBasti S1 (SH6) | 933M | 872M | Heavy hitter — front Wardens and the 600–750M squads |
| Ritz S1 (SH4) | 912M | 852M | Heavy hitter — front Wardens and the 600–750M squads |
| I'm Awesome! S1 (SH3) | 906M | 847M | Heavy hitter — front Wardens and the 600–750M squads |
| Fight to the End S1 (SH4) | 895M | 836M | Heavy hitter — front Wardens and the 600–750M squads |
| Ragnar 071603 S1 (SH3) | 871M | 814M | Heavy hitter — front Wardens and the 600–750M squads |
| Schnitzel Ninja S2 (SH4) | 858M | 802M | Heavy hitter — front Wardens and the 600–750M squads |
| Sanica S1 (SH3) | 855M | 799M | Heavy hitter — front Wardens and the 600–750M squads |
| • CeLo • S1 (SH3) | 824M | 770M | Heavy hitter — front Wardens and the 600–750M squads |
| Chaky S1 (SH6) | 821M | 768M | Heavy hitter — front Wardens and the 600–750M squads |
| MrWaterLemon S1 (SH5) | 807M | 754M | Heavy hitter — front Wardens and the 600–750M squads |
| ExChaos S1 (SH2) | 805M | 752M | Heavy hitter — front Wardens and the 600–750M squads |
| Gang&ter 007 S1 (SH5) | 786M | 735M | Heavy hitter — front Wardens and the 600–750M squads |
| I'm Awesome! S2 (SH1) | 773M | 723M | Heavy hitter — front Wardens and the 600–750M squads |
| Dublin 1890 S1 (SH4) | 771M | 721M | Heavy hitter — front Wardens and the 600–750M squads |
| 3C SPCX S2 (SH3) | 766M | 716M | Heavy hitter — front Wardens and the 600–750M squads |
| FMC S2 (SH6) | 759M | 709M | Heavy hitter — front Wardens and the 600–750M squads |
| Tayxo S2 (SH5) | 751M | 702M | Heavy hitter — front Wardens and the 600–750M squads |
| Ritz S2 (SH6) | 750M | 701M | Heavy hitter — front Wardens and the 600–750M squads |
| Eddy S1 (SH4) | 741M | 693M | Heavy hitter — front Wardens and the 600–750M squads |
| ColossusX S1 (SH5) | 739M | 691M | Heavy hitter — front Wardens and the 600–750M squads |
| Hnoo S1 (SH1) | 736M | 688M | Heavy hitter — front Wardens and the 600–750M squads |
| champoiii S1 (SH4) | 732M | 684M | Heavy hitter — front Wardens and the 600–750M squads |
| Spike12345 S1 (SH6) | 727M | 680M | Heavy hitter — front Wardens and the 600–750M squads |
| warrior wolf S1 (SH2) | 727M | 680M | Heavy hitter — front Wardens and the 600–750M squads |
| Lucian S1 (SH5) | 723M | 676M | Heavy hitter — front Wardens and the 600–750M squads |
| Ragnar 071603 S2 (SH1) | 718M | 671M | Heavy hitter — front Wardens and the 600–750M squads |
| Micky S2 (SH4) | 708M | 662M | Heavy hitter — front Wardens and the 600–750M squads |
| Fight to the End S2 (SH5) | 707M | 661M | Heavy hitter — front Wardens and the 600–750M squads |
| ExBasti S2 (SH5) | 696M | 650M | Line hitter — fronts and the cheap 2★ farm |
| kaliグラ S1 (SH6) | 695M | 650M | Line hitter — fronts and the cheap 2★ farm |
| Sanica S2 (SH6) | 693M | 648M | Line hitter — fronts and the cheap 2★ farm |
| Fenerbahçe S1 (SH3) | 685M | 641M | Line hitter — fronts and the cheap 2★ farm |
| Shozzi9 S1 (SH5) | 683M | 639M | Line hitter — fronts and the cheap 2★ farm |
| • CeLo • S2 (SH4) | 681M | 636M | Line hitter — fronts and the cheap 2★ farm |
| Momottë S1 (SH1) | 673M | 629M | Line hitter — fronts and the cheap 2★ farm |
| SABINKA S1 (SH5) | 667M | 623M | Line hitter — fronts and the cheap 2★ farm |
| ColossusX S2 (SH3) | 658M | 615M | Line hitter — fronts and the cheap 2★ farm |
| kami S1 (SH5) | 652M | 610M | Line hitter — fronts and the cheap 2★ farm |
| sam S1 (SH1) | 648M | 606M | Line hitter — fronts and the cheap 2★ farm |
| Aashman S1 (SH2) | 647M | 605M | Line hitter — fronts and the cheap 2★ farm |
| LORENZO 91 S1 (SH1) | 641M | 600M | Line hitter — fronts and the cheap 2★ farm |
| Eddy S2 (SH6) | 635M | 594M | Line hitter — fronts and the cheap 2★ farm |
| Fluffy S1 (SH6) | 635M | 593M | Line hitter — fronts and the cheap 2★ farm |
| kaliグラ S2 (SH6) | 632M | 590M | Line hitter — fronts and the cheap 2★ farm |
| huam31 S1 (SH4) | 631M | 589M | Line hitter — fronts and the cheap 2★ farm |
| Tohrment S1 (SH3) | 621M | 581M | Line hitter — fronts and the cheap 2★ farm |
| • Xena • S1 (SH1) | 621M | 580M | Line hitter — fronts and the cheap 2★ farm |
| Dublin 1890 S2 (SH2) | 621M | 580M | Line hitter — fronts and the cheap 2★ farm |
| Fenerbahçe S2 (SH1) | 619M | 579M | Line hitter — fronts and the cheap 2★ farm |
| Gang&ter 007 S2 (SH5) | 619M | 578M | Line hitter — fronts and the cheap 2★ farm |
| Allis Tsoi S1 (SH2) | 618M | 577M | Line hitter — fronts and the cheap 2★ farm |
| Sassafras McGill S1 (SH5) | 616M | 575M | Line hitter — fronts and the cheap 2★ farm |
| ExChaos S2 (SH3) | 615M | 575M | Line hitter — fronts and the cheap 2★ farm |
| BSM S1 (SH1) | 611M | 571M | Line hitter — fronts and the cheap 2★ farm |
| LittleMïz S1 (SH4) | 610M | 570M | Line hitter — fronts and the cheap 2★ farm |
| Eggs S1 (SH5) | 610M | 570M | Line hitter — fronts and the cheap 2★ farm |
| Buu S1 (SH1) | 607M | 567M | Line hitter — fronts and the cheap 2★ farm |
| Floki S1 (SH1) | 606M | 567M | Line hitter — fronts and the cheap 2★ farm |
| Eggplant S1 (SH6) | 606M | 567M | Line hitter — fronts and the cheap 2★ farm |
| Sassafras McGill S2 (SH5) | 606M | 566M | Line hitter — fronts and the cheap 2★ farm |
| Lyne S1 (SH5) | 606M | 566M | Line hitter — fronts and the cheap 2★ farm |
| MrWaterLemon S2 (SH6) | 604M | 565M | Line hitter — fronts and the cheap 2★ farm |
| ree S1 (SH4) | 598M | 559M | Line hitter — fronts and the cheap 2★ farm |
| Ghost_Hawk S1 (SH4) | 592M | 553M | Line hitter — fronts and the cheap 2★ farm |
| Lucian S2 (SH6) | 588M | 549M | Line hitter — fronts and the cheap 2★ farm |
| Willy Whackit S1 (SH1) | 587M | 549M | Line hitter — fronts and the cheap 2★ farm |
| exLUIS S1 (SH4) | 587M | 548M | Line hitter — fronts and the cheap 2★ farm |
| Kaerii S1 (SH4) | 585M | 547M | Line hitter — fronts and the cheap 2★ farm |
| LORENZO 91 S2 (SH2) | 582M | 544M | Line hitter — fronts and the cheap 2★ farm |
| Eggs S2 (SH5) | 582M | 544M | Line hitter — fronts and the cheap 2★ farm |
| Aashman S2 (SH3) | 581M | 543M | Line hitter — fronts and the cheap 2★ farm |
| Hnoo S2 (SH1) | 579M | 541M | Line hitter — fronts and the cheap 2★ farm |
| champoiii S2 (SH6) | 577M | 539M | Line hitter — fronts and the cheap 2★ farm |
| Snowman S1 (SH5) | 576M | 539M | Line hitter — fronts and the cheap 2★ farm |
| Spike12345 S2 (SH3) | 572M | 535M | Line hitter — fronts and the cheap 2★ farm |
| huam31 S2 (SH4) | 568M | 530M | Line hitter — fronts and the cheap 2★ farm |
| fREEEya S1 (SH4) | 561M | 524M | Line hitter — fronts and the cheap 2★ farm |
| sam S2 (SH3) | 558M | 521M | Line hitter — fronts and the cheap 2★ farm |
| BSM S2 (SH2) | 554M | 518M | Line hitter — fronts and the cheap 2★ farm |
| Momottë S2 (SH3) | 551M | 515M | Line hitter — fronts and the cheap 2★ farm |
| Snowman S2 (SH3) | 549M | 513M | Line hitter — fronts and the cheap 2★ farm |
| Ghost_Hawk S2 (SH6) | 547M | 511M | Line hitter — fronts and the cheap 2★ farm |
| Shozzi9 S2 (SH3) | 543M | 507M | Line hitter — fronts and the cheap 2★ farm |
| warrior wolf S2 (SH3) | 538M | 502M | Line hitter — fronts and the cheap 2★ farm |
| Anonymus S1 (SH3) | 537M | 502M | Line hitter — fronts and the cheap 2★ farm |
| Stone S1 (SH5) | 532M | 498M | Line hitter — fronts and the cheap 2★ farm |
| Seany S1 (SH3) | 530M | 495M | Line hitter — fronts and the cheap 2★ farm |
| Allis Tsoi S2 (SH4) | 530M | 495M | Line hitter — fronts and the cheap 2★ farm |
| Tohrment S2 (SH6) | 528M | 493M | Line hitter — fronts and the cheap 2★ farm |
| Kaerii S2 (SH6) | 527M | 493M | Line hitter — fronts and the cheap 2★ farm |
| MDTH JOKER S1 (SH2) | 521M | 487M | Line hitter — fronts and the cheap 2★ farm |
| 'mV S1 (SH1) | 520M | 486M | Line hitter — fronts and the cheap 2★ farm |
| Willy Whackit S2 (SH1) | 517M | 483M | Line hitter — fronts and the cheap 2★ farm |
| SABINKA S2 (SH6) | 513M | 480M | Line hitter — fronts and the cheap 2★ farm |
| Mint S1 (SH2) | 507M | 473M | Line hitter — fronts and the cheap 2★ farm |
| Anonymus S2 (SH2) | 506M | 473M | Line hitter — fronts and the cheap 2★ farm |
| Floki S2 (SH2) | 503M | 470M | Line hitter — fronts and the cheap 2★ farm |
| Buu S2 (SH2) | 501M | 469M | Line hitter — fronts and the cheap 2★ farm |
| Amy S1 (SH2) | 494M | 461M | Line hitter — fronts and the cheap 2★ farm |
| AymerVW S1 (SH2) | 493M | 461M | Line hitter — fronts and the cheap 2★ farm |
| Seany S2 (SH2) | 492M | 460M | Line hitter — fronts and the cheap 2★ farm |
| kami S2 (SH6) | 487M | 456M | Line hitter — fronts and the cheap 2★ farm |
| LittleMïz S2 (SH1) | 486M | 454M | Line hitter — fronts and the cheap 2★ farm |
| Amy S2 (SH2) | 476M | 445M | Line hitter — fronts and the cheap 2★ farm |
| AymerVW S2 (SH2) | 458M | 428M | Line hitter — fronts and the cheap 2★ farm |
| bimal S1 (SH2) | 451M | 422M | Line hitter — fronts and the cheap 2★ farm |
