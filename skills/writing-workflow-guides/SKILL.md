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
3. **What it is.** The subject in a short paragraph and, where it helps,
   one table and one layout block. State the file or data contract the
   subject follows so the reader knows what else can read it.
4. **Numbered steps, from nothing.** Step 1 obtains the inputs: every
   route the reader might take (copy, rebuild, build from source), with
   sizes, durations, and external inputs named. Later steps do the work and
   end at the result. Each step is one command block or one script.
5. **One complete example, shown in full.** A single script or command
   sequence with its knobs as named constants at the top, that the reader
   can save and run unchanged. Not fragments sharing a variable across
   sections; not "save a file with these fields" left to the reader.
6. **What happens.** One bullet per stage of the example saying what it
   does and what it writes. Point to where the exact or published recipe
   lives instead of restating it.
7. **Interpret or compare.** Where the reference numbers are and what makes
   a new result comparable to them.
8. **Optional steps last.** Each under its own heading with one sentence
   saying who needs it. If nobody in the audience needs it, leave it out.

## Vocabulary

Write in the reader's terms. An internal name (subcommand, study runner,
finding ID, workspace path, arm name) appears only where the reader must
type it or open it. Everywhere else, say what it does in words.

Paths are relative to the repository or to a `ROOT` the reader chooses.
Nothing outside the repository is assumed to exist. If the author's machine
holds a prebuilt input, the guide still tells the reader how to get one.

## Verification

Run every command and snippet in the page before delivering it, on the
published inputs at a reduced budget where the real run is long, and fix
the page to match what actually ran. A guide whose example has not been
executed is a draft. Record what was run and at what budget in the
delivery message, not in the page.

## Before delivering

- Fresh clone on another machine: does every path and input resolve?
- Top to bottom: does the reader reach the result without leaving the page?
- Every internal name: does the reader type it? If not, translate or delete.
- Every step: required for the result? If not, move it under Optional with
  its reason.
- Title and examples: about the subject, or about one tool or model?
- Did the example run, as written?

## Common mistakes

| Mistake | Fix |
|---|---|
| Documenting the runner's subcommands in sequence | Describe the reader's steps; name a subcommand only where typed |
| Absolute or artifact-root paths from the author's machine | `ROOT` chosen by the reader, plus a route to obtain the inputs |
| A dataset guide built around the last model used on it | The dataset is the subject; the model is a constant in the example |
| Reference sections (train, reconstruct, score) instead of a sequence | One script, one flow, one result |
| A step included because it exists | Optional section with the one-sentence reason, or gone |
| Snippet never executed; a setting the door rejects | Run it; the page shows what ran |
