# Changelog — data-subject-rights

All notable changes to this skill are documented here.

Format: `## [vX.Y] — YYYY-MM-DD`

---

## [v1.2] — 2026-09-24

Portfolio standard Level 1 (structural-tier) adoption. No change to DSR method,
deadlines, templates, or legal content.

- **New native sidecar** — `references/dsr-sidecar-schema.json` (triage verdict:
  rights invoked, computed deadline, identity-verification stance, decision,
  downstream duties).
- **New `validator/`** — `dsr_validator` package (structural tier): SCHEMA-1
  (schema conformance), CONSEQ-1 (a `grant`/`partial` decision contradicting an
  unresolved identity doubt — the Assessment Flow's own identity-check gate),
  DEADLINE-1 (Art. 12(3) one-/three-month window arithmetic), RIGHTS-1
  (read-generously completeness heuristic — an Art. 17-only triage must not
  silently drop a plainly-present Art. 15 component), SRC-1 (sources.lock
  coverage/freshness), RUNNER-0 (empty-registry fail-closed guard). 49 pytest
  cases; one `must_fail` fixture proven to trip exactly CONSEQ-1.
- **New `--emit-core-artefact`** — projects a validated sidecar into the
  portfolio `skill-artefact-1.1` shape. `subject` is the DSR request itself
  (`type: "other"`). `gaps[]` covers both the validator's own diagnostics and
  undischarged plain downstream duties (e.g. Art. 19 third-party
  notification). `handoffs[]`/`unknowns[]` are driven by which of the four
  named sibling handoffs (`ropa`, `legitimate-interest`, `dpa-art28`,
  `privacy-notice-eu`) came up in the run's own `downstream_duties[]` — never
  hard-coded. `sources[]` is read live from `sources.lock.json`.
- **New `sources.lock.json`** — `last_verified: 2026-07-07` for the core Art.
  15/17 method content (the actual legal verification pass date), not the
  fresher 2026-07-21 date, which was a documentation-only Digital Omnibus
  instrument-ID correction (see the note in the manifest itself).
- **New `conformance.json`** — `tier: "structural"`, `standard_version: "1.4"`.
  `scripts/check_conformance.py` reports `CONFORMANT`.
- **`SKILL.md`** — new "Machine-readable output" section.

**Status:** reviewed (carried from v1.1); no legal-content re-verification performed this release.

---

## [v1.1] — 2026-07-21

Verification-log closure on the Digital Omnibus instrument split. Documentation-only; no change to DSR method, deadlines, templates or the pending-legislation section.

- **`sources/verification-log.md` §4.1 — the portfolio NB is now actioned and closed.** The 2026-07-07 entry correctly identified that the GDPR amendments are Article 3 of **COM(2025) 837 final** (2025/0360(COD)) and flagged that sibling skills citing "COM(2025) 833" needed checking. That check has now been carried out portfolio-wide.
- **New finding recorded: COM(2025) 833 does not exist.** EUR-Lex holds no `52025PC0833`. The 19 November 2025 package is COM(2025) 836 (AI), COM(2025) 837 (data/privacy/cybersecurity) and COM(2025) 838 (European Business Wallets). The earlier working assumption — that `eu-data-act`'s use of 833 was probably correct because 833 was "a real instrument amending other law" — is therefore withdrawn.
- **Ownership recorded.** This skill owns the Digital Omnibus instrument-identification fact; `breach-sentinel` v3.2, `dpia-sentinel` v1.10, `ropa` v2.13, `privacy-notice-eu` v1.4 and `eu-data-act` v1.4 carry a pointer note to the primary source rather than a duplicated assertion.

**Status:** reviewed (carried from v1.0).

---

## [v1.0] — 2026-07-10

First reviewed release. Both promotion gates passed:

- **Gate 1 — legal verification pass (2026-07-07):** see the v0.9 entry below and `sources/verification-log.md`.
- **Gate 2 — Phase 8 `/skill-creator` eval benchmark (2026-07-10):** 6 fixtures × with-skill/baseline on Sonnet, 44 assertions. **With-skill 44/44 (100%) vs baseline 36/44 (82.1%), delta ≈ +18pp** — in the expected judgment-skill band per `docs/eval-methodology.md`. Baseline losses concentrated in the German erasure fixture (Art. 19 notification, erasure-endpoint date, backup transparency); baseline also applied the stale pre-BEG-IV 10-year retention figure and UK authorities where the skill applied the verified 8-year rule and current CJEU law (C-526/24). Eval-suite tweaks this release: eval 6 expectation aligned to the C-203/22 operative wording ("procedure and principles", not "factors and weights"); eval 3 expected answer notes the C-526/24 abuse distinction.
- Known non-discriminator: eval 6 (Art. 22) near-ties with baseline — structural value, not correctness delta. Candidate iteration-2 assertion: correct post-BEG-IV retention figure (grader suggestion).
- **Disclosure (2026-08-21):** `evals/evals.json` was edited after the Gate 2 benchmark above was run — eval 7 was added, and evals 2 and 6 were reworded. The suite is now 7 fixtures / 50 assertions. The 44/44-vs-36/44 figures quoted in this entry describe the pre-2026-07-12 suite only and have not been re-measured against the current 7-fixture / 50-assertion suite.

## [v0.9] — 2026-07-07

Initial pre-review build (general GDPR data subject rights skill — all rights, with access and erasure as deep tracks; scoped per user decision 2026-07-07: not DSAR-only).

- Architecture per `docs/skill-architecture-guide.md`: lean orchestrator SKILL.md (routing table, 15 legal precision points, sibling handoffs) + lazy-loaded reference modules.
- References: `procedural-framework.md` (Art. 12 modalities: form-free receipt, deadline math, Art. 12(6) identity proportionality, Art. 12(5) high bar), `art15-access.md` (EDPB 01/2022; C-154/21 recipients, C-487/21 copy, C-307/22 motive/fee, C-579/21 log data, C-203/22 trade-secret limits), `art17-erasure.md` (two-step test, Art. 17(3)(b) retention → Art. 18 restriction disposition, backups, Art. 17(2)/19 downstream, delisting, C-26/22 & C-64/22), `other-rights.md` (Art. 16/18/20/21/22 incl. C-634/21 SCHUFA), `restrictions-overlays.md` (Art. 23; BDSG §§ 34/35, § 26; DE retention anchors with verify-flags), `templates.md` (five letter skeletons EN/DE, DSR register schema, deadline computation block).
- Evals: 6 cases (recipient naming + deadline-from-receipt + ID proportionality; German partial-erasure/retention; litigation-motive DSAR under counsel pressure; dual objection regimes + suppression list; portability scope trap; Art. 22 rubber-stamping) — with-skill/baseline benchmark NOT yet run (Phase 8 pending; promotion gate per `docs/eval-methodology.md`).
- Known deferrals: no `index.html` portfolio page yet (needs a hand-authored `docs/portfolio/skill_pages/` ENTRY); non-DE jurisdiction overlays are flag-level only; German AO § 147 retention-period change (BEG IV, 8 vs 10 years) marked verify-before-citing.
- ⚠️ **SOURCE CAVEAT (initial build):** built from model training knowledge (cutoff Jan 2026) cross-checked against reviewed sibling skills — no live legal research performed at build time.
- ✅ **Legal verification pass completed same day (2026-07-07)** — five live-research clusters against primary sources; full record in `sources/verification-log.md`. All 14 cited CJEU cases confirmed real with correct dates; corrections applied: C-487/21 copy test ("essential to exercise rights effectively"), C-203/22 explanation standard ("procedure and principles actually applied"), C-129/21 downstream-duty split, C-507/17 territorial precision; EDPB 01/2022 citation updated to v2.1 and the wrong-channel rule qualified (¶54-55); AO § 147/HGB § 257 retention table corrected (books 10 yrs / Buchungsbelege 8 yrs since BEG IV, financial-sector 10-yr carve-out per BGBl. 2025 I Nr. 369) and BDSG §§ 34/35 structure fixed (§ 34(3) BfDI route only vs. federal public bodies; § 35(3) = satzungsgemäß/contractual periods); post-cutoff CJEU incorporated (C-526/24 abusive-first-request doctrine reconciled with C-307/22, C-247/23 rectification evidence limits, C-413/23 P pseudonymised-data scope, C-655/23 no-preventive-injunction, C-492/23 platform-controller duties); new "Pending Legislation — Digital Omnibus" section (COM(2025) 837 Art. 3, current-law-first rule). Remaining v1.0 gate: Phase 8 eval benchmark. NOTE: evals.json predates the C-526/24 doctrine — re-check the litigation-motive eval's expected answer before running Phase 8.
