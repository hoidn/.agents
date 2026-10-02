---
name: consistency-quality-pass
description: Use when specs, guides, examples, indices, or documentation routing are inconsistent, stale, hard to discover, or missing the prerequisites and choices a reader needs after changes; or when plans, prompts, configuration, evidence claims, or automated selection logic disagree with their governing contract.
---

# Consistency Quality Pass

Make the project's durable documentation useful, discoverable, and correct so readers can understand the system or complete a task without reconstructing session history.

Start with what the reader needs to understand or do. Agreement alone is not
enough: within the changed concept's scope, the relevant page must explain the
prerequisites, choices, and limits needed to use it, with examples where they
help. Usability of pages outside that scope is reported, not rewritten.

Edit maintained contracts, designs, guides, examples, entry points, and active
selection state. Use historical records as evidence. If a current route
misrepresents history, correct that route; add a short notice to the historical
record only when needed. Preserve its body and results unless the user asks
otherwise. Never rerun an experiment merely to change its label.

References in durable docs should be symbol/path/section-based, not line-number-based; use exact line numbers only for immutable evidence artifacts or when the line itself is the claim under review.

When context already identifies the relevant changed work, start there instead
of auditing repo-wide. Broaden only when those changes point to a stale
contract, index, or authority surface.

Preserve doc boundaries: specs are normative contracts; architecture/design docs
hold durable design choices; status/index/roadmap docs record completion and
discoverability; run artifacts and reports keep execution detail. Promote
ambiguous contracts to specs/design docs, but keep ordinary completion out of
global specs.

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

2. Trace current authority and use.
   Follow the entry point to the owning contract/design, guide, examples, and
   operational consumers: prompts, configuration, and selection state. Trace
   changed names, roles, states, and boundaries across all maintained specs and
   designs that restate the affected contract and their dependents, including
   generated references; do not stop at the initial file list. A plan or roadmap
   belongs here when it governs current decisions; its path or date does not
   decide. Consulting a source does not make it an edit target.

3. Identify the reader-facing problem.
   Describe what readers cannot find, understand, or safely follow: conflicting
   rules, missing guidance, stale examples, unnecessary restrictions, or a
   misleading route. No classification labels are required.

4. Decide the source of truth.
   Follow the project's authority rules. Governing specs, policy, and approved
   designs outrank summaries or copied prompt wording. Plans supply scoped
   decisions and evidence; put lasting guidance in the appropriate maintained
   spec, design, or guide. If a rule was decided but never written, record it
   once in the highest durable surface that governs future behavior; do not
   invent policy to fill a documentation gap.

5. Patch narrowly.
   - Correct the owning contract where needed, then reconcile other maintained
     specs and designs, guides, examples, summaries, indices, and operational
     consumers within the changed concept's scope.
   - Distinguish current instructions from explicitly scoped historical records;
     prefer a clear pointer over another copy of the same rule.
   - Replace label-based rules with contract-based rules.
   - Replace "always redo" with "audit/recover/promote when complete; redo on unrecoverable mismatch" when that preserves the contract.
   - Reconcile stale restatements and open questions with current authority;
     retain proposed work or limitations only when that authority supports them,
     without inventing narrower meanings for obsolete claims.
   - Keep genuine safety gates: provenance, verification, phase boundaries, and claim limits.
   - Update machine-readable routing state when the change affects selection, dependencies, or eligibility.

6. Validate.
   Choose checks that match the touched surface:
   - follow the relevant entry-point-to-contract-to-guide paths as a new reader;
     confirm the destinations, descriptions, status, and authority agree
   - check local links and section anchors, and compare documented commands,
     defaults, and examples with the owning contract and implementation
   - search maintained specs, designs, and their dependents for old/new terms
     and semantically equivalent claims; resolve paths, selectors, and commands
     needed to use or verify the changed guidance. Preserve intentional legacy
     behavior with its explicit scope. Historical citation chains do not expand
     edit scope
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
