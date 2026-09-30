---
name: consistency-quality-pass
description: Use when specs, guides, examples, indices, or documentation routing are inconsistent, stale, or hard to discover after changes; or when plans, prompts, configuration, evidence claims, or automated selection logic disagree with their governing contract.
---

# Consistency Quality Pass

Make the project's durable documentation useful, discoverable, and correct so readers can understand the system or complete a task without reconstructing session history.

Start with what the reader needs to understand or do. Agreement alone is not
enough: the relevant page must explain the prerequisites, choices, and limits
needed to use it, with examples where they help.

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

Historical artifacts inform current documentation; they are not the default
editing queue. Preserve recorded configurations and results; fix presentation
when current routes misrepresent them or the user requests it. Do not re-execute
experiments merely to align historical labels.

## Index And Catalog Surfaces

Indices, catalogs, READMEs, manifests, and hubs route readers to current
authority; they do not independently define behavior or policy.

Start from the relevant canonical entry points (such as the documentation hub,
README, or study index), then follow their links to the owning contract and
applicable guide. Check these routes when behavior, defaults, commands, status,
or ownership changes, even if no file was renamed. A working link to a stale
recipe or superseded authority is still a routing defect.

Patch their descriptions, links, status labels, and reading paths. Keep the
rules in the linked owning document rather than duplicating them in the index.

## Pressure Cases

This skill should prevent these failures:

- **Current-doc drift:** a spec adopts a new default while the guide's example still teaches the old one.
- **Stale reading path:** a hub, index, or README leads readers to a superseded plan or omits the current guide.
- **Consistent but unusable:** pages agree but omit prerequisites or choices readers need to perform the task.
- **Artifact-first distraction:** many historical labels are corrected while current guides, specs, and indices still disagree.
- **Routing mismatch:** human-readable roadmap or task prose disagrees with the machine-readable selection, queue, or workflow state.

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

Follow that footprint from the owning contract through dependent guides,
examples, prompts, workflows, and discovery routes, including generated
references where relevant.

Patch stale restatements, examples, status labels, routing entries, and open
questions so they point to the same owning contract. Preserve intentional
legacy or compatibility wording only when it is explicitly labeled and mapped
to the current concept.

## Process

1. Bound the work and state what must agree.
   Derive scope from the affected concepts and contracts, not merely the
   initial file list.
   For "yesterday's work", recover the changed concepts from the diff, plans,
   or session history, then trace their durable docs; do not default to an
   artifact inventory. Example: "The approved default changed, but the guide
   and its index entry still teach the previous recipe."
   Respect explicit scope limits; report affected surfaces outside them rather
   than silently expanding the task.

2. Find authority surfaces.
   Start with the owning spec or design, applicable user/developer guide, and
   reader entry points. Consult plans, prompts, workflow state, or manifests
   when they explain the affected behavior; do not make them the default queue.

3. Identify the reader-facing problem.
   Describe what readers cannot find, understand, or safely follow: conflicting
   rules, missing guidance, stale examples, unnecessary restrictions, or a
   misleading route. No classification labels are required.

4. Decide the source of truth.
   Follow the project's authority rules. Governing specs, policy, and approved
   designs outrank summaries or copied prompt wording. Plans supply scoped
   decisions and evidence; put lasting guidance in the appropriate maintained
   spec, design, or guide. Do not invent policy to fill a documentation gap.

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
   - resolve every cited path, selector, and command in scope by file/symbol
     lookup or safe execution
   - search affected surfaces using former and current terminology, including
     equivalent descriptions of the same rule; check meaning, not just matching
     words, and that the new rule appears wherever a dependent surface restates
     it. Remaining old wording must be consistent with the current contract or
     clearly scoped as historical
   - `git diff` over touched files
   - parse/syntax smoke checks for any machine-readable files touched
   - validators for selection or routing state when routing changed
   - dry-run or smoke check when workflow definitions or prompts changed

7. Report.
   Briefly state what readers can now find or use, where it lives, what was
   checked, and any intentional distinctions, exclusions, or unresolved gaps.

   Distinguish correctness from coverage: report whether inspected surfaces
   agree, and whether the identified changes were traced through their relevant
   authorities, dependents, and discovery routes. Working links, consistent
   inspected files, or approval of a narrow plan do not establish coverage.
   Completion requires resolving known in-scope contradictions and obsolete
   current guidance, not a repository-wide audit.

## Good Rewrites

Bad:

```text
The implementation uses the new default; the historical report now says "old".
```

Good:

```text
The owning contract, current guide and runnable example describe the new default; the index routes to them. The historical report keeps its original settings and is identified as history where current docs cite it.
```

## Common Mistakes

- Writing a new report instead of fixing the docs that future readers actually use.
- Checking that links resolve without checking whether they route to the current authority and recipe.
- Fixing only selected files while dependent guidance remains contradictory.
- Weakening evidence requirements instead of making admissibility evidence-based.
- Updating prose but not the machine-readable state the automation reads.
- Auditing the whole repo by default when context already identifies the
  relevant changed work.
- Pasting implementation churn into specs when status/index docs are the right
  surface.
