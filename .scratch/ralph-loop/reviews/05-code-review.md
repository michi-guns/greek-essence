# Ralph/JZ Controller Repair — Independent Code Review 05

**Verdict:** FAIL  
**Resolved engineering depth:** Tier 2 — Prototype (direct operator instruction; also consistent with root `AGENTS.md` and feature `SPEC.md` `implementation_depth: 2`)  
**Review type:** Fresh independent review of the current seven-path unstaged repair snapshot relative to the index  
**Reviewed unstaged binary diff SHA-256:** `ea49a8cf2d22e0645d566c5e28f7f5900028e018482894665f4ef720e55ef928`

## Exact scope and reviewed diff

Only the unstaged delta relative to the index on these seven paths was reviewed:

1. `.scratch/ralph-loop/tools/ralph_loop.py`
2. `.scratch/ralph-loop/tests/test_ralph_loop.py`
3. `.scratch/ralph-loop/tests/test_ralph_acceptance.py`
4. `.scratch/ralph-loop/tests/test_ralph_manager_preflight.py`
5. `.agents/skills/ralph-loop-manager/scripts/preflight.py`
6. `.scratch/ralph-loop/RALPH_LOOP.md`
7. `.agents/skills/ralph-loop-manager/SKILL.md`

The scoped delta is 52,146 binary-diff bytes and contains 417 insertions and 59 deletions across exactly seven paths. I inspected the full live files and the complete unstaged diff, not implementation prose alone.

I read root `AGENTS.md`, `NEXT.md`, `docs/README.md`, the bootstrap entry point, feature `AGENTS.md`, feature `SPEC.md`, the Ralph/JZ rebuild plan, rebuild implementation report, immutable reviews 03 and 04, the controller, preflight, focused/full Ralph tests, and both active controller documents. The live CLI reported frontier `contract-issue` for issue 02 and recommended `jz-issue-to-contract`; `features-cli docs execution` identified `jz-code-review-super-fast` as the review owner, and that live skill was read from the AI Arsenal source package. Its workflow/status-mutation instructions were overridden by this direct read-only review brief. The current issue-02 change-contract artifact does not yet exist, as expected at the live contract frontier; it was not treated as authority for this separate Ralph repair.

No implementation, test, documentation, signal, frontier, status, profile, email, remote, staging, commit, push, deployment, or visual-review action was performed. No Ralph or Hermes process was launched. This immutable review is the sole repository artifact written by this review session.

## Findings

### 1. HIGH — A second iteration for the same frontier owner fails before launch because the invocation run directory is recreated with `exist_ok=False`

**Location:** `.scratch/ralph-loop/tools/ralph_loop.py:337-356,508,522-523`; missing same-owner multi-iteration coverage near `.scratch/ralph-loop/tests/test_ralph_loop.py:556-567`

**Requirement:** The operator requires issue logs at `<issue>/.Ralph/runs/<unique-no-clobber-run-id>/iteration-####.log`, correct rerouting when the owner changes between iterations, and a controller capable of continuing its bounded loop. `RALPH_LOOP.md:30` says every controller invocation has a collision-resistant no-clobber run directory and changed owners receive their own run directory. The default controller may perform up to 100 iterations, and consecutive frontier actions commonly remain owned by the same issue. A run directory belonging to the current invocation must therefore accept that invocation's later `iteration-0002.log`, `iteration-0003.log`, and so on without weakening cross-invocation no-clobber behavior.

**Evidence / reproduction:** An isolated complete-`run_loop` probe held the same valid issue owner for two iterations, returned successful fake child processes, and counted child creation. Iteration 1 launched and wrote its log. Before iteration 2 could call `Popen`, `resolve_frontier_log_location(..., create=True)` called `run_dir.mkdir(..., exist_ok=False)` on the same invocation UUID directory and raised:

```text
FrontierRouteError: Ralph run directory already exists: <issue>/.Ralph/runs/3a8aab8fd24c4625973aa822f3d043bc
popen_count: 1
logs: [<issue>/.Ralph/runs/3a8aab8fd24c4625973aa822f3d043bc/iteration-0001.log]
```

The existing changed-owner test avoids the defect because the same UUID is created under two different owner directories. The existing two-invocation test also passes because each invocation receives a different UUID.

**Required correction:** Establish a no-clobber run directory once per owner for the current controller invocation, then reuse that exact invocation-owned directory for later iterations routed to the same owner. When the owner changes, create the same run ID under the new owner once. Preserve collision refusal against a directory not established by the current invocation and preserve one distinct bounded log per iteration.

**Required verification:** Add a complete two-iteration `run_loop` regression with an unchanged issue owner. Prove two child starts occur; one run directory contains independently readable `iteration-0001.log` and `iteration-0002.log`; no prior invocation evidence is overwritten; changed-owner routing still works; and a genuinely pre-existing/colliding run directory still fails before `Popen` or new filesystem creation.

### 2. HIGH — Reparse-point paths are accepted, and a pre-existing `.Ralph` junction can redirect run-directory creation outside the repository

**Location:** `.scratch/ralph-loop/tools/ralph_loop.py:303-316,320-334,348-355`; missing Windows junction/reparse coverage in `.scratch/ralph-loop/tests/test_ralph_loop.py:569-590`

**Requirement:** The direct brief requires absolute, traversal, Windows-drive, out-of-repository, symlink, and invalid-owner routes to fail closed before `Popen` **or filesystem creation**. `RALPH_LOOP.md:30` and manager `SKILL.md:65` likewise require contained safe owners and rejection before launch. This is an explicit path-safety acceptance boundary, not optional higher-tier hardening.

**Evidence / reproduction:** The implementation resolves `artifactPath` before checking `artifact.is_symlink()`, so the check observes the resolved target rather than the supplied link. It then verifies `owner.is_symlink()` only on that resolved target. A Windows temporary-directory probe used ordinary directory junctions (`cmd.exe /c mklink /J`, exit 0):

1. `repo/link` junctioned to `repo/target`; progress supplied `artifactPath: "link/frontier.md"`. `_frontier_artifact_owner` accepted it and returned the resolved `repo/target` owner instead of rejecting the reparse path.
2. `repo/.Ralph` junctioned to a sibling `outside` directory; progress supplied a valid contained non-issue artifact. `resolve_frontier_log_location(..., create=True)` accepted the route and created `outside/runs/junction-run`. The returned lexical path appeared under `repo/.Ralph`, but `run_dir.resolve()` proved the actual directory was outside the repository.

The ordinary file-symlink test is skipped on this Windows account because file-symlink privilege is unavailable; that skip does not cover junctions, which are available and reproduced the escape.

**Required correction:** Reject symlink/junction/reparse components in the supplied artifact path and owner path before accepting the route. Before creating a run directory, validate the existing `.Ralph`/`runs` chain against reparse redirection and prove the resolved destination remains under the validated owner/repository. Keep the solution narrow to evidence-path safety; do not add generalized filesystem infrastructure.

**Required verification:** Add Windows-capable temporary junction tests (and ordinary symlink tests where supported) proving: artifact-path reparse points are rejected; owner reparse points are rejected; a pre-existing `.Ralph` or `runs` junction cannot create anything outside the owner/repository; `Popen` remains uncalled; and no new run directory is created on every rejection. Retain the existing absolute/traversal/drive/out-of-repository matrix.

### 3. HIGH — A structurally invalid frontier with no `kind` is treated as valid, creates `.Ralph`, and launches the child

**Location:** `.scratch/ralph-loop/tools/ralph_loop.py:292-334`; `.agents/skills/ralph-loop-manager/scripts/preflight.py:122-138`; missing invalid-frontier-shape coverage near `.scratch/ralph-loop/tests/test_ralph_loop.py:569-581`

**Requirement:** The direct brief requires malformed, missing, or invalid frontier data to stop before `Popen` or filesystem creation. The operator permits narrow **strict** parsing of `features-cli progress ... --json` solely for routing. The live CLI frontier schema includes `kind`, and the controller must have enough validated structure to distinguish issue-owned from non-issue-owned artifacts without semantic workflow reasoning.

**Evidence / reproduction:** `_frontier_artifact_owner` requires a frontier object and `artifactPath`, but never validates `frontier.kind`. It also decides issue/non-issue ownership solely from optional `issueId`. An isolated complete-`run_loop` probe supplied otherwise plausible JSON with:

```json
{"frontier":{"artifactPath":".scratch/features/001/issues/02-owner/artifact.md"}}
```

The controller returned `LIMIT_REACHED`, called `Popen` once, and created `.Ralph`. Thus an incomplete frontier that cannot be strictly classified is fail-open. By contrast, the independent 13-case matrix showed CLI nonzero, malformed JSON, duplicate JSON, missing/non-object frontier, missing/non-string path, POSIX absolute, Windows-drive, traversal, invalid owner, invalid issue ID, and issue-directory mismatch all raised `FrontierRouteError` with `popen_count: 0` and `ralph_created: false`.

Preflight's separate `validate_progress` also uses ordinary `json.loads` and accepts any frontier object by reporting `kind or "none"`; the controller dry-run currently supplies the eventual hard stop for many such cases, but that does not make the controller's missing-kind launch acceptable.

**Required correction:** Strictly validate the minimum frontier routing schema, including a present valid `kind` and consistent issue/non-issue routing fields. Issue frontier kinds must carry a valid positive `issueId` matching the contained issue directory; non-issue frontier kinds must be explicitly classifiable as non-issue routes. Reject missing, unknown, or inconsistent routing shape without attempting workflow-state interpretation.

**Required verification:** Add complete dry-run and `run_loop` tests for missing/unknown `kind`, issue kind without `issueId`, non-issue kind with inconsistent issue fields, and malformed/duplicate frontier keys. Every case must prove no `.Ralph` creation and no `Popen`. Add equivalent strict preflight coverage and retain the currently passing valid live-frontier path.

## Review-04 HIGH ownership repair

The review-04 ownership-write/cleanup-ambiguity repair remains intact in this snapshot. The exact targeted regression command passed three tests: durable `starting`, bounded exact-PID `running` retries, PID-scoped cleanup, preserved `cleanup_ambiguous` evidence, later preflight/controller refusal, and successful-cleanup behavior all remained covered. Static inspection confirmed the runtime-state logic still uses the exact `Popen` PID and contains no name-based or bulk-kill path. None of the findings above reopens review-04's HIGH finding.

## Passing observations

Subject to the blocking findings:

- Two separate controller invocations at iteration 1 produced two distinct UUID run directories and preserved separately readable `FIRST-READABLE` and `SECOND-READABLE` logs.
- Changed-owner routing, valid issue-owner routing, no-clobber collision refusal, bounded live-tail capture, nonzero/timeout evidence, strict signal handling, and ownership ambiguity tests passed.
- Dry-run exited 0 with `launch_performed: false`; live preflight exited 2 only for the expected existing `COMPLETION_NOT_LAUNCH_COMPATIBLE` hard stop and also reported `launch_performed: false`.
- After both commands, the live issue-02 owner had no `.Ralph` directory.
- The scoped diff has no whitespace errors and passed scoped Prettier. Added-line scanning found no hardcoded-secret assignment, shell injection, dangerous eval/exec, unsafe pickle, or name-based/bulk process-kill match.
- Full lint, typecheck, unit tests, build, and content validation passed after dependencies were restored without browser download.

These observations do not override the findings.

## Commands and exact results

1. `git status --short --branch; git diff --name-status; git diff --cached --name-status` — exit 0; confirmed the intentionally dirty `feat/jz-ralph-workflow` worktree, the seven requested unstaged paths, and the pre-existing populated index.
2. `git diff --binary -- <seven paths> | sha256sum; git diff --stat -- <seven paths>; git diff --numstat -- <seven paths>; git diff --name-only -- <seven paths>; git diff --binary -- <seven paths> | wc -c` — exit 0; hash `ea49a8cf2d22e0645d566c5e28f7f5900028e018482894665f4ef720e55ef928`; exactly 7 paths, 417 insertions, 59 deletions, 52,146 bytes.
3. `features-cli docs current --feature greek-essence-showcase` — exit 0; live frontier `contract-issue`, issue 02, recommended skill `jz-issue-to-contract`; read-only.
4. `features-cli progress --feature greek-essence-showcase --json` — exit 0; feature slug matched, warnings `[]`, issue 02 artifact path returned; read-only.
5. `features-cli docs --help` — exit 1 with exact output `Unknown flag --help. Run --help for usage.` This failed exploratory invocation was not claimed as passing. `features-cli docs --index --json`, `features-cli docs issues`, and `features-cli docs execution` subsequently exited 0 and exposed the documented topics/owners without mutation.
6. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_ralph_loop.py' -v` — exit 0; 31 tests passed, 0 skipped/failed/errors.
7. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_ralph_acceptance.py' -v` — exit 0; 2 tests passed.
8. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_ralph_manager_preflight.py' -v` — exit 0; 12 tests run, 11 passed and 1 skipped (`file symlinks unavailable`).
9. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_*.py' -v` — exit 0; 58 tests run, 57 passed and 1 skipped (`file symlinks unavailable`).
10. Exact targeted review-04 command for the two ownership-write tests plus preflight cleanup-ambiguity test — exit 0; 3 tests passed.
11. `python -B .scratch/ralph-loop/tools/ralph_loop.py --dry-run` — exit 0; live owner resolved to issue 02, UUID run path reported, completion true, pause false, and `launch_performed: false`; no `.Ralph` created.
12. `python -B .agents/skills/ralph-loop-manager/scripts/preflight.py --repo . --target greek-essence-showcase` — exit 2; `HARD_STOP` with exactly the expected `COMPLETION_NOT_LAUNCH_COMPATIBLE`, one dirty-worktree warning, all other checks including `frontier-log-route` passed, `launch_performed: false`, and no `.Ralph` created.
13. Isolated same-owner complete-loop probe — probe command exit 0; reproduced finding 1 with `FrontierRouteError`, only 1 `Popen`, and only iteration-0001 evidence.
14. Isolated two-invocation complete-loop probe — probe command exit 0; 2 iteration-0001 logs existed in distinct run directories and retained `FIRST-READABLE` and `SECOND-READABLE` independently.
15. Isolated 13-case invalid-route matrix — probe command exit 0; CLI nonzero, malformed JSON, duplicate JSON, missing/non-object frontier, missing/non-string path, POSIX absolute, Windows drive, traversal, invalid owner, invalid issue ID, and issue mismatch all stopped with 0 `Popen` and no `.Ralph`; the missing-kind control reproduced finding 3 with 1 `Popen` and `.Ralph` creation.
16. Windows junction probes using temporary directories — probe command exit 0; both `mklink /J` commands exited 0; artifact junction was accepted; a pre-existing `.Ralph` junction was accepted and created `outside/runs/junction-run`, reproducing finding 2.
17. Initial parallel `pnpm format:check`, `pnpm lint`, and `pnpm typecheck` attempts — each exit 1 before running its script because pnpm attempted dependency restoration and Puppeteer postinstall failed: cached Chrome and headless-shell folders existed without their executables. These failures were preserved and not reported as passes.
18. `PUPPETEER_SKIP_DOWNLOAD=1 pnpm install --frozen-lockfile` — exit 0; 1,170 packages restored, Puppeteer browser download skipped, prepare completed.
19. Rerun `pnpm format:check` — exit 1; Prettier reported 8 pre-existing/out-of-scope files (the rebuild plan and seven `.playwright-cli` YAML files). This failed full command was not treated as a seven-path finding. `pnpm exec prettier --check <seven paths>` — exit 0; all scoped files matched style.
20. Rerun `pnpm lint` — exit 0. Rerun `pnpm typecheck` — exit 0.
21. `pnpm test:unit` — exit 0; 7 test files and 29 tests passed.
22. `pnpm build` — exit 0; production build compiled, typechecked, generated 8/8 static pages, and completed optimization.
23. `pnpm validate:content` — exit 0; English/Greek showcase content and media approval checks passed.
24. `git diff --check; git diff --cached --check` — exit 0; unstaged and cached whitespace checks both passed.
25. Added-line scoped static scan — exit 0; 417 added lines; 0 hardcoded-secret assignment, 0 shell-injection, 0 dangerous eval/exec, 0 unsafe-pickle, and 0 name-based/bulk-kill matches.
26. Final scoped binary hash/numstat/status and live-owner `.Ralph` absence check — exit 0; hash remained `ea49a8cf2d22e0645d566c5e28f7f5900028e018482894665f4ef720e55ef928`; 417/59 remained unchanged; no live issue-02 `.Ralph` existed before this artifact was written.

## Required route

Preserve reviews 01–05 unchanged. Return these findings to `jzgreekorch` for a separate fresh Tier-2 implementation session. Do not self-repair or self-convert this FAIL to approval. After repair, rerun focused/full gates and obtain a new immutable fresh code-review attempt. Review-03 stale handoff medium finding 3 remains explicitly ignored and must not be requested in this scope. Do not launch Ralph, run operational acceptance, mutate completion/pause signals or the feature frontier, email, stage, commit, push, deploy, or touch unrelated work.
