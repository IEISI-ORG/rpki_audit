# Conference Deck Template

Starting point for a new rpki_audit conference talk, based on the
`presentations/apnic62/` precedent. Produces a [Marp](https://marp.app/)
markdown deck with a custom theme, a Makefile, and a render-check script.

## Use it

1. Copy this directory to a new one named after the event:
   ```bash
   cp -r presentations/_template presentations/<event>
   cd presentations/<event>
   ```
2. Rename the two content files to match the directory name (the Makefile
   derives filenames from `$(notdir $(CURDIR))`, so this is the only rename
   needed):
   ```bash
   mv _template_presentation.md <event>_presentation.md
   mv _template-theme.css <event>-theme.css
   ```
3. In `<event>_presentation.md`, update `theme: _template` to `theme: <event>`
   (must match the `@theme` name at the top of the CSS file), and fill every
   `{{PLACEHOLDER}}`.
4. If you don't want a custom theme, delete `<event>-theme.css` and remove
   the `theme:` line plus `THEME`/`--theme-set` from the Makefile.
5. Re-run `bash do_reports` from the repo root first, so every figure you
   quote comes from the current audit run rather than a stale checked-in
   report.
6. Add a scope row for `<event>/` to `presentations/README.md` — audience
   and region assumptions must not silently drift between talks (see that
   file's existing table for the pattern).
7. Fill in `VERIFY_CLAIMS.md` from the template and run a fact-check pass
   against the current reports before presenting — this is what caught
   errors before the apnic62 talk.
8. Build and verify:
   ```bash
   make all
   make check SLIDES=<final slide count>
   ```

## What carries over between decks vs. what doesn't

**Reuse near-verbatim** (already-vetted framing, not audience-specific):
the three-layer ROA/ROV/ASPA problem statement, the zero-scrape methodology
section, the route-leak/ASPA rationale, and the full verdict-taxonomy
appendix.

**Rewrite per deck**: the global-results and ROA-signing numbers (pull from
the current run's reports, not copied from a past deck), and the entire
audience/region deep-dive section — that's the one section apnic62, pita30,
and ietf each did completely differently, matching their audience's scope
row in `presentations/README.md`.

**Never carry over**: retired dramatic language from a specific past talk
(the apnic62 deck used phrases like "SITV" / "Glass Houses" / "The Swamp"
that are frozen to that one 2026 talk, not house style). Use the current
report vocabulary — the 8-state classification matrix and verdicts
documented in the repo root `CLAUDE.md` (REGRESSED, VOLATILE, UNRELIABLE,
SECURE, PASSIVE, FORTUITOUS, etc.).
