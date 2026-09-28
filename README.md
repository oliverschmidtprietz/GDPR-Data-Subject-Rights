# Data Subject Rights — Deployment Guide

GDPR data subject rights handling (Art. 12–23): intake and triage of incoming requests, right-by-right assessment, exception and national-restriction analysis, and response drafting — access (Art. 15) and erasure (Art. 17) as deep tracks; rectification, restriction, portability, objection, and automated-decision rights covered in a compact track.

## What it does

- Triage: which right(s) a request invokes, concrete deadline computation, proportionate identity verification
- Access: full Art. 15 scoping per EDPB Guidelines 01/2022 and current CJEU case law (recipient naming, copy scope, motive irrelevance, third-party redaction)
- Erasure: two-step ground/exception test; statutory retention limited to covered records and periods under Art. 17(3)(b), with purpose limitation, access controls, and scheduled deletion. A formal Art. 18 restriction requires an independent Art. 18(1) ground; BDSG § 35(3) covers by-laws-based or contractual, not statutory, retention periods. Also covers backups and Art. 17(2)/19 downstream duties
- Refusals, fees, and extensions with the Art. 12(5) high-bar tests and mandatory remedies notices
- Deliverables: bilingual (EN/DE) response-letter skeletons, DSR register schema, .docx/.xlsx output via the document skills

## Installation

Copy or symlink the skill folder into your Claude Code skills directory:

```bash
ln -s /path/to/claude-skills/skills/data-subject-rights ~/.claude/skills/data-subject-rights
```

## Structure

```
data-subject-rights/
├── SKILL.md                          # Orchestrator: routing, legal precision points, handoffs
├── references/
│   ├── procedural-framework.md       # Art. 12: receipt, deadlines, identity, fees/refusal
│   ├── art15-access.md               # Access deep track (EDPB 01/2022 + CJEU)
│   ├── art17-erasure.md              # Erasure deep track (grounds, exceptions, downstream)
│   ├── other-rights.md               # Art. 16/18/20/21/22 compact track
│   ├── restrictions-overlays.md      # Art. 23 + German BDSG §§ 34/35, retention anchors
│   ├── templates.md                  # Letters (EN/DE), DSR register, deadline math
│   └── dsr-sidecar-schema.json       # Native machine-readable sidecar schema
├── validator/                        # Structural-tier validator (portfolio standard)
│   ├── validate.py                   # CLI: validate + --emit-core-artefact
│   ├── dsr_validator/                # Rules, runner, findings, core-artefact adapter
│   └── fixtures/                     # must_pass / must_fail sidecars
├── sources.lock.json                 # Reference-file verification manifest
├── conformance.json                  # Portfolio standard conformance declaration
└── evals/evals.json                  # 7 evaluation cases
```

## Sibling skills

Works with `ropa` (data inventory for scoping searches and recipient lists), `legitimate-interest` (Art. 21(1) re-balancing), `dpa-art28` (processor assistance duties), and `privacy-notice-eu` (transparency follow-ups).

## Version History

See [CHANGELOG.md](CHANGELOG.md) — the only place version history lives. Current version and status: see the `SKILL.md` frontmatter and the root README Skill Register.

## License

AGPL-3.0 — see repository LICENSE.
