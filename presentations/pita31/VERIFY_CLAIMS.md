# PITA 31 Presentation — Claims & Conclusions Verification Prompt

Use this prompt with Claude (or another LLM with access to the audit data) to systematically verify every factual assertion in `pita31_presentation.md` before the talk.

---

## Instructions for the verifier

You are fact-checking the PITA 31 presentation `pita31_presentation.md` against the 2026-09-15 rov_audit output (`reports/`, `rov_audit_v22_final.csv`, `roa_signing_trends.csv`). For each claim below, locate the authoritative source in the listed report file, confirm the number or statement matches, and flag any discrepancy. Where the claim is a technical assertion about RPKI/BGP protocol behaviour (not an audit statistic), evaluate it against RFC text or `CLAUDE.md`.

Use this working directory: `/home/terry/rpki_audit/`

**IMPORTANT — before verifying anything else:** re-run `bash do_reports` (or otherwise confirm `reports/` is fresher than 2026-09-15) if this talk is being given later than a few weeks after that date. Every number below was pulled from that specific run; PITA31 is not until April 2027, so this file **must** be re-verified against a fresh run close to the actual event, not just checked once now.

**Verdict for each claim:** ✅ Confirmed / ⚠️ Close but imprecise / ❌ Wrong / ❓ Not found in source

---

## Section I — Global Statistics (slides 10–11)

Source: `reports/statistics.md`, `reports/analyze_herd_immunity.md`

| Claim | Source field |
|---|---|
| 122,816 total networks; SECURE 22,704 (18.5%), PARTIAL 2,668 (2.2%), VULNERABLE 58,653 (47.8%), NOT ROUTED 38,661 (31.5%) | SUMMARY block |
| Global Core (top 100): 51/100 secure (51.0%), 78.6% traffic protected | HERD IMMUNITY STATUS, [GLOBAL CORE] |
| Transit Layer (top 1,000): 226/1,000 secure (22.6%), 76.3% traffic protected | HERD IMMUNITY STATUS, [TRANSIT LAYER] |

---

## Section II — ROA Signing (slide 13)

Source: `reports/analyze_roa_signing.md`, `reports/analyze_roa_signing_trends.md`

| Claim | Source field |
|---|---|
| Fully Signed (>90%) 46,387 (37.8%); Partially Signed 5,998 (4.9%); Totally Unsigned 70,431 (57.3%) | GLOBAL ROA SIGNING REPORT |
| NOT SIGNED (INSECURE) 59,298 (48.3%) is the largest single bucket; SIGNED (NO ROV) 34,096 (27.8%) | ROA SIGNING x ROV COVERAGE CLASSIFICATION |
| Global ROA coverage: 67.9% now vs. 53.2% 12mo ago (+14.7pp) | GLOBAL ROA COVERAGE TREND |
| APNIC region: 76.1% now vs. 49.2% 12mo ago, 50.8% 24mo ago | RIR ROA COVERAGE TREND, apnic row |

---

## Section III — Pacific Islands Local Context (slides 15–18) — the section needing the most scrutiny

Source: `reports/{as,ck,fj,fm,gu,ki,mh,nc,nr,pf,pg,pw,sb,tk,to,tv,vu,ws}_report.md`, `presentations/pita30/pita30_presentation.md`, `reports/analyze_roa_signing_trends.md`

| Claim | Source field |
|---|---|
| 18-economy aggregate: 174 total networks, 45 SECURE (25.9%), 64 VULNERABLE (36.8%), 65 other (37.4%) | Manual sum across the 18 `{cc}_report.md` header blocks. ✅ Confirmed by this session (2026-09-15) via a standalone re-sum script — re-verify again against fresh reports before presenting, this is the one number in the deck computed rather than read directly off one report file |
| New Caledonia 57.9% SECURE (11/19); PNG 38.5% SECURE (15/39, largest economy) | `nc_report.md`, `pg_report.md` header blocks |
| French Polynesia 0% SECURE / 83.3% VULNERABLE; Tokelau 0%/100%; Cook Islands 0%/100% | `pf_report.md`, `tk_report.md`, `ck_report.md` header blocks |
| PITA30 spotlight table (9 rows) — "then" column | `presentations/pita30/pita30_presentation.md`, slide "Pacific Routing Security: The Uncomfortable Truth" + "One Pacific Network Got This Right" |
| PITA30 spotlight table — "now" column (verdict + APNIC%) | Per-ASN rows in `ws_report.md` (AS17993, AS38800), `ck_report.md` (AS10131, AS152093), `fj_report.md` (AS4638, AS24390), `to_report.md` (AS38201), `sb_report.md` (AS45891), `nc_report.md` (AS18200) |
| Solomon Islands: 83.7% ROA coverage (apnic RIR), -1.7pp over 3mo | `analyze_roa_signing_trends.md`, "BIGGEST MOVERS — 3mo WINDOW" decliners, SB row |
| Micronesia (FM): ROA coverage 4.8% (24mo ago) -> 85.0% now, +80.2pp, largest 24mo mover in the dataset | `analyze_roa_signing_trends.md`, "BIGGEST MOVERS — 24mo WINDOW" improvers, FM row |
| Vodafone Fiji (AS38442) `REGRESSED`, transit upstream for Kiribati, Fiji, PNG, and Vanuatu | Appears in "TRANSIT SUPPLY CHAIN" tables of `ki_report.md`, `fj_report.md`, `pg_report.md`, `vu_report.md` — cross-referenced, not from one single file |

---

## Section IV — ASPA (slides 21–22)

Source: `reports/analyze_aspa_real_deployment.md`

| Claim | Source field |
|---|---|
| 3,031 ASNs (2.47%) hold a real published ASPA object | REAL ASPA ADOPTION section |
| Real adopters by RIR: ripencc 1,809, arin 681, apnic 393, lacnic 146, afrinic 2 | REAL ADOPTERS BY RIR |
| Ready-to-sign giants: 84 total, 7 (8.3%) signed, 77 (91.7%) not yet | MODEL vs REALITY section |
| None of the top-10 ready-but-unsigned giants (by cone) are Pacific networks | TOP 10 ready-but-unsigned list — visually confirm none of the 18 PIC economies' ASNs appear |

---

## Protocol / technical assertions (not audit statistics)

| Claim | Slide | Verdict |
|---|---|---|
| Gao-Rexford valley-free constraint statement | 7 | Check against `CLAUDE.md`'s "BGP Topology Semantics" section |
| Multi-collector consensus rule (≥2 regions = 4×, 1 region = 8×) | 7 | Check against `CLAUDE.md`'s "Multi-Collector Topology Pipeline" |
| RIPE Atlas 7-verdict taxonomy + "SECURE (Upstream Filtered) counts as non-ROV for target" | 8 | Check against `CLAUDE.md`'s "RIPE Atlas Forensic Methodology" |
| ASPA route-leak mechanics, RFC 9582 / RFC 9589 | 20 | Check against the actual RFC text, not just `CLAUDE.md`'s summary |
| `classify_verdict()` substring-match table, incl. the `VOLATILE` → SECURE and `Unverified`/`NOT ROUTED` → uncounted findings | 32 | Re-check directly against `rov_utils.py`'s `classify_verdict()` — this was pulled from source on 2026-09-15; if that function has changed since, the whole appendix needs a rebuild, not just a number update |

---

## Sign-off

- [ ] All Section claims confirmed against a **fresh** run close to the actual April 2027 event date — this file was built from the 2026-09-15 run, ~19 months before PITA31
- [ ] 18-economy aggregate (Section III, row 1) re-summed by hand, not just spot-checked
- [ ] PITA30 spotlight table's "then" column checked against the actual pita30 deck text, not memory of it
- [ ] No retired apnic62-era phrasing ("SITV", "Glass Houses", "The Swamp") carried over
- [ ] Tone matches `CLAUDE.md`'s honesty notes (APNIC filter_rate ambiguity, inherited vs. direct ROV, `FORTUITOUS ROV`)
- [ ] `classify_verdict()` re-checked against current `rov_utils.py` source, not just this file's 2026-09-15 snapshot
