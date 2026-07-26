# Greek Essence Ralph Loop

Ralph is a thin project-level context-refresh loop. Each iteration launches one fresh `jzgreekorch` session to complete exactly one durable `features-cli` frontier action. `features-cli` is the sole workflow ledger; Python never interprets JZ workflow state.

## Control signals

Both signals are strict repository-local JSON files:

- `.scratch/ralph-loop/completion-signal.json` has the exact schema `{"isEverythingDone": boolean}`.
- `.scratch/ralph-loop/pause-signal.json` has the exact schema `{"isPaused": boolean}`.

Exact schema means one JSON object containing only the named key with a JSON Boolean value. A missing, unreadable, malformed, extra-keyed, or non-Boolean signal is invalid and fails closed.

Completion and blocked pause are distinct:

- `isEverythingDone: true` means the full feature campaign is proven complete.
- `isPaused: true` means a genuine human-required blocker prevents authorized progress while completion remains false.

The controller never writes, resets, or infers either signal. Set `isPaused` from `true` to `false` only during an explicitly authorized resume or activation after the blocker has been resolved. Set `isEverythingDone` from `true` to `false` only during an explicitly authorized activation of new work. A resume from a blocked pause must not change completion merely to make the loop run.

## Minimal Python controller contract

Python is mechanical and owns only:

1. Strictly reading the completion and pause signals.
2. Acquiring and retaining one duplicate-free strict ownership record with exact schema `{"controller_pid": positive integer, "root_pid": positive integer or null, "launch_state": "idle"|"starting"|"running"|"cleanup_ambiguous"}`. A controller writes `idle` only with `root_pid: null`, writes durable `starting` before child creation, then retries the `running` record with the exact Windows root PID 25 times at 250 ms intervals. If all running writes fail, it cleans only that PID-scoped owned tree; it removes ownership evidence only after verified exit. Failed/ambiguous cleanup preserves `cleanup_ambiguous` evidence with the exact PID and blocks every later preflight or controller acquisition. A dead controller can recover only an `idle` record; starting, running, and cleanup ambiguity are launch-blocking. Process-name/PID discovery is diagnostic only and never establishes ownership or triggers name-based termination.
3. Running a high but finite iteration bound.
4. Launching a fresh `hermes -p jzgreekorch` process for each iteration, with no session resume and no model, provider, or reasoning override.
5. Enforcing one generous fixed timeout per iteration.
6. Before each child launch, mechanically invokes `features-cli progress --feature greek-essence-showcase --json` and strictly validates duplicate-free JSON and a known allowlisted `kind`. Artifact paths remain required for kinds whose pinned stable CLI source always supplies them. For the stable artifact-less issue shapes (`review-issue` and resumed `implement-issue`), it requires a positive `issueId` and derives exactly one contained `<feature>/issues/<issueId>-*` owner from the validated feature slug; for stable artifact-less feature shapes (`design-ready`, `feature-review`, `blocked`, and `archived`), it derives exactly one contained feature owner. A supplied artifact path must remain contained and consistent with that derived owner. All symlink/junction/reparse components and unsafe destinations fail closed before log creation or child launch. Every controller invocation creates a collision-resistant no-clobber run directory once per owner, then reuses only its own directory for later same-owner iterations: `<owner>/.Ralph/runs/<run-id>/iteration-####.log`. A changed owner receives its own run directory.
7. Capturing process output through a continuously drained, continuously materialized bounded tail log: on-disk evidence is observable while the child runs and is at most `MAX_LOG_BYTES` during and after capture; oversized output carries an explicit truncation marker plus retained tail.
8. Reporting a nonzero process exit as `HERMES_FAILED`.
9. On timeout, terminating only the owned root process tree, verifying exit, and reporting `TIMEOUT`; ambiguous cleanup fails closed.
10. Returning deterministic outcomes without interpreting repository workflow semantics.

The control flow is fixed:

```text
Acquire/retain one strict controller/root ownership record.
If a dead controller has a live or ambiguous recorded root -> preserve evidence and hard-stop.
Before every launch:
  strict-read completion signal
  if true -> COMPLETE
  strict-read pause signal
  if true -> BLOCKED

For iteration 1..max_iterations:
  launch fresh `hermes -p jzgreekorch` with no model/provider override
  enforce one generous fixed timeout
  capture output in a bounded iteration log
  on nonzero -> HERMES_FAILED
  on timeout -> terminate only owned process tree; verify exit; return TIMEOUT
  strict-read completion signal
  if true -> COMPLETE
  strict-read pause signal
  if true -> BLOCKED

After loop:
  return LIMIT_REACHED

Always:
  release lock on controlled exit
  preserve logs
  never infer JZ state
```

Python does not parse milestones, issues, contracts, reviews, task identities, engineering depth, `HANDOFF.md`, model output, email, or blocker prose. It owns no workflow transitions, semantic failure classification, retry reasoning, or profile configuration.

## Orchestrator contract

The fresh `jzgreekorch` session owns all semantic work. It must:

- read repository and feature authority plus `HANDOFF.md` and `KNOWLEDGE.md`;
- run `features-cli docs current --feature greek-essence-showcase` and `features-cli progress --feature greek-essence-showcase --json` at the start and end of the iteration;
- treat the live CLI frontier as authoritative and reconcile summaries without creating another ledger;
- complete exactly one frontier-owned action, including its ordinary delegation, repair, verification, and re-review loops, then stop rather than starting the next frontier action;
- delegate substantive implementation and required independent code or visual review to the appropriate fresh role profiles;
- apply the practicality policy below;
- update `HANDOFF.md` before every normal exit and add to `KNOWLEDGE.md` only durable, non-obvious facts;
- set completion true only after the full campaign goal is proven;
- set pause true only for a genuine human-required blocker, keep completion false, record the exact blocker and requested action in the handoff, and stop.

Ordinary implementation failures, failed checks, and in-contract review findings are not blocked pauses. The orchestrator repairs and re-verifies them within bounded, practical effort.

## Practicality policy

Classify every failure into exactly one category:

1. **Material regression → repair.**
2. **Invalid/stale/flaky evidence → bounded diagnosis, correct or retire the invalid check.**
3. **Understood low-impact exception → record exact failure, evidence, impact, bounded attempts, and continue.**

Category 3 is never allowed for **security, privacy, accessibility, data integrity, accepted user behavior, core bilingual parity, unusable builds, or unsupported claims**. These categories are non-waivable. Accepted exceptions must be truthful and evidence-backed; a failed command must never be reported as passing.

## Outcomes

- `COMPLETE`: completion was strictly read as true.
- `BLOCKED`: pause was strictly read as true; completion was not claimed.
- `LIMIT_REACHED`: the finite iteration bound ended with both signals false.
- `HERMES_FAILED`: the fresh orchestrator process exited nonzero.
- `TIMEOUT`: the owned process tree was terminated and verified after timeout.
- `INVALID_SIGNAL`: either signal failed strict validation.
- `LOCK_CONFLICT`: another controller owns the lock.
- `INTERRUPTED` / `ERROR`: the controller stopped safely and released controlled resources.

## Canonical commands

Run from the repository root:

```bash
# Read-only controller validation; no Hermes launch or signal mutation.
python .scratch/ralph-loop/tools/ralph_loop.py --dry-run

# Live execution until a deterministic outcome.
python .scratch/ralph-loop/tools/ralph_loop.py

# One observable fresh-orchestrator iteration.
python .scratch/ralph-loop/tools/ralph_loop.py --max-iterations 1
```

Implementation and tests for this contract are defined in later rebuild tasks; this document does not authorize launch or signal mutation.
