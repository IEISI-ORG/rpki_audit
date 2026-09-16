# APNIC-62 Presentation — Claims & Conclusions Verification Prompt

Use this prompt with Claude (or another LLM with access to the audit data) to systematically verify every factual assertion in `apnic62_presentation.md` before the talk.

---

## Instructions for the verifier

You are fact-checking the APNIC-62 presentation `apnic62_presentation.md` against current `rov_audit_v22` output. For each claim below, locate the authoritative source in the listed report file, confirm the number or statement matches, and flag any discrepancy. Where the claim is a technical assertion about RPKI/BGP protocol behaviour (not an audit statistic), evaluate it against RFC text or established operator practice.

Use this working directory: `/home/terry/rpki_audit/`

**Verdict for each claim:** ✅ Confirmed / ⚠️ Close but imprecise / ❌ Wrong / ❓ Not found in source

---

## ⚠️ READ THIS FIRST — 2026-09-16 rebuild summary

This file was last accurate against a May 2026 data run. This deck was **never actually
presented** (confirmed by the user 2026-09-16), so unlike `pita30/`, it is not a frozen
historical record — but that also means nobody has re-verified it since May. Rebuilding
this file against the current (2026-09-16) data surfaced real, material drift, not just
cosmetic staleness:

- **Slide 13 (Global Verdict Breakdown):** `REGRESSED` has nearly tripled (1,432 → 4,337
  ASNs; 4.5% → 10.9% traffic impact). `PARTIAL: VULNERABLE`'s traffic impact has more
  than halved (18.6% → 8.7%). Total ASN count 122,277 → 122,622.
- **Slide 14 (Herd Immunity):** Global Core secure count dropped 59/100 → 51/100.
- **Slides 24, 26, 27 (NZ, India, Indonesia):** all three claim the region's dominant
  transit operator is `PASSIVE (Clean Pipe)` (protected via upstream) — **all three are
  now `REGRESSED`** in current data, and traffic-protected percentages have collapsed:
  NZ 82.2%→5.3%, India 69.7%→4.2%, Indonesia 70.2%→31.1%.
- **Slide 25 (Japan):** claims 53.9% traffic protected, "up from 39.5% previously" —
  current data shows 35.0%, *below* the old baseline the deck cites as an improvement.
- **Slides 23, 28 (Australia, China):** relatively stable — close to current data.
- **Slide 16 (ROV Quadrant Map)** and its source `reports/analyze_rov_quadrants.md` no
  longer exist as an active pipeline output (retired script) — cannot be re-verified
  against a live report; would need manual recomputation from `rov_audit_v22_final.csv`.
- **Slides 31–33 (ASPA)** use the older model-based methodology
  (`analyze_aspa_realistic.md`, "Reality Gap: 9,986 links" framing). A newer,
  ground-truth data source now exists (`analyze_aspa_real_deployment.md`, real
  published ASPA objects) that the `pita31/` deck uses instead — this section's
  numbers are internally self-consistent with the old methodology's *current* output,
  but the methodology itself may be worth reconsidering (see Section V).
- Several named-network row tables (slides 19, 20, 21, 32) rank the **top N** by some
  metric — since the underlying rankings have reshuffled since May, some named ASNs no
  longer appear in the current top-N at all. Flagged per-table below rather than
  guessed at.

**If this deck is ever going to be presented, the numbers need a real refresh, not just
this fact-check pass** — see the summary this file's rebuild fed back to the user.

---

## Section I — Global Statistics (slide 13)

Source: `reports/statistics.md`

| Claim (as it appears on slide 13) | Current data | Verdict |
|---|---|---|
| 122,277 ASNs audited | 122,622 | ⚠️ Close but imprecise |
| CORE: ACTIVE PROTECTOR — 21 ASNs, 53.0% traffic | 21 ASNs, 52.2% traffic | ⚠️ Close but imprecise |
| ACTIVE LOCAL ROV — 287 ASNs, 5.8% traffic | 276 ASNs, 9.7% traffic | ❌ Wrong (traffic figure) |
| PASSIVE (Clean Pipe) — 986 ASNs, 10.3% traffic | 639 ASNs, 10.4% traffic | ❌ Wrong (ASN count) |
| STUB: PASSIVE — 19,318 ASNs | 19,124 ASNs | ⚠️ Close but imprecise |
| PARTIAL: VULNERABLE — 3,606 ASNs, 18.6% traffic | 2,666 ASNs, 8.7% traffic | ❌ Wrong — both figures |
| REGRESSED — 1,432 ASNs, 4.5% traffic | 4,337 ASNs, 10.9% traffic | ❌ Wrong — nearly 3x drift |
| STUB: VULNERABLE — 54,151 ASNs | 53,255 ASNs | ⚠️ Close but imprecise |
| CORE: UNPROTECTED — 3 ASNs, 4.6% traffic | 3 ASNs, 4.1% traffic | ⚠️ Close but imprecise |
| Overall: SECURE 23,055 (18.9%), PARTIAL 3,606 (3.0%), VULNERABLE 56,856 (46.5%) | SECURE 22,595 (18.4%), PARTIAL 2,666 (2.2%), VULNERABLE 58,764 (47.9%) | ❌ Wrong |

**Note:** current `statistics.md` also carries several verdict rows the deck doesn't
mention at all (`STUB: FORTUITOUS ROV`, `STUB: VOLATILE`, `STUB: UNRELIABLE`,
`VOLATILE`, `INCONSISTENT`, `UNRELIABLE`, `VULNERABLE (Atlas Verified)`,
`ACTIVE (Atlas Verified)`, `ACTIVE LOCAL ROV (Hardcoded)`, `Unverified (Transit/Peer?)`,
`NOT ROUTED`) — the deck's table appears to be a simplified/rolled-up subset, worth
confirming that's intentional rather than an omission if the slide is rebuilt.

---

## Section II — Herd Immunity (slides 14–15)

Source: `reports/analyze_herd_immunity.md`

| Claim | Current data | Verdict |
|---|---|---|
| Global Core (top 100): 59/100 secure (59.0%), 81.1% traffic protected | 51/100 (51.0%), 78.6% traffic | ❌ Wrong |
| Transit Layer (top 1,000): 294/1,000 secure (29.4%), 78.9% traffic protected | 227/1,000 (22.7%), 76.3% traffic | ❌ Wrong |

**Holdout table (slide 15)** — the ranking has reshuffled substantially; some deck rows
no longer appear in the current top-25, and new entries have appeared:

| ASN | Deck claims | Current data | Verdict |
|---|---|---|---|
| AS4134 (China Telecom Backbone) | rank #15, cone 65,065, excl% 79% | rank #20, cone 50,788, excl% 82% | ❌ Wrong (cone shrank ~22% — likely the IXP-phantom-pruning fix, see `[!] 86 IXP phantom networks excluded` note in the current report, not a real-world change) |
| AS4837 (China Unicom Backbone) | rank #21, cone 47,013, excl% 62% | rank #21, cone 48,116, excl% 61% | ⚠️ Close |
| AS3216 (Vimpelcom PJSC) | rank #26, cone 26,017, excl% 33% | rank #26, cone 26,727, excl% 32% | ⚠️ Close |
| AS9808 (China Mobile Backbone) | rank #49, cone 2,418, excl% 73% | rank #49, cone 2,761, excl% 73% | ⚠️ Close |
| AS9304 (HGC Global) | rank #55, cone 1,976, excl% 32% | rank #52, cone 2,406, excl% 30% | ⚠️ Close |
| AS9929 (China Unicom Industrial) | rank #58, cone 1,693, excl% 67% | rank #60, cone 1,603, excl% 67% | ⚠️ Close |
| AS18229 (CtrlS, India) | rank #112, cone 435, excl% 80% | rank #89, cone 584, excl% 78% | ⚠️ Close but rank moved a lot |
| AS45820 (Tata Teleservices ISP) | rank #126, cone 352, excl% 69% | not in current top-25 shown | ❓ Not found in the visible top-25 — check full report for current rank |
| AS52468 (UFINET PANAMA) | rank #35, cone 5,800, excl% 50% | not in current top-25 shown (current #35 is AS9498 Bharti Airtel) | ❓ Not found in visible top-25 — check full report |
| — | — | AS9498 (Bharti Airtel, India) now appears at #35, cone 6,974, excl% 61% | New entry not in deck at all |
| — | — | AS64073 (Vetta Group, NZ) now appears at #59, cone 1,689, excl% 14% | New entry — this is the deck's own NZ slide 24 "PASSIVE" example, now a holdout (see Section IV) |
| — | — | AS7713 (PT Telkom Indonesia) now appears at #47, cone 3,221, excl% 22% | New entry — this is the deck's own Indonesia slide 27 "PASSIVE" example, now a holdout |

---

## Section III — ROA Signing (slides 18–21)

Source: `reports/analyze_roa_signing.md`

| Claim | Current data | Verdict |
|---|---|---|
| Fully Signed (>90%): 45,196 ASNs (37.0%) | 46,349 (37.8%) | ⚠️ Close but imprecise |
| Partially Signed: 6,018 ASNs (4.9%) | 5,994 (4.9%) | ✅ Confirmed |
| Totally Unsigned: 71,063 ASNs (58.1%) | 70,279 (57.3%) | ⚠️ Close but imprecise |

**"Secure Providers, Unsigned Routes" table (slide 19)** — source is the
`NOT SIGNED, BY ROV COVERAGE TYPE` top-15 table, which has reshuffled. Only a partial
match was found for the deck's 6 named rows against the current top-15:

| ASN | Deck claims | Current data | Verdict |
|---|---|---|---|
| AS48185 (team.blue NV) | BE, cone 21,696, 0.0% signed | BE, cone 30,588, `NOT SIGNED (ROV UPSTREAM)` | ❌ Wrong (cone grew ~40%) |
| AS16735 (Algar Telecom) | BR, cone 2,319, 0.0% signed | BR, cone 1,979, `NOT SIGNED (ROV LOCAL)` | ❌ Wrong (cone shrank) |
| AS205794, AS46887, AS3786, AS2764 | — | not in current top-15 shown | ❓ Not found — full list needed to confirm whether they dropped out or just off the visible top-15 |

**"Fully Signed, Vulnerable Verdict" table (slide 20)** — source is `SIGNED (NO ROV)`
top-15, also reshuffled — most strikingly, **AS4134 (China Telecom Backbone), the
deck's #1 example, no longer appears in the current top-15 at all**, where the current
#1 by cone is AS37721 (Virtual Technologies & Solutions, BF, cone 50,259). This needs a
direct check on AS4134's current signing status — it may have changed classification
entirely, not just dropped in rank.

| ASN | Deck claims | Current data | Verdict |
|---|---|---|---|
| AS4134 (China Telecom Backbone) | cone 65,065, 100% signed, 0/0 feeds | not in current SIGNED (NO ROV) top-15 | ❌ Wrong / needs direct re-check |
| AS4837 (China Unicom Backbone) | cone 47,013, 98.8% signed, 0/0 feeds | cone 48,116, `SIGNED (NO ROV)`, 0/0 feeds | ⚠️ Close |
| AS17639 (Converge ICT) | cone 43,014, 97.8% signed, 0/10 feeds | cone 43,286, 0/10 feeds | ⚠️ Close |
| AS38001 (NewMedia Express) | cone 7,939, 100% signed, 0/8 feeds | cone 7,856, 0/8 feeds | ⚠️ Close |
| AS9304 (HGC Global) | cone 1,976, 100% signed, 2/15 feeds | cone 2,406, 2/15 feeds | ⚠️ Close |
| AS37721 (Virtual Technologies & Solutions) | not on deck's slide 20 list at all | now #1 in current list, cone 50,259, 0/15 feeds | New top entry the deck is missing |

**"Weighted ROA Outreach" table (slide 21)** — source is `reports/analyze_roa_strategy.md`
(not independently re-pulled for this rebuild — flag for a dedicated check).

**2026-09-16 formula change, logged here for the record:** the Impact Score formula
itself changed after this rebuild. It was `Cone × Unsigned Customers` (a binary count —
any customer under 10% signed counted as 1, everyone else as 0). It's now
`Cone × Signing Opportunity`, where Signing Opportunity is a partial-credit weighted sum
(`Σ (100 − signed_pct)` over downstream customers — a 0%-signed customer contributes
100, a 95%-signed one contributes only 5). This fixes a real distortion: the old cutoff
gave identical credit to a customer at 0% and one at 9%, and zero credit to one at 11%
even though it's still almost entirely unsigned. If the deck's ASPA/ROA outreach section
is ever refreshed, slide 21's numbers and its "Impact = (Provider Cone) × (Count of
Unsigned Customers)" description both need updating to match — the ranking order among
Tier-1s stays broadly similar (still cone-dominated, see Section III's structural note
above about squared-units size bias, which this change did not address), but the actual
Impact Score values and the "Unsigned Customers" column no longer exist in the script's
output.

---

## Section IV — APNIC Region (slides 23–28)

Source: `reports/au_report.md`, `nz_report.md`, `jp_report.md`, `in_report.md`,
`id_report.md`, `cn_report.md`

**This is where the most material drift in the whole deck lives — see the summary at
the top of this file.**

| Country | Claim | Current data | Verdict |
|---|---|---|---|
| AU | 2,915 networks, cone gravity 12,745, 26.5% secure → 91.8% traffic protected | 2,986 networks, cone gravity 12,301, 25.8% secure → 91.2% traffic | ⚠️ Close |
| AU | TPG Telecom AS7545: `PARTIAL: VULNERABLE (Mixed)` | same, still `PARTIAL: VULNERABLE (Mixed)`, 258 dependents | ✅ Confirmed |
| AU | AAPT AS2764: cone 413, 0.8% signed | cone 344, `VOLATILE` (was not `VOLATILE` in the deck's framing) | ⚠️ Cone/verdict drifted, signed% not independently re-checked here |
| NZ | 706 networks, cone gravity 2,287, 11.0% secure → 82.2% traffic protected | 704 networks, cone gravity 2,206, 11.4% secure → **5.3%** traffic protected | ❌ Wrong — traffic-protected collapsed |
| NZ | Vetta Group AS64073: cone 1,761, `PASSIVE (Clean Pipe)` | cone 1,689, **`REGRESSED`** | ❌ Wrong — status flip, not just drift |
| NZ | Two Degrees AS9790: `ACTIVE LOCAL ROV` | now `VOLATILE` | ❌ Wrong — status changed |
| JP | 968 networks, cone gravity 1,799, 30.2% secure → 53.9% traffic protected (deck itself frames this as "up from 39.5% previously") | 975 networks, cone gravity 1,802, 24.2% secure → **35.0%** traffic protected | ❌ Wrong — below even the deck's own cited historical baseline |
| JP | IIJ AS2497: 98% APNIC score, `PARTIAL: VULNERABLE (Mixed)` | 99% APNIC, still `PARTIAL: VULNERABLE (Mixed)` | ✅ Confirmed (close enough on APNIC%) |
| IN | 6,173 networks, cone gravity 14,176, 2.9% secure → 69.7% traffic protected, 22.2% exposed | 6,182 networks, cone gravity 13,851, 3.1% secure → **4.2%** traffic protected, **89.6%** exposed | ❌ Wrong — dramatic reversal |
| IN | Bharti Airtel AS9498: cone 7,328, `PASSIVE (Clean Pipe)` | cone 6,974, **`REGRESSED`** | ❌ Wrong — status flip |
| IN | TATA AS4755: cone 2,530, `PASSIVE (Clean Pipe)` | cone 2,482, **`REGRESSED`** | ❌ Wrong — status flip |
| ID | 3,969 networks, cone gravity 11,928, 1.6% secure → 70.2% traffic protected | 4,004 networks, cone gravity 9,897, 3.2% secure → **31.1%** traffic protected | ❌ Wrong — dramatic drop |
| ID | PT Telkom Indonesia AS7713: cone 4,804, `PASSIVE (Clean Pipe)` | cone 3,221, **`REGRESSED`** | ❌ Wrong — status flip |
| ID | Indosat AS4761 and AS55655: `REGRESSED` | AS4761 still cone 127 (was 148) — not confirmed still REGRESSED in this read, needs direct check; AS55655 confirmed still `REGRESSED`, 274 dependents | ⚠️ Partial re-check needed |
| CN | 6,491 networks, cone gravity 187,932, 1.1% secure → 37.6% traffic protected, 62.1% exposed | 6,482 networks, cone gravity 173,453, 1.2% secure → 39.9% traffic protected, 59.8% exposed | ⚠️ Close (relatively stable vs. the other 3) |
| CN | AS4809: `CORE: ACTIVE PROTECTOR`, cone 64,782 | cone 64,883, same status | ✅ Confirmed |
| CN | AS4134: `CORE: UNPROTECTED`, cone 65,065 | cone 50,788, same status | ⚠️ Cone shrank (IXP-phantom-pruning, see Section II) |
| CN | AS4837: `CORE: UNPROTECTED`, cone 47,013 | cone 48,116, same status | ✅ Confirmed |
| CN | CERNET AS38255: 3,859 downstream networks | `cn_report.md`'s transit-supply-chain table shows 3,859 **CN-country dependents** (exact match) — but `data/downstream_graph.json`'s **global** downstream count for AS38255 is 4,101, not 3,859 | ⚠️ Ambiguous, not a clean match — the deck's phrasing ("provides transit to 3,859 downstream networks", "3,859 Chinese and regional networks benefit") implies a global count, but 3,859 is actually CN-only. Self-caught while writing this rebuild: the "How to run this verification" script below checks the global count and gets a different number (4,101) than what this row first claimed as confirmed — fix that ambiguity before re-using either number on slide 28 or 32 |

---

## Section V — ASPA (slides 30–33)

**Methodology note:** this section uses `reports/analyze_aspa_realistic.md`'s
model-based approach ("Modeled: 'Regular' Networks", synthetic readiness buckets).
`reports/analyze_aspa_real_deployment.md` is a newer, ground-truth data source (real
published ASPA objects from `console.rpki-client.org`) that the `pita31/` deck now uses
instead. Both exist in the current pipeline; this section documents the deck's own
(model-based) claims against the model-based report's *current* output, and separately
notes what the ground-truth source shows, so whoever fixes the deck can decide which
approach to keep.

| Claim | Current model-based data (`analyze_aspa_realistic.md`) | Verdict |
|---|---|---|
| Of 121,152 'regular' networks: Trivial 64,786 (53.5%), Moderate 13,648 (11.3%), Complex 2,230 (1.8%), No upstreams 40,488 (33.4%) | "Modeled: 83,602 'Regular' Networks" — Trivial 66,121 (79.1%), Moderate 14,062 (16.8%), Complex 3,419 (4.1%) — **no "no upstreams" bucket in current output at all**, and the total denominator itself differs by ~37,550 networks | ❌ Wrong — this isn't drift, the denominator and bucket definitions appear to have changed between whatever version generated the deck's numbers and the current script |
| "The Impossibles": Apple (25), Dropbox (22), NAVER Cloud (21), Accenture (18) | Current "Complexity Giants" top list: ServiceNow (29), Fastly (27), Cisco Webex (27), Alibaba US (27), **Apple (27, not 25)**, Akamai Intl (26)... Dropbox appears as AS19679 with 24 (not 22), NAVER Cloud as AS23576 with 21 (matches) | ⚠️ Partial match — Apple and Dropbox provider counts don't match exactly, Accenture not found in the current top-40 shown at all |
| Reality Gap: 9,986 links left behind, down from 14,184 prior; Total C2P links 167,792; Theoretical max 87,155 (51.9%); Realistic forecast 77,168 (46.0%) | Not independently re-pulled for this rebuild (the script producing this specific framing — `analyze_aspa_readiness_v2.py`-style output — was not re-run here; only `analyze_aspa_realistic.md`'s readiness/complexity sections were checked above) | ❓ Not checked — needs a dedicated re-run before trusting these specific figures |

**What the ground-truth source (`analyze_aspa_real_deployment.md`) shows instead, for context:**
3,031 ASNs (2.47% of all audited) hold a real published ASPA object. Of 84 "ready-to-sign
giants" (cone > 100, 100% ROA hygiene, 100% secure upstreams), only 7 (8.3%) have signed;
77 (91.7%) haven't. Top ready-but-unsigned by cone: AS24482 SG.GS (64,668) — note this is
the *same* SG.GS the deck's slide 33 quadrant example cites (cone 64,564 there) — the
numbers are close enough to be the same entity read from two different angles.

---

## Section VI — ROV Quadrant Map (slide 16)

**Source no longer exists as a live report.** `reports/analyze_rov_quadrants.md` is not
produced by the current `do_reports` pipeline (the generating script appears to have
been retired). The deck's slide 16 itself already contains inline named examples with
specific cone/percentage figures (Hurricane Electric, China Telecom/Unicom Backbone,
Lumen, Cogent, Zayo, GTT, AT&T, SG.GS, Virtual Technologies & Solutions, Converge ICT) —
these cannot be re-verified against a report file with this rebuild's approach. Fully
re-verifying this slide would require manually recomputing the four-quadrant
classification (provider ROV status × customer signing %) directly from
`rov_audit_v22_final.csv` and `roa_signing`-equivalent per-ASN data — out of scope for
this pass; flagging as a known gap.

---

## Section VII — Technical / Protocol Claims

These are evaluated against RFC text and established BGP/RPKI practice, not the audit
data — protocol semantics don't drift with data refreshes, so these should still hold,
but slide numbers below are corrected to match the current deck.

| Claim | Slide | RFC / Reference |
|---|---|---|
| RPKI has three route states: Valid, Invalid, NotFound | 4, 5 | RFC 6811 §2 |
| ROV drops Invalid routes; NotFound routes pass | 5 | RFC 6811 §5, RFC 7115 |
| A more-specific prefix wins by longest-match regardless of RPKI state | 19 | BGP longest-prefix-match (RFC 4271) |
| Without a covering ROA, ROV provides no protection against more-specific hijacks | 19 | RFC 6811 + RFC 8893 |
| ASPA is built on top of ROV — a non-ROV provider cannot enforce ASPV | 33 | RFC 9589 §5 |
| Valley-free Gao-Rexford constraint: (c→p)* → (peer)? → (p→c)* | 8 | Gao-Rexford 2001, RFC 7908 |
| IXP route servers strip their ASN from AS-paths per RFC 7947 | 9 | RFC 7947 §2.2.2 |
| RFC 9582 = ASPA Objects, RFC 9589 = ASPV Algorithm | 30 | Check publication status is still current |

---

## Section VIII — Consistency Checks (internal to the deck)

Slide numbers corrected to match the current deck (see the full slide map this rebuild
used, available on request — computed directly from the file's own `---` separators).

| Check | Slides |
|---|---|
| Quadrant Q2 "Signed Customers, Unsecured Provider" (slide 16) — confirm consistent with slide 19/20's own framing of the same failure mode, now that all three use the toned-down non-dramatic naming | 16, 19, 20 |
| Holdout table (slide 15) entries — confirm verdicts match the equivalent per-country report rows | 15, 23–28 |
| AS9304 HGC appears in both the holdout table (slide 15) and the "Fully Signed, Vulnerable Verdict" table (slide 20) — confirm cone/verdict are consistent between the two | 15, 20 |
| CERNET AS38255 cited as 3,859 downstream networks (ASPV context, slide 32) vs the China slide's own mention (slide 28) — confirm same figure, same entity | 28, 32 |
| China's slide 28 table shows 39.9% traffic protected / 59.8% exposed — confirm these plus the PARTIAL remainder are internally consistent with the country report | 28 |
| **New (2026-09-16):** slides 24/26/27's PASSIVE-network examples (Vetta Group, Bharti Airtel, TATA, PT Telkom) are stale in the same direction across all three countries (all now REGRESSED) — worth checking whether this reflects one shared upstream/methodology change rather than three independent local regressions, before presenting this as three separate country stories | 24, 26, 27 |

---

## How to run this verification

```bash
cd /home/terry/rpki_audit
# Check a specific report file
cat reports/statistics.md | grep -A5 "CORE: ACTIVE"

# Spot-check impact score arithmetic (Hurricane Electric example, slide 21)
# Confirmed 2026-09-16: this matches the deck's claimed "2.55 Billion" exactly —
# the formula is applied correctly, even though the input cone/unsigned-customer
# numbers themselves weren't independently re-verified in this rebuild.
python3 -c "print(79819 * 31949 / 1e9, 'Billion')"

# Check CERNET's downstream count — NOTE: this returns the GLOBAL count (4,101 as of
# 2026-09-16), not the CN-country-only count (3,859) the deck actually cites on
# slides 28/32. Don't treat these two numbers as interchangeable — see Section IV.
python3 -c "
import json
data = json.load(open('data/downstream_graph.json'))
print('CERNET GLOBAL downstream count:', len(data.get('38255', [])))
"

# Re-run the full ASPA readiness/complexity numbers fresh
python3 analyze_aspa_realistic_v5.py

# Re-run the ground-truth ASPA adoption numbers fresh
python3 analyze_aspa_real_deployment.py
```
