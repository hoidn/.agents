---
name: designing-subtractive-features
description: Use when designing or revising a feature, API, spec, or internal architecture in a mature codebase where debt, indirection, duplicate paths, configuration surfaces, or compatibility machinery must not increase.
---

# Designing Subtractive Features

## Overview

Design the smallest final system, not the smallest patch. Do not finalize a design until user experience, domain contract, module ownership, migrations, and deletions agree.

**REQUIRED SUB-SKILL:** Use `design-spec-drafting` to select repository authorities before choosing an API.

## Design Gate

| Gate | Required evidence |
| --- | --- |
| Goal | Observable flow, non-goals, invariants, complexity target |
| Current state | Existing entry points, callers, config formats, implementations, persistence, owners |
| Alternatives | Goal-derived clean-slate design compared with incumbent |
| Public API | Common and advanced examples, names, returns, discovery, error behavior |
| Internal design | Target call graph, module owners, exceptions, migrations, deletions |
| Feasibility | Contract, compatibility, persistence, and net path-reduction proof |

Material contract or architecture gaps block design approval; report them alongside the candidate.

## Workflow

1. Follow the repository's documentation index and trace real callers before proposing signatures. Reading selected files alone does not establish ownership.
2. Derive a clean-slate target from the goal, compare it with the incumbent, then select or synthesize. Prior approval makes a candidate, not an answer.
3. Pressure-test realistic usage: common vs. advanced workflows, alternate configurations/backends, same vs. different inputs, return types, discovery, errors, and end-to-end examples.
4. Make ambiguous inputs, defaults, conversions, persistence, and failure modes explicit. Preserve real domain distinctions; cut ceremony.
5. Make every new entry point, type, adapter, record, schema field, alias, or service replace an existing one; otherwise prove it is irreducible or cut it.
6. Draft public behavior and internal architecture (including deletions) together; start implementation planning only after the gate passes.

Investigate repository facts yourself and batch only genuine product choices for the user.

**Spikes vs. shims:** Minimal throwaway feasibility spikes (e.g., an executable fixture required by `design-spec-drafting` to verify an unproven capability) are allowed during design, provided they are never shipped. Do not bypass the gate by landing a shipping prototype, compatibility shim, wrapper, or parallel path.

## Topology Test

Avoid layering a new abstraction over legacy paths:

```text
new API -> request/adapter -> old workflow -> config translation -> core
```

Converge onto one canonical path and delete displaced entry points:

```text
Python/CLI -> one public entry point -> canonical resolver -> existing core
specialized caller ----------------------------------------> existing core
```

Migrate callers and delete displaced entry points; keep genuinely specialized low-level paths direct.

## Common Rationalizations

| Rationalization | Correction |
| --- | --- |
| "It is already approved." | Without current codebase evidence, approval is provisional. |
| "The wrapper is thin." | Count the old path and config surface it leaves alive. |
| "Compatibility might need an alias." | Require a real contract or caller inventory before keeping compatibility machinery. |
| "Simplify after it works." | Complexity reduction is part of the design, not follow-up debt. |
| "A record/schema is safer." | Persist only irreducible facts. |

## Red Flags

Stop and revise when: signatures precede an ownership/caller map; examples introduce unjustified `Payload`/`Request`/`Result`/`Adapter` ceremony; new entry points leave equivalent old ones alive; the design lacks a concrete deletion list; or a shipping shim bypasses the gate.
