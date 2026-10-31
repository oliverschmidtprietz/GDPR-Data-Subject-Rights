# The Other Rights — Art. 16, 18, 20, 21, 22 GDPR (compact track)

## Rectification (Art. 16)

- Covers **inaccurate** facts and **incomplete** data (completion via supplementary statement).
- Opinions/assessments are rectifiable only where they rest on inaccurate facts; otherwise attach the data subject's contrary statement.
- Accuracy is judged **against the purpose** of the processing (a historic address in an archived contract is not "inaccurate") — confirmed CJEU C-247/23 *Deldits*, 13 Mar 2025 (gender-identity data in a public identification register).
- Evidence: the controller may require **relevant and sufficient evidence** of inaccuracy, but nothing disproportionate — C-247/23: medical certification may be asked for, proof of gender-reassignment surgery may not.
- Triggers Art. 19 recipient notification. Disputed accuracy → Art. 18(1)(a) restriction **during verification** (automatic on request, not discretionary).

## Restriction (Art. 18)

Four grounds: (a) accuracy contested — for the verification period; (b) unlawful processing but data subject prefers restriction over erasure; (c) controller no longer needs the data but data subject needs it for legal claims; (d) Art. 21(1) objection pending the balancing.

- "Restriction" = data kept but **blocked from any processing except storage**, legal claims, protection of others' rights, or important public interest (Art. 18(2)) — consent can unlock more.
- Implement technically (flag + access control), not as a memo. Lifting the restriction requires **prior notice** to the data subject (Art. 18(3)).
- Statutory retention is handled under Art. 17(3)(b) with purpose limitation, access controls, and scheduled deletion; it is not an Art. 18 restriction unless an independent Art. 18(1) ground applies (see `art17-erasure.md`).

## Portability (Art. 20)

- Scope: data **provided by** the data subject — declared data AND observed data (usage history, sensor/device data, search history) per WP242 rev.01; **NOT derived/inferred** data (scores, profiles, credit assessments).
- Conditions (cumulative): legal basis is **consent or contract**, AND processing is **by automated means**. LI-based processing is never portable (use Art. 15 instead).
- Format: structured, commonly used, machine-readable (CSV/JSON/XML with metadata — a PDF fails).
- Direct controller-to-controller transmission only **where technically feasible**; no duty to build compatible systems.
- Portability does not trigger erasure at the source — the data subject can have both, but must ask for both.
- Must not adversely affect others' rights (Art. 20(4)): e.g. a chat export contains other people — provide to the data subject for personal use, flag the limits of the receiving controller's basis.

## Objection (Art. 21)

Two very different regimes — never conflate them:

| | Art. 21(1) general objection | Art. 21(2)-(3) direct marketing |
|---|---|---|
| Applies to | Art. 6(1)(e)/(f) processing | Marketing incl. related profiling |
| Standard | "Grounds relating to his or her particular situation" required from the data subject | None — no reason needed |
| Effect | Processing pauses for balancing; controller must show **compelling legitimate grounds** overriding the data subject (reversed, stricter burden than the original LIA — run the `legitimate-interest` skill) | **Absolute stop**, immediately, no balancing |
| Aftermath | Balancing fails → erasure ground Art. 17(1)(c) | Suppression list: keep minimal contact data on a blocklist (basis: Art. 6(1)(c)/(f) compliance) — do not fully erase the suppression entry, or the person gets re-contacted |

Art. 21(4): the right must be brought to attention explicitly, separately from other information, at first communication. Art. 21(5): objection by automated means must be possible for information-society services.

## Automated individual decisions (Art. 22)

- Structure: a **prohibition with exceptions** (contract necessity, Union/MS law, explicit consent) — not a right the data subject must invoke first.
- **Scoring can itself be the Art. 22 decision** where a third party draws strongly on it (CJEU C-634/21 *SCHUFA*) — a controller cannot hide behind "the bank decided, we only scored".
- "Legal or similarly significant effect": credit denial, hiring rejection, benefit cuts, contract refusal; targeted advertising normally not, price discrimination possibly.
- **Human involvement must be meaningful**: authority and competence to change the outcome, actual engagement with the case — statistical rubber-stamping keeps the decision automated.
- Safeguards under 22(3): right to obtain human intervention, express one's point of view, contest the decision. Special-category data only under 22(4) conditions.
- Explanation duties link back to Art. 15(1)(h) (see `art15-access.md`) — the procedure and principles actually applied, not the algorithm; trade secrets limit detail via SA/court balancing, never the existence of the explanation (C-203/22).
- **Germany — insurance derogation (§ 37 BDSG):** for decisions taken in connection with performing an insurance contract, § 37 BDSG narrows Art. 22(1) beyond the Regulation's own 22(2)(a)/(c) exceptions — where the decision grants the request, or rests on binding medical-treatment fee regulations with 22(3)-style safeguards in place. Narrow and sector-specific; see `restrictions-overlays.md` for the full text and conditions. Do not extend it to general underwriting or marketing scoring.
