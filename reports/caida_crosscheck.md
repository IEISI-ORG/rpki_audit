# Topology cross-check against CAIDA AS relationships (20261001)

Observed links: 288,954. CAIDA links: 657,444 (8,351 p2c and 397,898 p2p of them never seen by our collectors). Rebuilt graph identical to downstream_graph.json: **True**.

## Our rule vs CAIDA, per observed link

| our rule | links | caida_same | caida_reversed | caida_p2p | caida_p2c | caida_absent |
|---|---|---|---|---|---|---|
| ratio_4x | 111,720 | 98,222 (88%) | 971 (1%) | 1,811 (2%) | 0 (0%) | 10,716 (10%) |
| pruned | 78,754 | 4,443 (6%) | 154 (0%) | 57,390 (73%) | 0 (0%) | 16,767 (21%) |
| tier1 | 40,944 | 30,703 (75%) | 14 (0%) | 8,581 (21%) | 0 (0%) | 1,646 (4%) |
| peer | 29,889 | 0 (0%) | 0 (0%) | 6,341 (21%) | 20,081 (67%) | 3,467 (12%) |
| ratio_8x | 17,243 | 3,165 (18%) | 36 (0%) | 11,184 (65%) | 0 (0%) | 2,858 (17%) |
| single_region | 6,302 | 0 (0%) | 0 (0%) | 4,444 (71%) | 777 (12%) | 1,081 (17%) |
| non_transit | 3,879 | 0 (0%) | 0 (0%) | 1,341 (35%) | 1,317 (34%) | 1,221 (31%) |
| t1_t1 | 223 | 0 (0%) | 0 (0%) | 184 (83%) | 36 (16%) | 3 (1%) |

Our p2c rules (tier1, ratio_4x, ratio_8x, pruned) should land in caida_same; dropped rules (peer, single_region, t1_t1, non_transit) in caida_p2p or caida_absent.

## Cone sizes: CAIDA's 25 largest

| AS | name | cc | audit cone (Go, rrc00) | our graph cone | CAIDA cone |
|---|---|---|---|---|---|
| 3356 | Lumen (Level 3) | US | 74030 | 67581 | 55625 |
| 3257 | GTT Communications Inc. | US | 69123 | 61214 | 43747 |
| 1299 | Arelion (fka. Telia Carrier) | SE | 71458 | 63896 | 42057 |
| 174 | Cogent Communications, LLC | US | 73849 | 61948 | 40963 |
| 2914 | NTT America, Inc. | US | 68933 | 57951 | 23297 |
| 6453 | TATA Communications (America | US | 67808 | 56416 | 23123 |
| 6939 | Hurricane Electric LLC | US | 80275 | 72203 | 22110 |
| 6461 | Zayo Bandwidth | US | 71946 | 58122 | 21393 |
| 6762 | Telecom Italia Sparkle (Seab | IT | 66665 | 57397 | 18942 |
| 3491 | PCCW Global (HK) Ltd. | HK | 67288 | 54548 | 17476 |
| 9002 | RETN Limited | GB | 48162 | 45590 | 12024 |
| 6797 | GlobalConnect AB | SE | 4 | 0 | 10687 |
| 1273 | Vodafone Group PLC | EU | 63250 | 50268 | 8209 |
| 5511 | Orange S.A. | FR | 62306 | 54349 | 7620 |
| 12956 | Telxius (Telefonica Global) | ES | 62395 | 50888 | 7603 |
| 4637 | Telstra International Limite | HK | 67304 | 57550 | 6807 |
| 1031 | PEER 1031 LLC | US | 1202 | 1120 | 4692 |
| 13786 | Seaborn (Seabras USA, LLC) | US | 967 | 869 | 4638 |
| 12389 | Rostelecom PJSC | RU | 15093 | 6948 | 4619 |
| 37468 | Angola Cables | AO | 793 | 0 | 4396 |
| 3320 | Deutsche Telekom AG | DE | 67344 | 48426 | 4312 |
| 7195 | EdgeUno | CO | 1805 | 0 | 4108 |
| 7473 | Singapore Telecommunications | SG | 290 | 260 | 4024 |
| 9498 | Bharti Airtel Ltd. | IN | 7421 | 6643 | 3968 |
| 22356 | Durand do Brasil Ltda | BR | 88 | 0 | 3925 |

## Cone sizes: NZ (CAIDA cone > 0)

| AS | name | cc | audit cone (Go, rrc00) | our graph cone | CAIDA cone |
|---|---|---|---|---|---|
| 135069 | Feenix Communications Limite | NZ | 55 | 55 | 161 |
| 9790 | Two Degrees Networks Limited | NZ | 111 | 110 | 147 |
| 4648 | Spark New Zealand | NZ | 48 | 48 | 118 |
| 45177 | Devoli | NZ | 55 | 50 | 88 |
| 55850 | Mercury NZ Limited | NZ | 51 | 52 | 82 |
| 9500 | One New Zealand Group Limite | NZ | 4 | 4 | 41 |
| 4768 | One New Zealand Group Limite | NZ | 31 | 31 | 39 |
| 38022 | REANNZ National Research and | NZ | 32 | 32 | 35 |
| 56030 | Voyager Internet Ltd. | NZ | 10 | 10 | 33 |
| 64073 | Vetta Group | NZ | 1675 | 928 | 32 |
| 23838 | Solarix Networks Limited | NZ | 22 | 22 | 27 |
| 24324 | Kordia Limited | NZ | 14 | 14 | 18 |
| 18400 | Xtreme Networks Limited | NZ | 16 | 16 | 17 |
| 4049 | CELLO GROUP LIMITED | NZ | 12 | 12 | 13 |
| 23655 | 2degrees Networks Limited | NZ | 11 | 10 | 13 |
| 4771 | Spark New Zealand Trading Lt | NZ | 6 | 6 | 8 |
| 45267 | Lightwire LTD | NZ | 4 | 4 | 8 |
| 17705 | InSPire Net Ltd | NZ | 6 | 6 | 7 |
| 151336 | Verge | NZ | 6 | 6 | 7 |
| 55785 | ISP Limited | NZ | 3 | 3 | 7 |
| 138398 | Prodigi Technology Services  | NZ | 4 | 4 | 6 |
| 24183 | DTS LTD | NZ | 4 | 4 | 6 |
| 45637 | UniFone New Zealand Ltd | NZ | 4 | 4 | 5 |
| 17492 | Vector Communications LTD. | NZ | 3 | 3 | 4 |
| 132040 | Vital Data Ltd | NZ | 1 | 1 | 4 |

## NZ customer links CAIDA has and we don't

| provider | customer | our rule for the link |
|---|---|---|
| 135069 | 4049 | peer |
| 135069 | 18015 | not observed |
| 135069 | 19551 | ratio_4x |
| 135069 | 23838 | peer |
| 135069 | 38022 | peer |
| 135069 | 63956 | not observed |
| 9790 | 3573 | peer |
| 9790 | 13150 | peer |
| 9790 | 14593 | peer |
| 9790 | 17978 | peer |
| 9790 | 20144 | not observed |
| 9790 | 20940 | peer |
| 9790 | 40934 | peer |
| 9790 | 54994 | peer |
| 9790 | 55256 | peer |
| 4648 | 13150 | peer |
| 4648 | 19551 | ratio_4x |
| 4648 | 20940 | peer |
| 4648 | 24324 | peer |
| 4648 | 36692 | peer |
| 4648 | 54113 | peer |
| 4648 | 55256 | peer |
| 4648 | 56030 | peer |
| 4648 | 198949 | peer |
| 45177 | 14789 | peer |
| 45177 | 18400 | peer |
| 45177 | 45267 | peer |
| 45177 | 61138 | not observed |
| 45177 | 64073 | ratio_4x |
| 45177 | 133878 | not observed |
| 45177 | 139341 | peer |
| 55850 | 4049 | peer |
| 55850 | 14593 | peer |
| 9500 | 4768 | peer |
| 4768 | 3573 | peer |
| 4768 | 17435 | not observed |
| 4768 | 18119 | not observed |
| 4768 | 26395 | not observed |
| 4768 | 38333 | peer |
| 4768 | 38748 | not observed |
| 4768 | 55872 | not observed |
| 4768 | 139876 | not observed |
| 38022 | 139272 | not observed |
| 56030 | 9245 | peer |
| 56030 | 18400 | peer |
| 56030 | 24459 | peer |
| 64073 | 112 | non_transit |
| 23838 | 23869 | not observed |
| 23838 | 38064 | single_region |
| 23838 | 136964 | peer |
| 24324 | 40934 | peer |
| 24324 | 54253 | peer |
| 24324 | 58580 | peer |
| 24324 | 136499 | peer |
