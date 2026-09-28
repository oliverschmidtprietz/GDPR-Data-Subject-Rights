# Right of Access — Art. 15 GDPR (deep track)

Primary sources: Art. 15; EDPB Guidelines 01/2022 on data subject rights — right of access (v2.1, adopted 28 Mar 2023, minor corrections 30 May 2024); CJEU C-154/21, C-487/21, C-307/22, C-579/21.

## The three layers of Art. 15

1. **Confirmation** whether personal data are processed at all (Art. 15(1) first limb) — even a "no data" answer is mandatory and deadline-bound.
2. **Access to the personal data themselves** plus the Art. 15(1)(a)-(h) meta-information (purposes, categories, recipients, retention, rights, source, automated decision-making incl. meaningful logic).
3. **A copy** of the personal data undergoing processing (Art. 15(3)) — free the first time.

Answer all three layers; a common failure is sending the copy but omitting the meta-information (or vice versa).

## Scope of "personal data" in the response

- Everything relating to the identified person: master data, communications content ABOUT the person, notes, scores, interaction logs, inferences and derived data (the assessment relates to the person even if the algorithm is proprietary).
- **Pseudonymised data** the controller can re-link: in scope. Identifiability is contextual per actor (CJEU C-413/23 P *EDPS v SRB*, GC, 4 Sep 2025): data a *recipient* has no reasonable means to re-identify may not be personal data in that recipient's hands — but the controller's own duties (including naming that recipient) are assessed from the controller's perspective. Opinions and comments expressed by a person are their personal data.
- **Consultation/audit logs**: the operations performed on the data subject's file (dates, purposes of access) are the data subject's personal data; the **identities of the employees** who performed them generally are not — disclose those only where essential for the data subject to exercise rights effectively, balanced against those employees' rights (CJEU C-579/21 *Pankki S*, 22 June 2023).
- Anonymous or aggregate data: out of scope. Data about other people mentioned alongside: Art. 15(4) redaction, below.

## "Copy" (Art. 15(3)) — C-487/21

A **faithful and intelligible reproduction** of all the personal data. This can require extracts of documents, entire documents, or database extracts where that is **essential to enable the data subject to exercise their GDPR rights effectively** (the operative test; unintelligibility without context — field labels, code translations — is the usual way a bare export fails it), always taking the rights and freedoms of others into account — but it is not a general right to documents. Practical rule: export the data; attach source documents where the data cannot be understood, or the rights not exercised, without them.

## Recipients (Art. 15(1)(c)) — C-154/21

On request, name **the actual recipients**, not just categories. Categories suffice only where (a) it is impossible to identify the recipients (e.g. future recipients not yet determined), or (b) the request is manifestly unfounded/excessive. Cross-check the `ropa` register's recipient column — it is the natural source for this list.

## Meaningful information about automated decision-making (Art. 15(1)(h))

For Art. 22-relevant processing: explain the **procedure and principles actually applied** to reach the specific result, in a concise, transparent, intelligible form a lay person can understand (CJEU C-203/22 *Dun & Bradstreet*, 27 Feb 2025). Neither an algorithm/mathematical formula nor a description of every processing step satisfies this — one workable technique the Court named is showing how a variation in the input data would have changed the result. Trade-secret protection justifies limiting detail, not refusing: the controller provides the allegedly protected information to the SA or court, which balances and determines the extent of access (see also C-634/21 *SCHUFA* on scoring).

## Rights of others (Art. 15(4))

The copy must not adversely affect the rights and freedoms of others — trade secrets, IP, and other individuals' data. This justifies **targeted redaction and abstraction, never blanket refusal**. Typical handling:
- Emails where the data subject is one of several people: redact the others' content, keep what relates to the requester.
- Whistleblower/complainant identities: redact; note the redaction and its ground in the response.
- Scoring logic: explain the procedure and principles actually applied to the specific result in an intelligible form; a counterfactual input variation may help. Do not promise factors, weights, formulas, or source code as categorical disclosure items.

## Practical mechanics for large holdings

- **Ask to specify** (EDPB 01/2022 ¶35) when holdings are extensive — offer a menu of processing areas. If the data subject insists on everything, everything it is.
- **Search obligation** covers all systems including archives and unstructured stores the controller actually operates (email, tickets, CRM, HR files); disproportionate-effort arguments shrink the *form* of the response, not the search itself. Use the `ropa` register to enumerate systems.
- **Layered response** is good practice: a readable summary letter + structured annexes per system.

## Employee access requests

Fully covered by Art. 15 — including performance notes, investigation files (subject to Art. 15(4) and, in Germany, § 34 BDSG — see `restrictions-overlays.md`). German labour-court practice (e.g. BAG 2 AZR 342/20, 27 Apr 2021) rejects blanket "give me all emails" claims that are too indeterminate to enforce procedurally — but this affects enforceability of sweeping court motions, not the underlying GDPR duty to run a proper search against a concrete request. Handle via the specify-mechanism, not refusal.

## Access response checklist

- [ ] Confirmation statement (or "no data" verdict)
- [ ] All Art. 15(1)(a)-(h) meta-information, per processing purpose
- [ ] Named recipients (or documented impossibility)
- [ ] Copy of the data, intelligible, with code/field translations
- [ ] Redactions logged with grounds (Art. 15(4))
- [ ] Retention periods or criteria per category
- [ ] Source information for non-directly-collected data (Art. 15(1)(g))
- [ ] Safeguards reference for third-country transfers (Art. 15(2)) — link to the `tia` skill's output where one exists
- [ ] Rights reminder (rectification, erasure, restriction, objection, SA complaint)
- [ ] Deadline met / extension was declared in month one
