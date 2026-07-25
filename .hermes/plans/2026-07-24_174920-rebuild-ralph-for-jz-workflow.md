# Rebuild Ralph for the JZ Workflow Implementation Plan

> **For Hermes:** Execute this plan under the Greek Essence feature-overseer rules. Delegate substantive implementation to fresh role profiles, preserve the active issue #01 worktree, and obtain independent code and operational review before activating the live campaign.

**Goal:** Replace the bootstrap-oriented Ralph supervisor with a thin, reliable loop that launches one fresh JZ orchestrator per iteration, completes exactly one `features-cli` frontier action per iteration, and runs until the Greek Essence feature campaign completes or safely pauses on a genuine blocker.

**Architecture:** Python owns only process mechanics: strict control-signal parsing, a high iteration bound, one-process locking, fresh Hermes launches, timeout/process-tree cleanup, lifecycle logs, and deterministic outcomes. The `jzgreekorch` profile owns workflow reasoning: it reads the project protocol, runs `features-cli docs current` and `progress --json`, executes exactly one frontier-owned JZ action through delegation and bounded repair loops, reconciles durable state, updates `HANDOFF.md`, and marks campaign completion only when the full campaign goal is proven. `features-cli` remains the sole workflow ledger.

**Tech Stack:** Python 3.11+ `unittest`, Hermes profiles and CLI, Bun-powered `features-cli`, Markdown protocol files, Next.js/pnpm repository gates, Resend `email-notification` skill.

---

## Locked decisions

1. Campaign target is `greek-essence-showcase` through all accepted milestones, issues, contracts, implementations, required reviews, and final feature completion. Deployment and separately authorized production actions are excluded.
2. One Ralph iteration completes exactly one durable `features-cli` frontier action. “One action” includes all ordinary delegation, repair, verification, and re-review required by that action.
3. The controller never parses milestones, issues, contracts, reviews, or JZ skills.
4. The controller does not verify or override profile models. Model/provider/reasoning configuration is profile-owned.
5. New profiles:
   - `jzgreekorch`: `gpt-5.6-sol`, high
   - `jzgreekimpl`: `gpt-5.6-terra`, high
   - `jzgreekrev`: `gpt-5.6-sol`, medium
   - `jzgreekvisualrev`: `gpt-5.6-sol`, medium
6. `tdd-solo` uses one fresh `jzgreekimpl` session for RED → GREEN. `tdd-ping-pong` uses two separate fresh sessions of the same `jzgreekimpl` profile: one RED agent and one GREEN agent.
7. The orchestrator is practical, deadline-aware, and responsible. It repairs material failures, corrects invalid tests, and may explicitly accept understood low-impact failures after bounded investigation when they do not threaten contractual behavior, user-visible quality, security, privacy, accessibility, data integrity, build viability, or the core demonstration.
8. Accepted exceptions must be truthful and evidence-backed; no failed command may be reported as passing.
9. Legacy `greekroot`, `greekimpl`, and `greekreview` profiles have already been exported under `%LOCALAPPDATA%/hermes/profile-archives/greek-legacy-20260724/`. Keep them installed until replacement acceptance passes, then delete them. `greekassets` is outside this replacement and remains untouched.
10. Preserve every existing Greek Essence worktree edit. Do not reset, stash, overwrite, stage, or commit active issue #01 files accidentally.

## Current live context

- Repository: `C:/Users/jimzord12/Documents/GitHub/greek-essence`
- Branch: `main`, intentionally dirty with issue #01 implementation and workflow artifacts.
- Live CLI frontier at planning time: `review-issue` for issue #01.
- `NEXT.md` is stale and still describes `implement-issue`; live `features-cli` state wins and summaries must be reconciled.
- `.scratch/ralph-loop/completion-signal.json` is currently `true` from the completed bootstrap campaign.
- `.scratch/ralph-loop/HANDOFF.md` and profile SOUL templates are bootstrap-oriented.
- The global `features-cli` shim is broken because it references a deleted pnpm virtual-store path. The source CLI under `C:/Users/jimzord12/Documents/GitHub/ai-arsenal/packages/features-cli` works with Bun when invoked using a native Windows path and `MSYS_NO_PATHCONV=1`.
- Existing controller safety worth retaining: strict Boolean completion parsing, lock ownership, bounded launches, fresh sessions, root PID-scoped Windows process-tree cleanup, logs, dry-run behavior, and interruption cleanup.
- Existing complexity to remove: campaign/task/tier controller identity, transition command, persisted retry counters, Diagnosis A/B agents, assessor prompts, lease extension, semantic workflow inference, bootstrap task assumptions, and dedicated-commit requirements.

## Planned file changes

### Create

- `.scratch/ralph-loop/profiles/jzgreekorch-SOUL.md`
- `.scratch/ralph-loop/profiles/jzgreekimpl-SOUL.md`
- `.scratch/ralph-loop/profiles/jzgreekrev-SOUL.md`
- `.scratch/ralph-loop/profiles/jzgreekvisualrev-SOUL.md`
- `.scratch/ralph-loop/tests/test_jz_orchestrator_contract.py`
- `.scratch/ralph-loop/tests/test_ralph_acceptance.py`
- Optionally `.scratch/ralph-loop/pause-signal.json` only if the blocked-stop design in Task 3 selects a repository signal rather than a controller-recognized outcome file.

### Rewrite substantially

- `.scratch/ralph-loop/tools/ralph_loop.py`
- `.scratch/ralph-loop/RALPH_LOOP.md`
- `.scratch/ralph-loop/HANDOFF.md`
- `.scratch/ralph-loop/IMPLEMENTATION_REPORT.md`
- `.agents/skills/ralph-loop-manager/SKILL.md`
- `.agents/skills/ralph-loop-manager/scripts/preflight.py`
- `.agents/skills/ralph-loop-manager/agents/openai.yaml`
- `.scratch/ralph-loop/profiles/README.md`
- `.scratch/ralph-loop/tests/test_ralph_loop.py`
- `.scratch/ralph-loop/tests/test_ralph_manager_preflight.py`

### Delete after replacement tests prove absence of references

- `.scratch/ralph-loop/tools/transition_campaign.py`
- `.scratch/ralph-loop/tests/test_ralph_transition.py`
- `.scratch/ralph-loop/tests/test_ralph_supervision.py`
- `.scratch/ralph-loop/tools/smoke_test.py` unless a distinct explicit live smoke wrapper still provides value after the one-iteration acceptance mode exists
- `.scratch/ralph-loop/profiles/greekroot-SOUL.md`
- `.scratch/ralph-loop/profiles/greekimpl-SOUL.md`
- `.scratch/ralph-loop/profiles/greekreview-SOUL.md`

### Reconcile without broadening

- `AGENTS.md`
- `NEXT.md`
- `.scratch/features/001-greek-essence-showcase/AGENTS.md`
- `.scratch/ralph-loop/KNOWLEDGE.md`
- `.scratch/ralph-loop/completion-signal.json` only during explicit campaign activation, not during implementation or tests

## Task 1: Protect the active worktree and capture a truthful baseline

**Objective:** Establish a reproducible baseline and path attribution before any Ralph or profile changes.

**Files:**

- Read: `AGENTS.md`
- Read: `NEXT.md`
- Read: `.scratch/features/001-greek-essence-showcase/AGENTS.md`
- Read: `.scratch/ralph-loop/*`
- Do not modify source files in this task.

**Steps:**

1. Run and save in working notes:
   ```bash
   git status --short --branch
   git diff --check
   git diff --stat
   git diff -- .scratch/ralph-loop .agents/skills/ralph-loop-manager
   ```
2. Run the source CLI because the global shim is currently broken:
   ```bash
   MSYS_NO_PATHCONV=1 bun 'C:\Users\jimzord12\Documents\GitHub\ai-arsenal\packages\features-cli\src\bin.ts' docs current --feature greek-essence-showcase
   MSYS_NO_PATHCONV=1 bun 'C:\Users\jimzord12\Documents\GitHub\ai-arsenal\packages\features-cli\src\bin.ts' progress --feature greek-essence-showcase --json
   ```
3. Attribute every dirty and untracked path to active issue #01, the existing workflow changes, or the upcoming Ralph rebuild. Stop rather than overwrite ambiguous concurrent work.
4. Record the archived legacy profile paths and hashes in the implementation report; do not duplicate archives.
5. Use a dedicated branch such as `feat/jz-ralph-workflow` only if branch creation can preserve the dirty worktree without staging or mixing issue #01 changes. Commit later with explicit Ralph-only pathspecs.

**Verification:** Baseline commands exit successfully; no file content changes; every existing path is attributed.

## Task 2: Repair the stable global `features-cli`

**Objective:** Restore the stable `features-cli` command so every fresh profile can use the workflow router without a source-path workaround.

**Files:**

- Source package: `C:/Users/jimzord12/Documents/GitHub/ai-arsenal/packages/features-cli/package.json`
- Global pnpm install outside the repository
- No Greek Essence source mutation expected.

**Steps:**

1. Confirm the broken shim and installed package metadata:
   ```bash
   command -v features-cli
   pnpm list -g --depth 0
   features-cli --help
   ```
2. Inspect the source package version and pack boundary. Run its package-defined validation before installation.
3. Produce a fresh package artifact from the AI Arsenal monorepo using its documented package command; do not install the stale `0.0.0` tarball.
4. Reinstall the generated current-version tarball with standalone pnpm 11.
5. Verify from the Greek Essence root:
   ```bash
   features-cli --help
   features-cli docs current --feature greek-essence-showcase
   features-cli progress --feature greek-essence-showcase --json
   ```
6. Verify a fresh Hermes profile process inherits the repaired command path.

**Acceptance:** Stable command exits zero, reports the same live frontier as direct source invocation, and its launcher targets an existing package path.

## Task 3: Define the minimal controller contract and blocked-stop mechanism

**Objective:** Freeze the controller’s deliberately small responsibilities before rewriting code.

**Files:**

- Modify: `.scratch/ralph-loop/RALPH_LOOP.md`
- Modify: `.agents/skills/ralph-loop-manager/SKILL.md`
- Test contracts will be encoded in Task 4.

**Required controller contract:**

```text
Before every launch:
  strict-read completion signal
  if true -> COMPLETE
  acquire/retain one controller lock

For iteration 1..max_iterations:
  launch fresh `hermes -p jzgreekorch` with no model/provider override
  enforce one generous fixed timeout
  capture output in a bounded iteration log
  on nonzero -> HERMES_FAILED
  on timeout -> terminate only owned process tree; verify exit; return TIMEOUT
  strict-read completion signal
  if true -> COMPLETE
  if orchestrator requested a genuine-blocker pause -> BLOCKED

After loop:
  return LIMIT_REACHED

Always:
  release lock on controlled exit
  preserve logs
  never infer JZ state
```

**Blocked-stop decision:** The controller needs one deterministic way to stop after a genuine human-required blocker without lying that the campaign is complete. Select the smallest mechanism during implementation:

- Preferred: a strict repository-local pause signal containing only `isPaused: boolean`, reset explicitly during campaign resume; or
- Equivalent: a strict controller outcome file written through a tiny project-owned helper.

Do not parse blocker prose from `HANDOFF.md`, model output, or email. Completion and pause must remain distinct.

**Practicality policy:** Document three classifications:

1. Material regression → repair.
2. Invalid/stale/flaky evidence → bounded diagnosis, correct or retire the invalid check.
3. Understood low-impact exception → record exact failure, evidence, impact, bounded attempts, and continue.

Never allow category 3 for security, privacy, accessibility, data integrity, accepted user behavior, core bilingual parity, unusable builds, or unsupported claims.

**Acceptance:** A reader can determine exactly what Python does and what only the orchestrator does; there is no campaign/task transition state.

## Task 4: Rewrite controller tests RED-first

**Objective:** Replace tests for removed supervision machinery with tests for the thin loop.

**Files:**

- Rewrite: `.scratch/ralph-loop/tests/test_ralph_loop.py`
- Create: `.scratch/ralph-loop/tests/test_ralph_acceptance.py`
- Delete later: `test_ralph_supervision.py`, `test_ralph_transition.py`

**RED cases:**

1. Exact Boolean completion signal accepts only `{ "isEverythingDone": <bool> }`.
2. True at startup launches no Hermes process.
3. False launches `jzgreekorch` once and does not pass `-m`, `--provider`, or `--resume`.
4. Every false iteration creates a fresh Hermes command/session.
5. Iteration that changes completion to true stops immediately.
6. Default iteration cap is high and finite (`100`); `--max-iterations 1` is supported.
7. Reaching the cap while false returns `LIMIT_REACHED` non-success.
8. Nonzero Hermes exit returns `HERMES_FAILED` and cites the iteration log.
9. Timeout terminates only the launched root process tree and returns `TIMEOUT`.
10. Ambiguous Windows process-tree cleanup fails closed.
11. Live lock prevents launch; stale lock recovery remains bounded and evidenced.
12. Exceptions and interruption release the lock.
13. Strict pause signal returns `BLOCKED` without changing completion.
14. Dry-run prints resolved repo, signal, profile command, timeout, iteration cap, and launch-performed false.
15. No controller state, assessor, diagnosis, task identity, campaign transition, or model override remains.

**Run RED:**

```bash
python -B -m unittest discover -s .scratch/ralph-loop/tests -p "test_*.py" -v
```

Expected: new contract tests fail against the old controller for explicit missing/incorrect behavior.

## Task 5: Implement the thin controller GREEN

**Objective:** Replace `.scratch/ralph-loop/tools/ralph_loop.py` with the smallest implementation that satisfies Task 4.

**Files:**

- Rewrite: `.scratch/ralph-loop/tools/ralph_loop.py`
- Delete: `.scratch/ralph-loop/tools/transition_campaign.py`
- Delete or reduce: `.scratch/ralph-loop/tools/smoke_test.py`

**Implementation outline:**

```python
ROOT_PROFILE = "jzgreekorch"
DEFAULT_MAX_ITERATIONS = 100
DEFAULT_ITERATION_TIMEOUT = 3 * 60 * 60

class LoopOutcome(str, Enum):
    COMPLETE = "COMPLETE"
    BLOCKED = "BLOCKED"
    LIMIT_REACHED = "LIMIT_REACHED"


def build_hermes_command() -> list[str]:
    return [
        "hermes", "-p", ROOT_PROFILE, "chat", "-Q", "--yolo",
        "--pass-session-id", "--source", "ralph", "-q", root_prompt(),
    ]


def run_loop(...):
    with controller_lock(...):
        if read_completion_signal(repo):
            return LoopOutcome.COMPLETE
        if read_pause_signal(repo):
            return LoopOutcome.BLOCKED
        for iteration in range(1, max_iterations + 1):
            execute_fresh_root(iteration, timeout)
            if read_completion_signal(repo):
                return LoopOutcome.COMPLETE
            if read_pause_signal(repo):
                return LoopOutcome.BLOCKED
        return LoopOutcome.LIMIT_REACHED
```

Retain only privacy-bounded lifecycle fields: timestamp, event, controller PID, root PID, iteration, outcome, and log path. Never log prompts, environment values, credentials, or email content.

**Run GREEN:**

```bash
python -B -m unittest discover -s .scratch/ralph-loop/tests -p "test_*.py" -v
python .scratch/ralph-loop/tools/ralph_loop.py --dry-run
```

Expected: all retained/new Ralph tests pass; dry-run performs no launch or mutation.

## Task 6: Rebuild the manager preflight around mechanics, not model/workflow semantics

**Objective:** Make preflight confirm only launch safety and required dependencies.

**Files:**

- Rewrite: `.agents/skills/ralph-loop-manager/scripts/preflight.py`
- Rewrite: `.scratch/ralph-loop/tests/test_ralph_manager_preflight.py`
- Modify: `.agents/skills/ralph-loop-manager/SKILL.md`

**Preflight checks:**

- Correct Greek Essence repository root.
- Required controller/protocol/signal files exist and are regular contained files.
- Git, Python 3.11+, Hermes, Bun, pnpm, and stable `features-cli` are available.
- `features-cli docs current --feature greek-essence-showcase` exits zero.
- `progress --json` parses and identifies that feature without warnings.
- `jzgreekorch`, `jzgreekimpl`, `jzgreekrev`, and `jzgreekvisualrev` exist.
- Do not inspect or assert profile model/provider/reasoning values.
- No live controller lock.
- Completion and pause signals have exact schemas and launch-compatible values.
- Email skill/script and environment shape are available; dry-run remains manager-owned before live activation.
- Worktree status is observable. Dirtiness is reported for orchestrator attribution, not automatically rejected when already campaign-owned.
- Controller dry-run passes.

**RED/GREEN:** Update tests first, run the focused preflight suite, implement the minimum checker, rerun to green.

```bash
python -B -m unittest .scratch.ralph-loop.tests.test_ralph_manager_preflight -v
```

If module naming is incompatible with the hyphenated path, use discovery with a focused filename pattern.

## Task 7: Create source-controlled role contracts

**Objective:** Define clean, narrow SOUL templates for all four profiles.

**Files:**

- Create: `.scratch/ralph-loop/profiles/jzgreekorch-SOUL.md`
- Create: `.scratch/ralph-loop/profiles/jzgreekimpl-SOUL.md`
- Create: `.scratch/ralph-loop/profiles/jzgreekrev-SOUL.md`
- Create: `.scratch/ralph-loop/profiles/jzgreekvisualrev-SOUL.md`
- Rewrite: `.scratch/ralph-loop/profiles/README.md`
- Create: `.scratch/ralph-loop/tests/test_jz_orchestrator_contract.py`

**Orchestrator contract must require:**

1. Read root and feature protocol plus Ralph handoff/knowledge.
2. Run `features-cli docs current` and `progress --json` at iteration start and end.
3. Treat CLI frontier as authoritative; reconcile stale `NEXT.md`/`HANDOFF.md` rather than creating a second ledger.
4. Complete exactly one frontier action.
5. Load the recommended live JZ skill and its references.
6. Delegate substantive implementation, code review, and visual review to the proper fresh profiles.
7. For `tdd-ping-pong`, launch separate RED and GREEN sessions, both using `jzgreekimpl`.
8. Continue ordinary repair/re-review without operator coordination.
9. Apply the practical failure classification and bounded-effort policy.
10. Update `HANDOFF.md` before every normal exit and `KNOWLEDGE.md` only for durable quirks.
11. Send email only for verified completion or genuine human-required blocker.
12. Mark completion true only after full feature completion; request pause for genuine blockers.
13. Never start the next frontier action in the same iteration.

**Implementer contract must allow:** RED-only, GREEN-only, or RED→GREEN briefs. It must preserve reviewer artifacts, report exact gates, and never self-review or select the next issue.

**Code reviewer contract must:** remain independent, write immutable review evidence, and never repair its own findings.

**Visual reviewer contract must:** use Playwright CLI and vision inspection, cover required EN/GR states/viewports, write immutable visual evidence, and never repair its own findings.

**Contract tests:** Assert profile names, required commands, one-action boundary, TDD topology, practical exception safeguards, and absence of stale bootstrap IDs/model names.

## Task 8: Create and configure the four live Hermes profiles

**Objective:** Install clean profiles whose configuration owns model/provider/reasoning and repository cwd.

**External state:** `%LOCALAPPDATA%/hermes/profiles/`

**Steps:**

1. Create alphanumeric profiles without cloning historical session/memory state:
   ```bash
   hermes profile create jzgreekorch --clone-from default --description "Greek Essence JZ workflow orchestrator"
   hermes profile create jzgreekimpl --clone-from default --description "Greek Essence JZ contract implementer for RED and GREEN phases"
   hermes profile create jzgreekrev --clone-from default --description "Greek Essence independent JZ code reviewer"
   hermes profile create jzgreekvisualrev --clone-from default --description "Greek Essence independent visual reviewer"
   ```
2. Configure each profile’s model/provider/reasoning and `terminal.cwd` using `hermes -p <profile> config set ...`. Ralph must not pass model overrides.
3. Replace each live profile `SOUL.md` with its reviewed repository template.
4. Ensure required project-local skills are visible from repository cwd. Make the external `email-notification` skill available to the orchestrator only as needed.
5. Verify with `hermes profile show <name>` and read-only role probes.
6. Do not delete legacy profiles yet.

**Acceptance:** Each profile starts from the repository, loads the intended SOUL, uses its profile-owned configuration, and performs only its role during a harmless read-only probe.

## Task 9: Rewrite durable handoff and campaign protocol

**Objective:** Make fresh orchestrators recover the live feature without bootstrap history or duplicated workflow state.

**Files:**

- Rewrite: `.scratch/ralph-loop/HANDOFF.md`
- Selectively trim/retain: `.scratch/ralph-loop/KNOWLEDGE.md`
- Reconcile: `NEXT.md`
- Reconcile: `.scratch/features/001-greek-essence-showcase/AGENTS.md`

**HANDOFF structure:**

```markdown
# Ralph Handoff

## Campaign

- Feature
- Goal
- Status
- Explicit exclusions

## Last iteration

- Starting frontier
- Action attempted
- Durable result
- Verification and accepted exceptions
- Ending frontier

## Next iteration

- Expected frontier
- Immediate instruction
- Relevant files
- Genuine blocker, if any

## Worktree

- Branch/HEAD
- Attribution summary
- Important uncommitted state
```

Do not copy issue counts or statuses that can be freshly obtained from `features-cli`. Record only enough to explain the last transition and recover interrupted work.

Retain K-001 Windows harness knowledge. Retain the process-orphan warning only if still relevant to the simplified controller’s owned-tree cleanup. Remove bootstrap task progress.

## Task 10: Validate practical orchestration with deterministic scenario tests

**Objective:** Prove the orchestrator contract handles both material and immaterial failures without perfectionism or silent waiver.

**Files:**

- Extend: `.scratch/ralph-loop/tests/test_jz_orchestrator_contract.py`
- Add fixture protocol text if needed under `.scratch/ralph-loop/tests/fixtures/`

**Scenarios:**

1. Material locale-parity failure → must route repair and cannot accept exception.
2. Accessibility failure on an affected surface → must repair.
3. Security/privacy/data-integrity failure → must pause/escalate if not repairable.
4. Stale test conflicting with accepted contract → may correct/remove test with evidence.
5. Known Windows environmental failure with stronger passing evidence → may accept and record after bounded investigation.
6. Marginal non-contract metric with polished live result → may accept without repeated expensive reruns.
7. Failed review with in-contract findings → must repair and re-review.
8. Genuine credential requirement → update handoff, email blocked, request pause, keep completion false.
9. Frontier advances after implementation → stop iteration rather than starting review.
10. Frontier advances after review → stop iteration rather than contracting the next issue.

Tests should validate protocol invariants and fixture transitions, not attempt to unit-test model intelligence.

## Task 11: Run independent code and operational review of the rebuild

**Objective:** Obtain fresh review before any live campaign activation.

**Profiles:**

- Implementation/rework: `jzgreekimpl`
- Code review: fresh `jzgreekrev`
- Operational acceptance review: another fresh `jzgreekrev`

**Review scope:**

- Controller simplicity and absence of semantic parsing.
- Strict signal schemas.
- Lock and process cleanup behavior on Windows.
- No model overrides.
- No stale profile/task references.
- One-action iteration contract.
- Correct TDD profile topology.
- Practical exception safeguards.
- Email escalation boundaries.
- Worktree preservation.
- Documentation/code/test agreement.

Write immutable review artifacts under `.scratch/ralph-loop/reviews/` using the next available numbers. Route substantive findings to `jzgreekimpl`; use fresh review attempts after repair.

## Task 12: Run hermetic and one-iteration acceptance gates

**Objective:** Exercise the rebuilt artifact without advancing the live Greek Essence frontier unexpectedly.

**Hermetic gates:**

```bash
python -B -m unittest discover -s .scratch/ralph-loop/tests -p "test_*.py" -v
python .scratch/ralph-loop/tools/ralph_loop.py --dry-run
python .agents/skills/ralph-loop-manager/scripts/preflight.py --repo . --target greek-essence-showcase
pnpm format:check
pnpm lint
pnpm typecheck
pnpm test:unit
pnpm build
pnpm validate:content
git diff --check
```

Do not require expensive browser/performance gates for controller-only code unless the rebuild changes application behavior or the active feature contract requires a fresh aggregate snapshot at activation time.

**Live one-iteration acceptance:** Use a disposable repository fixture or a non-mutating orchestrator probe first. A real live one-iteration run against Greek Essence requires explicit activation preparation because the current live frontier is review issue #01 and will mutate workflow artifacts.

Verify:

- one fresh `jzgreekorch` starts;
- it delegates to correct fresh profiles;
- it completes only the current frontier action;
- it updates handoff;
- it does not start the next frontier;
- controller exits with the expected bounded outcome;
- no child process survives;
- completion remains false unless the whole campaign is complete.

## Task 13: Activate the live Greek Essence campaign

**Objective:** Transition from tested infrastructure to unattended feature execution.

**Prerequisites:**

- Stable global `features-cli` works.
- All new profiles pass role probes.
- Controller/preflight tests pass.
- Independent reviews approve.
- Dirty worktree is fully attributed.
- No live Ralph lock or surviving owned process exists.
- Email dry-run targets `jimzordgtx@gmail.com` successfully.
- `HANDOFF.md`, `NEXT.md`, and live CLI frontier are reconciled.

**Steps:**

1. Reset the pause signal to unpaused through the documented explicit campaign activation procedure.
2. Explicitly change completion from `true` to `false` for the new feature campaign.
3. Run preflight and dry-run again.
4. Launch the controller as one tracked background process with completion notification:
   ```bash
   python .scratch/ralph-loop/tools/ralph_loop.py --max-iterations 100
   ```
5. Verify readiness from lifecycle log and process identity rather than waiting blindly.
6. Monitor meaningful boundaries. Do not launch a second controller.

**Expected first action:** Fresh CLI state decides. At plan creation it is `review-issue` for issue #01; do not hard-code this into the controller.

## Task 14: Retire legacy profiles and stale runtime state after acceptance

**Objective:** Remove obsolete role profiles only after the new campaign path is proven.

**Steps:**

1. Confirm the three archives still exist and their hashes match the recorded values.
2. Search repository/controller/runtime references for `greekroot`, `greekimpl`, and `greekreview`.
3. Delete profiles:
   ```bash
   hermes profile delete greekroot
   hermes profile delete greekimpl
   hermes profile delete greekreview
   ```
4. Do not delete `greekassets`.
5. Archive obsolete external controller-state/diagnosis records as historical evidence; do not mix them into the new runtime state or silently delete evidence.
6. Re-run profile list, preflight, controller dry-run, and one fresh role probe.

## Git and delivery strategy

This is a substantial workflow change and should normally use branch → PR → independent review → normal merge. The current worktree is intentionally dirty with active issue #01, so Git operations must use explicit Ralph-only pathspecs and must never stage unrelated feature implementation accidentally.

Before committing:

```bash
git status --short
git diff --check
git diff -- .scratch/ralph-loop .agents/skills/ralph-loop-manager .hermes/plans
```

Stage only reviewed Ralph/manager/plan paths. Verify the staged diff with `git diff --cached --check` and `git diff --cached --stat`. Do not include active application files, issue reports, status files, or unrelated changes unless separately reviewed and intentionally part of the same delivery.

## Risks and mitigations

1. **Orchestrator rationalizes important failures as “practical.”** Mitigation: explicit non-waivable categories, evidence requirements, independent reviewer scrutiny, and immutable accepted-exception records.
2. **Blocked campaign loops forever.** Mitigation: strict pause outcome distinct from completion.
3. **Profile command silently overrides profile configuration.** Mitigation: tests assert no `-m`/`--provider`; controller names profile only.
4. **Fresh profiles cannot access credentials or approved skills.** Mitigation: role probes and email dry-run before activation; no secrets copied into repository files.
5. **Broken `features-cli` causes every iteration to fail.** Mitigation: repair stable global installation before controller/profile acceptance.
6. **Dirty issue #01 edits are overwritten or accidentally committed.** Mitigation: baseline attribution, explicit pathspec staging, no reset/stash, diff verification before every Git action.
7. **Controller death leaves a live root.** Mitigation: retain owned PID tracking during execution, PID-scoped Windows tree cleanup, and fail-closed survivor verification without restoring assessor complexity.
8. **One action expands into the next action.** Mitigation: start/end frontier checks, root SOUL invariant, and scenario tests.
9. **Visual review becomes screenshot automation without judgment.** Mitigation: dedicated visual profile, vision inspection requirement, immutable grounded verdict.
10. **Controller simplification removes useful evidence.** Mitigation: retain privacy-bounded lifecycle and iteration logs while deleting semantic state.

## Completion criteria

The rebuild is complete when:

- the stable global CLI works;
- the thin controller and preflight pass all hermetic tests;
- four new profiles pass role acceptance;
- documentation, SOUL contracts, and code agree;
- independent review approves;
- one live bounded iteration proves exactly one frontier action and clean process exit;
- the live campaign is safely armed and launched;
- archived legacy profiles are retired only after replacement proof;
- no active issue #01 work is lost or falsely reported;
- no deployment, credential disclosure, remote mutation, or unrelated repository action occurs.
