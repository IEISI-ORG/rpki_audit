# Globalping probe coverage

Generated 2026-11-28 by `globalping_verify.py --coverage` from `GET /v1/probes` (no test cost). Globalping is in shadow mode: its results are not used in verdicts. A probe's AS is Globalping's GeoIP reading, not BGP. Atlas side: connected IPv4 probes in the probe archive of 20261014.

| | |
|---|---|
| Probes online | 5,656 |
| ASNs | 1,626 |
| Countries | 124 |
| Datacenter probes | 3,875 |
| Eyeball probes | 1,781 |
| ASNs with datacenter probes only | 832 |
| ASNs with a single probe | 938 |
| ASNs that also have an Atlas probe | 987 |
| ASNs with no Atlas probe | 639 |

## Transit ASes (cone > 0) testable from a probe inside or in a direct customer

| Testable by | ASes |
|---|---|
| All transit ASes | 6,977 |
| Atlas | 2,982 |
| Globalping | 1,642 |
| Globalping, eyeball probes only | 1,024 |
| Both | 1,374 |
| Globalping only | 268 (133 with eyeball probes) |

Largest Globalping-only transit ASes:

| AS | name | cc | cone |
|---|---|---|---|
| 7738 | V.tal | BR | 330 |
| 53181 | K2 Telecom e Multimidia LTDA ME | BR | 249 |
| 131111 | PT Mora Telematika Indonesia Tbk | ID | 225 |
| 23106 | American Tower Brasil | BR | 220 |
| 265269 | MEGA TELE INFORMATICA | BR | 188 |
| 150506 | PT Pusat Fiber Indonesia | ID | 186 |
| 1828 | Unitas Global | US | 179 |
| 21574 | Century Telecom Ltda | BR | 141 |
| 262462 | Aranet Play | BR | 124 |
| 263444 | Open X Tecnologia Ltda | BR | 123 |
| 268624 | Gamers Club Ltda | BR | 116 |
| 268696 | Tuddo Telecom Ltda. | BR | 113 |
| 28220 | Alares Internet | BR | 88 |
| 141137 | PT Media Cepat Indonesia | ID | 87 |
| 264997 | Direct Telecom Ltda | BR | 79 |
| 28260 | ALTA REDE CORPORATE NETWORK TELE | BR | 70 |
| 33652 | Comcast Cable Communications, LL | US | 65 |
| 58656 | bdHUB Limited | BD | 60 |
| 14868 | Ligga Telecomunicações S.A. | BR | 56 |
| 61621 | Norte.Net Telecomunicações Ltda | BR | 50 |

## ASes Atlas found without usable probes (`data/atlas/no_probes.json`)

40 ASNs in the list. Globalping has a probe inside 4 (7738 V.tal, 9341 PT Indonesia Comnets Plus, 19009 Everstream Solutions LLC, 24173 Netnam Company) and in a direct customer of 4 more (1828 Unitas Global, 23956 AmberIT Limited, 24088 Hanoi Telecom Joint Stock Compan, 28202 Master Internet).

## Fresh Atlas results (<= 7 days) Globalping can also test

This is the validation sample. SECURE is the scarce class.

| Atlas result | probe inside | probe in a direct customer | no probe |
|---|---|---|---|
| SECURE | 11 | 4 | 3 |
| VULNERABLE | 61 | 49 | 48 |
| INCONCLUSIVE | 54 | 58 | 48 |

## NZ and the Pacific (probes by the probe's country)

| cc | ASNs registered there | Globalping probes | Globalping ASNs | of them without an Atlas probe |
|---|---|---|---|---|
| NZ | 704 | 34 | 11 | 0 |
| SB | 10 | 1 | 1 | 132468 SATSOL LIMITED |
| GU | 10 | 2 | 2 | 395400 UNIVERSITY OF GUAM |
| NC | 19 | 2 | 1 | 0 |
| PF | 5 | 1 | 1 | 0 |

No probes: FJ, PG, VU, WS, TO, CK, KI, TV, NR, NU, FM, MH, PW, MP, TK, WF, TL, AS.
