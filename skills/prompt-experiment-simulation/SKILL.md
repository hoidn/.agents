---
name: workflow-behavior-simulation
description: Use when evaluating proposed prompt, workflow, DSL routing, artifact contract, provider-context, or review-decision changes whose behavioral effect is uncertain.
---

# Workflow Behavior Simulation

## Overview

Workflow and prompt changes are behavior changes. Treat them as experiments: compare old and new behavior on real task surfaces before applying, approving, or relying on the change.

Core rule: **produce an auditable simulated execution trace, not an in-head narrative.**

## When To Use

Use this when a proposed or committed change may affect:

- workflow topology, DSL routing, loop bounds, calls, match cases, or phase sequencing
- prompt behavior, review strictness, review vocabulary, or artifact judgment
- provider inputs, consumed context, prompt assets, or output contracts
- artifact lineage, state files, manifests, ledgers, counters, or promotion behavior
- a combination of workflow mechanics and agent judgment

Do not use this for typo fixes, purely mechanical validation rules with direct tests, or changes whose behavior is fully deterministic and already covered by runnable checks.

## Required Pass

1. Define the compared change.
   - Record exact revisions, files, prompts, workflow definitions, and insertion points.
   - State whether the comparison is proposal vs current, working tree vs HEAD, HEAD vs HEAD^, or another pair.
   - Do not apply edits before simulation unless explicitly asked.

2. Check scope and blast radius.
   - Find every workflow, stack, phase, prompt, script, manifest, or consumer affected.
   - Separate deterministic DSL/runtime behavior from provider judgment.
   - Separate upstream workflow issues from downstream implementation, validator, or artifact issues.

3. Build the evidence set.
   - Prefer real briefs, manifests, logs, state files, review reports, execution reports, prompt logs, and designs.
   - List excluded evidence, especially artifacts that would prejudice a blank-slate simulation.
   - Mark each key fact as `observed`, `specified`, or `inferred`.

4. Pick representative scenarios.
   Include at least:
   - one target case where the change should help
   - one hard case where the change may not be sufficient
   - one small/simple case where the change could add overhead

5. Simulate as an event log.
   For each compared version and each scenario, write a step-by-step trace with:
   - phase or workflow step
   - consumed inputs/artifacts
   - decision/output
   - rationale
   - produced artifacts/state
   - next route
   - confidence and assumptions

   If a step is deterministic, say so. If a step depends on provider judgment, explain why that judgment is likely and what evidence would change it.

6. Compare behavior.
   Assess:
   - whether important issues move earlier or later
   - whether scope is preserved, narrowed with authority, or silently dropped
   - artifact length, specificity, and process burden
   - likely review findings and severity
   - behavior, API semantics, architecture, maintainability, and scientific or user-facing correctness
   - checklist gravity, bookkeeping findings, evidence-table noise, or other process overhead
   - total iteration count and terminal outcome

7. Write an auditable simulation report.
   Include these sections:
   - `Inputs And Exclusions`
   - `Compared Versions`
   - `Scenario Setup`
   - `Evidence Ledger`
   - `Deterministic Workflow Delta`
   - `Simulated Event Log`
   - `Decision Rationale`
   - `Comparison`
   - `Assumptions And Falsifiers`
   - `Regression Risks`
   - `Recommendation`

   Use stable decision labels:
   - `ADOPT_AS_WRITTEN`
   - `ADOPT_NARROWLY`
   - `REVISE_AND_RESIMULATE`
   - `REJECT`
   - `BROADEN_WITH_SEPARATE_PROPOSAL`

8. Make a bounded recommendation.
   - Adopt only when the expected improvement is broader than the motivating incident.
   - Prefer a narrower edit when the change helps one phase but risks shared prompts or workflows.
   - Require a separate proposal when the fix must touch additional shared phases, prompts, contracts, or runtime behavior.

## Report Quality Bar

The report must let another engineer audit the simulation without trusting your memory.

Minimum acceptable detail:

- exact old/new revisions or file paths
- exact starting state
- trace of what happened, not just what could happen
- decision-by-decision rationale
- explicit assumptions and confidence
- evidence that would falsify the simulated outcome
- verification command for the report itself, usually `git diff --check`

If you cannot produce an auditable trace from the available evidence, write `REVISE_AND_RESIMULATE` or state that more evidence is required.

## Common Mistakes

- Producing a polished narrative instead of an event log.
- Saying what the workflow can do instead of what happened in the simulation.
- Hiding assumptions inside confident prose.
- Simulating only the motivating failure.
- Ignoring shared prompt or workflow consumers.
- Treating generated reports, ledgers, or docs completeness as blocking by default instead of asking whether they support a material outcome.
- Letting a redesign narrow scope without preserving omitted work through explicit authority, successor scope, or roadmap revision.
- Using upstream design prompts to fix downstream implementation or validator failures.

## Verification

For simulation-only work:

- Inspect compared workflow/prompt diffs and consumed artifacts.
- Save the simulation report where future workflow work will find it, usually under `docs/plans/`.
- Run `git diff --check` on the report.

When edits are later applied:

- Inspect prompt, workflow, script, and contract diffs together.
- Do not add tests that assert literal prompt wording.
- Prefer behavioral, artifact, routing, state-transition, or smoke checks that show the workflow still fits its consumers.
