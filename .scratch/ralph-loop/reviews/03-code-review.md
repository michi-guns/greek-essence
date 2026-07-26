# Ralph/JZ Rebuild — Independent Task 11 Code Review 03

**Verdict:** FAIL
**Resolved engineering depth:** Tier 2 — Prototype (direct operator instruction; consistent with root `AGENTS.md` and feature `SPEC.md` `implementation_depth: 2`)
**Review type:** Final fresh independent code-review attempt after the second and final bounded repair cycle
**Reviewed staged binary diff SHA-256:** `e8c67dff2c6768a26f7a7eae66cf043fa35f6285deb2ec4da8a491f66f9473c3`
**Expected staged binary diff SHA-256:** `e8c67dff2c6768a26f7a7eae66cf043fa35f6285deb2ec4da8a491f66f9473c3`
**Hash match:** yes

## Scope and reviewed diff

The implementation was reviewed from the immutable index through `git diff --cached` and staged-file reads. The staged snapshot contains 29 paths, 2,799 insertions, and 3,170 deletions:

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
- immutable reviews `.scratch/ralph-loop/reviews/01-code-review.md` and `02-code-review.md`
- `.scratch/ralph-loop/tests/fixtures/jz_orchestrator_scenarios.json`
- `.scratch/ralph-loop/tests/test_jz_orchestrator_contract.py`
- `.scratch/ralph-loop/tests/test_ralph_acceptance.py`
- `.scratch/ralph-loop/tests/test_ralph_loop.py`
- `.scratch/ralph-loop/tests/test_ralph_manager_preflight.py`
- deleted `test_ralph_supervision.py` and `test_ralph_transition.py`
- `.scratch/ralph-loop/tools/ralph_loop.py`
- deleted `tools/smoke_test.py` and `tools/transition_campaign.py`
- `NEXT.md`

I read root and feature authority, `docs/README.md`, the bootstrap entry point, the approved feature `PRD.md` and `SPEC.md`, the current issue/change contract and implementation report for feature context, the rebuild plan, immutable Task 11 reviews 01/02, current rebuild implementation report, controller, preflight, manager skill, Ralph protocol, all tests/fixtures, all four JZ SOULs, profiles README, `HANDOFF.md`, `KNOWLEDGE.md`, and `NEXT.md`. Live `features-cli` output was read only as authoritative context and was not mutated.

No visual certification, live Ralph/Hermes launch, signal mutation, feature-frontier action, email, staging, commit, push, deployment, remote change, implementation repair, or unrelated product/issue mutation was performed.

## Review-02 closure matrix

| Review-02 requirement | Result | Independent evidence |
|---|---|---|
| `run_loop` preserves ambiguous recorded-root ownership and blocks reacquisition | **Closed for the recorded-root path** | Focused/full tests passed `test_run_loop_preserves_ambiguous_root_record_and_blocks_reacquisition`; the strict record remains when `root_pid` is known and cleanup is ambiguous, and a subsequent launch is blocked. |
| Started-child ownership write failure cleans or fails closed | **Not closed** | Cleanup-success coverage passes, but the combined record-write failure plus cleanup-ambiguity path deletes the lock while the child remains unverified. Finding 1. |
| Live bounded log exists before exit, remains within cap, retains truncation/tail, and does not deadlock | **Closed** | A real-child probe observed early flushed output while the worker was alive, sampled the log 222 times with a maximum/final size of 512 bytes, retained the truncation marker and final tail, and completed without deadlock. |
| Preflight rejects duplicate-key, extra-key, malformed, and invalid ownership records consistently with the controller | **Closed** | Independent matrix covered duplicate `controller_pid`, duplicate `root_pid`, extra key, malformed JSON, and invalid root type: preflight returned `INVALID_RUNTIME_OWNERSHIP_RECORD` and the controller raised `LockConflict` for every case; valid dead-controller/no-root recovery was accepted by both. |

## Findings

### 1. HIGH — A started child can survive an ownership-write failure while `run_loop` deletes the only controller lock

**Location:** `.scratch/ralph-loop/tools/ralph_loop.py:294-308,399-409`; missing combined-failure coverage near `.scratch/ralph-loop/tests/test_ralph_loop.py:326-344`

**Requirement:** Immutable review 02 finding 1 explicitly requires process-start/ownership-record write failure handling to clean the launched child or fail closed. `RALPH_LOOP.md:26`, manager `SKILL.md:62-68`, plan Task 4 cases 10–12, and Risk 7 require preserving ambiguous ownership and preventing a second launch whenever owned-process cleanup cannot be verified. This is an explicit unattended-controller safety contract, not optional higher-tier hardening.

**Evidence / reproduction:** An isolated temporary-directory probe patched `Popen` to return a started root PID `54321`, `_write_runtime_record` to fail with `LockConflict("record write failed")`, and `terminate_process_tree` to fail with `ProcessTreeError("cleanup ambiguous")`, then exercised the complete `run_loop` path. The result was:

```json
{
  "exception": "ProcessTreeError",
  "message": "Started process root 54321 could not be durably recorded or safely cleaned up",
  "child_poll": null,
  "lock_exists": false,
  "lock_text": null
}
```

`hermes_executor` correctly identifies ambiguity at lines 297–307, but the ownership write never changed the existing record from `root_pid: null`. The `run_loop` finalizer then reads that null record and unlinks it at lines 399–407. The started child remains unverified while the next controller sees no lock and may launch concurrently. The passing `test_record_write_failure_terminates_started_child_before_propagating` covers only successful cleanup and therefore does not exercise this fail-closed branch.

**Required correction:** When a just-started child cannot be durably recorded and cleanup cannot be verified, preserve durable launch-blocking ambiguity carrying the root identity; do not return to a lock-absent or stale-null state. The finalizer must distinguish this path and must not unlink its safety evidence. Keep the solution mechanical and bounded; do not reintroduce semantic workflow state.

**Required verification:** Add an end-to-end `run_loop` test combining ownership-write failure with cleanup ambiguity. Prove the child remains unverified, durable ownership/ambiguity evidence remains, subsequent preflight and controller acquisition both hard-stop, and no second launch or unverified kill occurs. Retain the existing successful-cleanup case and rerun focused/full controller and preflight suites.

### 2. MEDIUM — Iteration logs are overwritten when a later controller run reuses the same iteration number

**Location:** `.scratch/ralph-loop/tools/ralph_loop.py:244-258`; missing cross-run preservation coverage in `.scratch/ralph-loop/tests/test_ralph_loop.py`

**Requirement:** Plan Task 3 says logs are always preserved, Task 5 requires preserved per-iteration evidence, and `RALPH_LOOP.md:60-63` says controlled exit must preserve logs. Failure/timeout outcomes cite these paths for diagnosis. Explicit evidence preservation must survive the realistic manager behavior of running another bounded controller after a prior exit.

**Evidence / reproduction:** In an isolated temporary state directory, a prior `logs/iteration-0001.log` containing `PRIOR-FAILURE-EVIDENCE` was created. A new successful `hermes_executor(..., iteration=1)` run then used the same path. `_iteration_log` returned the existing filename and `_BoundedIterationCapture.__init__` called `write_bytes(b"")`. The final result was:

```json
{
  "prior_preserved": false,
  "new_present": true,
  "final_text": "NEW-RUN-EVIDENCE\n"
}
```

The continuously bounded capture itself now works, but a restart after `HERMES_FAILED`, `TIMEOUT`, interruption, or a one-iteration manager boundary can erase the prior cited iteration evidence.

**Required correction:** Allocate iteration logs through a collision-free controller-run boundary (for example a unique run directory or no-clobber filename) while keeping the existing bounded live-tail behavior and deterministic cited path. Never truncate an earlier run's evidence.

**Required verification:** Pre-create or produce a prior run's iteration-1 log, run a second controller/executor iteration 1, and prove both immutable bounded logs remain independently readable and correctly cited. Re-run the live cap/tail/truncation/no-deadlock tests and full Ralph suite.

### 3. MEDIUM — Recovery authority still says to repair review 01 after the final review-02 repair cycle

**Location:** `NEXT.md:15`; `.scratch/ralph-loop/HANDOFF.md:13-14,20-22`; contrasted with `.scratch/ralph-loop/IMPLEMENTATION_REPORT.md:3,68-90`

**Requirement:** Root `AGENTS.md` makes `NEXT.md` the immediate project continuation; plan Task 9 requires `NEXT.md`, `HANDOFF.md`, and recovery evidence to let a fresh context recover the rebuild without stale or duplicated state. Task 11 review scope requires documentation/code/test agreement.

**Evidence / reproduction:** The staged implementation report says the second and final bounded repair cycle for immutable review 02 is complete and fresh review is current. Staged `NEXT.md` still instructs the next context to “repair the three blocking findings in immutable `01-code-review.md`.” Staged `HANDOFF.md` likewise says Task 11 “addresses only immutable review 01 findings” and instructs completion of “the current Task 11 repair/re-review cycle for immutable review 01.” A fresh context following root authority can therefore repeat the first repair scope and miss the actual exhausted review-02 cycle/current review outcome.

**Required correction:** Reconcile `NEXT.md`, `HANDOFF.md`, and the implementation report to the same durable Task 11 state without copying live feature counts/frontier details or changing signals. Because this review has failed after two bounded repair cycles, the immediate continuation must state that activation is blocked and route the immutable review-03 findings for orchestrator/operator decision rather than pretending review approval exists.

**Required verification:** Read all three files from a fresh context and prove they agree on: Tasks 1–10 complete; review 01 and review 02 immutable; the second/final bounded repair cycle already consumed; review 03 failed; Ralph activation remains blocked; and the live `features-cli` frontier remains external and untouched. Re-run contract tests and staged whitespace/hash checks.

## Passing observations

Subject to the findings above, the independently reviewed Task 11 scope produced no additional blocking defect at Tier 2:

- The controller remains thin and mechanical: no milestone/issue/review semantic parser, assessor, diagnosis loop, transition state, semantic retry state, or controller-owned engineering-depth judgment remains.
- The launch command names only `jzgreekorch` and passes no model/provider/reasoning override or session-resume flag.
- Completion and pause use distinct exact one-Boolean schemas, reject duplicate/extra/malformed values, and are not reset by controller or preflight.
- Known recorded-root ambiguity is preserved through `run_loop`, timeout cleanup is PID-scoped and verified, and reacquisition is blocked when the prior root is live or unknown.
- Live iteration capture continuously drains the child, materializes output before child exit, remains at or below the cap, retains explicit truncation plus a useful tail, and preserves usable nonzero/timeout evidence without pipe deadlock.
- Preflight and controller agree on strict duplicate-free ownership parsing for all independently probed malformed classes.
- The one-frontier-action boundary, fresh role delegation, TDD-solo and TDD-ping-pong topology, bounded practicality policy, non-waivable categories, and email escalation boundaries are represented consistently in active contracts and tests.
- Active manager/controller/profile contracts contain no exact legacy runtime-role reference and no Python model/provider/resume override flag.
- Added-line static scanning found no suspicious hardcoded-secret assignment, `os.system`, `shell=True`, dangerous `eval`/`exec`, or unsafe pickle use.
- The expected completion-true preflight hard stop remained the sole activation incompatibility observed by the live preflight; no launch occurred.

These passing observations do not override the findings.

## Commands and exact results

1. `git status --short && git diff --cached --name-status && git diff --cached --stat && git diff --cached --binary | sha256sum` — exit 0; 29 staged paths; 2,799 insertions and 3,170 deletions; hash matched `e8c67dff2c6768a26f7a7eae66cf043fa35f6285deb2ec4da8a491f66f9473c3`.
2. `git diff --cached --check` — exit 0; 0 whitespace errors.
3. `features-cli docs current --feature greek-essence-showcase` — exit 0; live frontier was `contract-issue` for issue 02; recommended live skill reported `jz-issue-to-contract`; no mutation.
4. `features-cli progress --feature greek-essence-showcase --json` — exit 0; feature identified correctly; warnings `[]`; live frontier remained `contract-issue`; no mutation.
5. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_ralph_loop.py' -v` — exit 0; 24 tests run, 24 passed, 0 skipped/failed/errors.
6. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_ralph_manager_preflight.py' -v` — exit 0; 11 tests run, 10 passed, 1 skipped (`file symlinks unavailable`), 0 failed/errors.
7. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_*.py' -v` — exit 0; 50 tests run, 49 passed, 1 skipped (`file symlinks unavailable`), 0 failed/errors.
8. `python -B .scratch/ralph-loop/tools/ralph_loop.py --dry-run` — exit 0; canonical repository, completion true, pause false, `jzgreekorch`, timeout 10,800, cap 100, and `launch_performed:false`; no Hermes/Ralph launch.
9. `python -B .agents/skills/ralph-loop-manager/scripts/preflight.py --repo . --target greek-essence-showcase` — exit 2; `HARD_STOP` with exactly one hard stop, `COMPLETION_NOT_LAUNCH_COMPATIBLE`; runtime lock absent; all other mechanical checks passed; one dirty-worktree warning; `launch_performed:false`. This expected completion-true activation stop is not itself a finding.
10. Isolated combined ownership-write/cleanup-ambiguity probe — exit 0; reproduced finding 1: `ProcessTreeError`, child `poll()` remained null, and `lock_exists:false` after complete `run_loop` finalization.
11. Isolated real-child live bounded-log probe — exit 0; early output was visible while the child was alive; 222 live samples; maximum/final size 512 bytes at a 512-byte cap; truncation marker and final tail present; worker exited; no deadlock/error.
12. Isolated strict ownership-record matrix — exit 0; duplicate controller key, duplicate root key, extra key, malformed JSON, and invalid root type were rejected by preflight with `INVALID_RUNTIME_OWNERSHIP_RECORD` and by controller with `LockConflict`; valid dead-controller/no-root recovery was accepted by both.
13. Isolated cross-run log-preservation probe — exit 0; reproduced finding 2: prior iteration-1 evidence was absent after the second iteration-1 run, while only new output remained.
14. Added-line staged static scan — exit 0; 2,799 added lines scanned; 0 hardcoded-secret assignment, 0 shell-injection, 0 dangerous-eval/exec, and 0 unsafe-pickle matches. Active staged manager/controller/profile scan found 0 exact legacy runtime-role references and 0 Python model/provider/resume override flag matches.
15. Final `git diff --cached --binary | sha256sum` and `git diff --cached --check` — exit 0; reviewed staged hash remained `e8c67dff2c6768a26f7a7eae66cf043fa35f6285deb2ec4da8a491f66f9473c3`; 0 whitespace errors.

## Required route

Ralph activation is blocked after two bounded repair cycles. Preserve reviews 01, 02, and this review 03 unchanged. Return these findings to `jzgreekorch` for an explicit orchestrator/operator decision; do not self-convert this FAIL to approval and do not proceed to operational acceptance, Task 12 live one-iteration acceptance, Task 13 activation, or Task 14 retirement while they remain unresolved. Any authorized repair must be performed by a separate fresh `jzgreekimpl` session under Tier 2, followed by the affected/full gates and a new immutable fresh code-review attempt. Do not launch Ralph, change completion/pause signals, advance the feature frontier, email, stage, commit, push, deploy, or touch unrelated product/issue work.
