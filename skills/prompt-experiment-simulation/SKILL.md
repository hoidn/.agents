---
name: workflow-behavior-simulation
description: Use before applying high-blast-radius changes to shared prompts, DSL routing, artifact contracts, or review criteria whose judgment-heavy effects cannot be verified by runnable validators or dry runs alone.
---

# Workflow Behavior Simulation

## Overview

Evaluate uncertain prompt or workflow changes against concrete scenarios before applying them broadly.

Core rules:
1. **Run real checks first.** Prefer validators, `--dry-run`, and narrow smoke tests over mental simulation.
2. **Label predictions as hypotheses, not observed execution.** Never fabricate step-by-step `"what happened"` logs or write permanent reports unless requested.

## When To Use

Use when a proposed change touches shared prompts, routing, review strictness, or artifact contracts whose behavioral effect is judgment-dependent and high-risk.

Skip this skill for typos, deterministic YAML/script rules covered by tests or `--dry-run`, or single-step local edits you can directly smoke-test.

## Pre-Flight Check

Keep the analysis in chat and under 300 words unless the user asks for a persisted document.

1. **Pin the diff and blast radius.** Name the exact files/prompts changed and every shared workflow or downstream consumer that reads them. Separate deterministic runtime changes (verify with `--dry-run`/tests) from provider-judgment changes.
2. **Test three real scenarios** (drawn from actual repo briefs, logs, or recent runs where available):
   - **Target case:** where the change should help.
   - **Hard/edge case:** where the change may fall short or misfire.
   - **Trivial case:** where the change could add unnecessary overhead, checklist gravity, or false blockers.
3. **Compare old vs. new per scenario.** For each case, state in 2–3 lines:
   - hypothesized behavior/route delta (explicitly mark `observed` vs. `specified` vs. `hypothesized`);
   - main regression risk (e.g., silent scope drop, stricter blocking on bookkeeping, extra loop cycles);
   - concrete evidence or test that would falsify the prediction.
4. **Decide:** `ADOPT`, `ADOPT_NARROWLY`, `REVISE`, or `REJECT`.

## Verification After Applying

- Inspect prompt, workflow, script, and contract diffs together.
- Run the narrowest real validation (`--dry-run`, schema/routing validator, or smoke run).
- Do not add tests that assert literal prompt wording; verify routing, contracts, and state transitions instead.
