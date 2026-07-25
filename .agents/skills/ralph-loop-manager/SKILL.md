---
name: ralph-loop-manager
description: Use when the operator asks to activate, resume, run, or monitor the project-owned Greek Essence Ralph loop. Validate its mechanical launch boundary, preserve strict completion and pause signals, run bounded fresh jzgreekorch iterations, and keep all workflow reasoning in the orchestrator.
version: 1.0.0
author: Greek Essence project
license: Project-owned
metadata:
  hermes:
    tags: [ralph-loop, orchestration, monitoring, notifications]
    related_skills: [email-notification]
---

# Ralph Loop Manager

## Overview

Manage the repository's existing thin Ralph controller. Do not invent a second workflow ledger and do not move JZ reasoning into Python. `features-cli` is the sole workflow ledger; each fresh `jzgreekorch` session owns exactly one frontier action.

This skill applies only to the Greek Essence repository and the accepted `greek-essence-showcase` feature campaign. It does not authorize deployment, pushes, history rewriting, credential disclosure, unrelated deletion, system changes, or out-of-repository work.

## Authoritative inputs

Before activation, resume, launch, or monitoring, read:

1. `AGENTS.md` and `NEXT.md`;
2. `.scratch/features/001-greek-essence-showcase/AGENTS.md` and the live frontier's authoritative files;
3. `.scratch/ralph-loop/RALPH_LOOP.md`;
4. `.scratch/ralph-loop/HANDOFF.md` and `.scratch/ralph-loop/KNOWLEDGE.md`;
5. `.scratch/ralph-loop/completion-signal.json` and `.scratch/ralph-loop/pause-signal.json`;
6. live `features-cli docs current --feature greek-essence-showcase` and `features-cli progress --feature greek-essence-showcase --json` output.

The CLI frontier is authoritative. `NEXT.md` and `HANDOFF.md` are recovery summaries, not parallel workflow state.

## Strict signals and authorized reset

The repository-local signals have exact schemas `{"isEverythingDone": boolean}` and `{"isPaused": boolean}`. Valid current values look like:

```json
{"isEverythingDone": false}
```

```json
{"isPaused": false}
```

Each file must contain one JSON object, only its named key, and a JSON Boolean. Missing, unreadable, malformed, extra-keyed, or non-Boolean content is a hard stop.

The meanings are independent:

- Completion true proves the full campaign is complete.
- Pause true records a genuine human-required blocker while completion remains false.

Neither the manager nor controller resets signals as routine startup behavior. Reset `isPaused` from true to false only during an explicitly authorized resume or activation after verifying that the blocker is resolved. Reset completion from true to false only during explicitly authorized activation of new work. Never clear pause merely because a process is being launched, and never set completion to represent a blocker.

## Responsibility boundary

### Python is mechanical

The controller only:

- strict-reads both signals before launch and after each iteration;
- acquires and retains one duplicate-free strict ownership record with `controller_pid`, `root_pid`, and `launch_state`; writes durable `starting` before child creation; retries the exact-PID `running` record 25 times with 250 ms waits; and, if persistence fails, cleans only that PID-scoped owned tree. It removes evidence only after verified exit. Ambiguous cleanup retains exact-PID `cleanup_ambiguous` evidence and hard-stops later controller acquisition/preflight; only a dead-controller `idle` record is recoverable. Process-name/PID discovery is diagnostic only and never establishes ownership or permits name-based termination;
- applies a high finite iteration limit and one generous fixed timeout;
- launches one fresh `hermes -p jzgreekorch` process per iteration without session resume or model/provider/reasoning overrides;
- before each child launch, mechanically validates the exit status and duplicate-free JSON of `features-cli progress --feature greek-essence-showcase --json` only to route logs. Routing requires a known allowlisted `kind`: issue kinds require a positive matching `issueId`; stable artifact-less `review-issue` and resumed `implement-issue` payloads derive exactly one contained `<feature>/issues/<issueId>-*` owner from the validated feature slug, while stable artifact-less `design-ready`, `feature-review`, `blocked`, and `archived` payloads derive exactly one contained feature owner. Kinds whose pinned source always supplies `artifactPath` still require it; a supplied path must be contained and consistent with the derived owner. It rejects malformed schema, zero/multiple owners, unsafe paths, and symlink/junction/reparse components before launch or log creation; an invocation creates each owner run directory once and reuses it only for that invocation's later iterations. Dry-run reports the resolved owner/run path without creating it;
- continuously materializes bounded iteration output while draining child pipes, preserving explicit truncation and a diagnostic tail without exceeding the cap, plus privacy-bounded lifecycle logs;
- reports nonzero exit as `HERMES_FAILED`;
- on timeout, terminates only its owned process tree, verifies exit, and fails closed on ambiguity;
- returns deterministic outcomes: `COMPLETE`, `BLOCKED`, `LIMIT_REACHED`, `HERMES_FAILED`, `TIMEOUT`, signal or lock failures, interruption, or error.

Python never parses JZ documents, frontier meaning, blocker prose, model output, handoff prose, or email. It owns no semantic workflow transition, failure judgment, or profile configuration.

### `jzgreekorch` is semantic

Each fresh orchestrator:

- reads repository/feature authority and Ralph recovery files;
- queries the live CLI frontier at iteration start and end;
- completes exactly one frontier action through appropriate fresh implementer, code-review, and visual-review delegation plus ordinary repair and re-review;
- never starts the successor frontier action in the same iteration;
- independently verifies durable results and reconciles `HANDOFF.md`;
- applies the practicality policy below;
- marks completion true only when the entire campaign goal is proven;
- requests blocked pause only for a genuine human-required blocker, leaves completion false, records the exact evidence and requested human action, and stops.

A failed test, gate, or in-contract review is ordinary workflow work, not a blocked pause.

## Practicality policy

The orchestrator classifies failures into exactly three categories:

1. **Material regression → repair.**
2. **Invalid/stale/flaky evidence → bounded diagnosis, correct or retire the invalid check.**
3. **Understood low-impact exception → record exact failure, evidence, impact, bounded attempts, and continue.**

Category 3 is never allowed for **security, privacy, accessibility, data integrity, accepted user behavior, core bilingual parity, unusable builds, or unsupported claims**. These categories are non-waivable. Every exception must be truthful and evidence-backed; never report a failed command as passing.

## Preflight

Before a live launch, run the project-owned read-only preflight from the repository root:

```bash
python .agents/skills/ralph-loop-manager/scripts/preflight.py \
  --repo . \
  --target greek-essence-showcase
```

Confirm mechanically that:

- the repository root and required contained regular files are correct;
- Git, Python 3.11+, Hermes, Bun, pnpm, and stable `features-cli` are available;
- both live CLI commands succeed and identify `greek-essence-showcase` without warnings;
- `jzgreekorch`, `jzgreekimpl`, `jzgreekrev`, and `jzgreekvisualrev` exist, without inspecting their model/provider/reasoning settings;
- no runtime ownership record is live, malformed, duplicate-keyed, or ambiguous; a dead controller with a recorded live/unknown root is a hard stop and must be preserved for inspection;
- both signals satisfy their exact schemas and have values compatible with the authorized action;
- worktree changes are observable and every pre-existing path is attributed rather than automatically rejected;
- controller dry-run succeeds without launch or mutation;
- notification support is available for verified campaign completion or a genuine human-required blocker.

A preflight failure is a hard stop. Report the failed check, evidence, consequence, smallest remediation, and `Ralph launched: no`. Do not repair by broadening scope or mutating signals.

## Activation and resume

Activation or resume requires explicit operator authorization and a resolved, repository-recorded campaign goal. Before changing a signal:

1. Verify no live controller owns the lock.
2. Re-read both strict signals and the live CLI frontier.
3. For resume, verify the recorded blocker is resolved, then explicitly set only pause to false; keep completion false.
4. For activation after completed work, explicitly set completion false and pause false only as authorized for the new active work.
5. Re-run preflight and controller dry-run.

Signal reset is part of authorized activation/resume, never controller startup and never an inferred convenience.

## Run and monitor

Use the canonical controller. For an observable manager boundary, run one fresh iteration:

```bash
python .scratch/ralph-loop/tools/ralph_loop.py --max-iterations 1
```

Track the process; never wrap it in an untracked launcher and never start a second controller while a live lock exists. After exit, inspect the cited log and reconcile live repository, signals, CLI frontier, and handoff rather than trusting process prose.

Interpret outcomes strictly:

| Outcome | Meaning | Manager action |
|---|---|---|
| `COMPLETE` | Completion is strictly true | Independently verify full campaign completion before reporting or notification |
| `BLOCKED` | Pause is strictly true; completion is not claimed | Verify a genuine human-required blocker, stop launches, and request the exact human action |
| `LIMIT_REACHED` | Bound ended with both signals false | Verify one-action progress, then preflight before another authorized iteration |
| `HERMES_FAILED` | Fresh orchestrator exited nonzero | Preserve log and route only mechanically safe recovery; do not reinterpret as blocked or complete |
| `TIMEOUT` | Owned tree timed out and was cleaned up | Verify cleanup evidence; stop on ambiguity |
| Signal/lock/error outcome | Mechanical safety condition failed | Hard stop and preserve evidence |

Completion is never inferred from a clean exit, frontier movement, email, handoff prose, or pause. Blocked pause is never reported as completion.

## Notification boundary

Load `email-notification` only for:

- independently verified full campaign completion; or
- a verified genuine human-required blocker with an exact requested action.

Do not send routine progress, check-failure, repair-cycle, or review-handoff email. Do not place secrets, credentials, personal data, prompts, or raw logs in email. Report provider API acceptance accurately; do not claim delivery without separate evidence.

## Verification checklist

- [ ] Only the Greek Essence feature campaign is in scope.
- [ ] Live `features-cli` output establishes the frontier.
- [ ] Completion and pause signals have exact, distinct schemas and meanings.
- [ ] Any signal reset occurred only during explicitly authorized resume/activation.
- [ ] Python responsibilities remain mechanical; orchestrator responsibilities remain semantic.
- [ ] No launch argument overrides profile model, provider, or reasoning.
- [ ] One fresh orchestrator performs at most one frontier action per iteration.
- [ ] The three-category practicality policy and all non-waivable categories are preserved.
- [ ] `BLOCKED` keeps completion false and stops further launches.
- [ ] Preflight and dry-run pass before live launch.
- [ ] Existing worktree paths remain attributed and untouched unless explicitly owned.
- [ ] No unauthorized external, remote, credential, deployment, or Git-history action occurred.
