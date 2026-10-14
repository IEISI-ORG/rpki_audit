# Topology cross-check against CAIDA AS relationships (20261001)

Observed links: 288,954. CAIDA links: 657,444 (8,351 p2c and 397,898 p2p of them never seen by our collectors). Rebuilt graph identical to downstream_graph.json: **True**.

## Our rule vs CAIDA, per observed link

| our rule | links | caida_same | caida_reversed | caida_p2p | caida_p2c | caida_absent |
|---|---|---|---|---|---|---|
| path | 158,311 | 146,108 (92%) | 108 (0%) | 482 (0%) | 0 (0%) | 11,613 (7%) |
| single_region | 93,058 | 0 (0%) | 0 (0%) | 70,782 (76%) | 2,380 (3%) | 19,896 (21%) |
| unconfirmed | 10,542 | 0 (0%) | 0 (0%) | 4,016 (38%) | 4,939 (47%) | 1,587 (15%) |
| peer | 9,845 | 0 (0%) | 0 (0%) | 6,195 (63%) | 1,878 (19%) | 1,772 (18%) |
| evidence_required | 8,992 | 233 (3%) | 0 (0%) | 7,528 (84%) | 0 (0%) | 1,231 (14%) |
| non_transit | 3,879 | 0 (0%) | 0 (0%) | 1,341 (35%) | 1,317 (34%) | 1,221 (31%) |
| ratio_4x | 1,726 | 1,214 (70%) | 3 (0%) | 242 (14%) | 0 (0%) | 267 (15%) |
| pruned | 1,249 | 9 (1%) | 520 (42%) | 579 (46%) | 0 (0%) | 141 (11%) |
| tier1 | 1,245 | 1,210 (97%) | 0 (0%) | 4 (0%) | 0 (0%) | 31 (2%) |
| t1_t1 | 107 | 0 (0%) | 0 (0%) | 107 (100%) | 0 (0%) | 0 (0%) |

Kept p2c rules (path; ratio_4x and restored as fallback, or tier1 without path triples) should land in caida_same; dropped rules (peer, single_region, t1_t1, non_transit) in caida_p2p or caida_absent. unconfirmed, pruned and evidence_required are p2c candidates we removed: caida_same there is a lost link.

## Cone sizes: CAIDA's 25 largest

| AS | name | cc | audit cone (Go, rrc00) | our graph cone | CAIDA closure | CAIDA cone (ppdc) |
|---|---|---|---|---|---|---|
| 3356 | Lumen (Level 3) | US | 75314 | 67861 | 74933 | 55625 |
| 3257 | GTT Communications Inc. | US | 70709 | 61722 | 66844 | 43747 |
| 1299 | Arelion (fka. Telia Carrier) | SE | 71996 | 75864 | 72012 | 42057 |
| 174 | Cogent Communications, LLC | US | 73928 | 68654 | 70265 | 40963 |
| 2914 | NTT America, Inc. | US | 70483 | 56131 | 63009 | 23297 |
| 6453 | TATA Communications (America | US | 70144 | 59460 | 62852 | 23123 |
| 6939 | Hurricane Electric LLC | US | 69355 | 51918 | 63019 | 22110 |
| 6461 | Zayo Bandwidth | US | 72635 | 51835 | 63476 | 21393 |
| 6762 | Telecom Italia Sparkle (Seab | IT | 69744 | 55531 | 60626 | 18942 |
| 3491 | PCCW Global (HK) Ltd. | HK | 69703 | 50299 | 59801 | 17476 |
| 9002 | RETN Limited | GB | 49086 | 46945 | 59742 | 12024 |
| 6797 | GlobalConnect AB | SE | 4 | 67 | 60353 | 10687 |
| 1273 | Vodafone Group PLC | EU | 498 | 41753 | 58469 | 8209 |
| 5511 | Orange S.A. | FR | 69594 | 47709 | 59657 | 7620 |
| 12956 | Telxius (Telefonica Global) | ES | 69630 | 45356 | 58817 | 7603 |
| 4637 | Telstra International Limite | HK | 5551 | 44401 | 54862 | 6807 |
| 1031 | PEER 1031 LLC | US | 1202 | 6453 | 47727 | 4692 |
| 13786 | Seaborn (Seabras USA, LLC) | US | 967 | 13457 | 47689 | 4638 |
| 12389 | Rostelecom PJSC | RU | 15908 | 29555 | 29670 | 4619 |
| 37468 | Angola Cables | AO | 793 | 26924 | 45619 | 4396 |
| 3320 | Deutsche Telekom AG | DE | 69487 | 46042 | 59652 | 4312 |
| 7195 | EdgeUno | CO | 1805 | 28276 | 47611 | 4108 |
| 7473 | Singapore Telecommunications | SG | 299 | 40325 | 58315 | 4024 |
| 9498 | Bharti Airtel Ltd. | IN | 7429 | 31451 | 37689 | 3968 |
| 22356 | Durand do Brasil Ltda | BR | 88 | 28780 | 47724 | 3925 |

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
| 17705 | InSPire Net Ltd | NZ | 6 | 7 | 7 | 7 |
| 151336 | Verge | NZ | 6 | 7 | 7 | 7 |
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
