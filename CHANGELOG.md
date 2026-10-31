# Changelog — data-subject-rights

All notable changes to this skill are documented here.

Format: `## [vX.Y] — YYYY-MM-DD`

---

## [v1.4] — 2026-10-31

Bundled tests made portable to the standalone public copy (`scripts/stage-public-copy.sh`
+ `scripts/check-public-portability.sh`). No change to the core DSR method or response
templates.

- **`validator/dsr_validator/_schema_paths.py` (new) exposes `find_schema()`**, which
  locates a shared portfolio schema (`docs/standards/schemas/*.schema.json`) by walking
  up from the file's own location — works identically whether the schemas sit at the
  monorepo root or at the root of a flat public copy (the staging script now copies
  them there). `validator/dsr_validator/test_core_artefact.py` and
  `validator/dsr_validator/test_runner.py` use it instead of a hard-coded path computed
  from `Path(__file__).resolve().parents[4]`, which only resolved correctly inside the
  monorepo.

## [v1.3] — 2026-10-02

Break-it test fix wave (adversarial probe pass, `scratchpad/breakit/data-subject-rights/P01-P14`). Validator rule fixes/additions, a jurisdiction-scope clarification, and a German-law expansion. No change to the core DSR method or response templates.

- **DEADLINE-1 false positive fixed.** The rule rejected a correctly computed deadline that had rolled forward past a weekend/holiday per the regulation it already cites (`procedural-framework.md`; Reg. (EEC, Euratom) No 1182/71 Art. 3(4), re-confirmed verbatim 2026-10-02: "Where the last day of a period... is a public holiday, Sunday or Saturday, the period shall end with the expiry of the last hour of the following working day"). Saturdays/Sundays are now rolled forward deterministically; a public holiday only rolls the deadline when declared via the new optional `deadline.holiday_rollover` field (date + reason) — never inferred. Month-end clamping and leap-year arithmetic are unaffected (regression-tested).
- **New `DEADLINE-2`** — an Art. 12(3) extension must be declared within the first month (new optional `deadline.extension_declared_at` field); a late declaration is now a rejection instead of silently passing.
- **New `FEE-1`** — a charged fee (new optional `fee` field: `charged`, `amount`, `currency`, `ground`) now requires a stated Art. 12(5) ground (`further_copy` or `manifestly_unfounded_or_excessive`); charging for a first copy with no ground stated is a rejection (Art. 15(3)).
- **New `ERASURE-1`** — an Art. 17 `refuse` must record a ground examined and/or an exception relied on (new optional `erasure_decision` field: `ground_examined`, `exception_relied_on`); a full `grant` while an Art. 17(3) exception (e.g. `(b)` statutory retention) is recorded on the same sidecar is now a rejection — partial disposition is the correct decision in that case.
- **`CONSEQ-1` widened** — now also fires on `decision=grant/partial` for Art. 15/Art. 17 requests when `identity_verification.verified` is explicitly `false`, even if `reasonable_doubts` was (wrongly) left `false`. Deliberately scoped to the two disclosure/destruction-risk rights to avoid false positives on lower-risk rights (e.g. Art. 16 rectification).
- **`RIGHTS-1` made bidirectional and widened** — previously only flagged an Art. 17-only triage missing a plain Art. 15 component; now also flags the reverse (an Art. 15-only triage whose text plainly asks for erasure, e.g. "delete everything you have on me"). Both phrase lists modestly widened (e.g. "what personal data you store about me", "delete my account").
- **`dsr-sidecar-schema.json` → schema 1.1** (backwards compatible — `schema_version` now accepts `"1.0"` or `"1.1"`; all four new fields are optional, a 1.0 sidecar omitting them stays valid).
- **Validator CLI fails closed** (`validate.py`) on a missing file, unreadable file, invalid UTF-8, invalid JSON, or non-object top-level JSON — a clean one-line message and exit 1, no raw traceback. Previously crashed with a Python traceback on all of these.
- **SKILL.md — new "Scope — jurisdiction" section**: this skill covers EU GDPR (+ German BDSG); a UK "SAR"/"DSAR" is explicitly out of scope — post-2021 CJEU rulings aren't binding in the UK, and the Data (Use and Access) Act 2025 changed UK subject-access handling (main provisions in force 5 Feb 2026 per SI 2026/82) — verify specifics on legislation.gov.uk rather than relying on this skill.
- **SKILL.md — new "Identity — competing claims and abuse" section**: joint-account/ex-partner/family-member requests are a disclosure risk, not a routine identity check; verify against the account holder, not the requester.
- **`restrictions-overlays.md`** — added BDSG §§ 32, 33, 36, and 37 (each fetched live from gesetze-im-internet.de 2026-10-02): §§ 32/33 restrict the Art. 13(3)/14 proactive notice duties (not an Art. 15 access request itself); § 36 restricts the general Art. 21(1) objection against public authorities only; § 37 narrows Art. 22(1) for insurance-contract-performance decisions. § 37 cross-referenced from `other-rights.md`'s Art. 22 section.
- **Digital Omnibus content moved** from SKILL.md into new `references/pending-legislation.md` (now covered by `sources.lock.json`/SRC-1 freshness instead of living outside it) and its status re-verified live 2026-10-02 (still EP committee stage; Council's 26 Jun 2026 general-approach vote was cancelled; no trilogue).
- **SKILL.md "Machine-readable output"** — added an explicit sentence: a validator pass means the sidecar is internally consistent and complete against its own schema and rules, NOT that the underlying legal analysis is correct.
- `sources.lock.json` — `last_verified` updated to 2026-10-02 for `procedural-framework.md`, `art17-erasure.md`, `other-rights.md`, and `restrictions-overlays.md` (content changes above); new entry for `pending-legislation.md`.
- Test suite: 49 → 94 pytest cases (new `test_fee.py`, `test_erasure.py`, `validator/test_validate_cli.py`; new assertions in `test_deadline.py`, `test_consequential.py`, `test_rights_detection.py`); 6 new `must_fail` fixtures and 7 new `must_pass` fixtures (including non-regression controls for leap-year month-end and exact-boundary extension arithmetic).

**Status:** reviewed (carried from v1.2) — this release did not re-run the full Phase 8 eval benchmark; see `sources/verification-log.md` "Break-it fix wave (2026-10-02)" for the legal-content verification record.

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
