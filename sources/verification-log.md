# Verification Log — data-subject-rights

Legal verification pass required before v1.0 (HANDOFF item 0, 2026-07-07). Every load-bearing claim in SKILL.md and references/ was live-checked against primary sources. This log records: claim → verdict → what the source actually says → source + access date.

**Method:** five parallel research clusters (CJEU case law; EDPB guidance; German statute law; Digital Omnibus impact; post-cutoff CJEU sweep), primary sources only (curia.europa.eu, eur-lex.europa.eu, edpb.europa.eu, gesetze-im-internet.de), secondary commentary as corroboration only. All URLs accessed 2026-07-07.

**Verdict scale:** CONFIRMED (claim accurate as written) · NEEDS-NUANCE (accurate but incomplete/imprecise — skill text adjusted) · INCORRECT (wrong — skill text corrected) · OUTDATED (was right, law/guidance moved).

**Re-run rule:** before any future version bump that touches legal content, re-check the items marked ⏳ watch and the Digital Omnibus status.

## Correction — propagation reconciliation (2026-07-12)

The 2026-07-07 verification identified the correct channel, statutory-retention, and C-203/22 rules, but those conclusions were not fully propagated to the orchestrator, references, templates, deployment guide, and evaluation contract. This correction reconciled `SKILL.md`, `references/procedural-framework.md`, `references/art15-access.md`, `references/art17-erasure.md`, `references/other-rights.md`, `references/restrictions-overlays.md`, `references/templates.md`, `README.md`, and `evals/evals.json`. The original verification entries below are preserved as the historical record; this note supersedes their earlier “fixed” status where the deployed wording remained stale.

---

## Cluster 2 — EDPB / WP29 guidance (verified 2026-07-07)

### 2.1 Guidelines 01/2022 citation — NEEDS-NUANCE (fixed)

- Skill claimed: "EDPB Guidelines 01/2022 on data subject rights — right of access (v2.0, adopted 28 Mar 2023)".
- Actual: current version is **v2.1, 30 May 2024** ("minor corrections"; substantively identical). v2.0 was adopted 28 Mar 2023 after consultation. No v3.0 or replacement exists as of 2026-07-07; the September 2025 "how to implement it" leaflet is non-normative.
- Fix applied: citation updated to v2.1 in `references/art15-access.md`.
- Source: https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-012022-data-subject-rights-right-access_en

### 2.2 Paragraph citations ¶35 / ¶52-57 / ¶64-79 — CONFIRMED

- ¶35: large holdings → controller may ask to specify; request read in general terms by default; if data subject insists, full scope stands. Exactly as skill states.
- ¶52-57: requests form-free, any channel the controller provides is effective (Example 8: general contact email instead of DPO inbox — no deadline extension), ¶57 receipt starts the one-month period.
- ¶64-79: reasonable-doubts standard (¶70), existing authentication channel first (¶66, ¶72-73), ID copies generally inappropriate/last resort with redaction and post-verification deletion (¶74-79), verification data strictly purpose-bound (¶65).
- Source: https://www.edpb.europa.eu/system/files/2023-04/edpb_guidelines_202201_data_subject_rights_access_v2_en.pdf (serves v2.1 text)

### 2.3 "Wrong channel still counts" — NEEDS-NUANCE (fixed)

- Skill claimed (procedural-framework.md): any channel counts; "internal routing delay is the controller's risk".
- Actual (¶54-55): correct for channels the controller itself provides — but the controller is "not obliged to act on a request sent to a random or incorrect e-mail (or postal) address, not directly provided by the controller, or to any communication channel that is clearly not intended to receive requests" (Example 9: cleaning-staff email), provided an appropriate channel was clearly communicated.
- Fix applied: qualifier added to `references/procedural-framework.md`.
- Source: Guidelines 01/2022 v2.1 ¶52-57.

### 2.4 Deadline counting per Reg. 1182/71 — CONFIRMED

- Section 5.3 ¶159-161 + Examples 32-33 confirm all three rules: same-date-next-month (received 5 Mar → due 5 Apr incl.; skill's "17 Mar → 17 Apr" analogous, no off-by-one), no-such-date → last day of following month (31 Aug → 30 Sep), weekend/public holiday → next working day.
- ¶159 also: clock starts when the request reaches an official channel (controller awareness not required); time may be suspended while identity verification or specification is pending IF the controller asked without undue delay — consistent with the skill's "only a genuine Art. 12(6) doubt raised promptly can defer".
- Source: Guidelines 01/2022 v2.1 ¶157-164.

### 2.5 Guidelines 5/2019 (RTBF) — CONFIRMED

- Full title includes "(part 1)"; final v2.0 adopted 7 Jul 2020; still current, never replaced. Announced part 2 (delisting exceptions) was never published.
- Source: https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-52019-criteria-right-be-forgotten-search-engines_en

### 2.6 WP242 rev.01 portability — CONFIRMED

- Still the operative Art. 20 guidance (on the EDPB Endorsed WP29 Guidelines list; cited by Guidelines 01/2022 itself). Provided = declared + observed (search history, traffic/location, wearable/smart-meter raw data, activity logs); derived/inferred (credit scores, risk profiles, health assessments) out of scope — verbatim match with the skill.
- Context note: since 12 Sep 2025 the EU Data Act provides a parallel non-GDPR portability regime for connected-product data.
- Sources: https://www.edpb.europa.eu/our-work-tools/general-guidance/endorsed-wp29-guidelines_en; https://ec.europa.eu/newsroom/document.cfm?doc_id=44099

### 2.7 Post-Jan-2026 EDPB sweep — no new DSR guidelines; three relevant documents

- No new/revised guidelines on Arts. 12/15/16/17/20/21/22 adopted Jan–Jul 2026; Guidelines 01/2022 untouched.
- **CEF 2025 erasure report** (adopted 18 Feb 2026): enforcement findings from 32 DPAs on Art. 17 practice (retention periods, backups, exercise conditions). https://www.edpb.europa.eu/our-work-tools/our-documents/other/coordinated-enforcement-action-implementation-right-erasure_en
- **OSS case digest on objection + erasure** (updated 25 Jun 2026): synthesis of one-stop-shop decisions on Arts. 17/21. https://www.edpb.europa.eu/news/news/2026/one-stop-shop-case-digest-right-object-and-right-erasure-updated_en
- Guidelines 1/2026 (scientific research, Art. 89 restrictions on DSRs): draft only, consultation closed 25 Jun 2026. ⏳ watch
- Guidelines 01/2025 (pseudonymisation) and 3/2025 (DSA-GDPR): not finally adopted as of 2026-07-07. ⏳ watch
- 2026 CEF topic is transparency (Arts. 12-14) — expect activity later in 2026. ⏳ watch
- EDPB-EDPS Joint Opinion 2/2026 (Feb 2026) on the Digital Omnibus — see Cluster 4.

---

## Cluster 1 — CJEU case law, 14 cited cases (verified 2026-07-07)

All 14 verified against the full EN judgment texts on EUR-Lex (CELEX), C-526/24 against CURIA press release 38/26, BAG against bundesarbeitsgericht.de. **All case numbers, party names, and dates are real and correct.** No fabricated holding found. Verdicts:

| Case | Verdict | Note |
|---|---|---|
| C-154/21 *Österreichische Post* (recipients), 12 Jan 2023 | CONFIRMED | Operative part matches skill near-verbatim, incl. both exceptions |
| C-487/21 (copy), 4 May 2023 | NEEDS-NUANCE → fixed | Operative test is "essential to enable effective exercise of rights", not "necessary for intelligibility" (intelligibility is the reasoning route, ¶41-45); rights-of-others caveat express. SKILL.md pt 6 + art15-access.md corrected |
| C-307/22 *FT*, 26 Oct 2023 | CONFIRMED | Free first copy + motive-irrelevance verbatim (¶38, 43); now qualified by C-526/24 abuse doctrine (Cluster 5) — reconciled in SKILL.md pt 3 |
| C-579/21 *Pankki S*, 22 Jun 2023 | CONFIRMED (framing nuance) | Date added to skill. Operative part frames log data as "information the person has the right to obtain" (Art. 15(1)) rather than expressly "their personal data" — skill shorthand defensible from ¶73-76, kept |
| C-634/21 *SCHUFA* (scoring), 7 Dec 2023 | CONFIRMED | "Draws strongly" condition correctly reproduced; formal name OQ v Land Hessen |
| C-26/22 & C-64/22 (insolvency), 7 Dec 2023 | CONFIRMED | Retention beyond public-register period precluded (op. pt 2) |
| C-129/21 *Proximus*, 27 Oct 2022 | NEEDS-NUANCE → fixed | Two duties differ: informing third-party controllers rests on Arts. 5(2)/24 accountability; informing search engines is Art. 17(2) "reasonable steps". art17-erasure.md corrected; date added |
| C-460/20 (delisting/inaccuracy), 8 Dec 2022 | CONFIRMED (+ addition) | "Relevant and sufficient evidence"/no-court-judgment verbatim (¶68, 72); added ¶73 limit (not-obvious inaccuracy → no delisting absent judicial decision) |
| C-507/17 *Google/CNIL*, 24 Sep 2019 | CONFIRMED (+ precision) | Added: all-EU-versions + geo-measures that "effectively prevent or seriously discourage" EU access; global balancing under national fundamental-rights standards |
| C-203/22 *Dun & Bradstreet*, 27 Feb 2025 | NEEDS-NUANCE → fixed | Operative wording: "procedure and principles actually applied", concise/intelligible; algorithm/formula neither required nor sufficient (¶59); counterfactual-variation technique (¶62). Skill's "factors and weights" over-specified — corrected in art15-access.md + other-rights.md. Trade-secret mechanism (disclose to SA/court, which balances) confirmed verbatim |
| C-300/21 (Art. 82), 4 May 2023 | CONFIRMED | Both propositions exactly match op. pts 1-2 |
| C-131/12 *Google Spain*, 13 May 2014 | CONFIRMED | Baseline framework intact |
| C-136/17 *GC and Others*, 24 Sep 2019 | CONFIRMED | "Strictly necessary" test for special-category delisting confirmed |
| BAG 2 AZR 342/20, 27 Apr 2021 | CONFIRMED | Procedural (§ 253(2) Nr. 2 ZPO specificity) holding; substantive Art. 15(3) scope expressly left open — skill's framing already says this |

Later developments on the Art. 82 line (log-only): C-340/21 (fear of future misuse), C-456/22 *Ummendorf* (no de-minimis reaffirmed), C-200/23 (temporary loss of control may suffice), German BGH VI ZR 10/24 (18 Nov 2024, loss of control as such) with a 2025 LG Erfurt CJEU referral pending. ⏳ watch
Sources: EUR-Lex CELEX 62021CJ0154, 62021CJ0487, 62022CJ0307, 62021CJ0579, 62021CJ0634, 62022CJ0026, 62021CJ0129, 62020CJ0460, 62017CJ0507, 62022CJ0203, 62021CJ0300, 62012CJ0131, 62017CJ0136; https://www.bundesarbeitsgericht.de/entscheidung/2-azr-342-20/

## Cluster 3 — German statute law (verified 2026-07-07, gesetze-im-internet.de current text)

### 3.1 AO § 147 / HGB § 257 / UStG § 14b retention — INCORRECT (fixed; this was the flagged item)

- The skill's "6→8 yrs booking records, 10 yrs ledgers/invoices" was garbled. Correct current law (§ 147(3) S. 1 AO; § 257(4) HGB): **books/records, inventories, annual accounts 10 yrs; Buchungsbelege 8 yrs (BEG IV shortened 10→8, in force 1.1.2025, for periods not expired 31.12.2024 — Art. 97 § 19a(2) EGAO); commercial/business letters and sonstige Unterlagen 6 yrs.**
- **Financial-sector reversal (post-cutoff statute):** the Gesetz zur Modernisierung und Digitalisierung der Schwarzarbeitsbekämpfung (BGBl. 2025 I Nr. 369, in force 30.12.2025) converted BEG IV's one-year deferral for the financial sector into a permanent carve-out: credit institutions (§ 1(1b) KWG), VAG-supervised insurers, and Wertpapierinstitute (§ 2(1) WpIG) **stay at 10 yrs for Buchungsbelege** (Art. 97 § 19a(3) EGAO: § 147(3) S. 1 AO in the version of 31.12.2024 continues to apply; parallel sentence inserted in § 257(4) HGB).
- UStG § 14b(1): invoices **8 yrs** — CONFIRMED; the reversal did NOT amend the UStG, so the pure VAT duty is 8 yrs for everyone since 1.1.2026 — but invoices that are simultaneously Buchungsbelege (the normal case) remain at 10 yrs in the financial sector via AO/HGB.
- Ablaufhemmung: § 147(3) S. 5 AO — period suspended while the tax Festsetzungsfrist is open. Added to the skill's table.
- Fixed in: art17-erasure.md Step-2 table, restrictions-overlays.md retention table (verify-hedges removed — settled law as of Jul 2026).
- Sources: https://www.gesetze-im-internet.de/ao_1977/__147.html; https://www.gesetze-im-internet.de/aoeg_1977/art_97__19a.html; https://www.gesetze-im-internet.de/hgb/__257.html; https://www.gesetze-im-internet.de/ustg_1980/__14b.html; https://www.gesetze-im-internet.de/ustg_1980/__27.html

### 3.2 § 34 BDSG — NEEDS-NUANCE (fixed)

- Actual structure: § 34(1) **Nr. 1** is solely the § 33 cross-reference (no-notification cases); **Nr. 2** holds both storage limbs as (a) retention-rule-only storage / (b) exclusive data-security or DP-control purposes, with the disproportionate-effort + TOM conditions applying cumulatively to both. Skill had presented the limbs as Nr. 1 vs Nr. 2 — corrected.
- § 34(2) confirmed (document grounds; reason the refusal unless that defeats its purpose). **§ 34(3) applies only against federal public bodies** (Auskunft via the BfDI) — the skill's generalized "route access via the SA" was wrong for private controllers (their route: ordinary Art. 77 complaint) — corrected.
- The draft 1. BDSG-ÄndG (2024, trade-secrets ground for § 34(1)) lapsed with the coalition collapse; § 34 unchanged as of 2026-07-07.
- Source: https://www.gesetze-im-internet.de/bdsg_2018/__34.html

### 3.3 § 35 BDSG — NEEDS-NUANCE (fixed)

- § 35(1) confirmed (non-automated, disproportionate, low interest → Art. 18 restriction) + added: unavailable where processing was unlawful (S. 3). § 35(2) added (restriction protecting the data subject's own interests).
- **§ 35(3) covers "satzungsgemäße oder vertragliche" (by-laws-based or contractual) retention periods — NOT statutory ones.** Statutory periods defeat erasure directly via Art. 17(3)(b) GDPR. The skill's anchor for the invoice disposition was mis-attributed — corrected.
- Source: https://www.gesetze-im-internet.de/bdsg_2018/__35.html

### 3.4 § 26 BDSG / employment — CONFIRMED in force, caveats added

- Unchanged as of 2026-07-07; Beschäftigtendatengesetz never left draft stage (lapsed by discontinuity, not revived). Caveats added to skill: CJEU C-34/21 (30 Mar 2023) — § 26(1)-type general clauses fail Art. 88(2), practice grounds HR processing on Art. 6(1)(b)/(f); CJEU C-65/23 (19 Dec 2024) — works agreements must themselves comply with Arts. 5/6/9 GDPR, full judicial review.
- Source: https://www.gesetze-im-internet.de/bdsg_2018/__26.html

### 3.5 Other anchors — CONFIRMED with rewording

- EStG § 41(1): Lohnkonto 6 yrs from end of year of last wage entry — CONFIRMED, unchanged by BEG IV.
- GwG § 8(4): 5 yrs; destruction ceiling "spätestens nach zehn Jahren" — reworded from "up to 10 by MS option" to "5 yrs, hard destruction cap 10 yrs". EU AMLR (Reg. 2024/1624) applies only from 10 Jul 2027 — no German change yet. ⏳ watch mid-2027
- AGG § 15(4): assertion deadline is **2 months** (not 6); + § 61b(1) ArbGG 3-month Klagefrist → the "~6 months retention practice" is the correct derived sum; skill table now shows the derivation.
- Sources: https://www.gesetze-im-internet.de/estg/__41.html; https://www.gesetze-im-internet.de/gwg_2017/__8.html; https://www.gesetze-im-internet.de/agg/__15.html; https://www.gesetze-im-internet.de/arbgg/__61b.html

## Cluster 4 — Digital Omnibus × GDPR Arts. 12-23 (verified 2026-07-07)

### 4.1 Correct instrument — HANDOFF's "COM(2025) 833" was the wrong number

- GDPR amendments are **Article 3 of COM(2025) 837 final** ("Digital Omnibus", 19 Nov 2025, procedure **2025/0360(COD)**). The AI companion is COM(2025) 836 (2025/0359(COD)) — **adopted June 2026** (EP plenary 16 Jun, Council 29 Jun 2026), touches GDPR only via special-category/bias provisions, NOT Arts. 12-23. There is no separate GDPR-amending proposal.
- NB for the portfolio: other skills referencing "COM(2025) 833 amends the GDPR" (e.g. eu-data-act's omnibus tracker framing) should be checked against this document split.
- **✅ ACTIONED 2026-07-21 — portfolio-wide correction complete.** Re-verified against EUR-Lex and the EP Legislative Train: the 19 November 2025 package is **COM(2025) 836** (Digital Omnibus on AI, 2025/0359(COD)), **COM(2025) 837** (Digital Omnibus Regulation — data, privacy, cybersecurity; GDPR amendments at Art. 3; 2025/0360(COD)) and **COM(2025) 838** (European Business Wallets). **EUR-Lex holds no `52025PC0833`** — the number was never a real Commission proposal, so the earlier assumption that `eu-data-act`'s use of 833 was correct does not hold either. Corrected in `breach-sentinel` v3.2, `dpia-sentinel` v1.10, `ropa` v2.13, `privacy-notice-eu` v1.4 and `eu-data-act` v1.4 (48 occurrences across 35 files). **This skill owns the fact**; other skills carry a pointer note rather than a duplicate assertion.
- Source: https://www.europarl.europa.eu/RegData/docs_autres_institutions/commission_europeenne/com/2025/0837/COM_COM(2025)0837_EN.pdf

### 4.2 What the tabled text does to DSRs (verbatim-verified from the proposal PDF)

- **Art. 12(5) replaced (Art. 3(4))**: refusal/fee also where, "for requests under Article 15", the data subject "abuses the rights conferred by this regulation for purposes other than the protection of their data"; burden for "excessive" lowered to "reasonable grounds to believe". Recital 35: "overly broad and undifferentiated requests should also be regarded as excessive"; named abuse examples are compensation-extraction and harassment. Deliberate partial reversal of C-307/22; EDPB-EDPS Joint Opinion 2/2026 (10 Feb 2026) objects, urging an abusive-intention test per C-526/24/C-416/23 instead. Commonly misreported as an "Art. 15 amendment" — Art. 15 itself is untouched.
- **Art. 22(1)-(2) rewritten** (permission rule; contract ground applies "regardless of whether the decision could be taken otherwise than by solely automated means"); 22(3)-(4) safeguards remain.
- **Art. 4(1) relative personal-data definition + new Art. 41a** (pseudonymisation implementing acts) — would switch DSRs off entirely for non-identifying entities.
- **Art. 13(4) expanded + new 13(5)** (transparency derogations); **new Arts. 88a/88b/88c** (cookie rules into GDPR; machine-readable consent-refusal and Art. 21(2) objection signals binding on controllers; AI legitimate-interest basis with unconditional right to object).
- **Untouched:** Art. 12(1)-(4), (6)-(8); Arts. 14, 15-21 as written; Art. 23. No change to DSR deadlines.

### 4.3 Status as of 2026-07-07 — ⏳ watch (procedure 2025/0360(COD))

- EP: joint ITRE-LIBE (co-rapporteurs Salla/Kaljurand), committee draft report PE786.818 of 22 Jun 2026; committee vote + plenary ahead.
- Council: no general approach; Cyprus Presidency compromises (Feb-Jun 2026) **delete** the Art. 4(1) redefinition, Art. 41a, the Art. 22 rewrite, and Arts. 88a-c, but **keep the Art. 12(5) abuse ground tightened** to "demonstrated abusive intention" (and drop the lowered proof bar). Coreper deadlock; file handed to the Irish Presidency 1 Jul 2026. Realistic adoption: not before 2027.
- Skill action taken: "Pending Legislation — Digital Omnibus" section added to SKILL.md with the current-law-first output rule.
- Sources: https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025%2F0360%28COD%29; https://www.edpb.europa.eu/system/files/2026-02/edpb_edps_jointopinion_202602_digitalomnibus_en.pdf; https://edri.org/wp-content/uploads/2026/03/EDRi-Data-Omnibus-Analysis-Council-Compromise-text.pdf; https://iapp.org/news/a/eu-member-states-leaked-digital-omnibus-compromise-proposal-eliminates-revised-gdpr-definition-of-personal-data

## Cluster 5 — Post-cutoff CJEU sweep, Jan 2025 – Jul 2026 (verified 2026-07-07)

New judgments the skill (training cutoff Jan 2026) could not fully know. Verified against CURIA press releases/InfoCuria where possible; exceptions flagged.

### 5.1 C-526/24 *Brillen Rottler*, 19 Mar 2026 — INCORPORATED (biggest correction)

- Even a **first** access request may be "excessive" under Art. 12(5) and refused as abusive — where the controller demonstrates the request was made not to verify processing but to **artificially create the conditions for an Art. 82 damages claim** (indicators: voluntary provision of the data shortly before, timing, conduct, publicly known serial request-and-sue patterns). Burden on the controller.
- Art. 82: damage from infringing Art. 15 itself is compensable (loss of control/uncertainty in principle included), BUT actual damage must be proven, and **no compensation where the data subject's own conduct is the determining cause** (causal chain broken).
- Skill impact: the "excessive = essentially repetition" framing and "manifestly unfounded is nearly a dead letter" needed qualification; motive-irrelevance (C-307/22) reconciled: legitimate non-privacy purpose ≠ abuse; manufacturing damages claims = abuse. Fixed in SKILL.md points 3+8, procedural-framework.md, restrictions-overlays.md.
- Sources: CURIA Press Release 38/26 https://curia.europa.eu/site/upload/docs/application/pdf/2026-03/cp260038en.pdf (read in full); Greenberg Traurig, Freshfields, CMS analyses concur. AG Szpunar opinion broadly followed.

### 5.2 C-203/22 *Dun & Bradstreet Austria*, 27 Feb 2025 — CONFIRMED (skill already cites; wording checked)

- Art. 15(1)(h): "meaningful information about the logic" = all relevant information about the **procedure and principles actually applied**, concise/intelligible, enabling the data subject to understand how the specific result was produced; handing over the algorithm or a complex formula does NOT satisfy the duty. Trade secrets: no blanket refusal — controller discloses to the SA/court, which balances and determines the extent of access. Matches skill's existing framing ("factors and weights, not the source code"; "full picture to SA/court").
- Source: https://curia.europa.eu/juris/document/document.jsf?docid=287305&doclang=en

### 5.3 C-247/23 *Deldits*, 13 Mar 2025 — INCORPORATED

- Art. 16: public-register authority must rectify inaccurate gender-identity data; accuracy assessed against the processing purpose; controller may require **relevant and sufficient evidence** but not disproportionate proof (surgery may not be demanded; medical certification can suffice). Added to other-rights.md Rectification.
- Sources: https://curia.europa.eu/site/upload/docs/application/pdf/2025-03/cp250034en.pdf; InfoCuria docid 296550

### 5.4 C-413/23 P *EDPS v SRB* (Grand Chamber), 4 Sep 2025 — INCORPORATED

- Opinions/comments are personal data. Pseudonymised data is not automatically personal data for every recipient — contextual "reasonable means of identification" test per recipient; BUT the controller's own transparency/recipient-naming duties are assessed from the controller's perspective. Added to art15-access.md scope section.
- Sources: https://curia.europa.eu/site/upload/docs/application/pdf/2025-09/cp250107en.pdf; FPF, Taylor Wessing analyses

### 5.5 C-655/23 *Quirin Privatbank*, 4 Sep 2025 — INCORPORATED

- Arts. 17/18 + 79 confer no self-standing GDPR right to a **preventive prohibitory injunction** against future processing (national law may provide one). Art. 82: purely compensatory, degree of fault irrelevant to quantum; "negative feelings" compensable only if proven concretely; parallel injunction doesn't reduce compensation. Added to art17-erasure.md and restrictions-overlays.md.
- Sources: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A62023CJ0655; A&O Shearman analysis

### 5.6 C-492/23 *Russmedia* (Grand Chamber), 2 Dec 2025 — INCORPORATED

- Online marketplace is (joint) controller of user-posted ads; e-Commerce hosting exemption is no GDPR escape; Arts. 24/32 require pre-publication checks for sensitive data + measures against copying/republication — otherwise erasure is defeated by mirror-site spread. Added to art17-erasure.md.
- Sources: InfoCuria docid 306764; Verfassungsblog, Bird & Bird analyses

### 5.7 Also noted (log-only, no skill text change)

- **C-416/23 *Österreichische Datenschutzbehörde*, 9 Jan 2025**: DPA-side Art. 57(4) — complaint volume alone never makes requests excessive; abusive intent must be established; consider fee before refusal. (Cited briefly in SKILL.md point 8.)
- **T-354/22 *Bindl v Commission* (GC), 8 Jan 2025**: EUR 400 for loss of control from unlawful US transfer (EUDPR) — first EU-court damages award without material loss.
- **C-414/24, 18 Jun 2026**: Art. 77 complaint and Art. 79 court action are parallel independent remedies; DPA may not park a complaint pending civil proceedings. ⏳ Verified via dpcuria docket + two firm analyses only — CURIA full text returned empty to automated fetch; one manual CURIA confirmation recommended before citing in skill output.
- **C-484/24 *NTH Haustechnik*, 18 Jun 2026**: unlawfully obtained personal data not automatically inadmissible as civil evidence — marginal to DSRs.
- **C-97/23 P *WhatsApp Ireland v EDPB*, 10 Feb 2026**: EDPB Art. 65 binding decisions directly challengeable — enforcement-map only.
- **C-394/23 *Mousse*, 9 Jan 2025**: ability to object later cannot justify legitimate-interest processing — relevant to `legitimate-interest` sibling skill more than here.

### 5.8 Nothing-found (documented absence, as of 2026-07-07)

- No CJEU judgment/AG opinion/new reference found 2025–2026 on: Art. 20 portability, Art. 15(4) squarely, search-engine delisting, new Art. 22 scoring references.
- C-446/21 and C-621/22: no follow-on activity in the window (both decided Oct 2024).
- Pending watch-list: no new post-2026 preliminary references on Arts. 12-23 confirmed; recommended manual pass over CURIA new-cases/OJ C-series notifications at next release. ⏳ watch
