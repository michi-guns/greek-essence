# Ralph/JZ Rebuild — Independent Task 11 Code Review 01

**Verdict:** FAIL
**Resolved engineering depth:** Tier 2 — Prototype (direct operator instruction; consistent with the repository default)
**Review type:** Fresh independent code review of the immutable staged snapshot
**Reviewed staged binary diff SHA-256:** `483739f9c85304a38676ab92e420615ad8a7674fb6967698d1fbcaeee50602bf`
**Expected staged binary diff SHA-256:** `483739f9c85304a38676ab92e420615ad8a7674fb6967698d1fbcaeee50602bf`
**Hash match:** yes

## Scope and ownership

The implementation under review was read from the index via `git diff --cached` and `git show :<path>`. The staged snapshot contains 26 paths, 2,110 insertions, and 3,157 deletions:

- `.agents/skills/ralph-loop-manager/SKILL.md`
- `.agents/skills/ralph-loop-manager/scripts/preflight.py`
- `.hermes/plans/2026-07-24_174920-rebuild-ralph-for-jz-workflow.md`
- `.scratch/ralph-loop/HANDOFF.md`
- `.scratch/ralph-loop/IMPLEMENTATION_REPORT.md`
- `.scratch/ralph-loop/KNOWLEDGE.md`
- `.scratch/ralph-loop/RALPH_LOOP.md`
- `.scratch/ralph-loop/pause-signal.json`
- `.scratch/ralph-loop/profiles/README.md`
- deleted legacy templates `greekimpl-SOUL.md`, `greekreview-SOUL.md`, and `greekroot-SOUL.md`
- new `jzgreekimpl-SOUL.md`, `jzgreekorch-SOUL.md`, `jzgreekrev-SOUL.md`, and `jzgreekvisualrev-SOUL.md`
- `.scratch/ralph-loop/tests/fixtures/jz_orchestrator_scenarios.json`
- `.scratch/ralph-loop/tests/test_jz_orchestrator_contract.py`
- `.scratch/ralph-loop/tests/test_ralph_acceptance.py`
- `.scratch/ralph-loop/tests/test_ralph_loop.py`
- `.scratch/ralph-loop/tests/test_ralph_manager_preflight.py`
- deleted `test_ralph_supervision.py` and `test_ralph_transition.py`
- `.scratch/ralph-loop/tools/ralph_loop.py`
- deleted `tools/smoke_test.py` and `tools/transition_campaign.py`

For documentation agreement only, I also inspected the explicit unstaged Task 9 protocol diffs in `NEXT.md` and `.scratch/features/001-greek-essence-showcase/AGENTS.md`. They are not included in the staged ownership or staged hash. I also read root `AGENTS.md`, the rebuild plan, `RALPH_LOOP.md`, manager `SKILL.md` and preflight, `IMPLEMENTATION_REPORT.md`, all four JZ SOULs, Ralph tests and fixtures, `HANDOFF.md`, `KNOWLEDGE.md`, root documentation entry points, and the four prior immutable Ralph review records. Historical legacy references in prior immutable reviews and historical plan/report evidence were not treated as active runtime references.

No visual certification, live Ralph launch, signal/frontier mutation, email, staging, commit, push, deployment, remote change, or implementation repair was performed.

## Findings

### 1. HIGH — A dead controller lock can be discarded while its Hermes root is still alive, allowing a second controller to launch

**Location:** `.scratch/ralph-loop/tools/ralph_loop.py:150-173,212-242,263-284`; `.agents/skills/ralph-loop-manager/scripts/preflight.py:262-280`; missing focused coverage in `.scratch/ralph-loop/tests/test_ralph_loop.py:203-216`

**Requirement:** The rebuild plan identifies retained safety as root-PID-scoped Windows cleanup and says controller death must not leave a live root unchecked (plan “Current live context,” Risk 7, and Task 4 lock/process cases). `KNOWLEDGE.md` K-002 explicitly requires a dead lock owner with a live recorded root to produce `AMBIGUOUS_SURVIVING_ROOT_PROCESS`, never a concurrent launch or an automatic kill of an unverified tree. The requested review scope specifically includes Windows lock/process cleanup and worktree-safe unattended operation.

**Evidence / reproduction:**

- `_acquire_lock` stores only `os.getpid()` in `ralph.lock`. If that PID is dead, it unlinks the lock and retries acquisition.
- `hermes_executor` obtains the Hermes root PID in `Popen`, but never records that root PID in the lock, another mechanical runtime record, or lifecycle evidence.
- Preflight likewise parses the lock as one controller PID and considers a dead owner launch-compatible.
- The passing stale-lock test proves only that a dead controller PID is removed. It has no representation or assertion for a surviving recorded root.
- Therefore, after abrupt controller termination (for example process kill or host-level failure while Hermes continues), the next preflight/controller cannot distinguish a harmless stale lock from K-002’s ambiguous surviving-root condition and can launch a concurrent orchestrator.

**Required correction:** Retain minimal mechanical owned-root evidence without restoring semantic controller state. Record controller ownership and the current Hermes root PID in a strict bounded runtime record or lock contract; clear the root only after observed/verified exit. When the controller owner is dead and the recorded root is still live or cannot be checked unambiguously, hard-stop with preserved evidence and do not unlink the lock, launch another controller, or kill an unverified tree. Keep normal stale recovery bounded when no root survives.

**Required verification:** Add focused tests that cover (1) dead controller/no root permits evidenced stale recovery, (2) dead controller/live recorded root hard-stops without unlink/kill/launch, (3) malformed or ambiguous root ownership hard-stops, (4) normal and timeout exits clear root ownership only after verified process exit, and (5) interruption/cleanup ambiguity remains visible in the reported outcome. Re-run the full Ralph suite, dry-run, and completion-true preflight.

### 2. MEDIUM — Iteration output is not bounded while the three-hour process is running

**Location:** `.scratch/ralph-loop/tools/ralph_loop.py:23,206-242`; missing behavior coverage in `.scratch/ralph-loop/tests/test_ralph_loop.py`

**Requirement:** Plan Task 3 and Task 5, `RALPH_LOOP.md`, and the manager contract require output to be captured in a bounded per-iteration log. This is an explicit resource/privacy safeguard, not optional production hardening.

**Evidence / reproduction:** `hermes_executor` passes the ordinary file handle directly to `Popen` at lines 216-220. The child can append without a size bound for the entire fixed timeout (default 10,800 seconds). `MAX_LOG_BYTES` is applied only at lines 237-239 after `process.wait` returns and the file is closed. A noisy or stuck child can therefore grow the file arbitrarily during execution; post-exit truncation does not make capture bounded.

**Required correction:** Bound capture as it occurs, using the smallest maintainable mechanical approach appropriate to Tier 2 (for example a capped/rotated sink or bounded reader that continues draining child pipes without deadlock). Preserve enough tail or deterministic truncation evidence to diagnose nonzero and timeout outcomes, and do not log prompts, environment values, credentials, or email content.

**Required verification:** Add a focused subprocess test that emits more than the configured cap before exit and proves the on-disk iteration evidence never exceeds the documented bound during/after capture, the child cannot deadlock on a full pipe, truncation is explicit, and nonzero/timeout outcomes still cite usable evidence. Re-run the full Ralph suite and dry-run.

### 3. MEDIUM — Recovery documents disagree about whether Task 10 is pending or complete

**Location:** unstaged Task 9 protocol diff `NEXT.md:11-15`; staged `.scratch/ralph-loop/HANDOFF.md` “Last iteration” and “Next iteration”; staged `.scratch/ralph-loop/IMPLEMENTATION_REPORT.md:1-5` and “Tasks 9–10” section

**Requirement:** Plan Task 9 requires fresh contexts to recover current rebuild work without duplicated/stale workflow state; root `AGENTS.md` requires `NEXT.md` to carry the immediate continuation. The Task 11 review scope explicitly requires documentation/code/tests agreement. `features-cli` remains authoritative for the feature frontier, but the rebuild-plan continuation is not a `features-cli` frontier and must still be internally consistent.

**Evidence / reproduction:** The staged implementation report states “Tasks 1–10” are complete and the snapshot is awaiting Task 11. In contrast, the explicit Task 9 `NEXT.md` diff says “Task 9 is complete. Begin Task 10,” while staged `HANDOFF.md` records Task 9 as the last completed rebuild action and only generically says to continue remaining tasks. A fresh recovery context following root authority can therefore repeat Task 10 or misidentify the current rebuild-plan boundary.

**Required correction:** Reconcile the immediate rebuild continuation and last durable rebuild action across `NEXT.md`, `HANDOFF.md`, and `IMPLEMENTATION_REPORT.md` without copying live feature counts/frontier state. Preserve the distinction between the Ralph rebuild plan and the live `features-cli` feature frontier.

**Required verification:** Read the three files from a fresh context and show they agree that Tasks 1–10 are complete, Task 11 review/rework is current, and live feature work must not advance. Re-run contract tests and `git diff --check`. Any protocol-file change must be intentionally attributed and reviewed; it must not be silently absorbed into the staged Ralph snapshot.

## Passing observations

Within the reviewed snapshot, the following requested areas are otherwise represented consistently:

- Controller workflow behavior is mechanical; no milestone/issue/review semantic parser, assessor, diagnosis loop, transition state, or model/provider/reasoning override remains.
- Completion and pause readers reject malformed JSON, duplicate keys, extra keys, and non-Boolean values.
- The launch command names only fresh `jzgreekorch` and contains no `-m`, `--model`, `--provider`, `--resume`, or equivalent configuration override.
- The orchestrator SOUL requires a start/end live frontier query, exactly one frontier action, stop-on-frontier-advance, fresh role delegation, immutable reviews, one-profile RED→GREEN for `tdd-solo`, and separate fresh `jzgreekimpl` RED/GREEN sessions for `tdd-ping-pong`.
- Practical exceptions are evidence-bounded and expressly non-waivable for security, privacy, accessibility, data integrity, accepted behavior, core bilingual parity, unusable builds, and unsupported claims.
- Email is restricted to independently verified full-feature completion or a genuine human-required blocker; routine progress and repair/review loops are excluded.
- Added-line static scan found no hardcoded-secret assignment, `os.system`, `shell=True`, dangerous `eval`/`exec`, or unsafe pickle match.
- Existing unrelated dirty and untracked work remained present; the staged snapshot hash was unchanged after the gates.

These passing observations do not override the blocking findings above.

## Commands and results

1. `git status --short && git diff --cached --name-status && git diff --cached --binary | sha256sum` — exit 0; 26 staged paths; hash `483739f9c85304a38676ab92e420615ad8a7674fb6967698d1fbcaeee50602bf` matched the expected snapshot.
2. `git diff --cached --check` — exit 0; 0 whitespace errors.
3. `git diff --cached --stat` — exit 0; 26 files changed, 2,110 insertions, 3,157 deletions.
4. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_*.py' -v` — exit 0; 36 tests run, 35 passed, 1 skipped (`file symlinks unavailable`), 0 failed, 0 errors.
5. `python -B .scratch/ralph-loop/tools/ralph_loop.py --dry-run` — exit 0; reported canonical repository, completion true, pause false, `jzgreekorch`, timeout 10,800, cap 100, and `launch_performed: false`; no Hermes process launched.
6. `python -B .agents/skills/ralph-loop-manager/scripts/preflight.py --repo . --target greek-essence-showcase` — exit 2; status `HARD_STOP`; exactly one hard stop, `COMPLETION_NOT_LAUNCH_COMPATIBLE`; all other listed mechanical checks passed, one expected dirty-worktree warning was emitted, and `launch_performed` was false. This is the intentionally expected completion-true activation stop and is not itself a review finding.
7. Added-line Python static scan over `git diff --cached --unified=0` — exit 0; 2,110 added lines scanned; 0 hardcoded-secret, 0 shell-injection, 0 dangerous-eval/exec, and 0 unsafe-pickle matches.
8. Index runtime-reference scan with `git grep --cached` — exit 0 for the wrapper; active legacy strings were confined to negative assertions/new profile substrings and prior immutable historical reviews. No active controller model override or legacy runtime profile reference was found.
9. `git diff -- NEXT.md` and `git diff -- .scratch/features/001-greek-essence-showcase/AGENTS.md` — exit 0; inspected only for Task 9 documentation agreement, not staged ownership.
10. `git diff --cached --binary | sha256sum` after all read-only gates — exit 0; hash remained `483739f9c85304a38676ab92e420615ad8a7674fb6967698d1fbcaeee50602bf`.

## Required route

Route all three findings to a separate fresh `jzgreekimpl` implementation/reconciliation session under Tier 2. The reviewer must not repair them. Preserve this artifact unchanged. After correction and focused/full verification, create a new staged immutable snapshot and obtain a fresh independent code-review attempt at the next available immutable review path. Do not self-convert this FAIL to approval. Operational acceptance review and any Task 12/13 live acceptance or activation must wait for a fresh PASS. Completion and pause signals must remain unchanged, and Ralph must not be launched during repair/re-review.
