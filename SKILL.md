---
name: data-subject-rights
description: |
  GDPR data subject rights handling under Articles 12-23 — intake, assessment, and response drafting for access, rectification, erasure, restriction, portability, objection, and automated-decision rights, including deadlines, identity verification, exceptions, and refusal reasoning. Triggers: "DSAR", "data subject access request", "subject access request", "SAR", "Auskunftsersuchen", "Auskunftsanspruch", "Art. 15", "right to erasure", "right to be forgotten", "delete my data", "Löschantrag", "Löschbegehren", "Betroffenenrechte", "data subject request", "we received a request from a data subject/customer/employee", "Widerspruch gegen Verarbeitung", "data portability", "restriction of processing", "how long do we have to respond", objection to marketing or profiling, Art. 22 automated decision complaints, questions about refusing or charging for a request.
metadata:
  author: Oliver Schmidt-Prietz
  license: AGPL-3.0
  version: 1.3
---

# Data Subject Rights (GDPR Art. 12–23)

## Disclaimer (show at session start, do not block)

> **Important:** This skill provides structured guidance on handling GDPR data subject requests based on the Regulation, EDPB Guidelines 01/2022 (right of access), and CJEU case law. It is not legal advice. Involve your DPO and qualified counsel for contested or high-risk requests.

## Scope — jurisdiction

This skill covers **EU GDPR** (plus German BDSG overlays, `references/restrictions-overlays.md`). A request citing UK law — "SAR"/"DSAR" under **UK GDPR**, the Data Protection Act 2018 — is **outside this playbook**: (1) CJEU rulings handed down after 31 Dec 2020 (the end of the Brexit transition period) are not binding on UK courts/the ICO, so the post-2021 CJEU case law point 3, 14 and others above do not transfer automatically; (2) the **Data (Use and Access) Act 2025** changed UK subject-access handling — a statutory "stop the clock" mechanism while the controller seeks clarification, and a "reasonable and proportionate search" standard — with the main data-protection provisions in force from 5 February 2026 (verify current commencement/wording on legislation.gov.uk before relying on specifics; this skill does not track UK law). Flag a UK-law request and recommend UK-qualified counsel rather than applying the EU analysis above.

## Identity — competing claims and abuse

A request about someone else's data wearing the data subject's name (ex-partner, joint-account co-holder, estranged family member) is a **disclosure risk, not a routine identity check**: verify identity against the actual account holder, not against whoever is asking, and never disclose one joint-account holder's personal data to another without an independent basis (consent, or data genuinely both parties' own). Treat a request that supplies only guessed/public information (an email address, a name) as unverified — see Legal Precision Point 7 and CONSEQ-1 below. DSR abuse (harassment campaigns, serial request-and-sue patterns) is a real but narrow limit — Legal Precision Points 3 and 8 — never a reason to add friction to ordinary requests.

## Routing

Determine what the user needs and load references accordingly:

| User Need | Load These References | Action |
|-----------|----------------------|--------|
| Any incoming request — first triage | `references/procedural-framework.md` | Run intake: right(s) invoked, requester identity, clock start, channel |
| Access request (Art. 15) | `procedural-framework.md` + `references/art15-access.md` | Scope the response, apply third-party and exception analysis |
| Erasure request (Art. 17) | `procedural-framework.md` + `references/art17-erasure.md` | Test grounds, then exceptions, then downstream duties (Art. 17(2), 19) |
| Rectification / restriction / portability / objection / Art. 22 | `procedural-framework.md` + `references/other-rights.md` | Assess the specific right |
| Refusing, charging, or extending | `procedural-framework.md` (Art. 12(5) section) | Draft reasoned refusal/extension with the high-bar tests |
| National law restrictions (esp. Germany) | `references/restrictions-overlays.md` | Check Art. 23 + BDSG §§ 32/33/34/35/36/37 carve-outs |
| Response letters, DSR register, deadline math | `references/templates.md` (+ docx skill for .docx output) | Draft the deliverable |
| Checking the Digital Omnibus reform status | `references/pending-legislation.md` | Confirm it is still a proposal before citing it |

**Intake questions (only those not already answered):** (1) Which right(s) does the request invoke — read it generously, a "delete everything and tell me what you have" email is BOTH Art. 17 and Art. 15. (2) When and through which channel was it received? (3) Requester's relationship (customer, employee, third party/agent)? (4) Any identity doubts — concrete, not hypothetical? (5) Controller's jurisdiction and sector (retention laws)?

## Assessment Flow

**Intake → Identity check (only if reasonable doubts) → Clock confirmation → Right-by-right assessment → Exceptions/restrictions → Downstream duties → Response draft → Register entry**

Adapt to the user: an experienced privacy team dumping full context gets a verdict and a draft; a first-timer gets the procedure explained. Always compute and state the concrete deadline date.

## Legal Precision Points

These are areas where training knowledge is commonly imprecise. Always apply these rules:

1. **The clock starts when a request reaches an official or reasonably expected controller channel.** A general support inbox counts even if the controller prefers a privacy portal; internal routing delay does not move the deadline. A completely random, apparently incorrect, or clearly unrelated address does not automatically count where an appropriate channel was clearly communicated. Requests remain form-free, and a prompt, justified Art. 12(6) identity query may suspend the response period only while necessary information is outstanding.

2. **Extension is +2 months, declared within the first month, with reasons** (Art. 12(3)) — only for complexity or number of requests. An extension declared late is a violation, not an extension.

3. **Motive is irrelevant — but abuse is a real limit.** A legitimate non-privacy purpose (preparing litigation, fee-checking) never justifies refusal (CJEU C-307/22 *FT*, 26 Oct 2023) — never reason from "why they are asking" to "whether to comply". Distinct from that: even a *first* request may be refused as excessive where the controller demonstrates it was made not to check processing but to **manufacture an Art. 82 damages claim** (CJEU C-526/24 *Brillen Rottler*, 19 Mar 2026 — indicators: data volunteered shortly before, timing, serial request-and-sue patterns; burden on the controller).

4. **First copy is free** (Art. 12(5), 15(3)). A reasonable admin-cost fee applies only to *further* copies or manifestly unfounded/excessive requests. C-307/22: even a first copy of a patient file must be free.

5. **Recipients must be named specifically on request** (CJEU C-154/21 *Österreichische Post*, 12 Jan 2023) — categories suffice only where identification is impossible or the request is manifestly unfounded/excessive. Default to naming actual recipients.

6. **"Copy" means faithful, intelligible reproduction of the personal data** (CJEU C-487/21, 4 May 2023) — including document extracts, entire documents, or database extracts where that is **essential to enable the data subject to exercise their rights effectively** (the operative test; unintelligibility without context is the usual reason), taking the rights of others into account — but it is not a general right to whole documents or file copies.

7. **Identity verification must be proportionate** (Art. 12(6), EDPB 01/2022): "reasonable doubts" is the standard. Do not demand ID-card copies by default — use the existing authentication channel (account login, known email). Data collected for verification is purpose-bound and minimal.

8. **"Manifestly unfounded or excessive" is a high bar with the burden on the controller** (Art. 12(5)). Repetition is judged against "reasonable intervals" (Recital 63) relative to how often the data changes — but repetition is not the only route: an abusive first request can be excessive (C-526/24, see point 3). Broad scope alone is NOT excessive — ask the data subject to specify (EDPB 01/2022) but the full request stands if they decline. (SA-side parallel: complaint volume alone never suffices; abusive intent must be established — C-416/23.)

9. **Erasure is conditional, not absolute.** Test an Art. 17(1) ground first, THEN Art. 17(3) exceptions. Statutory retention defeats erasure only for the covered records and period under Art. 17(3)(b). Keep those records separated from ordinary operational use through purpose limitation, access controls, and a scheduled deletion date. Do not label this an Art. 18 restriction unless an independent Art. 18(1) ground applies; BDSG § 35(3) concerns by-laws-based or contractual, not statutory, retention periods.

10. **Erasure reaches backups, but staged deletion is defensible** if the backup cycle is documented, the data is restored-then-deleted (or deletion is re-applied on restore), and the data is not otherwise processed in the meantime (DSK practice). Say "deleted from live systems, expiring from backups by [date]" — never silently ignore backups.

11. **Downstream duties are part of erasure/rectification, not optional extras.** Art. 19: notify each recipient unless impossible or disproportionate effort, and tell the data subject about those recipients on request. Art. 17(2) (data made public): reasonable steps to inform other controllers, including search engines; consent withdrawal propagates (CJEU C-129/21 *Proximus*, 27 Oct 2022).

12. **Direct-marketing objection is absolute** (Art. 21(2)–(3)) — no balancing, includes related profiling, effective immediately. A general Art. 21(1) objection reverses the burden: the CONTROLLER must demonstrate *compelling* legitimate grounds overriding the data subject — stricter than the original Art. 6(1)(f) balance. For that re-balancing, run the `legitimate-interest` skill.

13. **Portability ≠ access.** Art. 20 covers only data *provided by* the data subject (including observed data — usage logs, device data — per WP242 rev.01, but NOT derived/inferred data like scores or profiles), processed by automated means, on consent or contract legal bases only. It does not oblige the controller to adopt compatible systems, and transmission direct-to-another-controller only "where technically feasible".

14. **Art. 22 is a prohibition-style right, and scoring can itself be the decision** (CJEU C-634/21 *SCHUFA*, 7 Dec 2023): where a third party's decision draws strongly on an automated score, the scoring falls under Art. 22. Check the Art. 22(2) exceptions and 22(3) safeguards (human intervention, right to contest) — "a human clicked approve" is not meaningful human involvement if they routinely rubber-stamp.

15. **Third-party data inside a response is a redaction problem, not a refusal ground** (Art. 15(4)). Rights of others justify targeted redaction (other individuals in emails, trade secrets in scoring logic) — never blanket denial. For log/consultation data: operations on the data subject's file (dates, purposes) are their personal data, but the identity of the employees who accessed it generally is not (CJEU C-579/21 *Pankki S*, 22 June 2023).

## Pending Legislation — Digital Omnibus (NOT law)

The Commission's Digital Omnibus proposal (procedure 2025/0360(COD)) would amend the GDPR, including Art. 12(5) and Art. 22. **Apply current law; flag the proposal in one sentence where relevant; never blend proposed text into the analysis.** Status, DSR-relevant items, and what's untouched: `references/pending-legislation.md` (covered by `sources.lock.json`, so SRC-1 freshness applies to it like every other reference file).

## Sibling Skill Handoffs

- **Locating the data:** the `ropa` skill's Art. 30 register (and its JSON sidecar) is the authoritative inventory of where personal data lives — use it to scope access/erasure responses instead of guessing at systems.
- **Art. 21(1) objection balancing:** run the `legitimate-interest` skill for the compelling-grounds re-assessment.
- **Processor-side requests:** a processor receiving a DSR must route it to the controller without undue delay and assist per Art. 28(3)(e) — the `dpa-art28` skill covers the contractual assistance clause.
- **Notice accuracy:** if handling a request reveals the privacy notice omitted the processing, flag it and reference the `privacy-notice-eu` skill.

## Output Formats

**Triage verdict:** right(s) invoked, deadline date (computed), identity-verification stance, and a numbered action plan.

For every Art. 15 triage—even where the question focuses only on deadlines, recipients, or identity—the final response must affirmatively state that the controller must provide all Art. 15(1)(a)–(h) meta-information (including purposes, data categories, recipients, retention, source, rights, complaint rights, and automated-decision information) and that the first copy is free.

**Response letters:** grant / partial grant with redaction reasoning / reasoned refusal / extension notice — bilingual EN/DE structures in `references/templates.md`. For .docx deliverables, read the docx skill first.

**DSR register entry:** every request gets a log row (schema in `references/templates.md`) — request date, right(s), identity check, deadline, extension, outcome, downstream notifications. Accountability (Art. 5(2)) means the file must show WHY a refusal or redaction was justified.

## Machine-readable output

For a triage this skill has scored, write the native sidecar (schema:
`references/dsr-sidecar-schema.json`) and validate it:

```bash
uv run skills/data-subject-rights/validator/validate.py <sidecar.json>
```

Add `--emit-core-artefact <path>` to also write the portfolio core-artefact
projection (`skill-artefact-1.1` shape) for handoff to another skill or tool.
This is a **structural**-tier validator (schema conformance + a handful of
consequential-input rules — see `conformance.json`), not a full legal rule
engine; it does not replace the judgement calls in the Assessment Flow above.
**A validator pass means the sidecar is internally consistent and complete
against its own schema and the rules above — it is not a statement that the
underlying legal analysis (which right applies, whether a ground or
exception is correctly identified) is correct.**

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
