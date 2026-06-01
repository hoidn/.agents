---
name: consistency-quality-pass
description: Use when docs, plans, backlog items, workflow prompts, YAML, manifests, run state, artifact labels, evidence claims, or selector behavior disagree; when stale wording causes brittle decisions; or when status labels obscure the actual contract.
---

# Consistency Quality Pass

Use this skill to resolve contradictions across project authority surfaces without weakening the underlying contract.

Core rule: prefer current contract completeness over origin labels. Prefer the highest durable authority over stale duplicated wording. Remove label-driven policy and other accidental rigidity while preserving provenance, verification, and claim boundaries.

When context already identifies the relevant changed work, start there instead
of auditing repo-wide. Broaden only when those changes point to a stale
contract, index, or authority surface.

Preserve doc boundaries: specs are normative contracts; architecture/design docs
hold durable design choices; status/index/roadmap docs record completion and
discoverability; run artifacts and reports keep execution detail. Promote
ambiguous contracts to specs/design docs, but keep ordinary completion out of
global specs.

## Index And Catalog Surfaces

`docs/index.md` is the repo's primary documentation hub. More generally, index,
catalog, map, README, manifest, and hub documents are discoverability
authorities, not semantic authorities. They route readers to the current source
of truth across specs, design docs, plans, artifacts, prompts, workflows, and
runtime evidence.

During a consistency pass, check relevant index/catalog surfaces when adding,
renaming, deprecating, or changing the routing/ownership of specs, system
architecture, design docs, plans, implementation architecture, workflows,
prompts, artifacts, evidence, or status labels.

Treat stale or missing routing as `discoverability_gap`.

Patch index/catalog surfaces as routing layers: descriptions, links, status
labels, reading paths, and clarification pointers. Behavior and policy should be
owned by the linked spec, design doc, plan, artifact manifest, or runtime
evidence.

## Pressure Cases

This skill should prevent these failures:

- **Label-driven rejection:** an artifact is rerun only because it was called exploratory or decision-support, even though its dataset, config, metrics, visuals, and provenance may satisfy the current contract.
- **Stale duplicate authority:** a backlog item says "fresh run required" while a governing design allows audit/recover/promote.
- **Prompt amplification:** a generic planning prompt faithfully preserves over-specific or stale wording from a selected item.
- **Routing mismatch:** human-readable roadmap or backlog prose disagrees with the selector manifest, queue state, or workflow state.
- **Discoverability gap:** a result exists, but canonical indexes or summaries do not make it findable enough for future work.

## Contract Drift Sweep

When a pass changes or stabilizes a durable concept, derive its concept
footprint before patching dependent surfaces.

The footprint includes:

- names: public terms, symbols, fields, statuses, commands, files, artifacts;
- roles: producer, consumer, owner, authority, reviewer, runtime, adapter;
- states: lifecycle labels, terminal outcomes, failure modes, waivers;
- boundaries: public/internal, normative/informative, runtime/authoring,
  generated/authored, semantic/view;
- evidence: required artifacts, reports, manifests, tests, snapshots, run state;
- examples: snippets, templates, fixtures, prompts, guides, compatibility docs.

Use that footprint to run a focused sweep across the relevant authority chain:
specs, system architecture, implementation architecture, design docs, plans,
authoring guides, prompts, workflow definitions, templates, fixtures, manifests,
indexes/catalogs, and generated evidence references.

Patch stale restatements, examples, status labels, routing entries, and open
questions so they point to the same owning contract. Preserve intentional
legacy or compatibility wording only when it is explicitly labeled and mapped
to the current concept.

## Process

1. State the disputed behavior in one sentence.
   Example: "The workflow is rerunning FFNO instead of auditing the existing row."

2. Find authority surfaces.
   Check only the relevant set:
   - specs or repo policy
   - roadmap and steering docs
   - design docs
   - backlog item frontmatter and body
   - execution plan
   - workflow YAML and prompts
   - selector or manifest scripts
   - queue state, run state, or artifact manifests
   - durable summaries and docs indexes

3. Classify the inconsistency.
   Use these labels in notes or the final report:
   - `semantic_conflict`: two sources require different behavior
   - `stale_duplicate`: old wording survived after authority changed
   - `over_specific_instruction`: wording forces one implementation path unnecessarily
   - `missing_recovery_path`: rerun/block is required when audit or recovery could be valid
   - `label_driven_policy`: labels decide admissibility instead of evidence fields
   - `routing_mismatch`: prose and machine-readable selection state disagree
   - `discoverability_gap`: result exists but is not findable from canonical entry points

4. Decide the source of truth.
   Prefer, in order:
   - normative specs or explicit repo policy
   - current approved design
   - active roadmap or backlog gate
   - durable artifact manifest
   - generated reports and summaries
   - prompt wording or stale duplicated prose

   If the correct rule is missing, write it once in the highest durable surface that governs future behavior.

5. Patch narrowly.
   - Replace label-based rules with contract-based rules.
   - Replace "always rerun" with "audit/recover/promote when complete; rerun on unrecoverable mismatch" when that preserves the contract.
   - Remove or update stale duplicate wording across dependent backlog/design/prompt surfaces.
   - Keep genuine safety gates: provenance, verification, phase boundaries, and claim limits.
   - Update machine-readable routing state when the change affects selection, dependencies, or eligibility.

6. Validate.
   Choose checks that match the touched surface:
   - `rg` over the concept footprint for stale names, examples, status labels,
     unresolved open questions, and missing new-rule coverage
   - `rg` for old contradictory phrases and new rule coverage
   - `git diff` over touched files
   - markdown/frontmatter parse smoke checks
   - JSON/YAML parser checks
   - selector/manifest validators when routing changed
   - workflow dry-run or orchestrator smoke check when YAML or prompts changed

7. Report.
   Include:
   - root cause
   - source of truth chosen
   - files changed
   - old rule versus new rule
   - verification run
   - remaining intentional distinctions

## Good Rewrites

Bad:

```text
Do not reuse historical roots as paper evidence.
```

Good:

```text
Do not reuse roots with unrecoverable contract or provenance gaps as paper evidence. A root's original exploratory or decision-support label is not by itself disqualifying if the current audit proves the row contract is complete.
```

Bad:

```text
Run all rows fresh under one output root.
```

Good:

```text
Produce all rows under the locked contract. First audit existing roots; promote them if the contract is satisfied directly or after deterministic recovery. Rerun only rows with actual mismatch or unrecoverable gaps.
```

## Common Mistakes

- Fixing only the selected backlog item while leaving the governing design contradictory.
- Adding a special-case exception when a general contract rule is simpler.
- Weakening evidence requirements instead of making admissibility evidence-based.
- Updating prose but not the selector or manifest that the workflow reads.
- Trusting a status label without checking the producing artifact or manifest.
- Treating prompt wording as authority when it merely repeated stale context.
- Auditing the whole repo by default when context already identifies the
  relevant changed work.
- Pasting implementation churn into specs when status/index docs are the right
  surface.
