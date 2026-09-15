# {{EVENT}} Presentation — Claims & Conclusions Verification Prompt

Use this prompt with Claude (or another LLM with access to the audit data) to systematically verify every factual assertion in `{{event}}_presentation.md` before the talk.

---

## Instructions for the verifier

You are fact-checking the {{EVENT}} presentation `{{event}}_presentation.md` against the {{DATA_RUN_DATE}} rov_audit output. For each claim below, locate the authoritative source in the listed report file, confirm the number or statement matches, and flag any discrepancy. Where the claim is a technical assertion about RPKI/BGP protocol behaviour (not an audit statistic), evaluate it against RFC text or established operator practice.

Use this working directory: `/home/terry/rpki_audit/`

**Verdict for each claim:** ✅ Confirmed / ⚠️ Close but imprecise / ❌ Wrong / ❓ Not found in source

---

## Section I — Global Statistics (slide {{N}})

Source: `reports/statistics.md`

| Claim | Source field |
|---|---|
| {{total ASNs audited}} | total ASN count |
| {{verdict counts / traffic %}} | verdict breakdown table |

---

## Section II — Herd Immunity (slide {{N}})

Source: `reports/analyze_herd_immunity.md`

| Claim | Source field |
|---|---|
| {{top-100 core secure count / traffic %}} | core layer table |
| {{top-1,000 transit secure count / traffic %}} | transit layer table |

---

## Section III — ROA Signing (slide {{N}})

Source: `reports/analyze_roa_signing.md`, `reports/analyze_roa_signing_trends.md`

| Claim | Source field |
|---|---|
| {{signing status counts}} | ROA signing breakdown |

---

## Section IV — {{LOCAL_CONTEXT_TITLE}} (slide {{N}})

Source: `reports/{{cc}}_report.md` (per-economy) or the relevant audience-specific report

| Claim | Source field |
|---|---|

---

## Section V — ASPA (slide {{N}})

Source: `reports/analyze_aspa_real_deployment.md`, `reports/aspa_path_protection.md`

| Claim | Source field |
|---|---|

---

## Protocol / technical assertions (not audit statistics)

List any claims about RFC behaviour, Gao-Rexford valley-free semantics, or
RPKI/ROV mechanics that need checking against `CLAUDE.md` or the relevant
RFC rather than a report file.

| Claim | Slide | Verdict |
|---|---|---|

---

## Sign-off

- [ ] All Section claims confirmed against current-run reports (not stale checked-in CSVs)
- [ ] No retired apnic62-era phrasing ("SITV", "Glass Houses", "The Swamp") carried over
- [ ] Tone matches CLAUDE.md's honesty notes (e.g. APNIC filter_rate ambiguity, inherited vs. direct ROV)
