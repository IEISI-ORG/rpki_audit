# CLAUDE.md

This file provides guidance for AI assistants working on the **Global ROV Audit & Triangulation Tool**.

## Project Overview
A high-performance toolkit for auditing global RPKI adoption (ROV and ROA) using "Valley-Free" BGP dependency analysis to measure "Herd Immunity" and detect security regressions.

## Core Architecture
- **Go 1.20+**: Performance-intensive MRT parsing and Customer Cone calculation.
- **Python 3.10+**: Multi-source data triangulation, forensic automation, and reporting.
- **Forensics**: Active data-plane verification via **RIPE Atlas** probes in downstream customer cones.

## Building and Running
- **Compile Go**: `make build` (Generates `bgp-extractor`, `cone-calculator`, `fetch-roa`).
- **Data Pipeline**: `bash do_data_gathering` (Full sync: Topology -> ROA -> Timeseries -> Packing).
- **Report Suite**: `bash do_reports` (Generates all HTML/Markdown reports in `reports/`).
- **Policy Check**: `python3 tests/test_policy_integrity.py` (Verify Tier 1 gravity and classification).
- **Forensic Test**: `python3 verify_forensic_smart.py <ASN>` (Customer-cone perspective test).
- **Forensic Batch**: `python3 batch_verify_smart_v4.py` (Re-verify stale/high-priority targets).

## BGP Topology Semantics (READ THIS BEFORE TOUCHING TOPOLOGY CODE)

### AS-Path Direction in RIPE RIS TABLE_DUMP2 Dumps
A path is written `[PEER_0, PEER_1, ..., ORIGIN_N]` where:
- `PEER_0` is the AS **nearest to the route collector** (observer / peer of the collector)
- `ORIGIN_N` is the AS that **originated the prefix** (rightmost = origin)

| Direction  | Data-plane traffic | Route announcements |
|---|---|---|
| LEFT → RIGHT | flows toward the origin/destination | ← flows outward from origin |
| RIGHT | upstream / provider direction | source of the announcement |
| LEFT  | downstream / customer direction | destination of the announcement |

### For any ASN X at position i in path [P0…Pn]:

- **Left neighbor** `path[i-1]` = toward the collector = **data-plane downstream** (X's customer or X's peer at the peak).  
  ⚠️ Do NOT call this "upstream" — that is the opposite of standard BGP convention.
- **Right neighbor** `path[i+1]` = toward the origin = **data-plane upstream** (X's provider or X's peer at the peak).  
  ⚠️ Do NOT call this "downstream".

### Gao-Rexford Valley-Free Constraint
A valid BGP path must have the shape (no valley allowed):

```
(customer→provider)* → (peer↔peer)? → (provider→customer)*
```

Once a path goes **downhill** (provider → customer), it can **never go uphill again**.  
A "valley" = downhill segment followed by an uphill segment = routing policy violation.

Tier 1s appear near the **peak** (center) of valley-free paths.  
Stubs appear at the **edges** (leftmost = near collector, rightmost = origin).

### Topology Inference Rules (must be identical in cone-calculator.go AND build_topology_from_go.py)
Applied in this priority order:

1. **Non-transit ASNs** (RIRs, root servers, IXP route servers listed in `isNonTransit`/`IS_NON_TRANSIT`) → skip (no cone relationship)
2. **Tier 1 ↔ non-Tier-1** → Tier 1 is **always** the provider (bypasses degree-ratio check entirely)
3. **Tier 1 ↔ Tier 1** → peering link, drop (no cone relationship)
4. `degree(A) > 4 × degree(B)` → A is provider of B
5. `degree(B) > 4 × degree(A)` → B is provider of A
6. Otherwise → peering link, drop

**The 4× ratio threshold is STRICT `>`** — exactly 4× counts as peering.

### Degree Semantics for Provider Inference
The "degree" used in the ratio check is the **total unique neighbor count** in the undirected adjacency graph built from `relationships.csv`.  It is NOT the left-count or right-count — those are recorded but not used for provider inference (future improvement: using `right_count ≈ 0` as a Tier-1 signal).

### Tests
- `tests/test_gao_rexford.py` — Unit + integration tests for all of the above rules.  Run on every topology-related change.
- `tests/test_policy_integrity.py` — Tier 1 cone gravity + verdict classification.

## Multi-Collector Topology Pipeline

### Why multiple collectors?

RIPE RIS collectors sit inside IXPs and peer with ASNs over the IXP fabric. IXP route
servers strip their own ASN from AS paths (RFC 7947), so a route exchanged at AMS-IX
looks indistinguishable from a transit route in the dump. The degree-ratio heuristic
then misclassifies IXP peers as provider→customer relationships ("IXP phantom cones").

**The fix:** use collectors at geographically diverse IXPs. A real T1→stub transit link
appears in dumps from Singapore, Uruguay, and Frankfurt simultaneously. An AMS-IX
phantom only appears in European-biased collectors.

### Collectors (`rov_utils.RRC_COLLECTORS`)
| RRC | Location | IXP | Region |
|---|---|---|---|
| rrc00 | Amsterdam | RIPE-NCC Multihop | EU |
| rrc14 | Palo Alto | PAIX | NA |
| rrc19 | Johannesburg | NAP Africa JB | AF |
| rrc23 | Singapore | Equinix SG | APAC |
| rrc24 | Montevideo | LACNIC Multihop | AMER |

### Consensus rules (`rov_utils.RRC_CONFIRM_REGIONS = 2`)
- Link seen in ≥2 distinct regions → confirmed transit → use `PROVIDER_RATIO` (4×)
- Link seen in only 1 region → suspect IXP peering → use `RRC_SINGLE_REGION_RATIO` (8×)
- Tier-1 override is always applied regardless of collector count
- `_prune_ixp_phantoms()` is applied as a backstop after the ratio rules

### Valley-free and why it cannot detect this
A path `[AS48362, AS57344, origin]` is genuinely valley-free (downhill all the way).
The valley-free constraint catches **shape** violations, not **semantic** ones.
It cannot tell whether the descent was via a paying transit relationship or free IXP
peering — both produce identical AS paths after the route server strips its ASN.

## Known Data Quality Issue: IXP Phantom Cone Inflation

The degree-ratio heuristic in `build_topology_from_go.py` (and `cone-calculator.go`) **over-counts cone sizes for IXP participants**. A network that peers with hundreds of networks via an IXP route server acquires an inflated degree count, causing the 4× ratio rule to misclassify IXP peers as provider→customer relationships.

**Symptom**: Small networks (hosting companies, hobbyist ASNs, municipal utilities) appear with cone sizes of 10,000–60,000 in the audit results.

**Detection**: `rov_utils.cone_quality(asn, downstream, providers_of)` returns `excl_pct` — the % of direct customers with ≤ 2 total providers. Legitimate transit has captive customers (high `excl_pct`); IXP phantoms have peers with 10–20 providers each (low `excl_pct`).

**Mitigation**: All report scripts must filter using `excl_pct >= rov_utils.CONE_QUALITY_THRESHOLD` (5%) for non-Tier-1 networks. The `analyze_herd_immunity_v2.py` script does this. **Tier 1s are exempt** — their Tier 2 customers legitimately multi-home.

**Root fix needed** (TODO): Use the `Left_Count`/`Right_Count` columns from `output/asn_stats.csv` (produced by `bgp-extractor`) during topology building to detect IXP participants and demote those links to peering rather than provider→customer.

## APNIC Timeseries Data Quality

### Minimum sample size (`rov_utils.APNIC_MIN_SAMPLES = 30`, `APNIC_REGRESSION_CURRENT_MIN_SAMPLES = 100`)
The APNIC ROV measurement API returns per-day rows with multiple rolling windows:
`'7'`, `'14'`, `'28'`, `'112'` days. Each window has `seen`, `filtered`, and
`filter_rate = seen / (seen + filtered)`.

**A 7-day window can have as few as 2–6 total observations** for sparse networks (e.g.
Telstra International AS4637 had `seen=2, filtered=4` → 6 samples → 33% "rate" that is
pure noise). `_fetch_apnic_ts_rates()` now uses **adaptive window selection**: it picks
the shortest window where `seen + filtered >= APNIC_MIN_SAMPLES`, falling back through
14 → 28 → 112 days. Data points with no window meeting the threshold are stored with
`rate = None` and excluded from all statistics.

Cache format is now `[[date, rate, samples, window_days], ...]` (dated, since
2026-10-11). Two undated legacy formats, `[[rate, samples], ...]` and `[float, ...]`,
are accepted until their 7-day TTL expires, except for countries listed in
`APNIC_EXCLUDED_WINDOWS`, which are re-fetched at once because an undated series
cannot be masked. Statistics live in the pure function `_ts_stats(raw, cc)`
(tests: `tests/test_apnic_timeseries.py`).

`APNIC_REGRESSION_CURRENT_MIN_SAMPLES = 100` is a separate, stricter threshold used
only when determining `current_for_regression` in `sync_apnic_timeseries()`. Large
transit ASNs can have weeks where APNIC ad impressions drop to 30-50/day (barely above
the 30-sample floor), producing 0% rates that are noise not signal. The regression check
requires `n >= 100` for the most recent data point (within 30 days); if no such point
exists, the regression flag is skipped rather than trusting a marginal reading.

### APNIC measures user-visible filtering, not ASN-level ROV policy
`filter_rate` reflects whether end-users in that ASN could reach the RPKI-invalid
beacon — it **cannot distinguish** between:
- **Direct filtering**: the ASN itself drops invalid routes (the ASN has ROV policy)
- **Inherited filtering**: the ASN's upstream drops invalid routes, protecting the ASN's users without the ASN doing anything

A network that is purely passively behind a filtering upstream will show a high
`filter_rate`. If that upstream changes routing, the score collapses to 0% even though
the ASN's own policy never changed. This is the most common cause of `current=0%,
hist_max=100%` patterns in the regression data — inherited filtering was lost, not a
genuine ROV policy rollback.

**Implication**: "ACTIVE LOCAL ROV" verdicts based solely on APNIC data cannot confirm
the ASN itself is filtering. For herd immunity (are users protected?) this is fine; for
per-ASN policy auditing, Atlas forensics provide stronger evidence.

### Regression detection uses a 1-year lookback
`sync_apnic_timeseries()` computes `historical_max = max(rates[-365:])`, **not**
`max(rates)` over all time. 6 years of daily data includes 2019–2020 measurement noise
spikes that never reflected real ROV deployment. Using the all-time max falsely flagged
2,803 networks as REGRESSED (including AT&T, whose stable 55–58% current score had an
all-time spike to 100% from early-era noise).

A genuine regression is: **was consistently enforcing ROV in the past 12 months, and
the current score has dropped by > 30 points**.

### Excluded measurement windows (`APNIC_EXCLUDED_WINDOWS`)
The APNIC Labs test window of **5–18 Aug 2026** lifted readings for non-filtering NZ
and AU networks. Left in, it would flag them REGRESSED (current vs 1-year max) until
Aug 2027. Each entry is `(first_day, last_day, {country codes}, reason)`. A daily point is
dropped from all statistics when its **rolling window** `[date - window_days + 1, date]`
overlaps the range. So the 7-day reading for 22 Aug is dropped too, and for sparse
networks on the 112-day window the effect lasts into December. Only the listed
countries are masked.

## ROVista: a second measurement, weighted the same as APNIC

`rov_utils.sync_rovista()` pulls the public ROVista API (rovista.netsecurelab.org) in one
call (`/rovista/api/overview?count=100000`), cached at `data/rovista/overview.json`,
refreshed daily, with fallback to the cached copy on failure. Rows whose `lastUpdatedDate`
is older than `ROVISTA_TTL_DAYS = 7` are dropped: about 9,600 listed ASes were last
measured in 2024–2025 (AS681's last reading is 2025-03-03).

**What it measures**: an IP-ID side channel on hosts inside the AS tests whether they can
reach RPKI-invalid prefixes. Like APNIC, it **cannot tell local from upstream filtering**
(a single-homed stub behind a filtering provider scores 100%). It reaches networks APNIC
can't, because APNIC needs end users seeing ads: Akamai Prolexic, TransTeleCom, MegaFon and
Comcast backbone ASes have ROVista scores and no APNIC score.

**Weak spots** (checked 2026-10-13): in 2026 each AS is tested against only 1–2 invalid
prefixes (Cloudflare `103.21.244.0/24` and `193.43.75.0/24`; the median in 2024 was 17),
so scores are effectively binary. Per-AS target counts need one API call per AS and are
not fetched.

**Combination rule** (`rov_utils.measurement_evidence(apnic, rovista)`): both scores are
read on the same 0–100 scale, with the same thresholds (`MEASURE_FILTERING_MIN = 95`,
`MEASURE_NOT_FILTERING_MAX = 30`). It returns `FILTERING`, `NOT_FILTERING`, `NONE`
(no data or only mid-range readings), or `DISPUTED` when one is ≥ 95 and the other < 30.
A mid-range reading never contradicts the other source. Everything that used
`apnic >= 95` / `apnic < 30` in `rov_no_scrape_v22.py` now uses this.

**DISPUTED verdict** (`rov_utils.apply_dispute`): two tests of the same thing disagreeing
is no consensus, so the verdict becomes `DISPUTED` (`classify_verdict` → `PARTIAL`) and
the AS doesn't enter `safe_asns` on measurement evidence. Kept as they are: Tier 1 and
hardcoded verdicts, and any AS with a conclusive fresh Atlas result (a third, direct test
breaks the tie). Applied after REGRESSED and FORTUITOUS. First run: 1,630 DISPUTED ASes,
e.g. Spark AS4648 (APNIC 1.75%, ROVista 100%), Bharti Airtel AS9498, Rostelecom AS12389.

## RIPE Atlas Forensic Methodology

### 7-day TTL on all results
`load_atlas_verdicts()` reads `data/atlas/as_NNNN.json` files and checks the embedded
`timestamp` field. Results older than `ATLAS_TTL_DAYS = 7` are **discarded entirely**
(not used in the audit) and their ASNs returned in the `stale` set so
`batch_verify_smart_v4.py` can re-queue them. This prevents stale "VULNERABLE" verdicts
from permanently overriding fresh APNIC/bgp.tools data.

### Full path taxonomy (`_classify_probe` in `verify_forensic_path_v2.py`)
Each probe produces one of **7 verdicts** based on the traceroute paths to
`valid.rpki.isbgpsafeyet.com` (`path_v`) and `invalid.rpki.isbgpsafeyet.com` (`path_i`):

| Verdict | Meaning | Counts as for target |
|---|---|---|
| `INCONCLUSIVE (Probe Down)` | Valid destination unreachable | skip |
| `INCONCLUSIVE (Off-Path)` | Target ASN not in `path_v` — probe routes around target | skip |
| `INCONCLUSIVE (Partial)` | Ping score 10–90%; inconsistent | skip |
| `VULNERABLE` | Target in `path_i` AND invalid reachable — **target confirmed non-ROV** | non-ROV |
| `VULNERABLE (Bypass Route)` | Invalid reachable but path avoided target — target's ROV unknown | non-ROV (network leaks) |
| `SECURE (Target Filtered)` | Target is the drop boundary — **target confirmed doing ROV** | ROV |
| `SECURE (Upstream Filtered)` | Target forwarded invalid prefix; upstream dropped it — **target NOT doing ROV** | non-ROV |
| `SECURE (Pre-Target Filtered)` | Something before target filtered it; target's ROV unknown | skip |

**`SECURE (Upstream Filtered)` is treated as non-ROV** for the target: the target
forwarded the invalid prefix even though an upstream caught it. This is recorded in both
`load_atlas_verdicts` (maps to `vulnerable`) and in `non_rov_hops`.

### `non_rov_hops` — global non-ROV evidence
Every ASN in `path_i` forwarded the invalid prefix and is confirmed non-ROV at that hop.
These are aggregated across all probes in `analyze_results()` and stored as
`non_rov_hops: [int]` in the result file. Over time, running Atlas tests across many
targets builds a map of ASNs confirmed to be forwarding RPKI-invalid prefixes.

⚠️ **Known false entries** (2026-10-13): 54 of the 517 ASNs in `non_rov_hops` are
rated SECURE, including AS174, AS1299 and AS7018, which are well-known ROV deployers.
The cause has not been investigated (candidates: IP-to-AS mapping of hops, or the AS
that dropped the packet being recorded as a forwarder). Don't treat membership as proof
until this is fixed. Only 203 of 801 result files carry the field.

### Off-path probe detection
Before classifying a probe, `_classify_probe` checks whether the target ASN appears in
`path_v`. If not, the probe routed around the target entirely (multi-homed customer using
a different provider for this destination). **This probe tells us nothing about the
target's ROV policy** and is discarded as `INCONCLUSIVE (Off-Path)`.

This was the root cause of false VULNERABLE verdicts for NTT (AS2914), PCCW (AS3491),
and Vodafone (AS1273): all Atlas probes were routing directly to Cloudflare via Bharti
Airtel or other providers, never traversing the target.

### Atlas override guard in `rov_no_scrape_v22.py`
`atlas_vulnerable` is only allowed to downgrade a network's `safe_asns` status if
current evidence is weak. If a network is **in both `rov_set` (bgp.tools ROV tag) AND
has `apnic_score >= 60%` or `rovista_score >= 60%`** (and isn't DISPUTED), the Atlas
result is treated as a potential probe-path
artefact and the network stays in `safe_asns`. This protects well-evidenced secure
networks from stale or mis-targeted Atlas results while still allowing Atlas to override
networks with no independent corroboration.

### Measurement provenance and IPv6
Each result file stores `measurement_ids` (`ping_valid`, `ping_invalid`, `trace_valid`,
`trace_invalid`), `probe_ids` and `af`, so a verdict can be re-checked on atlas.ripe.net.
Files written before 2026-10-11 have none. `batch_verify_smart_v4.py --af 6` runs the
same test over IPv6 and writes to `data/atlas/v6/`. That directory is outside
`load_atlas_verdicts()`'s glob, so IPv6 results do not change audit verdicts.
`--asns` / `--cc` select targets explicitly. The default smart selection ranks by cone
size and never reaches small-cone countries such as NZ.

### IX hops: resolve via PeeringDB, check the route-server looking glass
An IX hop in a traceroute never shows **who** dropped or forwarded an invalid route. Route-server
ROV, the participant's own import filter, and the origin not announcing on that session all
produce the same traceroute. Before attributing anything to a network on an IX path:
- **Resolve IX LAN hops via PeeringDB `netixlan`** (ip → ASN). Atlas gives no ASN, and IX LAN
  prefixes are usually unannounced, so RIPEstat returns nothing (e.g. AKL-IX `43.243.21.0/24`).
  PeeringDB flags such as `is_rs_peer` can be stale, so confirm against the looking glass.
- **Check the IX route-server looking glass**, using Cloudflare's intentionally invalid beacon
  (`103.21.244.0/24`, `2606:4700:7000::/48`) as the control. Where AS13335 has an RS session up
  and its other routes are accepted, the beacon appears as accepted (no RS ROV) or filtered as
  RPKI-invalid (RS ROV). If Cloudflare isn't on the RS, its absence means nothing.
- Report only what is measured. E.g. One NZ AS9500 (2026-10-11): valid via Cloudflare's AKL-IX
  port, invalid via another session → "VULNERABLE"; the reason the IX path isn't used is
  undetermined. Not "filters on IX peering".
- IX.nz route servers (AS63830, Alice-LG at `lg.ix.nz`, BIRD) drop RPKI-invalids (reject reason
  `63830:64513:14`). BIRD applies IRR checks first, so an IRR rejection can mask an RPKI one.

### Country beacon baseline (`nz_beacon_baseline.py`)
Every connected Atlas probe in a country (`--cc`, default NZ; IPv4 and IPv6) pings and
ICMP-traceroutes two valid/invalid pairs: Cloudflare's isbgpsafeyet.com pair and the RIPE NCC
RIS beacons (AS12654: `93.175.146.1` valid, `93.175.147.1` invalid; `2001:7fb:fd02::1` /
`2001:7fb:fd03::1`). Raw results, `probes.csv` and `ases.csv` go to
`data/atlas/baseline/<cc>_<date>/` (outside the audit's glob), the summary to
`reports/<cc>_beacon_baseline.md`. `--reanalyse <dir>` rebuilds outputs without credits.
- Cloudflare announces its invalid prefix directly to its peers, so the cf test mostly
  measures the network's Cloudflare session.
- Only ~52 of 327 RIS peers carry the RIS invalid prefix (mostly via AS8455), so failing to
  reach it usually means no upstream offered it, not local ROV.
- Stop ASNs are where a trace went silent. Per the IX section above, that isn't attribution.

### Probe selection (`batch_verify_smart_v4.py`)
Probes are selected from the target's **customer cone** using `downstream_graph.json`
(the phantom-pruned topology), not the stale packed ASN data. **Single-homed customers
are preferred**: a probe in an ASN with exactly one provider (the target) *must* route
through the target — its traceroute provides clean, unambiguous attribution. Multi-homed
customers are used as fallback but the off-path check will discard any that route around
the target.

### Target selection (`batch_verify_smart_v4.select_targets`)
The 02:00 cron runs 50 targets a night in this order:
1. **DISPUTED**, largest cone first, up to `DISPUTED_SLOTS` (currently all 50, Terry's
   choice 2026-10-14). A conclusive result settles the dispute, so the AS leaves the list.
   An inconclusive one (e.g. all probes off-path) keeps it DISPUTED, and it is retried
   once the result is 7 days old.
2. **Stale** results (older than `ATLAS_TTL_DAYS`).
3. REGRESSED / CORE: UNPROTECTED, then VULNERABLE / UNRELIABLE, then Unverified, by cone.

ASes with no usable probes are written to `data/atlas/no_probes.json` (`v6/` for
`--af 6`) and skipped by smart selection for 7 days; `--asns` / `--cc` ignore the list.
Tests: `tests/test_batch_targets.py`.

## Key Development Conventions
### 1. Performance & Data Storage
- **Packed Data**: 120k+ ASN records are consolidated into `data/as_data.jsonl.gz`.
- **Ingestion**: ALWAYS use `rov_utils.load_all_asn_data()` for high-performance loading (<1s).
- **TTL Policy**: All external data fetches enforce a **7-day TTL**: APNIC scores, APNIC timeseries, Atlas forensic results, bgp.tools tags, ROVista rows (by `lastUpdatedDate`).
- **Upstream outages**: `fetch_csv(..., cache_paths=...)` saves each good bgp.tools download (`asns.csv`, `rpkirov.csv`) to `data/bgptools/` and falls back to it on failure. `rov_no_scrape_v22.py` refuses to write the audit (exit 1) when 0 ROV tags loaded or the row count drops below 90% of the existing file. Added after the 2026-10-11 bgp.tools outage, which produced an 88k-row audit with every name "Unknown", and the cron job committed it.
- **bgp.tools User-Agent**: requests to bgp.tools use `BGPTOOLS_HEADERS` (project name + repo URL), per their API rules. Other sources keep `HEADERS`.

### 2. Safety Verdicts & Topology
- **Centralized Logic**: Use `rov_utils.classify_verdict()` to bucket strings into `SECURE`, `VULNERABLE`, or `PARTIAL`.
- **Primary Labels**: `REGRESSED`, `VOLATILE`, `UNRELIABLE`, `SECURE`, `PASSIVE`, `FORTUITOUS`.
- **STUB: FORTUITOUS ROV**: A stub whose APNIC score is high (>=95%) but has no direct confirmation of local ROV (`rov_set`, `cf_set`, or Atlas "Target Filtered"). The protection is real (users are safe) but comes from the upstream's filtering, not the stub's own routers. Applied in `rov_no_scrape_v22.py` after `assign_verdict`. `classify_verdict()` maps this to `SECURE`. Stubs with direct evidence stay `STUB: ACTIVE LOCAL ROV`.
- **INCONSISTENT**: Network is in bgp.tools `rov_set` (declared ROV intent) but the measurements show `< 30%` actual filtering (`measurement_evidence(...) == "NOT_FILTERING"`: APNIC or ROVista < 30% and the other not ≥ 95%). Either partial deployment (ROV on some links/routers only), stale declaration, or misconfiguration. Overrides all other verdicts for `rov_set` members meeting the threshold. `classify_verdict()` maps this to `VULNERABLE`. 100 networks after ROVista was added (52 before), no Tier 1s. Key examples: AS7303 Telecom Argentina (8%), AS3292 TDC Denmark (0%), AS32 Stanford (1%), AS20764 RASCOM (ROVista 0%, no APNIC).
- **DISPUTED**: APNIC and ROVista disagree (one ≥ 95%, the other < 30%). `classify_verdict()` maps it to `PARTIAL`. See the ROVista section.
- **STUB: VOLATILE also means "safe behind a dirty feed"**: `assign_verdict` returns it for `is_safe` stubs with `dirty_feeds > 0`, not only for volatile timeseries. With ROVista, ~800 stubs land here: they measure as filtering although a provider doesn't filter, which is the case where the measurement most likely reflects local ROV.
- **Infrastructure Blacklist**: Root Servers and RIRs (AS3333, AS4608, etc.) are marked as non-transit in `cone-calculator.go` (`isNonTransit` logic).
- **REGRESSED override**: `rov_no_scrape_v22.py` overwrites the `assign_verdict()` result with `"REGRESSED"` when the 1-year APNIC timeseries shows a drop of > 30 points. This only fires when `regression=True` in `ts_map` **and `is_safe=False`** — a network with strong current ROV evidence (`rov_set`, `cf_set`, or APNIC >= 95%) stays at its earned verdict. Note: `rov_set`/`cf_set` members always remain `is_safe=True` even when volatile (the volatile guard at line 46 has an explicit `asn not in rov_set and asn not in cf_set` exception). APNIC regression for `atlas_secure` networks with `current=0%, hist_max=100%` is most often an inherited-filtering artifact — see the APNIC data quality note above.

### 3. CI & Quality
- **Linter**: Python code is linted with `ruff`.
- **Formatting**: Go code is formatted with `gofmt`.
- **Policy Integrity**: Every commit must pass `tests/test_policy_integrity.py` to ensure Tier 1 cones haven't regressed.

## bgp.tools Classification Tags
- **API docs**: https://bgp.tools/kb/api — all bulk endpoints, User-Agent requirement
- **Tag list**: https://bgp.tools/tags.txt — 15 tags including `cdn`, `gov`, `uni`, `mobile`, `corp`, `ddosm`
- **Pipeline**: `rov_utils.fetch_bgp_tools_tags()` downloads all tags → `pack_asn_data.py` injects `tags: [...]` into each packed record
- **Cache**: `data/tags/<tag>.csv` with 7-day TTL
- **Access**: `d.get('tags', [])` on any record from `load_all_asn_data()`
- **Warning**: CDN-tagged ASNs (e.g. OVH AS16276) also sell transit — do NOT auto-add tag lists to `IS_NON_TRANSIT`

## Key Files
- `rov_utils.py`: Central shared library (constants, fetchers, classification, TTL management).
- `rov_no_scrape_v22.py`: Main global audit engine (v22).
- `cone-calculator.go`: Go implementation of Customer Cone gravity logic.
- `build_topology_from_go.py`: Multi-collector topology builder with IXP phantom pruning.
- `verify_forensic_path_v2.py`: RIPE Atlas forensic engine — full 7-outcome path taxonomy.
- `batch_verify_smart_v4.py`: Prioritised Atlas re-verification scheduler.
- `triangulate_top_giants.py`: Multi-perspective forensic triangulation.
- `sync_transit_timeseries.py`: Proactive regression scanner for all transit providers.
- `TODO.md`: Roadmap and pending regression investigations.

## Standardized Columns (Audit CSV)
- `asn`: Autonomous System Number
- `verdict`: Core safety status (REGRESSED, SECURE, VULNERABLE, VOLATILE, etc.)
- `cone`: Customer cone size (Network Gravity)
- `apnic_score` / `rovista_score`: measured filtering rate, 0–100; `-1` = no data (ROVista: none within 7 days).
- `regression`: Boolean flag for historical RPKI drop (1-year lookback, >30pt drop).
- `atlas_result`: RIPE Atlas forensic consensus verdict (7-outcome taxonomy, 7-day TTL).
- `non_rov_hops`: ASNs on the invalid traceroute path — confirmed forwarding RPKI-invalid prefixes.
