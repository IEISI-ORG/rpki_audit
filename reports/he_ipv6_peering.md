# Hurricane Electric's IPv6 peering at scale

Generated 2026-10-16 by `he_ipv6_analysis.py` from the RIPE RIS dumps of 11 Oct 2026 (rrc00, rrc14, rrc19, rrc23, rrc24; existing `bgp-extractor` output) and CAIDA AS relationships 20261001. CAIDA infers its labels from IPv4 paths, so "HE peer" below means a network HE peers with in IPv4.

## Summary

- **HE is mid-path in 35.2% of IPv6 paths** seen by RIS (6,073,410 of 17,231,333), against 15.2% of IPv4 paths. No other network passes on more than 11.1% of IPv6 paths.
- **HE passes its peers' IPv6 routes to its other peers.** In IPv6 it passed the routes of 4,670 of the 4,672 CAIDA peers seen behind it to a non-customer (another peer, a provider or a Tier 1); in IPv4, 5 of 7,512. Valley-free routing passes a peer's routes to customers only, so in IPv6 HE acts as transit for its peers.
- **Many networks reach the IPv6 Internet mostly through HE.** For 2,976 ASes, HE passed on at least half of their observed IPv6 paths (1,397 of them HE peers); in IPv4, 1,733 (74 peers). 345 ASes are passed on by HE alone in IPv6; 243 of these have another network passing their routes in IPv4.
- **ROV:** the audit rates HE `ACTIVE LOCAL ROV` (decided by apnic, APNIC 100.0%). Peers that take HE's IPv6 table get HE's filtering on the routes they use from it. The audit's topology does not show this (see Consequences).
- **ASPA:** 171 of the 1,397 HE peers that rely on HE for at least half of their IPv6 paths publish ASPA; 147 list HE as a provider and **24 leave it out**. ASPA-validating networks would drop their paths that run through HE.

## 1. Share of paths each network passes on

Paths in which the AS passed its right neighbour's route on to another AS (it is mid-path), out of all paths with two or more ASes. A path counts once per collector peer and prefix.

| | IPv4 | | IPv6 | |
|---|---|---|---|---|
| rank | AS | share | AS | share |
| 1 | 3356 Lumen (Level 3) (US) | 16.2% | 6939 Hurricane Electric LLC (US) | 35.2% |
| 2 | 6939 Hurricane Electric LLC (US) | 15.2% | 3356 Lumen (Level 3) (US) | 11.1% |
| 3 | 1299 Arelion (fka. Telia Carrier) (US) | 15.0% | 1299 Arelion (fka. Telia Carrier) (US) | 10.2% |
| 4 | 174 Cogent Communications, LLC (US) | 14.2% | 174 Cogent Communications, LLC (US) | 8.3% |
| 5 | 2914 NTT America, Inc. (US) | 7.2% | 58453 China Mobile International (US) | 7.1% |
| 6 | 3257 GTT Communications Inc. (US) | 4.2% | 2914 NTT America, Inc. (US) | 5.2% |
| 7 | 3491 PCCW Global, Inc. (US) | 3.8% | 6762 Telecom Italia Sparkle (Seabone) (IT) | 4.4% |
| 8 | 6453 TATA Communications (America) Inc (US) | 3.7% | 9808 China Mobile Backbone (CN) | 4.2% |

Totals: IPv4 83,569,776 paths, IPv6 17,231,333.

## 2. Peers' routes passed to non-customers

Per AS: CAIDA peers whose routes it passed to a CAIDA peer or provider of its own, or to a Tier 1 (from `triples.csv`, any path position). Valley-free routing never does this; a network that does it for all its peers is giving them transit. Top networks by IPv6 count:

| AS | IPv6 passed up / peers seen | IPv4 passed up / peers seen |
|---|---|---|
| 6939 Hurricane Electric LLC (US) | 4,670 / 4,672 | 5 / 7,512 |
| 212024 Marc Schmitt (DE) | 530 / 530 | 700 / 700 |
| 394256 Tech Futures Interactive Inc. (CA) | 310 / 310 | 459 / 459 |
| 64073 Vetta Online Ltd (AU) | 250 / 250 | 423 / 423 |
| 401753 BIXCE Inc (VG) | 233 / 233 | 284 / 284 |
| 58057 Securebit AG (DE) | 145 / 145 | 176 / 176 |
| 1257 Tele2 Sverige AB (SE) | 79 / 79 | 131 / 131 |
| 5405 Inter.link GmbH (DE) | 39 / 39 | 209 / 216 |

The networks after HE pass on every CAIDA peer's route in IPv4 as well, which points to CAIDA labelling some of their customers as peers rather than to an IPv6-only policy; none comes near HE's scale.

## 3. Networks whose paths go mostly through HE

Share of an AS's paths that HE passed on, out of all paths where its route was passed beyond its neighbour (paths where HE is the collector's own peer are left out: HE peers with RIS directly). By the AS's CAIDA relationship with HE:

| | IPv4 | | | IPv6 | | |
|---|---|---|---|---|---|---|
| ASes | HE customer | HE peer | no CAIDA link | HE customer | HE peer | no CAIDA link |
| >= 50% via HE | 1,656 | 74 | 3 | 1,096 | 1,397 | 483 |
| >= 90% via HE | 466 | 17 | 1 | 510 | 345 | 182 |
| only HE passes it on | 213 | 11 | 1 | 201 | 64 | 80 |

CAIDA lists 2,255 HE customers and 7,808 HE peers. In IPv4, HE carries most paths only for its customers. In IPv6, its peers join them: they get IPv6 transit from HE over their peering sessions.

## 4. Consequences for this audit

- **Topology.** `HE` is in `EVIDENCE_REQUIRED_ASNS`: path inference counts only its IPv4 triples, and a degree-rule customer needs an IPv4 Tier 1 export. Our graph gives HE 1,999 direct customers (CAIDA 2,255). Counting IPv6 triples would add HE's peers as customers and push its cone toward the whole Internet, as it was when HE was a Tier 1 (cone 80,275).
- **ROV.** The audit's dirty-feed logic follows the IPv4 graph. A network that uses HE for IPv6 gets HE's filtered feed on those routes, which the audit doesn't credit; and a network whose other providers don't filter is less exposed in IPv6 than its verdict says. This is inferred from how HE's routes are exported: RIS shows the routes HE passes on, not which routes each peer installs from HE.
- **ASPA.** One ASPA record covers IPv4 and IPv6. The 24 peers below rely on HE for at least half of their IPv6 paths but leave HE out of their record. Validating networks that receive their routes from HE (a peer) check the hop to HE and drop those paths. Listing HE fixes IPv6 but also authorises HE to pass their IPv4 routes upward.

| AS | name | IPv6 share via HE | ASPA providers |
|---|---|---|---|
| 394232 | TelKel inc. (CA) | 99% | 174, 22652, 46345, 53820, 396313, 396879 |
| 43133 | Cosmonova Broadcast LLC (UA) | 91% | 174, 3356, 9002, 34867, 35415, 197563 |
| 199399 | National Infrastructures for Resea (GR) | 91% | 5408 |
| 267013 | INTERNET SOLUTION PROVIDER TELECOM (BR) | 89% | 16735, 61618 |
| 57099 | Boundless Networks Limited (GB) | 88% | 174, 6461 |
| 207994 | Blockchain Creek B.V. (RU) | 88% | 6830, 35133, 41441, 50263, 50629, 50952 … |
| 269288 | DW SOLUTIONS SERVICOS DE TELECOMUN (BR) | 84% | 52873, 61618 |
| 196881 | Liberty-izone Ltd (GB) | 83% | 174, 3257 |
| 209870 | Cylo Ltd (NL) | 81% | 174, 43861 |
| 12735 | TurkNet Iletisim Hizmetleri A.S. (TR) | 79% | 3257, 5405, 6762, 9002, 9121 |
| 20912 | Panservice s.a.s. di Cuseo Fabrizi (IT) | 77% | 174, 3257, 9002 |
| 13238 | YANDEX LLC (RU) | 77% | 1299, 9002, 20764, 57304 |
| 274610 | NEXT BRASIL TELECOM LTDA (BR) | 73% | 28260, 269553 |
| 137406 | Airlive Communications Inc. (PH) | 72% | 17639, 18233, 45499, 135607 |
| 4181 | TDS TELECOM (US) | 71% | 1299, 3257 |
| 42695 | Cleura AB (SE) | 70% | 174, 1299, 3356, 36352 |
| 268047 | Masterinfo Internet (BR) | 69% | 263998, 268829, 272713 |
| 43256 | Global Broadband Solution Inc (GB) | 68% | 6774, 13335, 33763, 37431, 37451, 63293 |
| 50698 | TETA s.r.o. (CZ) | 65% | 5588, 29208 |
| 6206 | Netrouting B.V. (DE) | 64% | 174, 1299, 2914, 3356, 3549, 6453 |
| 203462 | NOVACONN SRL (IT) | 60% | 1299, 6762, 9002 |
| 61696 | DOMUS TELECOM (BR) | 59% | 16735, 52863, 53062, 53065, 266156 |
| 58507 | Wireline (AU) | 56% | 174, 2914, 7474 |
| 198704 | Unknown (PL) | 52% | 6778, 20804 |

## Method and limits

- RIS sees paths from its collector peers only, so shares describe those views, not traffic.
- CAIDA's labels come from IPv4 paths; where a network has a real IPv6 transit contract with HE it still counts as an HE peer here. That is the effect being measured.
- `triples.csv` is distinct per collector (no path counts); `exports.csv` counts RIB entries.
- No new BGP extraction was run (Terry, 2026-10-15). Related: `reports/caida_vs_project.md` (last-three-hop test, ASPA counts for HE's upward exports).
