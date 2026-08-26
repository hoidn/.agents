---
name: git-bisect-debugging
description: Use when hunting a regression's origin with git bisect — especially long ranges, ML/integration tests, or shared working trees. Covers endpoint verification, exit-code discrimination, environment-era shims, untracked-file checkout collisions, disposable clones, and the cleanup contract.
---

# Git Bisect Debugging

Battle-tested process for `git bisect run` over long commit ranges. Every rule here was paid for by a real failure (PtychoPINN, 2026-07-02: 753-commit range, ML integration test, ~5 min/step — see Worked Example at the end).

**Core principle:** a bisect is an experiment. Verify the instrument (endpoints + script) before running it, keep every step auditable (per-step logs), and leave the lab clean (reset contract). A bisect that starts before both endpoints are verified wastes its entire runtime if the topology is wrong.

## Phase 0 — Before anything else

1. **Rule out test/fixture drift.** If the test compares against a baseline fixture, check whether the fixture or the test itself changed over the range: `git log --oneline GOOD..BAD -- <fixture> <testfile>`. A byte-identical fixture across the range proves a genuine code/data regression; a tightened fixture means you're bisecting the wrong thing.
2. **Check standing rules and tree ownership.** Is the working tree shared with parallel work (other agents, running workflows, dirty submodules)? Does the project ban worktrees or clones? If the mechanically-correct approach conflicts with a standing rule, ask the human ONE crisp question with concrete options — do not work around the rule, and do not burn round-trips relaying authorization through intermediaries.
3. **Estimate cost.** steps ≈ log2(range) + endpoint runs. At 5 min/step, 750 commits ≈ 12 runs ≈ 1 h. If the test is stochastic (ML training), confirm it's seeded; plan to re-run boundary commits 2–3× if the signal looks noisy.

## Phase 1 — Write the run script FIRST

Template (adapt paths; keep the structure):

```bash
#!/usr/bin/env bash
# git bisect run semantics: 0=good, 1=bad, 125=skip. NEVER let 126/127 leak
# (shell emits them for missing/non-executable scripts and git reads them as BAD).
set -u
REPO=/abs/path/to/tree-under-test        # the CLONE if using one — never mix
PY=/abs/path/to/env/python               # absolute; PATH python may differ in subprocesses
LOGDIR=/abs/path/to/scratch/bisect_logs; mkdir -p "$LOGDIR"
cd "$REPO" || { echo "SKIP cannot cd"; exit 125; }

export PYTHONPATH="$REPO"                # environment-era shim — see Snag 2

SHA=$(git rev-parse --short HEAD); LOG="$LOGDIR/step_$(date +%H%M%S)_${SHA}.log"
echo "=== step $SHA $(date) ===" | tee "$LOG"

# Preconditions that make a commit UNTESTABLE (not bad): missing submodule
# content, missing data deps. Check them explicitly -> 125.
[ -f path/to/required/submodule_file ] || { echo "SKIP($SHA): submodule missing" | tee -a "$LOG"; exit 125; }

# Fresh per-step scratch: stale artifacts from another commit poison results
# (memory-mapped caches, generated datasets). Delete ONLY this test's scratch.
rm -rf .artifacts/path/to/this-tests-scratch

"$PY" -m pytest path/to/test.py::the_one_test -q -p no:cacheprovider >>"$LOG" 2>&1
RC=$?
echo "pytest rc=$RC" | tee -a "$LOG"
[ "$RC" -eq 0 ] && { echo "RESULT good($SHA)" | tee -a "$LOG"; exit 0; }

# BAD only for THE failure under investigation — grep its specific signature.
if grep -qE 'assert cur_amp|assert cur_phase' "$LOG"; then   # <- your signature here
  echo "RESULT bad($SHA)" | tee -a "$LOG"; exit 1
fi
# Everything else (ImportError, CLI flag missing, collection error, missing
# outputs) = infrastructure -> conservative SKIP.
echo "RESULT skip($SHA): non-target failure" | tee -a "$LOG"; exit 125
```

Non-negotiables baked in above:
- **Exit-code discrimination by log signature, not raw pytest rc.** A failing test that fails for a *different* reason than the regression is a skip, not a bad. Grep for the exact assertion/message under investigation.
- **Per-step unique logs** (timestamp + SHA). The root-cause analysis works from these; without them a 10-step run is unauditable.
- **One test selector**, `-p no:cacheprovider`, absolute interpreter path.

## Phase 2 — Verify BOTH endpoints with the script itself

Run the script manually at BAD and at GOOD (plain `git checkout`, or in the clone) **before** `git bisect start`:
- BAD must exit **1** — failing *on the target signature*, not merely failing.
- GOOD must exit **0** — actually passing, not skipping.

**If GOOD returns 125, suspect environment-era drift (Snag 2) before walking endpoints back.** A 125 at an endpoint predicts 125s across a large slice of the range — diagnose it now, not 6 steps in.

## Phase 3 — Run

```bash
git bisect start && git bisect bad <BAD> && git bisect good <GOOD>
git bisect run bash /abs/path/bisect_run.sh
```
- Launch as ONE tracked background job and **block on / get notified by that job**. Never detach-and-poll, never park expecting a callback from an untracked process (`cmd & pid=$!; wait "$pid"` if scripting the wait; `tail --pid=<PID> -f /dev/null` to watch a process you didn't start).
- Delegate the *analysis* of large logs/diffs to a fresh agent; the run itself emits only small verdict lines.

## Phase 4 — After first-bad

1. **Skip-adjacency honesty:** if the first-bad commit is adjacent to 125-skipped commits, the true first-bad may be among the skips — report the narrowed range, not false precision.
2. **Root-cause, don't just name the SHA:** read the first-bad diff; classify the mechanism (code regression / data-pipeline change / test-or-fixture tightening / combination); verify the mechanism explains the ORIGINAL failure at HEAD (a first-bad commit whose change was later reverted/superseded does not explain HEAD — look for compounding regressions).
3. **Cleanup contract (always, even on abort):** `git bisect reset`; verify `git rev-parse --abbrev-ref HEAD` and `git rev-parse HEAD` match the pre-bisect branch/SHA; `git status --porcelain` clean of tracked changes; delete any clone.

## Snag catalog (detection → fix)

### Snag 1: Untracked-file checkout collision
**Symptom:** `git bisect good <sha>` (or the first `git bisect run` step) aborts: "The following untracked working tree files would be overwritten by checkout".
**Cause:** generated artifacts were once *tracked*, later untracked (a "chore: untrack …" commit). Every commit before that untracking still tracks those paths; your tree has them untracked → git refuses to overwrite. Can affect 90%+ of a range.
**Fix (in order of preference):** (a) **disposable local clone** (Snag 4) — collisions are harmless in a clone that starts clean; (b) temporarily *relocate* (never delete) the colliding data — only with owner's consent, it may belong to a live workflow; (c) narrow the range to commits after the untracking commit — partial answer only. Check which side of the untracking commit the regression likely sits before choosing (c). Never `checkout -f` over data you don't own.

### Snag 2: Environment-era drift (false "untestable")
**Symptom:** old commits fail instantly with ImportError/ModuleNotFoundError/unknown CLI flag — including the GOOD endpoint.
**Cause:** today's environment satisfies HEAD-era code only. Classic case: package not pip-installed; a *later* commit added an in-script `sys.path` bootstrap, so newer commits self-serve while older ones can't import (subtlety: `python -m pytest` puts CWD on sys.path so in-process imports work, but a `python script.py` **subprocess** gets sys.path[0]=script-dir — imports break only in the subprocess).
**Fix:** environment-only shims in the run script (`export PYTHONPATH="$REPO"`, PATH adjustments) — NEVER edits to tracked files. Find the drift by diffing infrastructure between endpoints: `git log -S "sys.path" GOOD..BAD -- <runner>` or compare the file at both SHAs.

### Snag 3: Submodules across the range
**Symptom:** `git submodule update --init --recursive` errors per step ("Failed to recurse into …"), or module content vanishes after checkout.
**Fix:** first check whether the needed submodule's pointer changes in the range at all: `git log --oneline GOOD..BAD -- <submodule-path> | wc -l`. If **0** (common), skip submodule plumbing entirely — verify content exists once; in a clone, `cp -r` the content from the main tree and `rm` the inner `.git` gitfile (a dangling gitfile breaks `git status` in the clone). Only if the pointer moves do you need per-step `git submodule update` (init once from the local cache: `git config submodule.<name>.url /main/repo/.git/modules/<name>` — and if that clone fails "a second time", `rm -rf <clone>/.git/modules/<name>` and fall back to the copy strategy). Init ONLY the submodules the test needs — broken unrelated submodules (auth failures) otherwise poison every step.

### Snag 4: Disposable local clone (the shared-tree escape hatch)
When the main tree is shared (parallel agents, live workflows) or Snag 1 bites:
```bash
git clone /path/main /path/main-bisect-clone   # local => hardlinked objects, fast & cheap
# submodule content per Snag 3; then bisect entirely inside the clone
```
- The run script's `REPO`, `PYTHONPATH`, and `cd` must ALL point at the clone.
- The clone frees the main tree for parallel work — fix waves can proceed simultaneously.
- Check disk first (`df`); a full checkout + per-step artifacts can be GBs. Don't put it on tmpfs.
- Delete the clone in the cleanup phase.
- **A clone may conflict with "no worktrees" project rules in spirit — that's a human's call, not yours (Phase 0.2).**

### Snag 5: Stale cross-commit artifacts
**Symptom:** results flip depending on run order; a commit "passes" using data generated by different-era code.
**Fix:** the run script deletes the test's generated scratch before every step so each commit regenerates its own (see template). Delete only that test's scratch, nothing else.

### Snag 6: Stochastic tests
ML training tests are seeded but still sensitive. If the metric sits near the threshold at some commits, `git bisect run` happily converges on noise. Mitigate: verify endpoints with real margin (0.23 vs 0.096 threshold = safe; 0.10 vs 0.096 = suspect); re-run the two commits flanking the reported first-bad before believing it.

## Worked example (PtychoPINN, 2026-07-02)
753-commit range, 5-min ML integration test. Hit, in order: GOOD endpoint 125 via Snag 2 (`ptycho` not installed + pre-`b069bfaa` commits lack the runner's sys.path bootstrap; fixed with `export PYTHONPATH=$REPO`); Snag 1 via `state/NEURIPS-…` (54MB/6834 files, tracked until `9ab90eb7`, collided on 678/753 commits); resolved via Snag 4 clone (user explicitly overrode the project's no-worktree rule) with Snag 3 FRC-submodule copy (`cp -r` + `rm ptycho/FRC/.git`, pointer unchanged in range); Snag 5 handled by per-step `rm -rf .artifacts/integration/grid_lines_hybrid_resnet`. Process failures to avoid repeating: launching the run detached and "parking" for a callback that never comes (three separate stalls), and starting endpoint verification before diagnosing why an endpoint might be untestable.
