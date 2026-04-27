---
name: workflow-authoring
description: Use when writing or revising agent-orchestration workflow YAML or workflow prompts, especially when converting an ad hoc agent task into a structured workflow or when prompt, runtime, and artifact responsibilities are easy to blur.
---

# Workflow Authoring

## Overview

Use this for repos built on the agent-orchestration DSL.

Core rule: **prompts own local non-deterministic judgment; workflows own deterministic control**.

If you find yourself putting counters, loop mechanics, keep/discard rules, ledger updates, waits, parsing, or routing logic into a prompt, stop and move that behavior back into the workflow.

Treat the repo's workflow drafting guide as a live checklist, not background reading.

## Required Reading Order

Before drafting or changing a workflow:

1. `docs/index.md`
2. `docs/workflow_drafting_guide.md`
3. `specs/dsl.md`
4. `specs/variables.md`, `specs/dependencies.md`, `specs/providers.md`
5. `workflows/README.md` and one current example using the same pattern

If the repo has equivalent docs under different names, use the nearest equivalent set.

## Authoring Checklist

1. Define the step boundary.
   The provider step should do one coherent judgment-heavy task.

2. Split deterministic from non-deterministic work.
   Prompts choose, propose, revise, review, or edit.
   Workflows parse outputs, enforce contracts, gate, loop, wait, record state, and decide next steps.

3. Keep the four surfaces distinct.
   - workflow boundary: `inputs` / `outputs`
   - runtime dependencies: `depends_on` / `consumes`
   - provider prompt sources: `input_file`, `asset_file`, prompt injection
   - artifact storage or lineage: `artifacts`, `expected_outputs`, `output_bundle`, `publishes`

4. Prefer structured control flow over shell glue when the DSL supports it.
   Use shell gates only when no structured form fits cleanly.

5. Keep prompts task-local.
   A prompt may mention required input files, required output files, and local success criteria.
   A prompt should not talk about workflow loops, downstream gates, global orchestration ownership, or later phase transitions.

6. Make path authority explicit.
   If the step must write a file, tell it the exact authoritative path.
   Avoid multiple plausible state roots or duplicate report locations.

7. Keep string-rich or high-entropy state in JSON files when the DSL surface is awkward.
   Do not force brittle scalar contracts just because a value is logically small.

## Prompt Editing Checklist

When changing a workflow prompt:

- Name the actor: drafter, reviewer, reviser, implementer, or runtime.
- Do not assign work to an actor that cannot do it. Plans sequence work; reviews decide whether to accept or reject; workflows route and record state.
- Avoid workflow or DSL terms in provider prompts unless the provider step directly owns that concept.
- Use plain terms. Define any necessary term locally.
- Keep generic prompts project-agnostic; put project nouns only in project-specific prompts or inputs.
- Use existing artifact or template sections before inventing new structure.
- Prefer one sharp instruction over long negative lists.
- Check whether the edit changes behavior, review strictness, or only phrasing.

## Common Mistakes

- Prompt says "the workflow owns..." or "continue the loop".
- Prompt is asked to manage counters, gate decisions, ledger appends, or keep/discard resets.
- Prompt tells a plan to escalate, a reviewer to implement, or an implementer to manage loop cycles.
- Prompt uses undefined jargon such as "gate", "claim", or "workflow" where a plain result, check, or step would be clearer.
- A generic prompt contains project-specific nouns or examples that narrow its behavior.
- The same contract is expressed differently in prompt text, workflow YAML, and docs.
- A one-off workflow invents a second plausible state/report path for the same task.
- Tests assert literal prompt wording instead of behavior or contracts.

## Verification

- Run the narrowest relevant pytest selector first.
- If you add or rename tests, run `pytest --collect-only` on that module.
- For workflow or prompt changes, run at least one orchestrator validation or smoke check from the target repo root.
- Inspect the prompt and workflow diff together before claiming the split is clean.

## Related Skills

- **REQUIRED BACKGROUND:** `superpowers:brainstorming` before designing new workflow behavior
- **REQUIRED SUB-SKILL:** `superpowers:writing-plans` for multi-step workflow changes
- **REQUIRED SUB-SKILL:** `superpowers:verification-before-completion` before claiming success
