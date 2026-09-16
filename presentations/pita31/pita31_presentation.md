---
marp: true
theme: pita31
paginate: true
footer: "PITA 31 · Fiji (venue/dates tentative) · April 2027 · Terry Sweetser · IEISI"
backgroundColor: "#ffffff"
color: "#1a1a2e"
---

<!-- _class: title-slide -->

# Routing Security & RPKI — The PITA31 Checkpoint
### What Changed Since PITA30, and What Still Hasn't

**Presenter:** Terry Sweetser
**Organization:** IEISI
**Conference:** PITA 31 AGM Business Forum & Tradeshow · Fiji (tentative) · April 2027

---

# Agenda

1. **Why Measurement Matters** — BGP security is not binary
2. **Methodology** — Zero-scrape triangulation at scale
3. **Global Results** — 122,816 ASNs audited
4. **Herd Immunity** — Where does protection actually come from?
5. **ROA Signing** — Secure providers, unsigned routes, and outreach targets
6. **Pacific Islands: Progress Since PITA30** — 18 economies, named accountability check
7. **ASPA Readiness** — The next layer and the real adoption gap
8. **Recommendations** — Concrete actions for Pacific operators, APNIC, and the region

---

<!-- _class: section-divider -->

# Part I: The Problem

Why "Is BGP secure?" is the wrong question

---

# The Measurement Problem

BGP security deployment has **three distinct layers** — each independently measurable, each independently breakable.

| Layer | Question | Standard |
|---|---|---|
| **ROA** | Have you *claimed* your prefixes? | RPKI ROA signing |
| **ROV** | Are you *filtering* invalid routes? | BGP origin validation |
| **ASPA** | Are you *validating* the path? | AS_PATH verification |

> **A network that enforces ROV but has not signed its own ROAs is filtering for others while its own prefixes remain unprotected.**
> A network that signs ROAs but skips ROV claims security it cannot deliver.

The real question for this room: **"What percentage of Pacific Islands traffic is actually protected right now, and by whom?"** — Part V answers this with named networks, not averages.

---

<!-- _class: section-divider -->

# Part II: Methodology

Zero-scrape triangulation at scale

---

# Zero-Scrape Architecture

**No web scraping. Only structured API data and BGP table dumps.**

```
RIPE RIS MRT Dumps (5 global collectors)
    ↓ Go MRT Parser (bgp-extractor)
    ↓ Valley-Free Topology Builder
    ↓ Customer Cone Calculator (cone-calculator.go)
                    ↓
         ┌──────────┴──────────┐
  APNIC RPKI API          bgp.tools API
  (239 countries)         (ROV tags)
  APNIC Timeseries        Cloudflare Safe List
         └──────────┬──────────┘
                    ↓
         RIPE Atlas Forensic Engine
         (7-verdict path taxonomy)
                    ↓
         122,816 ASNs audited
```

All data with 7-day TTL — stale results are discarded, not stacked.

---

# Topology & Multi-Collector Validation

**Gao-Rexford Valley-Free constraint** governs all legitimate BGP paths:

```
(customer→provider)* → (peer↔peer)? → (provider→customer)*
```

Once a path descends to a customer, it cannot go back up to a provider — this is how we tell provider from customer from a raw AS-path, and how we place Tier-1s at the peak.

**Why one collector isn't enough:** IXP route servers strip their own ASN from paths (RFC 7947), so an IXP peer can look like a transit customer. The fix is regional consensus — a link only counts as confirmed transit if it's seen from **≥2 geographically distinct** RIPE RIS collectors (Amsterdam, Palo Alto, Johannesburg, Singapore, Montevideo); a link seen from only one region gets a stricter 8× degree-ratio threshold instead of the standard 4×.

---

# RIPE Atlas Forensic Verification

For large transit ASNs, APNIC telemetry is insufficient — it measures *user-visible filtering*, not *local ROV policy*.

**7-probe-level verdicts from dual traceroute to RPKI-valid/invalid beacons:**

| Verdict | Meaning |
|---|---|
| `SECURE (Target Filtered)` | Target is the drop boundary — **confirmed ROV** |
| `SECURE (Upstream Filtered)` | Target forwarded invalid; upstream caught it — **NOT doing ROV** |
| `VULNERABLE` | Target in path_i AND invalid reachable — **confirmed non-ROV** |
| `VULNERABLE (Bypass Route)` | Invalid reachable, path avoided target — network leaks |
| `INCONCLUSIVE (Off-Path)` | Probe routed around target — discarded |

> **Key insight:** `SECURE (Upstream Filtered)` counts as **non-ROV for the target** — the target forwarded the invalid prefix. The upstream saved it, the target did not filter.

---

<!-- _class: section-divider -->

# Part III: Global Results

---

# Global Verdict Breakdown

**122,816 networks audited globally, 2026-09-15.**

| Bucket | Networks | Share |
|---|---|---|
| SECURE | 22,704 | 18.5% |
| PARTIAL | 2,668 | 2.2% |
| VULNERABLE | 58,653 | 47.8% |
| NOT ROUTED (no active routes to classify) | 38,661 | 31.5% |

Of networks that are actually routing traffic (84,155), **just over 1 in 4 is SECURE** and roughly **7 in 10 are VULNERABLE or PARTIAL**. This is the global baseline every regional number in this deck is measured against.

---

# The Herd Immunity Scoreboard

Traffic protection concentrates in a small number of large networks — "herd immunity," not universal adoption.

| Layer | Networks Secure | Traffic Protected |
|---|---|---|
| **Global Core** (top 100 transit) | 51 / 100 (51.0%) | 78.6% |
| **Transit Layer** (top 1,000 transit) | 226 / 1,000 (22.6%) | 76.3% |

Fewer than a quarter of the top 1,000 transit networks are SECURE, yet they carry over three-quarters of global traffic protection between them — most of the internet is protected by a small set of large, well-run networks, not by broad adoption. Several of the Pacific's own upstreams sit in this core (Cogent, Hurricane Electric, NTT, Telstra International all appear as `CORE: ACTIVE PROTECTOR` transit for Pacific economies — see Part V).

---

<!-- _class: section-divider -->

# Part IV: ROA Signing

---

# Global ROA Signing Status

**Signing (ROA) and filtering (ROV) move independently — most of the internet has done at most one of the two.**

**This project's own network-level classification** (from the audited ASN, not APNIC's route-object measure below):

| Signing status | Networks | Share |
|---|---|---|
| Fully Signed (>90%) | 46,387 | 37.8% |
| Partially Signed | 5,998 | 4.9% |
| Totally Unsigned | 70,431 | 57.3% |

**The two biggest buckets by ROA×ROV cross-classification:** `NOT SIGNED (INSECURE)` — 59,298 (48.3%), the largest single bucket globally — and `SIGNED (NO ROV)` — 34,096 (27.8%): signed, but nobody's filtering on their behalf either.

**A separate, narrower measure — APNIC Labs' own trend data on *announced route objects with a valid ROA*** (not the same metric as the network-level table above; reported for IPv4 and IPv6 separately, since they move differently):

| | Now | 12mo ago | Change |
|---|---|---|---|
| IPv4 route objects valid | 68.0% | 53.2% | +14.8pp |
| IPv6 route objects valid | 75.3% | 57.4% | +17.9pp |
| APNIC region, IPv4 | 76.5% | 49.1% | +27.4pp |
| APNIC region, IPv6 | 83.5% | 48.1% | +35.4pp |

IPv6 is consistently ahead of IPv4 here — worth knowing before anyone in this room assumes "ROA coverage" means IPv4 only. The APNIC region (every economy in this deck) is growing faster than the global average on both.

---

<!-- _class: section-divider -->

# Part V: Pacific Islands — Progress Since PITA30

18 economies. Named networks. What actually changed.

---

# Regional Snapshot — September 2026

**18 Pacific economies** (American Samoa, Cook Islands, Fiji, Micronesia, Guam, Kiribati, Marshall Islands, New Caledonia, Nauru, French Polynesia, Papua New Guinea, Palau, Solomon Islands, Tokelau, Tonga, Tuvalu, Vanuatu, Samoa) — **174 networks total.**

| | Count | Share |
|---|---|---|
| SECURE | 45 | 25.9% |
| VULNERABLE | 64 | 36.8% |
| Other (not routed / mixed / unclassified) | 65 | 37.4% |

**Leaders:** New Caledonia (57.9% SECURE, 19 networks) and Papua New Guinea (38.5% SECURE, the region's largest economy at 39 networks) are ahead of the regional average.
**Furthest behind:** French Polynesia (0% SECURE, 83.3% VULNERABLE), Tokelau (0% SECURE, 100% VULNERABLE), Cook Islands (0% SECURE, 100% VULNERABLE).
*Caveat: American Samoa, Cook Islands, Tokelau, Tuvalu, and Palau all have fewer than 5 networks — percentages there swing on one or two ASNs.*

---

# PITA30 Spotlight: Where Are They Now

PITA30 (April 2026) named these networks by name. This is the honest follow-up — not a repeat of the pitch.

| Network | PITA30 (Apr 2026) | Now (Sep 2026) |
|---|---|---|
| Univ. of South Pacific (Fiji) | "operating securely" | Confirmed: `STUB: ACTIVE LOCAL ROV` |
| OPT New Caledonia | "operating securely" | 100% APNIC (unchanged); cone now flagged `PARTIAL: VULNERABLE (Mixed)` |
| Vodafone Samoa | 97% APNIC, SECURE | 99% APNIC; downgraded to `PARTIAL: VULNERABLE (Mixed)` |
| Tonga Communications | 93% APNIC, PARTIAL | 100% APNIC; flagged `STUB: VOLATILE` |
| Digicel Samoa | 1% APNIC, VULNERABLE | 100% APNIC; flagged `STUB: UNRELIABLE` |
| Telecom Fiji | 75% APNIC, PARTIAL | 65% APNIC; reclassified `Unverified` |
| Telecom Cook Islands | 0% APNIC, PARTIAL | 0% APNIC; `STUB: VULNERABLE` — unchanged |
| VakaNet (Cook Islands) | VULNERABLE | `STUB: VULNERABLE` — unchanged |
| Solomon Telekom | 1% APNIC, VULNERABLE | 1% APNIC; `STUB: VULNERABLE` — unchanged |

**One clean win, three no-change, two scores that jumped but our own system won't yet certify as durable, one score that fell.** No network here has an unambiguous, fully-verified "solved" story — including the ones the numbers look best for.

---

# Local Proof: Signed Isn't Filtered

Part I's warning, showing up in this region's own data:

**Solomon Islands** — ROA coverage is 83.7% (APNIC RIR data), essentially flat over the last quarter. Its ROV picture: 54.5% of networks VULNERABLE. Prefixes are signed; routes still aren't widely filtered.

**Micronesia (FSM)** — ROA coverage went from 4.8% to 85.0% over two years (+80.2pp) — the single largest 24-month improvement of any country/region in the entire global dataset. Its ROV picture, however, is only 16.7% SECURE (small network count — 6 total, so treat this cautiously). Signing moved fast here; filtering hasn't caught up.

Both are the same lesson from Part I, playing out with this room's own networks: **a signed prefix is not a filtered route.**

---

# The Gap: Who Still Needs to Act

**Zero SECURE networks today:** French Polynesia, Tokelau, Cook Islands, Nauru.

**A shared risk worth naming:** Vodafone Fiji (AS38442) is currently `REGRESSED` and is a direct transit upstream for Kiribati, Fiji, Papua New Guinea, and Vanuatu simultaneously. A single regressed upstream sitting under four separate Pacific economies is a regional concentration risk, not just a Fiji problem.

This is where PITA31 should focus its direct outreach — not the networks already in the spotlight table, but the ones with no SECURE presence at all yet.

---

<!-- _class: section-divider -->

# Part VI: ASPA — The Next Layer

---

# Why ROV Alone Is Insufficient: Route Leaks

**ROV validates the origin AS. It cannot validate the AS-PATH.**

```
Legitimate path:   [Cogent] → [IIJ] → [Customer_A]    ← valid
Route leak path:   [Cogent] → [Customer_A] → [IIJ]     ← ROV sees same origin, passes
```

A route leak occurs when a customer AS re-advertises a provider's routes to another provider — creating a path that violates the Gao-Rexford valley-free constraint but is **invisible to ROV**. For Pacific networks with only one or two international transit paths, a leak on that path is not a technicality — it can be a national outage.

**ASPA (Autonomous System Provider Authorization)** solves this: each AS publishes a signed list of its authorized upstream providers in RPKI, and ASPV rejects paths that violate it. **RFC 9582** (ASPA Objects) + **RFC 9589** (ASPV Algorithm) — both now published.

---

# Real ASPA Adoption: The Ground Truth

**3,031 ASNs (2.47% of all audited networks) hold a real, published ASPA object** — not a model, the actual RPKI repository data.

| RIR | Real adopters |
|---|---|
| RIPE NCC | 1,809 |
| ARIN | 681 |
| APNIC | 393 |
| LACNIC | 146 |
| AFRINIC | 2 |

APNIC — the region every economy in this deck belongs to — has 393 real adopters. None of the named Pacific networks in Part V's spotlight table have a published ASPA object yet. That's expected: ASPA needs ROA hygiene and secure upstreams first, and Part V showed the region is still working on those two.

---

# The Giants Aren't Signing Yet

**Of the 84 networks globally that are "ready to sign"** — cone size > 100, 100% ROA hygiene, 100% secure upstreams — **only 7 (8.3%) have actually published an ASPA object. 77 (91.7%) haven't.**

This is the same pattern Part IV showed for ROA/ROV: being *technically ready* and *actually doing it* are two different numbers. None of the top-10 ready-but-unsigned giants are Pacific networks — the region isn't at the ROA-hygiene bar ASPA requires yet, so this is a marker for where Pacific networks will land *after* Part V's gaps close, not a near-term ask.

---

<!-- _class: section-divider -->

# Part VII: Recommendations

---

# Recommendations: For Network Operators

**If your network was named in PITA30's table, you have a checklist:**

1. Register ROAs for every announced prefix — my.apnic.net → RPKI (free, 1–2 days for a typical Pacific ISP)
2. Enable RPKI-based filtering on border routers — supported natively on Cisco IOS-XR, Juniper JunOS, Nokia SR-OS
3. Verify with a public tool — stat.ripe.net or bgp.tools — not "my team said it's done"
4. Register with **MANRS** and publish your status

**Target for PITA32:** not just a higher APNIC score, but a verdict this audit can actually certify — `ACTIVE LOCAL ROV`, not `VOLATILE` or `UNRELIABLE`. A score that jumps in one quarter and holds for the next two is worth more than one that jumps once.

---

# Recommendations: For RIRs and Policy Bodies

**A concrete ask for the APNIC Routing Security SIG and PITA jointly:** agree a fixed cohort of Pacific networks to snapshot at every PITA event, the same ASNs each time, so the next checkpoint is a clean before/after — not a reconstruction from a past deck's marketing table, which is what this deck had to do.

Continue APNIC's free training and direct technical assistance to Pacific operators (training@apnic.net) — cost was never the barrier here; French Polynesia, Tokelau, Cook Islands, and Nauru have zero SECURE networks each, and all are capacity-constrained markets where free technical assistance is the highest-leverage intervention available.

---

# Recommendations: For the Ecosystem

**Shared-upstream risk is a regional issue, not a per-country one.** Vodafone Fiji's `REGRESSED` status (Part V) affects transit into Kiribati, Fiji, PNG, and Vanuatu at once — coordinating on shared upstreams should be a standing PITA agenda item, not something each economy chases independently.

International peering partners increasingly prefer or require RPKI-enabled peers. As Pacific networks negotiate better interconnection — lower latency, lower cost — routing security posture is now commercial leverage, not just technical hygiene.

---

<!-- _class: section-divider -->

# Part VIII: Conclusion

---

# What the Data Says — Honestly

**Four caveats before anyone quotes a number from this deck:**

1. **Methodology has moved since PITA30.** The verdict taxonomy has been refined since April 2026; a verdict *string* from PITA30 isn't always a clean apples-to-apples match to today's. APNIC score is the more directly comparable number, and even that needs care (see below).
2. **Big score jumps deserve scrutiny before celebration.** Digicel Samoa's 1%→100% and Tonga Communications' 93%→100% are exactly the kind of moves our own system flags `UNRELIABLE` / `VOLATILE` rather than certifying outright.
3. **Small economies produce noisy percentages.** Five of the 18 economies here have fewer than 5 networks each.
4. **A high APNIC score can mean the network's upstream is protecting it, not the network itself** (`FORTUITOUS ROV`) — real protection for users, but not evidence of local policy. Several Pacific "SECURE"-looking stubs likely fall in this category.

---

# Summary: Who Should Do What

| Audience | One ask |
|---|---|
| **Named PITA30 operators** | Turn a good score into a verdict this audit certifies, not just a bigger number |
| **The 4 zero-SECURE economies** | Take up APNIC's free training and technical assistance — start with one ROA |
| **APNIC / PITA jointly** | Fix a cohort to track between events, so PITA32 doesn't need to reconstruct a baseline |
| **The region** | Treat shared-upstream regression (Vodafone Fiji) as a coordinated problem |

**One ask, same as PITA30's:** leave today with a named person, a target date — and this time, a commitment this audit can independently verify at PITA32.

---

# Questions & Discussion

---

<!-- _class: section-divider -->

# Appendices

---

# Appendix A: Full Verdict Taxonomy

How `rov_utils.classify_verdict()` buckets every verdict string (substring match, checked in this order):

| Contains | Bucket |
|---|---|
| `REGRESSED`, `UNRELIABLE`, `UNPROT`, `INCONSISTENT` | VULNERABLE |
| `ACTIVE`, `PASSIVE`, `PROTECTOR`, `VOLATILE`, `FORTUITOUS` | SECURE |
| `PARTIAL` | PARTIAL |
| `VULNERABLE` / `VULN` | VULNERABLE |
| none of the above (e.g. `NOT ROUTED`, `Unverified (Transit/Peer?)`) | not counted in SECURE/PARTIAL/VULNERABLE at all |

**Two things worth knowing before you read a verdict as good news:** `VOLATILE` buckets as SECURE today, despite meaning "swung by 30+ points in 90 days" — that's why this deck calls it out by name rather than letting the bucket speak for it (see Tonga Communications, Part V). And `Unverified (Transit/Peer?)` / `NOT ROUTED` networks are excluded from every SECURE/VULNERABLE percentage in this deck — they are not silently counted as either.
