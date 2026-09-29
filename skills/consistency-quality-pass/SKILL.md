---
name: consistency-quality-pass
description: Use when specs, guides, examples, indices, or documentation routing are inconsistent, stale, or hard to discover after changes; or when plans, prompts, configuration, evidence claims, or automated selection logic disagree with their governing contract.
---

# Consistency Quality Pass

Keep current specs, designs, guides, examples, indices, and reading paths consistent and up to date so the next reader can find and follow the governing contract without reconstructing session history.

Default priority: fix durable documentation and discoverability before tidying historical artifacts. Prefer the highest durable authority over stale duplicated wording, without weakening provenance, verification, or claim boundaries. An explicit user scope, including an artifact-only task, takes precedence.

References in durable docs should be symbol/path/section-based, not line-number-based; use exact line numbers only for immutable evidence artifacts or when the line itself is the claim under review.

When context already identifies the relevant changed work, start there instead
of auditing repo-wide. Broaden only when those changes point to a stale
contract, index, or authority surface.

Preserve doc boundaries: specs are normative contracts; architecture/design docs
hold durable design choices; status/index/roadmap docs record completion and
discoverability; run artifacts and reports keep execution detail. Promote
ambiguous contracts to specs/design docs, but keep ordinary completion out of
global specs.

Historical artifacts are evidence for resolving current documentation, not the
default editing queue. Preserve their recorded configuration and results; fix
their presentation when a current route misrepresents them or the user requests
it. Relabeling old PNGs, regenerating reports, or writing a new audit summary
does not substitute for correcting the owning docs and their reader-facing
routes. Do not re-execute experiments merely to align historical labels.

## Index And Catalog Surfaces

Index, catalog, map, README, manifest, and hub documents are discoverability
authorities, not semantic authorities. They route readers to the current source
of truth across specs, design docs, plans, artifacts, prompts, workflows, and
runtime evidence.

Start from the relevant canonical entry points (such as the documentation hub,
README, or study index), then follow their links to the owning contract and
applicable guide. Check these routes when behavior, defaults, commands, status,
or ownership changes, even if no file was renamed. A working link to a stale
recipe or superseded authority is still a routing defect.

Treat stale or missing routing as `discoverability_gap`.

Patch index/catalog surfaces as routing layers: descriptions, links, status
labels, reading paths, and clarification pointers. Behavior and policy should be
owned by the linked spec, design doc, plan, artifact manifest, or runtime
evidence.

## Pressure Cases

This skill should prevent these failures:

- **Current-doc drift:** a spec adopts a new default while the guide's example still teaches the old one.
- **Stale reading path:** a hub, index, or README leads readers to a superseded plan or omits the current guide.
- **Artifact-first distraction:** many historical labels are corrected while current guides, specs, and indices still disagree.
- **Label-driven rejection:** an artifact is redone only because of how it was once labeled (e.g. "draft", "exploratory"), even though its inputs, configuration, results, and provenance may satisfy the current contract.
- **Stale duplicate authority:** a task item says "must be redone from scratch" while a governing design allows audit/recover/promote.
- **Prompt amplification:** a generic planning prompt faithfully preserves over-specific or stale wording from a selected item.
- **Routing mismatch:** human-readable roadmap or task prose disagrees with the machine-readable selection, queue, or workflow state.
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

1. Bound the work and state what must agree.
   For "yesterday's work", recover the changed concepts from the diff, plans,
   or session history, then trace their durable docs; do not default to an
   artifact inventory. Example: "The approved default changed, but the guide
   and its index entry still teach the previous recipe."

2. Find authority surfaces.
   Check only the relevant set:
   - specs or repo policy
   - roadmap and steering docs
   - design docs
   - current user/developer guides, commands, examples, and templates
   - durable summaries, docs indices, README links, and reading paths
   - task/backlog item metadata and body
   - execution plan
   - workflow definitions and prompts
   - automation that selects or routes work
   - queue state, run state, or artifact manifests

3. Classify the inconsistency.
   Use these labels in notes or the final report:
   - `semantic_conflict`: two sources require different behavior
   - `stale_duplicate`: old wording survived after authority changed
   - `over_specific_instruction`: wording forces one implementation path unnecessarily
   - `missing_recovery_path`: redo/block is required when audit or recovery could be valid
   - `label_driven_policy`: labels decide admissibility instead of evidence fields
   - `routing_mismatch`: prose and machine-readable selection state disagree
   - `discoverability_gap`: result exists but is not findable from canonical entry points

4. Decide the source of truth.
   Prefer, in order:
   - normative specs or explicit repo policy
   - current approved design
   - active roadmap or task gate
   - durable artifact manifest
   - generated reports and summaries
   - prompt wording or stale duplicated prose

   If the correct rule is missing, write it once in the highest durable surface that governs future behavior.

5. Patch narrowly.
   - Correct the owning contract where needed, then reconcile dependent guides,
     examples, summaries, indices, and routes within the changed concept's scope.
   - Distinguish current instructions from explicitly scoped historical records;
     prefer a clear pointer over another copy of the same rule.
   - Replace label-based rules with contract-based rules.
   - Replace "always redo" with "audit/recover/promote when complete; redo on unrecoverable mismatch" when that preserves the contract.
   - Remove or update stale duplicate wording across dependent task/design/prompt surfaces.
   - Keep genuine safety gates: provenance, verification, phase boundaries, and claim limits.
   - Update machine-readable routing state when the change affects selection, dependencies, or eligibility.

6. Validate.
   Choose checks that match the touched surface:
   - follow the relevant entry-point-to-contract-to-guide paths as a new reader;
     confirm the destinations, descriptions, status, and authority agree
   - check local links and section anchors, and compare documented commands,
     defaults, and examples with the owning contract and implementation
   - text search over the concept footprint for stale names, examples, status
     labels, unresolved open questions, and missing new-rule coverage
   - text search for old contradictory phrases and new rule coverage
   - `git diff` over touched files
   - parse/syntax smoke checks for any machine-readable files touched
   - validators for selection or routing state when routing changed
   - dry-run or smoke check when workflow definitions or prompts changed

7. Report.
   Include:
   - current documentation and discoverability gaps fixed, then any artifact changes
   - root cause
   - source of truth chosen
   - files changed
   - old rule versus new rule
   - verification run
   - remaining intentional distinctions

   A documentation pass is not complete while known in-scope contradictions
   remain in current docs or canonical routes still lead to obsolete guidance.
   This does not require a repo-wide audit or cosmetic normalization of history.

## Good Rewrites

Bad:

```text
The implementation uses the new default; the historical report now says "old".
```

Good:

```text
The owning contract, current guide and runnable example describe the new default; the index routes to them. The historical report keeps its original settings and is identified as history where current docs cite it.
```

Bad:

```text
Regenerate all deliverables from scratch in one new location.
```

Good:

```text
Produce all deliverables under the locked contract. First audit existing ones; promote them if the contract is satisfied directly or after deterministic recovery. Regenerate only those with actual mismatch or unrecoverable gaps.
```

## Common Mistakes

- Spending the pass on historical labels while current specs, guides, examples, or indices remain inconsistent.
- Writing a new report instead of fixing the docs that future readers actually use.
- Checking that links resolve without checking whether they route to the current authority and recipe.
- Fixing only the selected task item while leaving the governing design contradictory.
- Adding a special-case exception when a general contract rule is simpler.
- Weakening evidence requirements instead of making admissibility evidence-based.
- Updating prose but not the machine-readable state the automation reads.
- Trusting a status label without checking the producing artifact or manifest.
- Treating prompt wording as authority when it merely repeated stale context.
- Auditing the whole repo by default when context already identifies the
  relevant changed work.
- Pasting implementation churn into specs when status/index docs are the right
  surface.
