---
name: designing-subtractive-features
description: Use when designing or revising a feature, API, spec, or internal architecture in a mature codebase where debt, indirection, duplicate paths, configuration surfaces, or compatibility machinery must not increase.
---

# Designing Subtractive Features

## Overview

Design the smallest final system, not the smallest patch. Do not approve until
user experience, domain contract, owners,
migrations, and deletions agree.

**REQUIRED SUB-SKILL:** Use `design-spec-drafting` to select repository
authorities before choosing an API.

## Approval Gate and Quick Reference

| Gate | Required evidence |
| --- | --- |
| Goal | Observable flow, non-goals, invariants, complexity target |
| Current | Doors, callers, config currencies, bodies, persistence, owners |
| Alternatives | Goal-derived clean slate compared with incumbent |
| Public | Normal/advanced examples, names, returns, discovery, errors |
| Internal | Target graph, owners, exceptions, migrations, deletions |
| Proof | Contract, compatibility, persistence, path-count feasibility |

Material contract/topology gaps block approval; report them with the candidate.

## Workflow

1. Follow the documentation index; trace callers before signatures. Selected
   files are not an ownership proof.
2. Derive a clean-slate target, compare with the incumbent, then select or
   synthesize. Prior approval makes a candidate, not an answer.
3. Pressure-test ordinary/grouped examples, alternate models, same/different
   input, paths, returns, workspace, discovery, errors, and visualization.
4. Table ambiguous inputs, defaults, conversions, persistence/replay, and
   failures. Preserve domain distinctions; remove ceremony.
5. Make each new door, type, adapter, record, schema field, alias, or service
   replace something; otherwise prove it irreducible or cut it.
6. Draft behavior and internal architecture together; plan only after the gate.

Investigate repository facts yourself and batch only genuine product choices.
Do not seek partial approvals. Withholding approval does not authorize a
prototype, shim, mock, or parallel path.

## Topology Test

```text
new API -> request/adapter -> old workflow -> config translation -> core
```

should become:

```text
Python/CLI -> one public door -> canonical resolver -> existing core
specialized caller -------------------------------> existing core
```

Migrate callers and delete displaced doors; retain specialized paths.

## Common Mistakes and Rationalizations

| Rationalization | Correction |
| --- | --- |
| "It is already approved." | Without current evidence, approval is provisional. |
| "I read the relevant docs." | Trace the complete maintained path and consumers. |
| "The wrapper is thin." | Count the old path it leaves alive. |
| "Compatibility might need an alias." | Require a contract or consumer inventory. |
| "Simplify after it works." | Complexity reduction is not follow-up debt. |
| "Gaps are implementation details." | Contract- or topology-changing gaps block approval. |
| "A record/schema is safer." | Persist only irreducible facts. |
| "Use a provisional path." | Missing evidence does not expand scope. |

## Red Flags

Stop when signatures precede the owner map; examples leak unjustified
`Payload`/`Request`/`Result`/`Adapter` ceremony; new doors leave equivalents
alive; behavior lacks a target graph/deletions; planning starts with gaps; or a
prototype bypasses the gate. Never claim approval before every gate passes.
