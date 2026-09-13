# TODO List

- [x] Investigate volatile changes where an ASN regresses in RPKI/ROV status. 
    - [x] Example: AS45355 regression detected and implemented in pipeline.
    - [x] Regression detection now uses full historical max from APNIC.
    - [x] Proactive scanning for regressions across all transit ASNs (`sync_transit_timeseries.py`).
- [x] Incorporate raw timeseries data from APNIC for trend analysis.
    - [x] `sync_apnic_timeseries` now handles full history.
    - [x] `regression` flag added to audit results.
- [x] Data Storage Refactoring:
    - [x] Moved from 122k individual files to a single `data/as_data.jsonl.gz`.
    - [x] Implemented `load_all_asn_data()` in `rov_utils.py` for high-performance ingestion (0.8s vs ~20s).
    - [x] Archived legacy `data/html` (7.3GB) and `data/apnic_roa` (272MB) into compressed cold storage.
- [ ] Evaluate moving to SQLite for random access if needed (currently memory-based load is fast enough).
- [ ] Add a command-line tool to "unpack" or "query" the packed ASN data for quick debugging.
- [x] Reactivate Quadrant Analysis:
    - [x] Refactored `old/analyze_rov_quadrants_v3.py` into `analyze_rov_quadrants_v4.py`.
    - [x] Uses `rov_utils.load_topology()`, `load_all_asn_data()`, and `is_secure()`; also now applies the IXP phantom cone-quality filter (`cone_quality()` / `CONE_QUALITY_THRESHOLD`) that v3 never had — 70 phantom networks excluded on the first live run.
    - [x] Integrated into `do_reports`, writing `reports/analyze_rov_quadrants.html`. Verified end-to-end against live data (3.5s runtime, sensible Q1-Q4 placement).
- [x] Write a new ASPA-realistic analysis script:
    - [x] Wrote `analyze_aspa_realistic_v5.py` fresh (not patched from the stale `old/analyze_aspa_realistic_v4.py`).
    - [x] Uses `rov_utils.load_all_asn_data()`, `TIER_1_ASNS`/`NON_TRANSIT_ASNS` for filtering, and `is_secure()`/`is_partial()`. Adds a ranked top-30 "realistic enforcers" table (providers ranked by ROV-weighted leverage, not raw customer count) — the concrete per-provider ranking that `analyze_aspa_readiness_v2.py` doesn't produce (it only reports the aggregate top-100 gap %).
    - [x] Integrated into `do_reports`, writing `reports/analyze_aspa_realistic.html`. Verified end-to-end against live data (1.6s runtime, 69.3% realistic-vs-theoretical protection ratio).
- [x] Update ROA Signing Data:
    - [x] `do_roa_sync.py` + `pack_asn_data.py` run automatically inside `do_data_gathering`, triggered by the `full` cron mode — **weekly (Sunday 03:00), not daily**. The daily `reports` cron job does not touch ROA data, it only reruns analysis against the last weekly-packed archive. Verified 7 consecutive successful runs in `logs/cron.log` (2026-06-28 through 2026-08-09), each ending `[SUCCESS] Global ROA Sync Complete`.
    - [x] Fixed the bare `except:` on the `Fetching IPv4/IPv6 Geo` calls in `rov_utils.py`'s `load_metadata()` — added `resp.raise_for_status()` and now logs the real exception (`FAIL (ExceptionType: message)`) instead of swallowing it silently. Non-fatal either way (Cymru fallback still covers it), but the next real failure will be diagnosable instead of just "FAIL".
- [x] Repository Maintenance:
    - [x] Trimmed the git repository of large data blobs from historical commits using `git filter-repo`. `.git` went from 555MB → 76MB (86% reduction; 95% vs the 1.4GB it was before this session's earlier plain `gc`). Purged ~9.65GB of raw historical content: `data/html/` (legacy scrape cache, 7.3GB), `data/parsed/` (pre-refactor per-file era, 346MB), `bgp-table.txt` (1.6GB), `table.txt`, `output/`, `results/`, `logs/cron.log`, `reports/old/`, `fetch-roa` binary. Explicitly kept: `data/asn_meta.json`/`data/downstream_graph.json` (actively maintained, committed as recently as the day before this work) and all versioned audit CSVs (`rov_audit_v*`, `rov_no_scrape_v*` — historical ROV/ROA research snapshots). Also untracked (but did not delete on disk) `data/parsed/*.json`, `results/*`, `.locks/*` — all covered by `.gitignore` but never actually untracked after the rules were added. Done via an isolated fresh clone (`git clone --no-local`), verified byte-for-byte against the original before force-pushing (full tree hash comparison, 95 of 96 commits preserved — the 1 dropped was a confirmed byte-identical redundant sibling merge commit, zero data loss). A backup bare clone was kept at `/home/terry/rov_audit_backup_pre_filter_repo.git` until the rewrite was verified good, then deleted.
    - [x] `logs/cron.log` fixed to never be committed at all (not just rotated) — it's purely operational logging, not a research artifact. Rotated locally via copytruncate for disk hygiene; rotated archives and the live file are both gitignored.
    - [x] Implement a 7-day TTL for all APNIC Labs data fetches to avoid overloading their servers (Implemented in `rov_utils.py`).
    - [x] Monthly cron commit of report outputs — `rov_cron.sh commit` mode, scoped to `git add -u -- reports/ '*.csv'` (tracked files only, no push). Scheduled 1st of month 07:00.
    - [x] Archived `rov_no_scrape_v21.py` (dead engine snapshot, unreferenced by `do_reports`) into `old/` via `git mv`, alongside the already-archived v19/v20.
- [ ] Forensic Automation:
    - [x] Implement smart "Customer Cone" probe selection to test transit providers from their customers' perspective (`batch_verify_smart_v4.py`).
    - [x] Implement a 7-day TTL for forensic re-verification to catch regressions without wasting Atlas credits.
    - [x] Create a weekly cron-like trigger to run the smart forensic scan — actually implemented as nightly (02:00) via `rov_cron.sh atlas`, which exceeds the original weekly spec.


- [x] Reproduce the archived RPKI RFC routing-security reference page: https://web.archive.org/web/20220724031723/http://rpki-rfc.routingsecurity.net/
    - [x] Original site is dead; reproduced from `RPKI_RFCS.md` at repo root as a static markdown reference (the source was a D3.js reading-dependency graph, not a data page — reproduced the underlying curation, not the visualization). Sourced from the Wayback snapshot at `2022-07-27T16:37:30Z` (nearest crawl of the data file to the `2022-07-24` page snapshot originally noted here).
    - Faithful reproduction of the 2022 snapshot only (63 RFCs, MUST/SHOULD/MAY tiers, 29 UPDATE/OBSOLETE relationships) — RFCs published since then (e.g. ASPA RFC 9582) are deliberately excluded. Extending the list is a separate future item if wanted.
    - 4 of the 63 entries have known title/author corruption baked into the original source data (not introduced here) — flagged inline in `RPKI_RFCS.md` via a footnote.

- [x] Track global/per-country/per-RIR ROA-signing trends over time (24/12/6/3-month lookback), prompted by an APNIC-62 finding that China's ROA coverage jumped dramatically.
    - [x] New data source: `stats.labs.apnic.net/roa?d=<date>` — APNIC Labs' per-country ROA-publication measurement (distinct from the drop-invalid/filtering page already used elsewhere). Confirmed it supports historical dates via the `d` param, with a verified off-by-one-month bug (send month M-1, 0-indexed, to get calendar month M) — documented and compensated for in `rov_utils._apnic_roa_date_param()`.
    - [x] `rov_utils.fetch_apnic_roa_by_country()` fetches + parses the per-country IPv4 route-object validity table; historical dates cache indefinitely (immutable fact), the current snapshot uses the standard 7-day TTL.
    - [x] New data asset `data/cc_to_rir.json` — country→RIR mapping derived from the NRO combined delegated-stats file (majority RIR by count of `asn` allocation records per country), since APNIC's own table only breaks down by UN-geoscheme region, not RIR.
    - [x] New script `analyze_roa_signing_trends.py`: global/RIR/per-country ROA-coverage trend across 5 snapshots (now, -3, -6, -12, -24 months), RIR rollups weighted by route-object count, current ASN counts per RIR/country as context (no historical ASN-count trend — our own audit data is snapshot-only), and symmetric biggest-improver/biggest-decliner tables per lookback window. Wired into `do_reports` → `reports/analyze_roa_signing_trends.html`.
    - [x] Verified the motivating claim: China (CN) went from 2.8% (24mo ago) to 89.3% (now) IPv4 route objects covered by a valid ROA, with the bulk of the jump in the most recent 6 months (4.3% → 89.3%).

- [x] Add ASPA analysis grounded in real deployment, not just the modeled readiness scripts.
    - [x] `analyze_aspa_readiness_v2.py` and `analyze_aspa_realistic_v5.py` are both purely modeled (topology + current ROV status → hypothetical readiness/leverage) — neither checks whether any ASN has actually published an ASPA (RFC 9582) object.
    - [x] New data source: `console.rpki-client.org/aspa.html` — a real RPKI relying-party validator's live view of every ASPA object it has validated across all repositories. Ground truth, current-snapshot only (no history available from this source, unlike the ROA endpoint above).
    - [x] `rov_utils.fetch_real_aspa_deployment()` fetches + parses it into `{customer_asn: [provider_asn, ...]}`, 7-day TTL.
    - [x] New script `analyze_aspa_real_deployment.py`: (1) global real-adoption rate, (2) cross-check of `analyze_aspa_readiness_v2.py`'s "ready-to-sign giants" against who has actually signed — only 8.2% of 97 model-ready giants have (an actionable outreach list of the other 91.8%), (3) **topology validation** — Jaccard overlap between each real ASPA record's declared Provider Set and our own Gao-Rexford-inferred upstream set (32.4% exact match, 0.602 mean overlap across 2,581 comparable ASNs) — a genuine accuracy check on this project's core topology inference, (4) real adopters by RIR (reuses `data/cc_to_rir.json`) — RIPE NCC dominates (1,795 of 3,031), consistent with RIPE NCC being the first region to support ASPA object creation. Wired into `do_reports` → `reports/analyze_aspa_real_deployment.html`.

- [x] Extend ASPA analysis from adoption stats to objective, measurable protection: average declared providers per record, and which real observed BGP paths ASPA actually protects.
    - [x] Average declared providers per real ASPA record added to `analyze_aspa_real_deployment.py`: 3.31 (max 225).
    - [x] New standalone compiled Go binary `aspa-path-protection.go` (not touching the shared `bgp-extractor.go`, which discards per-prefix AS_PATHs) — re-reads the same `bgpdump -m` output `bgp-extractor` is piped from to get prefix + full AS_PATH per route, dual-stack (IPv4+IPv6). For every observed route, de-duplicates consecutive repeated ASNs (AS-path prepending) before computing hops, then checks each customer→provider hop against `data/aspa_real.json` (ground truth) to compute what fraction of the path is ASPA-protected. Two independent ranked views: top-10 by fraction protected, and a supplementary top-10 of the longest genuine paths (own bounded top-K pool per collector, gathered in the same pass — not a filter over the fraction pool's survivors, which would miss long-but-decent-fraction paths already evicted there).
    - [x] Excludes AS-path padding/poisoning (`maxRealisticHops = 15`): confirmed via raw `bgpdump` output that some very long (28-30 hop) "paths" were BGP-community-signaled (`65535:101`-style) artificial prepending for traffic engineering, not genuine transit relationships — verified by three unrelated entry paths converging on an identical multi-hop tail regardless of origin.
    - [x] Memory design: an early version held every qualifying record (tens of millions across 5 collectors) in memory before ranking and drove a 30GB machine to 28GB used + 24GB swap — had to be killed. Rewrote around a bounded per-collector top-K min-heap (`container/heap`); re-verified at ~91M total routes across all 5 real collector dumps, ~13-19MB peak RSS, ~9-10min wall-clock with all 5 collectors processed concurrently via goroutines.
    - [x] Wired into `Makefile` (4th Go binary) and `do_reports` → `reports/aspa_path_protection.html`; CI's Go Vet/Compile Binaries steps extended to cover it.
