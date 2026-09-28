# Right to Erasure — Art. 17 GDPR (deep track)

Primary sources: Art. 17, 18, 19; CJEU C-131/12 (Google Spain), C-136/17 (GC and Others), C-460/20 (Google/inaccuracy), C-129/21 (Proximus), C-26/22 & C-64/22 (SCHUFA insolvency); EDPB Guidelines 5/2019 (RTBF in search engines).

## Two-step test — always in this order

**Step 1 — Is there an Art. 17(1) ground?**

| Ground | Typical scenario |
|---|---|
| (a) No longer necessary for the purposes | Retention period expired; account closed and no residual purpose |
| (b) Consent withdrawn, no other basis | Newsletter, optional profile fields |
| (c) Art. 21(1) objection and no overriding grounds / Art. 21(2) objection | Marketing data always; LI-based processing after failed re-balancing |
| (d) Unlawful processing | No valid basis from the start |
| (e) Legal obligation to erase | Sector law |
| (f) Child's information-society-services data | — |

No ground → no erasure duty (refuse with reasons; consider whether rectification/restriction fits instead).

**Step 2 — Does an Art. 17(3) exception defeat it?**

| Exception | Typical scenario |
|---|---|
| (a) Freedom of expression and information | Press archives, review platforms |
| (b) **Legal obligation** / public task | **Statutory retention: DE — AO § 147 / HGB § 257: books & annual accounts 10 yrs; Buchungsbelege incl. invoices 8 yrs (10→8 per BEG IV from 1.1.2025; banks/insurers/Wertpapierinstitute stay at 10 yrs); commercial letters 6 yrs — table in `restrictions-overlays.md`; payroll, AML/KYC** |
| (c) Public health | — |
| (d) Archiving/research/statistics (Art. 89(1)) | If erasure would render the purpose impossible |
| (e) Legal claims | Ongoing or concretely anticipated litigation — not a blanket "we might be sued someday" |

**Partial disposition is the norm:** the exception protects only the records and period it actually covers. Correct answer to "delete my customer account" with open invoices: erase marketing and profile data now; retain the invoice-relevant records under Art. 17(3)(b), separated from ordinary operational use through purpose limitation and access controls, with a scheduled deletion date. Do not label statutory retention an Art. 18 restriction unless an independent Art. 18(1) ground applies. State the concrete expiry.

## Backups and technical reality

- Erasure covers backups, but **staged deletion is defensible** (DSK practice): document the backup rotation, guarantee deletion-on-restore, do not otherwise process the data, and tell the data subject: "erased from live systems as of [date]; backup copies expire by [date] and are protected against restoration into use."
- "Deletion" does not mandate physical destruction where impossible (e.g. WORM storage, blockchain): rendering the data permanently unusable/inaccessible (crypto-shredding, key destruction) is the accepted equivalent — document the method.
- Erasure from search indexes and caches of the controller's own systems is part of the job; third-party search engines are an Art. 17(2) matter, below.

## Downstream duties — never skip

1. **Art. 19 notification:** tell **each recipient** (processors AND independent recipients — pull the list from the `ropa` register) about the erasure/rectification/restriction, unless impossible or disproportionate effort (document the assessment). On request, tell the data subject who was notified.
2. **Art. 17(2) — data made public:** take reasonable steps (technology and cost considered) to inform other controllers processing the published data, including link/copy/replication removal requests. Consent withdrawal propagates (C-129/21 *Proximus*, 27 Oct 2022 — directory data): informing third-party controllers rests on accountability (Arts. 5(2), 24); informing search engines is the Art. 17(2) "reasonable steps" standard.
3. **Processors:** instruct erasure under the DPA (Art. 28(3)(g)); collect confirmation.

## Delisting (search-engine RTBF) — only when the user IS or faces a search engine

- Balancing framework from C-131/12 as refined by C-136/17 (special-category data: stricter necessity test) and EDPB 5/2019.
- **Inaccuracy claims** (C-460/20, 8 Dec 2022): the requester must provide **relevant and sufficient evidence** of manifest inaccuracy — only what can reasonably be required; no court judgment against the publisher may be demanded. Where manifest inaccuracy is not evident from that evidence, the operator need not delist absent a judicial decision.
- Geographic scope (C-507/17 *Google/CNIL*, 24 Sep 2019): delisting on all EU Member State versions, plus measures that effectively prevent or at least seriously discourage EU access via other versions. Global delisting is not required by EU law but not precluded — an SA/court may order it after balancing under national fundamental-rights standards.

## Credit agencies / registers (C-26/22 & C-64/22 SCHUFA)

Parallel retention of public-register data (e.g. insolvency discharge) beyond the public register's own deletion deadline is unlawful — private-sector mirrors cannot out-retain the official source. Pattern to generalize: **when the authoritative source must delete, downstream replicas lose their basis.**

## Boundaries and platform cases (2025)

- **Erasure ≠ injunction:** Art. 17/18 (with Art. 79) confer no self-standing GDPR right to a *preventive* prohibition of future processing — national law may provide injunctive relief alongside (CJEU C-655/23 *Quirin Privatbank*, 4 Sep 2025). Frame forward-looking demands accordingly.
- **Platforms hosting user content:** a marketplace/portal operator is (joint) controller of personal data in user-posted ads and cannot invoke the e-Commerce hosting exemption against GDPR duties; Arts. 24/32 require measures (pre-publication checks for sensitive data, safeguards against copying/republication) precisely so that erasure is not defeated by mirror-site spread (CJEU C-492/23 *Russmedia*, GC, 2 Dec 2025).
- Enforcement climate: the EDPB's 2025 coordinated enforcement action on Art. 17 (report adopted 18 Feb 2026) flags retention periods, backup handling, and conditions imposed on exercising the right as the recurring failure points — the exact areas this file addresses.

## Refusal drafting

A lawful refusal states: the ground examined, why it fails (or which exception prevails), the partial measures taken instead (including purpose limitation and access controls for retained records, or a formal restriction where independently grounded), the expiry of any retention, and the Art. 12(4) remedies notice (SA complaint, judicial remedy). Template in `templates.md`.
