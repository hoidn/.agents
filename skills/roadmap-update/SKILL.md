---
name: roadmap-update
description: Use when adding, removing, splitting, reordering, or changing planned roadmap phases, tranches, backlog waves, milestone queues, or workflow-drained project plans.
---

# Roadmap Update

## Overview

Roadmaps usually have both human-readable intent and machine-readable routing state. Update them together, or future agents will follow the stale surface.

Core rule: **do not update roadmap prose without updating every selector, manifest, tranche brief, and index that makes the roadmap executable or discoverable.**

## When to Use

Use this when work changes:

- roadmap phases, tranches, waves, milestones, or dependencies
- project-roadmap files under `docs/plans/`
- tranche or task briefs under `docs/plans/**/tranches/`
- manifests under `state/**/roadmap/`, `state/**/tranche_manifest.json`, or equivalent selector inputs
- backlog or queue manifests that drive workflow selection
- workflow-drained plans where selectors choose the next item

For agent-orchestration workflows, also use `workflow-authoring`.

## Required Pass

1. Find the authoritative surfaces:
   - project brief or seed item
   - roadmap prose
   - tranche/task briefs
   - machine-readable manifest or queue
   - selector/update scripts
   - docs index or navigation files
   - active workflow run state, if any

2. Decide source of truth before editing.
   - If the workflow regenerates the manifest from a roadmap phase, rerun or resume that phase instead of hand-editing derived state.
   - If the workflow drains from an existing manifest, update the manifest directly and validate it.
   - Treat historical snapshots like `*.pre-drain-*` as provenance unless the workflow explicitly reads them.

3. Update human-readable roadmap artifacts.
   - Add, remove, split, or reorder sections in the roadmap prose.
   - Create or update each tranche/task brief referenced by the roadmap.
   - Keep dependency rationale and completion gates aligned with the new structure.

4. Update machine-readable routing artifacts.
   For major-project tranche manifests, each new tranche needs:

   ```text
   tranche_id
   title
   brief_path
   design_target_path
   design_review_report_target_path
   plan_target_path
   plan_review_report_target_path
   execution_report_target_path
   implementation_review_report_target_path
   item_summary_target_path
   prerequisites
   status
   design_depth
   completion_gate
   ```

   Use `pending` for new work. Preserve `completed` tranche metadata such as `last_item_outcome`, `last_execution_report_path`, and `last_item_summary_path`. Do not mark work completed because the prose exists.

5. Check active-run safety.
   - Inspect whether the running selector reads the manifest live or uses a cached artifact.
   - If an active run is between selector iterations, update before the next selection.
   - If a provider or script may overwrite the file from stale state, pause/resume or wait for the current update step to finish before editing.
   - Do not edit unrelated run snapshots to force a result.

6. Validate deterministically.
   Prefer the project’s validator/selector scripts. For agent-orchestration major-project manifests:

   ```bash
   python workflows/library/scripts/validate_major_project_tranche_manifest.py \
     --root <repo> \
     --project-brief-path <brief> \
     --project-roadmap-pointer <file containing roadmap path> \
     --tranche-manifest-pointer <file containing manifest path> \
     --state-root <tmp validation dir>

   python workflows/library/scripts/select_major_project_tranche.py \
     --root <repo> \
     --project-brief-path <brief> \
     --project-roadmap-path <roadmap> \
     --tranche-manifest-path <manifest> \
     --state-root <state root> \
     --output-bundle <tmp selection json>
   ```

   Also run `python -m json.tool` or the repo’s structured parser on JSON/YAML files you edited.

7. Check discoverability.
   If you created durable docs, specs, roadmap files, or generated projections that future agents should find, update relevant indexes such as `docs/index.md`.

8. Report the routing effect.
   State the before/after tranche count, ready/pending/completed/blocked counts, next selected item, and whether an active workflow picked up or should pick up the change.

## Common Mistakes

- Updating `docs/plans/...roadmap.md` but not `state/.../tranche_manifest.json`.
- Adding manifest entries without creating the referenced brief files.
- Changing dependencies in prose while leaving `prerequisites` stale.
- Editing historical pre-run snapshots instead of the live selector input.
- Marking new work `completed` because it has a design, plan, or brief.
- Forgetting that active workflows may update manifests after a tranche finishes.
- Creating durable roadmap docs without adding them to the project docs index.

## Quick Checks

Before calling the update done:

- The roadmap prose and manifest list the same planned work.
- Every manifest `brief_path` exists.
- Every prerequisite references a known tranche/task.
- The dependency graph is acyclic.
- New work is `pending`.
- Completed work kept its completion metadata.
- The selector chooses the expected next item.
- Any active workflow state was checked for overwrite risk.
