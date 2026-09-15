---
marp: true
theme: _template
paginate: true
footer: "{{EVENT}} · {{LOCATION}} · {{DATE}} · Terry Sweetser · IEISI"
backgroundColor: "#ffffff"
color: "#1a1a2e"
---

<!--
  rpki_audit conference-deck template.

  Before writing content:
  - Rename this file and the theme CSS to `<event>_presentation.md` /
    `<event>-theme.css`, update `theme:` above to match, and fill every
    {{PLACEHOLDER}}.
  - Regenerate the source reports first (`bash do_reports`) so every number
    you quote comes from the current run, not a stale checked-in report.
  - Use the CURRENT report vocabulary: the 8-state classification matrix
    (SIGNED (ROV) / SIGNED (NO ROV) / NOT SIGNED (ROV UPSTREAM) / etc.),
    REGRESSED / VOLATILE / UNRELIABLE / SECURE / PASSIVE / FORTUITOUS.
    Do NOT reuse retired dramatic phrasing from the apnic62 talk (e.g.
    "SITV", "Glass Houses", "The Swamp") — those are frozen to that one
    2026 talk, not house style.
  - Add a scope row for this deck to `presentations/README.md` so audience
    intent doesn't drift between talks.
  - Fill VERIFY_CLAIMS.md and run a fact-check pass before presenting.
-->

<!-- _class: title-slide -->

# {{TALK_TITLE}}
### {{TALK_SUBTITLE}}

**Presenter:** Terry Sweetser
**Organization:** IEISI
**Conference:** {{EVENT}} · {{LOCATION}} · {{DATE}}

---

# Agenda

1. **Why Measurement Matters** — BGP security is not binary
2. **Methodology** — Zero-scrape triangulation at scale
3. **Global Results** — {{TOTAL_ASNS}} ASNs audited
4. **Herd Immunity** — Where does protection actually come from?
5. **ROA Signing** — Secure providers, unsigned routes, and outreach targets
6. **{{AUDIENCE_DEEP_DIVE_TITLE}}** — <!-- e.g. "APNIC Region Deep-Dive" / "Pacific Islands Progress Check" -->
7. **ASPA Readiness** — The next layer and the Reality Gap
8. **Recommendations** — Concrete actions for {{AUDIENCE}}

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

The real question: **"What percentage of {{AUDIENCE}} traffic is actually protected right now, and by whom?"**

---

<!-- _class: section-divider -->

# Part II: Methodology

Zero-scrape triangulation at scale

<!-- Boilerplate — reuse near-verbatim from apnic62/apnic62_presentation.md
     ("Zero-Scrape Architecture", "Topology: Valley-Free BGP",
     "Multi-Collector IXP Phantom Mitigation", "RIPE Atlas Forensic
     Verification", "APNIC Data Quality: Adaptive Window Selection") unless
     this venue needs a shorter methodology section. -->

---

<!-- _class: section-divider -->

# Part III: Global Results

---

# Global Verdict Breakdown

<!-- DATA SOURCE: reports/statistics.md (current run). Pull the verdict
     breakdown table and total ASN count. -->

---

# The Herd Immunity Scoreboard

<!-- DATA SOURCE: reports/analyze_herd_immunity.md — top-100 core /
     top-1,000 transit secure counts and traffic-weighted coverage. -->

---

<!-- _class: section-divider -->

# Part IV: ROA Signing

---

# Global ROA Signing Status

<!-- DATA SOURCE: reports/analyze_roa_signing.md,
     reports/analyze_roa_signing_trends.md — the China trend finding is a
     strong, narratively-compelling candidate here if relevant to the
     audience. -->

---

<!-- _class: section-divider -->

# Part V: {{AUDIENCE_DEEP_DIVE_TITLE}}

<!-- This is the section that should differ most between decks. Check
     presentations/README.md's scope table for this deck's audience before
     writing it: region-specific (apnic62-style per-economy slides),
     initiative-progress (pita31-style before/after comparison), or generic
     (ietf-style, no region assumed). -->

---

<!-- _class: section-divider -->

# Part VI: ASPA — The Next Layer

---

# Why ROV Alone Is Insufficient: Route Leaks

<!-- Boilerplate — reuse near-verbatim from apnic62. -->

---

# ASPA Readiness: The Simplicity Opportunity

<!-- DATA SOURCE: reports/analyze_aspa_real_deployment.md,
     aspa_real_vs_model.csv, the aspa-path-protection Go tool output. -->

---

# The Reality Gap

<!-- DATA SOURCE: reports/aspa_path_protection.md — links left behind by
     partial ASPA deployment. -->

---

<!-- _class: section-divider -->

# Part VII: Recommendations

---

# Recommendations: For Network Operators

<!-- TODO: audience-specific asks. -->

---

# Recommendations: For RIRs and Policy Bodies

<!-- TODO: audience-specific asks. -->

---

# Recommendations: For the Ecosystem

<!-- TODO: audience-specific asks. -->

---

<!-- _class: section-divider -->

# Part VIII: Conclusion

---

# What the Data Says — Honestly

<!-- Keep this slide's tone calibrated: state what the data supports and
     what it doesn't (e.g. APNIC filter_rate cannot distinguish direct vs.
     inherited ROV — see CLAUDE.md). Don't overclaim. -->

---

# Summary: Who Should Do What

---

# Questions & Discussion

---

<!-- _class: section-divider -->

# Appendices

---

# Appendix A: Full Verdict Taxonomy

<!-- Boilerplate — reuse from apnic62 (8-state classification matrix). -->
