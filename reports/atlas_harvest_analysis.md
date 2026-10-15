# Public Atlas traces to Cloudflare's RPKI-invalid beacon

Generated 2026-10-15 by `analyze_harvest.py` from `atlas_harvest.py` output (third-party measurements, no credits). A trace that reaches the invalid host means the ASes on its path forwarded the invalid route then; most receive it straight from Cloudflare, so this tests that session. Traces that stop attribute nothing. Invalid side only: there is no paired valid trace, so there is no off-path check. An AS counts as a forwarder only if it is the probe's own AS, has >= 2 hops, or hands the trace straight to Cloudflare (a single hop between two other ASes is usually a border-router address). Probe home ASNs known for 52,384 probes.

IX LAN hops are attributed to the participant holding the address (PeeringDB netixlan). 35 IXP ASNs never count as forwarders: at least two of three signals agree (PeeringDB info_type 'Route Server', AS0 ASPA, announcing an IX LAN prefix while PeeringDB lists it on that LAN; one alone isn't enough), and the ASN doesn't carry traffic in RIS (an IXP's route servers are transparent; its ASN is mid-path for at most 2 members with non-transparent sessions). AS0 on its own means no providers: Cogent, Arelion, AT&T, GTT, Deutsche Telekom and Liberty Global publish it, which supports their Tier 1 status.

Only traces from the last 7 days count, the same freshness rule as the audit's own Atlas results. The first harvest is mostly older campaigns (IPv6: 7,423 of 7,499 traces in June 2026; IPv4: mostly January 2026), so little of it is current; the daily harvest adds new public measurements.

| | IPv4 | IPv6 |
|---|---|---|
| traces (any age) | 16,353 | 7,499 |
| reached the invalid host (any age) | 8,956 | 3,141 |
| reached it, last 7 days | 23 | 0 |
| ASes seen forwarding (any age) | 2,893 | 1,389 |
| ASes seen forwarding, last 7 days | 7 | 0 |

## IPv4: audit says SECURE, but current traces show the AS forwarding

Candidates for an Atlas re-test. A PASSIVE stub here means its users reached the invalid host.

| AS | name | cc | cone | verdict | decided by | probes (7 d) | last seen |
|---|---|---|---|---|---|---|---|
| 5410 | Bouygues Telecom SA | FR | 0 | STUB: PASSIVE (Clean Pipe) | apnic | 1 | 2026-10-08 |

1 ASes in all.

## IPv4: current evidence where the audit has only a declaration or nothing

Decided by a declaration (bgp.tools tag, isbgpsafeyet) or not at all in the audit.

| AS | name | cc | cone | verdict | decided by | probes (7 d) | last seen |
|---|---|---|---|---|---|---|---|

0 ASes in all.

## NZ networks seen forwarding (IPv4, current)



| AS | name | cc | cone | verdict | decided by | probes (7 d) | last seen |
|---|---|---|---|---|---|---|---|

0 ASes in all.

