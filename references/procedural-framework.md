# Procedural Framework — Art. 12 GDPR

The modalities layer that applies to EVERY data subject request, regardless of which right is invoked.

## Receipt and form

- Requests are **form-free**: no magic words or required form/portal (EDPB 01/2022 ¶52-57). Official or reasonably expected controller channels count regardless of preferred routing — including email, letter, phone, social media, in-app channels, or a general contact inbox instead of the DPO address — and internal routing delay is the controller's risk. A completely random, apparently incorrect, or clearly unrelated address or channel does not automatically count (e.g. an individual employee's unrelated inbox) where an appropriate channel was clearly communicated (¶54-55). "Send me everything you have on me" is an Art. 15 request; "stop using my data for ads" is an Art. 21(2) objection.
- Read requests **generously and cumulatively**: a single email often invokes several rights. When genuinely ambiguous, ask — but asking does not stop the clock.
- The data subject may act **through an agent** (lawyer, consumer platform) with a mandate; verify the mandate, not just the agent.

## Deadlines (Art. 12(3))

| Event | Rule |
|---|---|
| Baseline | **One calendar month from receipt** — Regulation (EEC, Euratom) No 1182/71 counting: ends on the same date of the next month (request 17 Mar → due 17 Apr); if no such date, last day of month; if the end falls on a Saturday, Sunday or public holiday, the period ends with the expiry of the following working day (Art. 3(4), confirmed verbatim against the current consolidated text 2026-10-02) |
| Extension | **+2 months max**, only for complexity or number of requests; the data subject must be told **within the first month, with the reasons** — a notice declared after the first month has elapsed is a violation, not a valid extension |
| No action | If the controller will not act, it must say so within one month, with reasons and a pointer to the SA and judicial remedies (Art. 12(4)) |
| "Without undue delay" | The month is a ceiling, not a target — simple requests should be answered faster |

Always compute and state the **concrete due date** in triage output.

## Identity verification (Art. 12(6))

- Standard: **reasonable doubts** about identity — concrete, not routine. Verification is the exception, not a default intake step.
- **Proportionality** (EDPB 01/2022 ¶64-79): authenticate through the channel that already exists (logged-in account, registered email). ID-card copies are a last resort, must be redactable, and verification data is purpose-bound (no reuse, prompt deletion).
- If the controller **cannot identify** the data subject at all (Art. 11), it says so and Arts. 15-20 do not apply — but the data subject may provide additional identifying information (Art. 11(2)).
- Verification does not extend the deadline. A prompt, justified identity query defers the substantive response; a late or pretextual one does not.
- **Competing claims (joint accounts, ex-partners, family members):** a requester who names a data subject but is not that data subject is not entitled to their data merely by producing a name, email, or other guessed/public detail. Verify identity against the actual account holder's existing authentication channel — never against whatever the requester supplies — and treat an unresolved or failed check as `verified: false` even if nobody formally flagged "doubts". Disclosing or erasing one joint-account holder's data on another's say-so is a wrongful-disclosure/destruction risk, not a courtesy.

## Fees and refusal (Art. 12(5))

- **Free by default.** First copy under Art. 15(3) is free (confirmed for medical records even when the purpose is non-privacy — CJEU C-307/22).
- A **reasonable, administrative-cost-based fee** OR refusal is possible only for **manifestly unfounded or excessive** requests — and the **controller bears the burden of demonstrating** this.
- "Excessive, in particular because of their repetitive character": judge repetition against **reasonable intervals** (Recital 63) relative to how frequently the data changes. A second access request after 14 days with no processing change may be excessive; one after a year is not.
- **Abuse doctrine (C-526/24 *Brillen Rottler*, 19 Mar 2026):** even a FIRST request can be excessive where the controller demonstrates it serves not to verify processing but to artificially create the conditions for an Art. 82 damages claim — indicators the Court named: the data were volunteered shortly before, elapsed time, the requester's conduct, publicly known serial request-and-sue patterns. Burden stays on the controller; document the demonstration.
- **Manifestly unfounded** remains rare in practice — abusive intent must be evident (e.g. explicit harassment campaigns); the CJEU handles claim-manufacturing via "excessive" instead (C-526/24). The motive-irrelevance rule (C-307/22) still forecloses "they only want it for litigation" arguments — a genuine non-privacy purpose is not abuse.
- **Broad scope is not excessive.** For large data holdings, EDPB 01/2022 ¶35 allows asking the data subject to specify the processing operations concerned — but if they decline, the request covers everything.
- When recording a charged fee in the sidecar (`fee.charged`), state the ground (`fee.ground`: `further_copy` or `manifestly_unfounded_or_excessive`) — a fee charged on a first copy with no ground stated is a violation of Art. 15(3)/12(5), not a judgement call.

## Facilitation duty (Art. 12(2))

The controller must **facilitate** the exercise of rights: no dark patterns, no login walls for non-account channels, no demanding reasons. Making the data subject justify the request is itself a violation pattern.

## Communication quality (Art. 12(1))

Concise, transparent, intelligible, easily accessible, clear and plain language — the response letter must be understandable to a lay reader. Where the request came electronically, respond electronically unless asked otherwise (Art. 12(3)).

## Processor-side receipt

A processor receiving a request does not answer it — it forwards to the controller **without undue delay** and assists per Art. 28(3)(e). The forwarding lag does not move the controller's deadline (clock started at the processor's receipt if the processor receives requests on the controller's behalf — check the DPA's allocation; see the `dpa-art28` skill).

## DSR register (accountability)

Log every request: see `templates.md` for the schema. Under Art. 5(2) the controller must be able to show, per request: when received, what was invoked, how identity was handled, what was decided and why, and which recipients were notified.
