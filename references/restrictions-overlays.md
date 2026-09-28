# National Restrictions and Overlays — Art. 23 GDPR

Art. 23 lets Union/Member State law restrict Arts. 12-22 for listed objectives (national security, crime, others' rights...), by measures respecting essence and proportionality. Always check the controller's Member State law — this file covers Germany in depth; for other jurisdictions, flag the existence of Art. 23 measures and recommend local counsel.

## Germany — BDSG restrictions (most litigated in practice)

### § 34 BDSG — access restrictions

Access (Art. 15) does not apply where:
1. **§ 34(1) Nr. 1** — the data subject is not owed notification under the § 33 cases (pure cross-reference to the information-duty exceptions).
2. **§ 34(1) Nr. 2** — the data **(a)** are stored only because statutory or charter-based (satzungsmäßige) retention rules bar deletion, or **(b)** serve exclusively data-security or data-protection-control purposes — AND (both limbs, cumulative) access would require disproportionate effort AND processing for other purposes is excluded by appropriate technical/organisational measures. The classic case: data kept ONLY because AO/HGB force it, locked from operational use.

Strict reading required: these are narrow and the controller carries the burden; grounds must be documented and the data subject told the reasons, unless stating them would defeat the refusal's purpose (§ 34(2)). **§ 34(3) (Auskunft via the BfDI instead) applies only against federal public bodies** — against private controllers the data subject's route is the ordinary Art. 77 complaint to the competent SA.

### § 35 BDSG — erasure restrictions

- **§ 35(1)**: where **non-automated** processing makes erasure impossible or disproportionately costly and the data subject's interest in erasure is low, restriction (Art. 18) replaces erasure — narrow, mostly paper archives; NOT available where the processing was unlawful (§ 35(1) S. 3).
- **§ 35(2)**: restriction instead of erasure also where erasure would impair the data subject's OWN legitimate interests (protective, Art. 17(1)(a)/(d) cases).
- **§ 35(3)**: concerns **satzungsgemäße (articles/by-laws-based) or contractual**, not statutory, retention periods and provides restriction instead of erasure for those periods. Statutory retention defeats erasure directly via Art. 17(3)(b) GDPR.

### Employment context (§ 26 BDSG + labour case law)

- Employee DSRs are normal DSRs — no HR exception. Sensitive spots: investigation files (Art. 15(4) redaction of witnesses/whistleblowers), performance data, works-council documents (co-determination context).
- § 26 BDSG status (verified 2026-07): unchanged and in force; the planned Beschäftigtendatengesetz never left draft stage. But CJEU C-34/21 (30 Mar 2023) makes reliance on the § 26(1) general clause doubtful (Art. 88(2) deficit — practice increasingly grounds HR processing on Art. 6(1)(b)/(f) directly), and C-65/23 (19 Dec 2024) holds works agreements (§ 26(4)) must themselves comply with Arts. 5, 6(1), 9 GDPR under full judicial review — a Betriebsvereinbarung is no safe harbour.
- BAG 2 AZR 342/20 (27 Apr 2021): sweeping court motions for "copies of all emails" can fail procedural specificity — handle DSAR breadth via the EDPB specify-mechanism, not refusal.
- LAG damages practice under Art. 82 for late/incomplete DSAR responses is active; deadline discipline matters financially in Germany. CJEU C-300/21 (Österreichische Post, 4 May 2023): mere infringement is not damage — but actual non-material damage has **no de-minimis threshold**. Refinements: loss of control, uncertainty, and fear of future misuse can themselves be non-material damage if proven concretely (C-340/21; C-200/23; C-526/24); compensation is purely compensatory — degree of fault irrelevant to quantum (C-655/23); no compensation where the data subject's own conduct is the determining cause of the damage (C-526/24).

### Retention anchors

Verified against current statute text 2026-07-07 (see `sources/verification-log.md`).

| Records | Period | Source |
|---|---|---|
| Books/records, inventories, annual accounts, management reports (Bücher, Jahresabschlüsse) | 10 yrs | AO § 147(1) Nr. 1, 4a + (3); HGB § 257(1) Nr. 1 + (4) |
| Accounting documents incl. invoice copies (Buchungsbelege, Rechnungen) | 8 yrs (10→8 per BEG IV, from 1.1.2025 for periods not yet expired 31.12.2024). **Exception:** credit institutions (§ 1(1b) KWG), VAG-supervised insurers, and Wertpapierinstitute (§ 2(1) WpIG) stay at 10 yrs (Art. 97 § 19a(3) EGAO / HGB § 257(4) S. 2, since 30.12.2025) — their pure UStG invoice duty is nonetheless 8 yrs | AO § 147(1) Nr. 4 + (3); HGB § 257(1) Nr. 4 + (4); UStG § 14b(1) |
| Commercial/business letters | 6 yrs | HGB § 257(1) Nr. 2-3; AO § 147(1) Nr. 2-3 |
| Payroll: Lohnkonto | 6 yrs from end of the calendar year of the last recorded wage payment | EStG § 41(1) |
| AML/KYC records | 5 yrs; hard destruction ceiling 10 yrs | GwG § 8(4) |
| Application/rejection documents | ~6 months practice = 2-month assertion window (AGG § 15(4)) + 3-month Klagefrist (ArbGG § 61b(1)) + service buffer | AGG/ArbGG-driven practice |

AO § 147(3) S. 5 Ablaufhemmung: the period does not expire while the documents remain relevant for taxes whose Festsetzungsfrist is still open — state this when computing concrete expiry dates.

Rule of application: statutory retention defeats erasure **only for the covered records and period** under Art. 17(3)(b). Keep those records separated from ordinary operational use through purpose limitation, access controls, and a scheduled deletion date. Do not label this an Art. 18 restriction unless an independent Art. 18(1) ground applies. BDSG § 35(3) is confined to by-laws-based or contractual retention periods. Never use retention as a blanket "we keep everything 10 years" justification.

## Other jurisdictions — flag-level notes

- **Austria**: DSG § 4(5)-(6) (access refusal for business secrets is NOT a blanket ground — CJEU C-203/22 confirms explanation duty stands).
- **France**: CNIL enforces DSAR deadlines actively; Code du travail overlays for employee monitoring data.
- **Ireland**: DPA 2018 ss. 59-61 (legal privilege, opinions given in confidence).
- General rule: privilege, whistleblower-protection, and criminal-procedure laws commonly restrict Art. 15 — ask which sector/jurisdiction before finalising a refusal.
