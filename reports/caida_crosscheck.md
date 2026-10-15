# Topology cross-check against CAIDA AS relationships (20261001)

Observed links: 288,954. CAIDA links: 657,444 (8,351 p2c and 397,898 p2p of them never seen by our collectors). Rebuilt graph identical to downstream_graph.json: **True**.

## Our rule vs CAIDA, per observed link

| our rule | links | caida_same | caida_reversed | caida_p2p | caida_p2c | caida_absent |
|---|---|---|---|---|---|---|
| path | 159,350 | 147,130 (92%) | 108 (0%) | 483 (0%) | 0 (0%) | 11,629 (7%) |
| single_region | 93,110 | 0 (0%) | 0 (0%) | 70,817 (76%) | 2,382 (3%) | 19,911 (21%) |
| unconfirmed | 10,554 | 0 (0%) | 0 (0%) | 4,022 (38%) | 4,945 (47%) | 1,587 (15%) |
| peer | 9,924 | 0 (0%) | 0 (0%) | 6,264 (63%) | 1,883 (19%) | 1,777 (18%) |
| evidence_required | 8,993 | 233 (3%) | 0 (0%) | 7,529 (84%) | 0 (0%) | 1,231 (14%) |
| non_transit | 2,592 | 0 (0%) | 0 (0%) | 1,205 (46%) | 206 (8%) | 1,181 (46%) |
| ratio_4x | 1,721 | 1,210 (70%) | 3 (0%) | 241 (14%) | 0 (0%) | 267 (16%) |
| pruned | 1,358 | 9 (1%) | 600 (44%) | 604 (44%) | 0 (0%) | 145 (11%) |
| tier1 | 1,245 | 1,210 (97%) | 0 (0%) | 4 (0%) | 0 (0%) | 31 (2%) |
| t1_t1 | 107 | 0 (0%) | 0 (0%) | 107 (100%) | 0 (0%) | 0 (0%) |

Kept p2c rules (path; ratio_4x and restored as fallback, or tier1 without path triples) should land in caida_same; dropped rules (peer, single_region, t1_t1, non_transit) in caida_p2p or caida_absent. unconfirmed, pruned and evidence_required are p2c candidates we removed: caida_same there is a lost link.

## Cone sizes: CAIDA's 25 largest

| AS | name | cc | audit cone (Go, rrc00) | our graph cone | CAIDA closure | CAIDA cone (ppdc) |
|---|---|---|---|---|---|---|
| 3356 | Lumen (Level 3) | US | 75788 | 68397 | 74933 | 55625 |
| 3257 | GTT Communications Inc. | US | 71533 | 62416 | 66844 | 43747 |
| 1299 | Arelion (fka. Telia Carrier) | SE | 72871 | 76369 | 72012 | 42057 |
| 174 | Cogent Communications, LLC | US | 74731 | 69187 | 70265 | 40963 |
| 2914 | NTT America, Inc. | US | 71495 | 56820 | 63009 | 23297 |
| 6453 | TATA Communications (America | US | 71204 | 60157 | 62852 | 23123 |
| 6939 | Hurricane Electric LLC | US | 70472 | 52927 | 63019 | 22110 |
| 6461 | Zayo Bandwidth | US | 73566 | 52565 | 63476 | 21393 |
| 6762 | Telecom Italia Sparkle (Seab | IT | 70753 | 56308 | 60626 | 18942 |
| 3491 | PCCW Global (HK) Ltd. | HK | 70800 | 51039 | 59801 | 17476 |
| 9002 | RETN Limited | GB | 49086 | 46943 | 59742 | 12024 |
| 6797 | GlobalConnect AB | SE | 4 | 67 | 60353 | 10687 |
| 1273 | Vodafone Group PLC | EU | 498 | 41751 | 58469 | 8209 |
| 5511 | Orange S.A. | FR | 70695 | 48583 | 59657 | 7620 |
| 12956 | Telxius (Telefonica Global) | ES | 70694 | 46409 | 58817 | 7603 |
| 4637 | Telstra International Limite | HK | 5551 | 45231 | 54862 | 6807 |
| 1031 | PEER 1031 LLC | US | 1202 | 6452 | 47727 | 4692 |
| 13786 | Seaborn (Seabras USA, LLC) | US | 967 | 13455 | 47689 | 4638 |
| 12389 | Rostelecom PJSC | RU | 15908 | 32646 | 29670 | 4619 |
| 37468 | Angola Cables | AO | 793 | 29971 | 45619 | 4396 |
| 3320 | Deutsche Telekom AG | DE | 70598 | 46040 | 59652 | 4312 |
| 7195 | EdgeUno | CO | 1805 | 28274 | 47611 | 4108 |
| 7473 | Singapore Telecommunications | SG | 299 | 40323 | 58315 | 4024 |
| 9498 | Bharti Airtel Ltd. | IN | 7429 | 32571 | 37689 | 3968 |
| 22356 | Durand do Brasil Ltda | BR | 88 | 28778 | 47724 | 3925 |

## Cone sizes: NZ (CAIDA cone > 0)

| AS | name | cc | audit cone (Go, rrc00) | our graph cone | CAIDA closure | CAIDA cone (ppdc) |
|---|---|---|---|---|---|---|
| 135069 | Feenix Communications Limite | NZ | 55 | 142 | 8591 | 161 |
| 9790 | Two Degrees Networks Limited | NZ | 111 | 297 | 217 | 147 |
| 4648 | Spark New Zealand | NZ | 48 | 135 | 9254 | 118 |
| 45177 | Devoli | NZ | 55 | 168 | 152 | 88 |
| 55850 | Mercury NZ Limited | NZ | 51 | 143 | 142 | 82 |
| 9500 | One New Zealand Group Limite | NZ | 4 | 41 | 46 | 41 |
| 4768 | One New Zealand Group Limite | NZ | 31 | 35 | 42 | 39 |
| 38022 | REANNZ National Research and | NZ | 32 | 34 | 35 | 35 |
| 56030 | Voyager Internet Ltd. | NZ | 10 | 33 | 33 | 33 |
| 64073 | Vetta Group | NZ | 1675 | 150 | 67 | 32 |
| 23838 | Solarix Networks Limited | NZ | 22 | 25 | 27 | 27 |
| 24324 | Kordia Limited | NZ | 14 | 19 | 19 | 18 |
| 18400 | Xtreme Networks Limited | NZ | 16 | 17 | 17 | 17 |
| 4049 | CELLO GROUP LIMITED | NZ | 12 | 14 | 13 | 13 |
| 23655 | 2degrees Networks Limited | NZ | 11 | 15 | 14 | 13 |
| 4771 | Spark New Zealand Trading Lt | NZ | 6 | 15 | 15 | 8 |
| 45267 | Lightwire LTD | NZ | 4 | 8 | 8 | 8 |
| 151336 | Verge | NZ | 6 | 7 | 7 | 7 |
| 17705 | InSPire Net Ltd | NZ | 6 | 7 | 7 | 7 |
| 55785 | ISP Limited | NZ | 3 | 5 | 7 | 7 |
| 24183 | DTS LTD | NZ | 4 | 6 | 6 | 6 |
| 138398 | Prodigi Technology Services  | NZ | 4 | 6 | 6 | 6 |
| 45637 | UniFone New Zealand Ltd | NZ | 4 | 5 | 5 | 5 |
| 17492 | Vector Communications LTD. | NZ | 3 | 5 | 4 | 4 |
| 132040 | Vital Data Ltd | NZ | 1 | 4 | 5 | 4 |

## NZ customer links CAIDA has and we don't

| provider | customer | our rule for the link |
|---|---|---|
| 135069 | 18015 | not observed |
| 135069 | 19551 | pruned |
| 135069 | 63956 | not observed |
| 9790 | 20144 | not observed |
| 9790 | 20940 | peer |
| 4648 | 19551 | pruned |
| 4648 | 20940 | peer |
| 4648 | 198949 | peer |
| 45177 | 61138 | not observed |
| 45177 | 64073 | unconfirmed |
| 45177 | 133878 | not observed |
| 4768 | 17435 | not observed |
| 4768 | 18119 | not observed |
| 4768 | 26395 | not observed |
| 4768 | 38748 | not observed |
| 4768 | 55872 | not observed |
| 4768 | 139876 | not observed |
| 38022 | 139272 | not observed |
| 64073 | 112 | non_transit |
| 23838 | 23869 | not observed |
| 23838 | 24107 | unconfirmed |
| 23838 | 38064 | single_region |
