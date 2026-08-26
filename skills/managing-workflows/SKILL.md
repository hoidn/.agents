---
name: managing-workflows
description: Use when asked to keep an orchestrator workflow running over time, monitor progress, recover crashes, fix incorrect workflow mechanics, or manage a long-running agent workflow without repeated user prompts.
---

# Managing Workflows

Manage means actively supervising a running workflow until it is healthy, complete, or genuinely blocked. Do not merely report status; inspect behavior, recover mechanical failures, and keep the user informed.

## Core Rules

- Use `launching-workflows` for launch, relaunch, resume, watchdog, tmux, and run-id handling.
- Monitor both persisted run state and live stream output. A run can be technically alive while making the wrong choice.
- Prefer `orchestrator resume <run_id>` after an approved/reviewed stage fails downstream. Relaunch only when restarting earlier stages is intended.
- Kill or ignore stale watchdogs only after confirming their target run id, workspace, and state roots.
- Fix workflow mechanics autonomously when the defect is clear: YAML wiring, checksum/run-state mismatch, stale watchdog targeting, crash recovery, deterministic scripts, artifact paths, validation errors, or workflow-owned routing logic.
- Do not silently change provider prompts while managing. If prompt behavior looks wrong, write proposed prompt edits to `docs/plans/workflow_prompt_change_queue.md` and wait for explicit user approval before applying them.
- Prompt-change proposals should be concrete: file, current problem, suggested edit, expected behavior change, and risk.
- Prefer deterministic workflow/script fixes over prompt fixes when the choice is mechanical: routing, dependency eligibility, stale state, artifact contracts, checksums, and provider context should not be left for a model to infer.
- When prompt changes are necessary, prefer subtractive or replacement edits. Remove misleading instructions, stale nouns, evidence rituals, or broad process checklists before adding new rules.
- Keep prompt proposals minimal and general. Do not add project-specific nouns, one-off examples, negative-command lists, or extra evidence requirements unless the workflow itself is project-specific and the requirement is unavoidable.
- Keep fixes general. Do not encode one project’s noun, run id, target design, or transient failure as policy unless the workflow itself is project-specific.
- Separate product progress from bookkeeping. Treat report, manifest, parity, inventory, and closeout churn as suspicious unless it changes real runtime/product behavior or fixes a concrete contract failure.
- If repeated blocks or revisions occur, step back: identify the loop pattern, the stale assumption, and the smallest general workflow-mechanics fix.

## Monitoring Loop

1. Check status: run state, heartbeat, current step, recent artifacts, and tmux stream.
2. Decide whether behavior is healthy, crashed/stalled, or alive-but-wrong.
3. For crashes/stalls, repair or resume and verify the new run id.
4. For alive-but-wrong behavior, inspect prompts/workflow/scripts enough to identify root cause.
5. Apply mechanical fixes directly; queue prompt fixes in Markdown, favoring deletions or shorter replacements.
6. Run the narrowest validation: dry-run for workflow changes, targeted tests for scripts, status check for resumed runs.
7. Report what changed, what was verified, and whether progress is real.

## Provider Capacity Stalls

Codex provider sessions can stall on `Selected model is at capacity. Please
try a different model.` — the turn ends and the session waits for input. The
deterministic recovery is injecting `proceed` + Enter into the session's tmux
pane.

An installed watchdog automates this:

- Script: `~/.local/bin/capacity-watchdog.sh` (log:
  `~/.local/state/capacity-watchdog.log`)
- Runs as tmux session `capacity-watchdog` on
  `/tmp/claude-tmux-sockets/claude.sock`; relaunch after reboot with
  `tmux -S /tmp/claude-tmux-sockets/claude.sock new -d -s capacity-watchdog "bash ~/.local/bin/capacity-watchdog.sh"`.
- Before manually unblocking a Codex session or starting another supervisor,
  check whether it is already running to avoid double injection.

Detection rules the watchdog encodes (keep these if reimplementing):

- match only the live pane tail (last ~10 lines above the composer); a wider
  capture re-matches stale scrollback and injects into a healthy session;
- never inject while the session shows an active turn (`esc to interrupt`);
- send text and Enter separately with delays, then a second Enter — the Codex
  TUI drops an Enter that follows text too quickly;
- fire once per appearance, re-arm when the message clears, timed retry
  (180s) while it persists.

Current target is the single pane `orchestration:0.1` on
`/tmp/tmux-1000/default`. Intended generalization: enumerate all Codex
provider panes each poll cycle (match on pane command/title) with per-pane
armed/retry state, so workflow-launched provider sessions are covered too.

## Prompt Change Queue

When queuing a prompt change, append:

```markdown
## <date> <workflow/run>

- Prompt file:
- Observed bad behavior:
- Root cause in prompt text:
- Proposed edit:
- Expected behavior change:
- Risk / tradeoff:
```

Do not apply queued prompt edits until the user gives explicit feedback approving the actual prompt change.

Good prompt proposals usually delete or replace confusing text. Bad proposals add a second layer of instructions telling the model not to follow the first layer.

## Common Mistakes

- Treating a watchdog probe as continuous monitoring.
- Restarting instead of resuming after expensive approved stages.
- Trusting status summaries without reading stream output.
- Fixing the current run with hardcoded run-specific policy.
- Letting agents spend cycles proving stale evidence instead of implementing or deleting the relevant behavior.
- Adding prompt complexity to compensate for workflow state that should be filtered, routed, or validated deterministically.
