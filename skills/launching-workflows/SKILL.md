---
name: launching-workflows
description: Use when launching, relaunching, resuming, or monitoring orchestrator workflows, especially when a watchdog, tmux session, long-running provider step, or periodic crash recovery is involved.
---

# Launching Workflows

Use this skill whenever starting or restarting an orchestrator workflow. The
main failure to avoid is launching a one-shot watchdog and thinking it is a
periodic recovery loop.

## Required Flow

1. Validate first.
   - For YAML or `.orc`, run the closest `python -m orchestrator run ... --dry-run`.
   - Fix validation errors before launching a long run.

2. Launch the workflow in tmux.
   - Use the `tmux` skill.
   - Use a clear session name.
   - Include `--stream-output` for live inspection.
   - Enable observability flags when useful: `--step-summaries`, summary provider, and `--live-agent-notes`.

3. Capture the actual run id.
   - Read it from tmux output: `Created new run: <run_id>`.
   - Confirm `.orchestrate/runs/<run_id>/state.json` exists.
   - Do not point watchdogs at an old failed run unless deliberately repairing that old run.

4. Start the watchdog as a real loop.
   - A single `python -m orchestrator run workflows/examples/generic_run_watchdog.yaml ...` is only one probe.
   - A watchdog loop must include `while true`, an immediate probe, and `sleep <interval>`.
   - Use target-specific `state_root`, `evidence_root`, and `repair_result_target_path`.

5. Verify both processes.
   - Capture both tmux panes.
   - Check the target run state.
   - Check the first watchdog probe output is `RUNNING_OK`, `COMPLETED`, or a handled repair state.

6. Report monitor commands.
   - Give copyable tmux capture commands for the workflow and watchdog sessions.

## Watchdog Loop Template

```bash
tmux -S /tmp/claude-tmux-sockets/claude.sock new-session -d -s <watchdog-session> \
  "cd <repo> && export PYTHONPATH=<repo>\${PYTHONPATH:+:\$PYTHONPATH}; \
   while true; do \
     echo \"==== \$(date -Iseconds) watchdog probe for <run_id> ====\"; \
     python -m orchestrator run workflows/examples/generic_run_watchdog.yaml \
       --stream-output \
       --input target_run_id=<run_id> \
       --input state_root=state/<owner>/watchdog-<run_id> \
       --input evidence_root=artifacts/work/<owner>/watchdog-<run_id> \
       --input repair_result_target_path=artifacts/work/<owner>/watchdog-<run_id>/repair-result.json \
       --input max_stale_minutes=30; \
     echo \"==== \$(date -Iseconds) watchdog cycle complete; sleeping 1800s ====\"; \
     sleep 1800; \
   done"
```

## Common Mistakes

- Mistaking one watchdog probe for a loop. If there is no `while true`, it is not a watchdog loop.
- Starting the watchdog before the new run id is known, then targeting a stale run.
- Reusing old watchdog state paths, which hides which run was actually probed.
- Checking only tmux output and not `.orchestrate/runs/<run_id>/state.json`.
- Relaunching into an old tmux session whose pane still shows stale output.

## Minimum Status Check

```bash
python - <<'PY'
from pathlib import Path
import json
run = "<run_id>"
p = Path(".orchestrate/runs") / run / "state.json"
d = json.loads(p.read_text())
print("status:", d.get("status"))
print("current_step:", d.get("current_step"))
print("updated_at:", d.get("updated_at"))
PY
```

