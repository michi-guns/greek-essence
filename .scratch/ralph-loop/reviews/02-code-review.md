# Ralph/JZ Rebuild — Independent Task 11 Code Review 02

**Verdict:** FAIL
**Resolved engineering depth:** Tier 2 — Prototype (direct operator instruction; consistent with root `AGENTS.md` and feature `SPEC.md` `implementation_depth: 2`)
**Review type:** Fresh independent code review of the immutable staged snapshot after repair of review 01
**Reviewed staged binary diff SHA-256:** `727de91918953a18c9c2f6df38ac3ab13b8106e8fa9ba19887110e0ddf8c13fb`
**Expected staged binary diff SHA-256:** `727de91918953a18c9c2f6df38ac3ab13b8106e8fa9ba19887110e0ddf8c13fb`
**Hash match:** yes

## Scope and reviewed diff

The implementation was reviewed from the index through `git diff --cached` and `git show :<path>`. The staged snapshot contains 28 paths, 2,505 insertions, and 3,170 deletions:

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
- `.scratch/ralph-loop/reviews/01-code-review.md`
- `.scratch/ralph-loop/tests/fixtures/jz_orchestrator_scenarios.json`
- `.scratch/ralph-loop/tests/test_jz_orchestrator_contract.py`
- `.scratch/ralph-loop/tests/test_ralph_acceptance.py`
- `.scratch/ralph-loop/tests/test_ralph_loop.py`
- `.scratch/ralph-loop/tests/test_ralph_manager_preflight.py`
- deleted `test_ralph_supervision.py` and `test_ralph_transition.py`
- `.scratch/ralph-loop/tools/ralph_loop.py`
- deleted `tools/smoke_test.py` and `tools/transition_campaign.py`
- `NEXT.md`

I also read root and feature authority, `PRD.md`, the approved `SPEC.md`, issue 01 and its change contract/implementation report, root documentation/bootstrap entry points, the rebuild plan, immutable review 01, all repaired controller/preflight/tests/docs, all four JZ SOULs, `HANDOFF.md`, `KNOWLEDGE.md`, `NEXT.md`, and the rebuild implementation report. Live `features-cli` output was consulted only as current authoritative context; it was not mutated and is not part of the reviewed staged hash. The implementation files executed by the tests had no unstaged modifications.

No visual certification, live Ralph/Hermes launch, signal mutation, frontier action, email, staging, commit, push, deployment, remote change, implementation repair, or unrelated product/issue mutation was performed.

## Review-01 closure matrix

| Review-01 finding | Result | Evidence |
|---|---|---|
| Dead-controller/live-or-ambiguous-root ownership and clearing semantics | **Not closed** | The strict controller/root record and dead-owner acquisition checks were added, but `run_loop` unconditionally deletes that record after an ambiguous cleanup exception, erasing the surviving-root evidence. Preflight also accepts duplicate-key ownership JSON. Findings 1 and 3 below. |
| Live bounded logs without deadlock and with usable truncation evidence | **Not closed** | Pipe draining, post-exit bounding, tail retention, and nonzero/timeout evidence work, but no iteration log exists while the child is running. Finding 2 below. |
| Tasks 1–10 / Task 11 recovery consistency | **Closed** | Staged `NEXT.md`, `HANDOFF.md`, and `IMPLEMENTATION_REPORT.md` consistently say Tasks 1–10 are complete and Task 11 repair/re-review is current, while keeping the live feature frontier external and authoritative. |

## Findings

### 1. HIGH — The controller deletes the surviving-root ownership record after cleanup becomes ambiguous

**Location:** `.scratch/ralph-loop/tools/ralph_loop.py:303-334,340-380`; missing end-to-end coverage in `.scratch/ralph-loop/tests/test_ralph_loop.py:289-300,331-340`

**Requirement:** Review 01 finding 1, rebuild plan Task 4 case 10–12 and Risk 7, `RALPH_LOOP.md`, manager `SKILL.md`, and `KNOWLEDGE.md` K-002 require ambiguous owned-tree cleanup to fail closed while preserving the controller/root ownership evidence. A subsequent preflight/controller must see the recorded live or unknown root and must not launch concurrently or kill an unverified tree. Root ownership may be cleared only after verified exit.

**Evidence / reproduction:**

- `hermes_executor` correctly leaves `root_pid` recorded when `terminate_process_tree` raises and emits `cleanup_ambiguous` (`ralph_loop.py:303-324,331-334`).
- That exception propagates to `run_loop`, whose unconditional `finally` executes `lock.unlink(missing_ok=True)` at lines 377–380 without inspecting the recorded root or whether cleanup was verified.
- A read-only temporary-directory reproduction wrote `root_pid: 54321` into the active ownership record and raised `ProcessTreeError("simulated ambiguous surviving root")` from the iteration. It returned `{"exception":"ProcessTreeError", ... "lock_exists_after_run_loop":false}`. Thus the exact evidence intended to make the next launch fail closed was erased.
- The added test `test_cleanup_ambiguity_preserves_recorded_root_and_is_visible` invokes `hermes_executor` directly and never exercises `run_loop`'s finalizer. Conversely, `test_exception_and_keyboard_interrupt_release_lock` requires unconditional deletion for generic exceptions but never distinguishes a root-free exception from an exception carrying an unverified root.
- `test_root_ownership_clears_only_after_verified_normal_exit` creates a lock but calls `hermes_executor` without `lock=lock`; its final `root_pid is None` assertion therefore proves only the fixture's initial value, not set-then-clear behavior.

**Required correction:** Keep the mechanical ownership record when the recorded root is non-null or record state cannot be safely read after a cleanup/interrupt/error path. Remove it only after the root has been verified exited and the record has been safely cleared to `root_pid: null`. Also make process-start/record-write failure handling fail closed so a launched child cannot escape before ownership is durably represented. Do not add semantic workflow state.

**Required verification:** Add an end-to-end `run_loop` test in which cleanup is ambiguous and prove the strict record remains with the root PID, a following preflight/acquisition hard-stops, and no second launch or unverified kill occurs. Add a real set-then-clear normal-exit test that passes the lock into `hermes_executor`, plus interruption and ownership-record write-failure cases. Re-run focused controller/preflight tests, the full Ralph suite, dry-run, and completion-true preflight.

### 2. MEDIUM — The bounded iteration log is created only after process exit, so live/crash evidence is absent

**Location:** `.scratch/ralph-loop/tools/ralph_loop.py:250-272,275-334`; misleading coverage name at `.scratch/ralph-loop/tests/test_ralph_loop.py:302-329`

**Requirement:** Review 01 finding 2 required capture to be bounded as it occurs, continuously drained without deadlock, and to preserve usable deterministic truncation evidence. The repaired `RALPH_LOOP.md` now expressly promises a continuously drained bounded tail and plan Tasks 3/5 require preserved iteration logs. For a three-hour iteration, lifecycle/root evidence must be inspectable while the process runs and must not disappear entirely if the controller is abruptly terminated.

**Evidence / reproduction:**

- `_BoundedIterationCapture.append` stores all retained bytes only in an in-memory `bytearray` (`ralph_loop.py:253-268`).
- The iteration path is not written or even created until `finalize()` calls `write_bytes` at lines 270–272, which occurs only from the executor `finally` at line 330.
- A real child-process probe printed and flushed `EARLY-EVIDENCE`, slept, then printed `TAIL-EVIDENCE`. During the child run the cited `iteration-0001.log` did not exist (`exists:false`); after exit it appeared with both lines. An abrupt controller termination during a long iteration therefore leaves no iteration output evidence.
- The child pipe is continuously drained, and the post-exit log is bounded with useful tail/truncation behavior. However, `test_iteration_log_is_bounded_during_capture_keeps_tail_and_does_not_deadlock` does not inspect the path during capture; all its assertions run after `hermes_executor` returns. Its name overstates what it proves.

**Required correction:** Use the smallest Tier-2 mechanism that continuously materializes a bounded iteration log while draining the child, retaining explicit truncation state and a useful tail without allowing the on-disk file to exceed `MAX_LOG_BYTES`. Preserve privacy boundaries and avoid pipe deadlock.

**Required verification:** Add a subprocess test that observes flushed early output in the on-disk log before child exit, checks the file never exceeds the cap during oversized output, proves the child completes without deadlock, and confirms the final nonzero/timeout log still contains explicit truncation evidence and a useful tail. Include a controller-abort/crash-oriented evidence check proportionate to the existing explicit preservation contract.

### 3. MEDIUM — Preflight does not strictly parse the controller/root ownership record and can accept duplicate-key ambiguity

**Location:** `.agents/skills/ralph-loop-manager/scripts/preflight.py:54-77`; missing strict-record coverage in `.scratch/ralph-loop/tests/test_ralph_manager_preflight.py`

**Requirement:** Review 01 finding 1 and the repaired manager/controller documentation require one **strict** controller/root ownership record; malformed or ambiguous ownership must hard-stop. The controller itself uses duplicate-key-rejecting `_strict_json`, so preflight and controller must agree on launch safety.

**Evidence / reproduction:**

- `runtime_lock_status` uses ordinary `json.loads` at line 59. Python silently keeps the last duplicate property.
- A temporary record containing `{"controller_pid":2147483647,"root_pid":54321,"root_pid":null}` was reported by preflight as launch-compatible: `[true, "stale controller_pid=2147483647; root_pid=none", null]`.
- The same record is ambiguous and is rejected by the controller's duplicate-key-aware parser. Preflight can therefore report safety for a record the controller correctly treats as invalid, contrary to documentation/code agreement and fail-closed preflight behavior.
- Existing preflight tests cover malformed value types but not duplicate ownership keys.

**Required correction:** Parse the ownership record with the same duplicate-key rejection semantics as the controller (prefer one shared small mechanical parser only if it remains simple and avoids import side effects), and return `INVALID_RUNTIME_OWNERSHIP_RECORD` without mutation for any duplicate property.

**Required verification:** Add focused preflight tests for duplicate `controller_pid` and `root_pid` keys, extra keys, malformed JSON, live/unknown roots, and the valid dead-controller/no-root stale case. Prove preflight and controller classify the same strict records consistently.

## Passing observations

Subject to the findings above, the following requested Task 11 areas are represented consistently and did not produce another blocking defect at Tier 2:

- The controller is substantially simpler and mechanical. It contains no milestone/issue/review semantic parser, assessor, diagnosis loop, campaign transition state, persisted semantic retry state, or controller-owned engineering-depth judgment.
- The launch command names only `jzgreekorch`; no model/provider/reasoning override or session resume flag is passed.
- Completion and pause signals use distinct exact one-Boolean schemas and are never reset by controller/preflight. Completion true prevents launch; pause true is separately blocked.
- Dead-controller/live-or-unknown-root acquisition checks exist and correctly preserve the pre-existing record before launch; the remaining defect is post-launch finalization and preflight strictness.
- Windows cleanup is PID-scoped through `taskkill /PID <owned-root> /T /F` and verifies the root process return before treating timeout cleanup as complete.
- The pipe reader prevents the oversized-output deadlock reproduced by review 01, and final post-exit logs retain a bounded diagnostic tail and explicit truncation marker.
- The orchestrator contract requires start/end live frontier checks, exactly one frontier action, stop-on-frontier-advance, fresh role delegation, and no successor work.
- TDD topology is explicit: one fresh `jzgreekimpl` owns RED → GREEN for `tdd-solo`; separate fresh `jzgreekimpl` RED and GREEN sessions are required for `tdd-ping-pong`.
- Tier-2 proportionality is carried through all role contracts. Practical exceptions are evidence-bounded and remain non-waivable for security, privacy, accessibility, data integrity, accepted behavior, core bilingual parity, unusable builds, and unsupported claims.
- Email is limited to independently verified full-feature completion or a genuine human-required blocker; routine progress, ordinary failures, and review repair loops are excluded.
- Stale legacy runtime profiles, model pins, bootstrap IDs, transition tools, and supervision machinery are absent from active controller/profile contracts. Remaining matches are new-profile substrings, negative assertions, or immutable/historical evidence.
- Tasks 1–10 / Task 11 recovery prose is now consistent. The current live feature frontier was read successfully (`contract-issue` for issue 02, warnings empty) but was neither copied into the staged recovery ledger nor advanced.
- Added-line static scanning found no hardcoded-secret assignment, `os.system`, `shell=True`, dangerous `eval`/`exec`, or unsafe pickle match.
- Unrelated staged/unstaged/untracked product and issue work remained present; the staged hash was unchanged after all read-only gates.

These passing observations do not override the three findings.

## Commands and exact results

1. `git status --short && git diff --cached --name-status && git diff --cached --binary | sha256sum && git diff --cached --stat` — exit 0; 28 staged paths; 2,505 insertions and 3,170 deletions; hash matched `727de91918953a18c9c2f6df38ac3ab13b8106e8fa9ba19887110e0ddf8c13fb`.
2. `features-cli docs current --feature greek-essence-showcase && features-cli progress --feature greek-essence-showcase --json` — exit 0; current live frontier `contract-issue` for issue 02; feature identified correctly; warnings `[]`; no workflow mutation.
3. `git diff --cached --check` — exit 0; 0 whitespace errors.
4. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_*.py' -v` — exit 0; 46 tests run, 45 passed, 1 skipped (`file symlinks unavailable`), 0 failed, 0 errors.
5. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_ralph_loop.py' -v` — exit 0; 21 tests run, 21 passed, 0 skipped, 0 failed, 0 errors.
6. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_ralph_manager_preflight.py' -v` — exit 0; 10 tests run, 9 passed, 1 skipped (`file symlinks unavailable`), 0 failed, 0 errors.
7. `python -B .scratch/ralph-loop/tools/ralph_loop.py --dry-run` — exit 0; canonical repository, completion true, pause false, `jzgreekorch`, timeout 10,800, cap 100, and `launch_performed:false`; no Hermes/Ralph launch.
8. `python -B .agents/skills/ralph-loop-manager/scripts/preflight.py --repo . --target greek-essence-showcase` — exit 2; `HARD_STOP` with exactly one hard stop, `COMPLETION_NOT_LAUNCH_COMPATIBLE`; runtime lock absent; all other listed mechanical checks passed; one expected dirty-worktree warning; `launch_performed:false`. This expected completion-true activation stop is not itself a finding.
9. Temporary end-to-end ownership-finalization probe — exit 0; raised the simulated `ProcessTreeError` and reported `lock_exists_after_run_loop:false`, reproducing finding 1 without launching Hermes or mutating the repository.
10. Temporary real-child live-log probe — exit 0; during the running child the iteration log was absent; after exit it existed with both flushed evidence lines, reproducing finding 2 without launching Hermes.
11. Temporary duplicate-key preflight ownership probe — exit 0; the duplicate-`root_pid` record was incorrectly returned launch-compatible, reproducing finding 3 without repository mutation.
12. Added-line static scan over `git diff --cached --unified=0` — exit 0; 2,505 added lines scanned; 0 suspicious hardcoded-secret, shell-injection, dangerous-eval/exec, or unsafe-pickle matches.
13. Active runtime/reference scan over staged manager/controller/profile/test paths — exit 0 for the wrapper; matches were new JZ profile names and negative assertions only; no active legacy runtime role, model override, semantic controller state, assessor, or transition path found.
14. `git diff --cached --binary | sha256sum` after verification — exit 0; hash remained `727de91918953a18c9c2f6df38ac3ab13b8106e8fa9ba19887110e0ddf8c13fb`.

## Required route

Route all three findings to a separate fresh `jzgreekimpl` repair session under Tier 2 — Prototype. Preserve review 01 and this review 02 unchanged. The reviewer must not repair implementation or tests and this FAIL must not be self-converted to approval. After focused/full repair verification, create a new immutable staged snapshot and obtain a fresh independent Task 11 code-review attempt at the next available immutable path. Operational acceptance review and Tasks 12–13 must wait for a fresh code-review PASS. Do not launch Ralph, change completion/pause signals, advance the feature frontier, email, stage, commit, push, deploy, or touch unrelated product/issue work during repair/re-review.
