---
name: writing-workflow-guides
description: Use when asked to write a guide, how-to, README section, or workflow page that a reader will follow to reproduce a task (obtain or build a dataset, train, evaluate, run a tool), especially in a repository with study runners, sealed artifact roots, or machine-specific paths. Also use when a reader asks "is there a guide or example for X".
---

# Writing Workflow Guides

A workflow guide is one runnable path from nothing to the result, written
for a stranger with a fresh clone on another machine. It is not a tour of
the tools that were last used on the subject.

## The page

1. **Title is the subject.** The thing the reader has or wants (a dataset,
   a task), never a tool, runner, or the model that was last trained on it.
2. **Two-line purpose.** What the reader ends up with.
3. **What it is.** At most 120 words of prose, plus one table or one
   layout block. Name the file or data contract the subject follows so the
   reader knows what else can read it. Internals of the tools belong in
   "What happens", after the example.
4. **Numbered steps, from nothing.** Step 1 obtains the inputs: every
   route the reader might take (copy, rebuild, build from source), each as
   prose plus at most one command block, with sizes, durations, and external
   inputs named. Later steps do the work and end at the result.
5. **Exactly one script.** The page contains one script or one command
   sequence, shown in full, with its knobs as named constants at the top,
   that the reader saves and runs unchanged. If obtaining an input needs
   code, that code is part of this script, not a second one. Fragments
   that share a variable across sections, and "save a file with these
   fields" left to the reader, are not the script.
6. **What happens.** One bullet per stage of the script: what it does and
   what it writes. Point to where the exact or published recipe lives
   instead of restating it.
7. **Interpret or compare.** Where the reference numbers are and what makes
   a new result comparable to them.
8. **Optional steps last.** Each under its own heading with one sentence
   saying who needs it, and at most one command block. Code an optional
   step needs goes into the one script behind a constant, not into the
   section. If nobody in the audience needs it, leave it out.

Budget: 800 words outside code blocks.

## Vocabulary

Backticked text outside code blocks is one of four things: a path the
reader opens, a command the reader types, a field name the reader reads or
writes, or a name that appears in the page's script. Finding IDs, contract
versions, helper and internal function names, subcommands the reader never
types, and document anchors are written as prose ("the maintained
evaluator", "the published tables") or not at all.

Paths are relative to the repository or to a `ROOT` the reader chooses.
Nothing outside the repository is assumed to exist. If the author's machine
holds a prebuilt input, the guide still tells the reader how to get one.
Instructions given to the author (environment paths, interpreter locations)
are not copied into the page.

## Verification

Run the script and every command line in the page before delivering it, on
the published inputs at a reduced budget where the real run is long, and fix
the page to match what actually ran. A guide whose script has not been
executed is a draft. Record what was run and at what budget in the delivery
message, not in the page.

## Before delivering

Measure the page; do not estimate it:

```bash
awk '/^```/{c=!c;next} !c' GUIDE.md | wc -w                       # under 800
awk '/^```/{c=!c;next} !c' GUIDE.md | grep -o '`[^`]*`' | sort -u  # read every item
grep -n '[A-Z][A-Z]*-[A-Z-]*[0-9][0-9][0-9]\b' GUIDE.md            # finding IDs: prints nothing
```

- Fresh clone on another machine: does every path and input resolve?
- Top to bottom: does the reader reach the result without leaving the page?
- Count the scripts: one. "What it is" prose: under 120 words.
- Every item the second command prints: opened, typed, read/written by the
  reader, or in the script? If not, prose or delete.
- Every step: required for the result? If not, Optional with its reason.
- Title and script: about the subject, or about one tool or model?
- Did the script run, as written?

## Common mistakes

| Mistake | Fix |
|---|---|
| Documenting the runner's subcommands in sequence | Describe the reader's steps; name a subcommand only where typed |
| Absolute or artifact-root paths from the author's machine | `ROOT` chosen by the reader, plus a route to obtain the inputs |
| A dataset guide built around the last model used on it | The dataset is the subject; the model is a constant in the script |
| Reference sections (train, reconstruct, score) instead of a sequence | One script, one flow, one result |
| A second script for a sanity check or an input route | Fold it into the one script or describe it in prose |
| A step included because it exists | Optional section with the one-sentence reason, or gone |
| Snippet never executed; a setting the door rejects | Run it; the page shows what ran |
