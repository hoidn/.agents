---
name: merge-target-design-into-baseline
description: Use when a completed target design, migration design, architecture delta, or implementation target must be incorporated into an authoritative baseline spec or system design.
---

# Merge Target Design Into Baseline

## Overview

Merge completed target designs by promoting durable implemented contracts into
the baseline. Do not copy tranche history, live workflow status, or temporary
evidence narration into an authoritative design.

The core question is: "What is now true about the system?" not "What work just
finished?"

## Required Flow

1. Find the authority graph.
   - Read the repo routing docs first, such as `docs/index.md`,
     design indexes, capability matrices, and relevant `AGENTS.md`.
   - Identify the baseline document that should own the durable contract.
   - Identify target docs that are completed, still active, or historical.

2. Audit before editing.
   - Compare target-design claims against current implementation evidence,
     tests, specs, docs, and commit history.
   - Separate implemented contracts from planned, partial, compatibility, or
     migration-only claims.
   - Preserve old defaults in the baseline only when implementation still
     conserves them as current defaults or explicit compatibility behavior.
   - If the target says "complete" but evidence is unclear, keep the claim out
     of the baseline or phrase it as an evidence requirement.

3. Merge semantics, not chronology.
   - Add or revise baseline language for durable behavior, interfaces,
     invariants, validation rules, source-map/provenance rules, runtime
     ownership, and compatibility boundaries.
   - Replace stale future wording such as "blocked until X lands" with current
     baseline wording such as "X is the consumed substrate; regressions
     invalidate promotion evidence."
   - Keep unfinished target work in the target or roadmap docs.

4. Remove target-era framing from baseline docs.
   - Avoid phrases like "G8 is done", "current drain", "active manifest lane",
     "recently landed", "this tranche", "implementation just completed", or
     "current checkout status" unless the baseline explicitly documents a
     stable compatibility lane.
   - Prefer descriptive contract language: "runtime-native transitions are the
     semantic route"; "certified adapters are compatibility backends"; "views
     are representations, not semantic authority."

5. Reconcile companion docs.
   - Update routing/index docs so readers know which doc is authoritative.
   - Update drafting guides and capability matrices when they would otherwise
     teach old behavior.
   - If a target doc remains, mark it as incorporated, historical, or a
     companion decision record rather than leaving it as an active replacement
     for the baseline.

6. Verify and commit narrowly.
   - Run markdown/diff checks available in the repo, at minimum
     `git diff --check` for edited docs.
   - Search for stale phrases introduced or left behind.
   - Stage only the baseline-merge files. Leave unrelated generated plans,
     run artifacts, and dirty worktree files alone.

## What To Promote

Promote these when implemented or accepted:

- public language/runtime contracts;
- current compiler pipeline and default route;
- typed data and effect models;
- resource, context, state, path, resume, and provenance ownership;
- validation and diagnostic rules;
- compatibility boundaries and deprecation direction;
- durable authoring guidance.

Keep these out of the baseline:

- implementation tranche schedules;
- one-run workflow status;
- "done" claims without durable contract meaning;
- temporary adapter names unless they define a stable compatibility boundary;
- review/fix iteration history;
- generated backlog, plan, or report narration;
- speculative future work not yet accepted.

## Audit Checks

- Routing docs are not enough; the authoritative baseline must describe the
  current contract.
- Superseded behavior appears only when implementation still supports it as a
  current default or explicit compatibility boundary.
- Compatibility behavior is labeled as compatibility, not as the default.
- Capability existence is distinct from adoption by every workflow family.
- Stale wording can survive in detailed sections after top-level summaries are
  corrected.

## Quick Checklist

- Baseline owns the durable post-target behavior.
- Target doc no longer reads as the only place to learn current behavior.
- Superseded old defaults appear only when conserved as explicit compatibility.
- Active target work remains separate from completed baseline contracts.
- No tranche/run-history language leaks into authoritative specs.
- Verification output is fresh.
- Commit scope contains only relevant docs.
