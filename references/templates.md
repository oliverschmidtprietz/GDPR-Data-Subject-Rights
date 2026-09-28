# Templates — Response Letters, DSR Register, Deadline Math

For .docx output, read the docx-processing skill first, then populate these structures. Keep Art. 12(1) plain-language discipline: a lay reader must understand every letter.

## Deadline computation (state this in every triage)

```
Received:        [date] (channel: [email/letter/portal/phone])
Due:             [same calendar date next month; if absent, last day of month;
                  weekend/holiday → next working day]
Extension:       [none | +2 months declared on [date] with reasons — new due date]
```

## Response letter skeletons (EN structure — mirror in DE; key German terms in brackets)

### A. Access — full grant (Art. 15) [Auskunft]

1. Reference + confirmation of processing
2. The Art. 15(1)(a)-(h) block, per purpose: purposes; categories; **named recipients**; retention period/criteria; rights reminder; source (if not collected directly); automated decision-making incl. meaningful logic; third-country safeguards
3. The copy: annexes per system, field-code translations
4. Redactions made and their grounds (Art. 15(4)) — state that redaction occurred
5. Remedies notice: SA complaint (name the competent SA), judicial remedy

### B. Erasure — partial grant (Art. 17) [Löschung]

1. Reference + what was requested
2. Erased now: [categories/systems], effective [date]; backup expiry [date]
3. Retained under Art. 17(3)(b): [records], statutory ground (e.g. AO § 147/HGB § 257), purpose limitation and access controls, scheduled deletion on [date]
4. Formal Art. 18 restriction (optional — only where an independent Art. 18(1) ground is identified): [records, ground, permitted processing]
5. Recipients notified per Art. 19: [list or "available on request"]
6. Art. 17(2) steps taken (if data was public)
7. Remedies notice

### C. Reasoned refusal (any right) [Ablehnung]

1. Reference + the right invoked
2. The test applied and why it fails (ground absent / exception prevails / Art. 12(5) with the controller's demonstration)
3. What was done instead (partial measures, restriction, specify-offer)
4. Remedies notice (Art. 12(4): SA + judicial remedy) — mandatory
5. No fee statement (or fee justification)

### D. Extension notice (Art. 12(3)) — must go out within month one

1. Reference + receipt date
2. Extension length (≤2 months) + new due date
3. **Reasons** (complexity/number — concretely, not boilerplate)

### E. Identity verification query (Art. 12(6)) — only on reasonable doubts

1. What raised the doubt (concretely)
2. The **least intrusive** verification requested (existing channel first)
3. Statement that verification data is used only for this purpose and then deleted
4. Note: the request stays logged; substantive response follows promptly after verification

## DSR register schema (one row per request)

| Field | Content |
|---|---|
| id | DSR-YYYY-NNN |
| received / channel | date + intake channel |
| data_subject_category | customer / employee / applicant / third party (via agent?) |
| rights_invoked | Art. 15 / 16 / 17 / 18 / 20 / 21 / 22 (multiple allowed) |
| identity_check | none needed / verified on [date] via [method] / failed |
| due / extended_due | computed dates; extension reasons |
| systems_searched | from the `ropa` register |
| outcome | granted / partial / refused (+ ground) |
| redactions | Art. 15(4) grounds applied |
| recipients_notified | Art. 19 list or disproportionate-effort note |
| downstream | Art. 17(2) steps; processor instructions + confirmations |
| closed | date; responder |

Export as .xlsx via the xlsx skill on request; this register is itself personal data (retention: statute-of-limitations horizon for Art. 82/83 exposure, then erase).

## Suppression-list note (after marketing objections)

Keep the minimum identifier set on a blocklist so the person is not re-contacted; document basis (compliance with Art. 21(3)) and say so in the response — full erasure of the suppression entry would defeat the objection.
