---
name: design-spec-drafting
description: Use when drafting or revising specs, system architecture, implementation architecture, design docs, or plans where the governing docs must be selected from repository context.
---

# Design Spec Drafting

Before drafting or revising a spec, system architecture, implementation
architecture, design doc, or plan:

1. Read the repo's `docs/index.md`.
2. Use its reading paths, clarification table, and linked entries to choose the
   relevant referenced `.md` files.
3. Read only the docs relevant to the in-context design type:
   - specs: normative `specs/` surfaces and linked explanatory docs;
   - system architecture: governing system/design docs and any required spec
     deltas;
   - implementation architecture: the accepted parent design, templates, plans,
     and implementation-handoff docs;
   - ordinary design/planning: closest existing design docs, active plans, and
     referenced policy or evidence docs.
4. Draft against those authorities. If ownership is unclear, state which doc
   should own the contract before editing.

## Feasibility Proof Trigger

When drafting or reviewing a design or architecture doc, check whether it relies
on an unproven capability claim.

Require a short feasibility proof, or mark the claim as an open prerequisite,
when the design depends on:

- replacing a special-case path with a generic mechanism;
- combining subsystems in a shape not covered by existing specs or fixtures;
- preserving a public API while changing its implementation substrate;
- a type, lowering, state, resume, runtime, or source-map capability that is not
  already specified or tested;
- a negative architecture claim such as no compiler-special branch, no hidden
  input, no runtime ref value, or no report parsing.

The proof should identify the relevant spec/design/test authority and either
show a minimal executable fixture or record the missing capability as a
design gap.

Specs document accepted capability contracts only.

Do not rely on memory when `docs/index.md` routes to a current source of truth.
