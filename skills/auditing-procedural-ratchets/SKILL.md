---
name: auditing-procedural-ratchets
description: Use when instructions, plans, reviews, ledgers, tests, or workflow rules appear to accumulate authority, inflate acceptance scope, turn optional diagnostics into blockers, or force disproportionate process artifacts.
---

# Auditing Procedural Ratchets

## Overview

Treat over-bureaucracy as a causal systems defect, not a prose-cleanup exercise. Restore the smallest authoritative acceptance contract while preserving real safety requirements, factual evidence, and necessary recovery controls.

**Core principle:** repetition, execution, or recording does not promote a tactic or observation into authority.

## When to Use

Use for symptoms such as:

- scope inflation, process creep, or “while here” obligations;
- authorized files being treated as owned modules or mandatory test suites;
- historical reports, reviews, todos, or ledgers becoming completion gates;
- supplemental checks becoming blocking without proving a current-contract violation;
- recovery tactics becoming unconditional plans, reviews, handoffs, or reports;
- agents refusing completion because self-created paperwork is incomplete;
- rules that suppress necessary emergent work because it was absent from the initial checklist.

Do not use to evade an explicit current requirement, affected external contract, safety invariant, or reproducible product failure.

## Non-Negotiable Invariants

1. Current authority defines requirements; artifacts only record or implement them.
2. Preserve observations and contradictory evidence. Correct their authority label or blocking effect, not the fact that they occurred.
3. A required check remains required. A supplemental check blocks only when its result demonstrates a current requirement, affected contract, or sourced safety invariant is violated.
4. Mutation permission does not imply ownership, review admission, test scope, or future maintenance duty.
5. New blocking work requires all four: a concrete trigger, causal link to the current task, affected invariant or deliverable, and explicit closure condition.
6. The audit creates no durable registry, ledger, ticket, dashboard, review cadence, or provenance ceremony unless current authority requires that artifact.
7. This skill governs audit method; it is not a project acceptance source. Deadlines, sunk cost, and management urgency likewise do not create or erase requirements.

## Quick Reference

| Symptom | Ask | Root correction |
|---|---|---|
| A record or tool says “required” | Which current source created the obligation? | Restore traceability or remove the gate |
| Authorized/touched file expands test scope | Which contract or behavior changed? | Test the affected boundary, not file proximity |
| Supplemental failure blocks completion | What current criterion does it falsify? | Block only through that criterion; otherwise disclose |
| Recovery paperwork runs on every task | Is interruption, transfer, or external effect present? | Trigger recovery state conditionally |
| Controller adds work mid-task | Are trigger, causal link, affected invariant, and closure all named? | Admit only when all four exist |

## Audit Workflow

### 1. Freeze the acceptance unit

Write the narrow claim that completion would make. List every requirement needed to substantiate that claim and its authoritative source. Separate:

- required checks;
- optional diagnostics;
- blocking safety or contract invariants;
- factual observations that must be disclosed but do not block.

Do not derive a broader claim from touched files, test proximity, historical practice, or available evidence.

### 2. Build a disputed-source authority map

Map only sources participating in the suspected ratchet:

| Source statement | Class | Actual authority | Legitimate effect | Ratcheted effect |
|---|---|---|---|---|
| Normative spec or explicit user requirement | governing | binding in scope | defines requirement | none |
| Approved current plan or task | delegated/current | binding within higher authority | defines local acceptance | treated as universal precedent |
| Guide or prompt | procedural | subordinate | selects a tactic | silently expands acceptance |
| Report, review, ledger, todo, prior run | descriptive/recovery | no independent normative force | preserves facts or state | becomes a gate |
| Controller, test selector, automation | mechanism | implements authority | executes a sourced rule | mistaken for the rule’s source |
| Audit skill or analysis method | procedural | no project acceptance authority | constrains reasoning | cited as the requirement source |
| Deadline, sunk cost, or urgency | operational pressure | no acceptance authority | constrains timing or resources | broadens or weakens the gate |

Do not inventory the entire repository. Stop when each blocking behavior has a traced source or is shown to have none.

### 3. Trace causal chains

For each symptom, quote the exact chain:

```text
source wording
→ agent/controller interpretation
→ persisted copy or automation
→ blocking or suppressive behavior
→ concrete cost or missed work
```

Classify the defect:

- **description → obligation**;
- **permission → ownership**;
- **diagnostic → gate**;
- **recovery tactic → universal ritual**;
- **todo/status → requirement**;
- **repetition → authority**;
- **artifact → evidence for itself**;
- **failure → unrelated repair scope**;
- **initial checklist → ban on necessary emergent work**.
- **audit method → project requirement**;
- **deadline or sunk cost → authority**.

### 4. Select the root correction

Edit the highest causal source that is both wrong and within scope. Prefer, in order:

1. restore explicit authority and acceptance wording;
2. remove or narrow the inference that creates the ratchet;
3. correct controller or prompt behavior derived from that inference;
4. update only consumers proven to execute or currently repeat the wrong rule;
5. delete obsolete duplicate procedure.

Keep historical facts intact. Do not harmonize every adjacent document, add a policy registry, or create a replacement ceremony. If the real authority is correct and only one controller misreads it, fix the controller.

### 5. Test both failure directions

A remediation is incomplete until scenarios cover both:

- **under-control:** claim laundering, skipped required checks, hidden failures, unsafe completion, lost recovery state;
- **over-control:** inferred whole-module gates, unrelated supplemental failures, unconditional reviews, stale history, duplicate artifacts, and blocked necessary emergent work.

Minimum scenario set:

| Scenario | Expected behavior |
|---|---|
| Exact required selector passes | complete at that claim’s exercised scope |
| Required selector cannot run | remain unverified; diagnose in scope |
| Supplemental test fails unrelatedly | disclose at its actual scope; do not repin current work |
| Supplemental test proves current regression | block through the violated requirement |
| Authorized file changes public consumer contract | admit consumer work through the affected contract |
| Historical report names “owned modules” | preserve wording as history; infer no gate |
| Flaky required check | retain all outcomes; follow authoritative reliability policy |
| Necessary work discovered mid-task | admit only with trigger, causal link, affected invariant, and closure condition |

For flaky required checks, retain every outcome. A rerun is sufficient only when the current check contract or an existing reliability policy says so; otherwise report the evidence boundary as unresolved rather than selecting the favorable run.

### 6. Apply in causal order

1. Authority and acceptance wording.
2. Deterministic skill selection and task-local expiry.
3. Review admission and supplemental-result classification.
4. Todo, recovery-state, and cleanup admission.
5. Focused ratchet detection after the primary rules stabilize.

After each stage, simulate the scenarios above. Do not infer success from good-sounding prose.

## Required Output

Target 700 words and never exceed 1,200, counting headings and tables. Before returning, count the draft and compress wording or omit elaboration—not required fields—until it fits. Use exactly:

1. **Decision** — at most three sentences.
2. **Acceptance unit** — one claim plus a table of at most eight requirements and sources.
3. **Causal findings** — at most five chains, one line per arrow in each chain.
4. **Remediation** — a table of at most ten source edits with `change`, `preserve`, and `why`.
5. **Simulation** — the eight minimum scenarios above, one terse row each; add a row only for a distinct affected boundary.
6. **Residual risks** — at most five unresolved judgments or missing facts.
7. **A/B handoff** — one paragraph naming immutable candidate, treatment delta, expected behavior, and known confounders.

Every item must support a decision or executable edit. Existing evidence retains facts; the audit does not propose a new storage destination merely to preserve them. Return the record in chat unless the user or current authority requests a persisted artifact.

## Example

```text
“Files A–C are owned modules”                    historical report
→ reviewer says all tests in A–C are mandatory  unsupported interpretation
→ ledger copies “required full-module gate”      repeated description
→ controller blocks on unrelated legacy test    executable ratchet

Root correction: remove the reviewer/prompt inference that authorization or
historical ownership creates a gate; make the controller consume the current
acceptance unit. Preserve the legacy failure result at its actual scope.
```

## Common Mistakes and Rationalizations

| Rationalization | Correction |
|---|---|
| “Keep every safeguard.” | Preserve the protected invariant; retire controls with no causal relation to it. |
| “The ledger says required.” | A ledger records authority; it does not create it. |
| “We should ticket it so the fact is not lost.” | Preserve the existing evidence. Create a ticket only through an applicable requirement or explicit request. |
| “Formal change control prevents recurrence.” | Correct the causal source first. Do not install a new governance system by default. |
| “Audit every related file to be safe.” | Trace disputed causal sources; repository adjacency is not authority. |
| “The process is cheap compared with a regression.” | Cost does not establish effectiveness or applicability. Test the claimed control. |
| “This skill says the check is required.” | The skill constrains audit reasoning; only current project or user authority defines the check. |
| “The rerun passed, so the first failure no longer matters.” | Preserve both outcomes; use a sourced retry or reliability rule to decide sufficiency. |
| “Update every consumer for consistency.” | Update only consumers proven to execute or currently repeat the wrong rule. |
| “We already invested in these todos.” | Sunk cost cannot supply their missing authority or causal link. |

## Red Flags

Stop and re-scope if the remediation:

- creates more permanent process than it removes;
- treats an observation, todo, report, or prior run as normative by existence;
- cannot name the current requirement behind a blocker;
- uses “owned,” “authorized,” “affected,” or “historical” as synonyms;
- declares success without testing under-control and over-control scenarios;
- suppresses an actual changed contract because it was not in the initial plan;
- proposes a registry, dashboard, ticket, SLA, recurring audit, or mandatory report without current authority.
- cites this audit method, urgency, or sunk cost as the source of a project requirement;
- treats a favorable rerun as sufficient without a current retry or reliability contract.

After remediation is ready, **REQUIRED NEXT SKILL:** use `running-controlled-agent-ab-tests` to test process behavior without letting trial artifacts manufacture authority.
