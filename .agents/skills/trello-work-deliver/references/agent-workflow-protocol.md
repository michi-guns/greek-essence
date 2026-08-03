# Trello Agent Development Workflow Protocol

## 1. Purpose

This protocol defines how users and software-development agents coordinate durable Work Units on Trello through `jz-trello-flow` after cloning AI Arsenal and opening a repository in Claude Code, Codex, Pi, or Hermes Agent.

The protocol deliberately stays lightweight. It specifies lifecycle authority, safety-critical mutation rules, minimum evidence, recovery, and responsibility boundaries. It does not replace agent judgment or prescribe one engineering methodology.

## 2. Authority and responsibility

Use this precedence when instructions conflict:

1. Direct human instructions and repository-defined autonomy/escalation policy.
2. The current canonical Work Unit and its acceptance criteria.
3. Trello state as read and mutated through `jz-trello-flow`.
4. Repository-local instructions and workflow rules.
5. Superpowers or another engineering-practice system.
6. Harness defaults and agent conventions.

### Trello and `jz-trello-flow` own

- Durable Work Unit identity and canonical description.
- Status and Trello-list synchronization.
- Native Trello card members as plural human assignment/attention state, and Work Unit `owner` as the separate single stable agent or worker execution claim. Membership is not authorization, exclusivity, or an atomic claim, and the two representations are not synchronized automatically. Member-filtered listing covers all visible board cards, including ordinary cards, while archived cards remain excluded and metadata filters apply only to Work Units.
- Lifecycle transition validation.
- Version checks, durable operation identity, replay recognition, read-back verification, diagnostics, and recovery plans.
- Concise evidence summaries and links needed to resume the task.

Trello state is authoritative for task coordination. A Superpowers phase, local todo, chat statement, Git branch, or agent belief cannot independently advance a Work Unit.

### Superpowers owns

When installed and applicable, Superpowers owns software-engineering practice, including:

- Design exploration and brainstorming.
- Implementation planning.
- Test-driven development.
- Systematic debugging.
- Plan execution and subagent coordination.
- Code review and response to review.
- Verification before completion.

Superpowers may produce designs, plans, reviews, test results, and other repository artifacts. Agents summarize relevant outcomes and link durable artifacts from the Work Unit. This protocol does not prescribe Superpowers artifact filenames, internal phases, hidden hooks, or tool names.

When Superpowers is unavailable, the harness may use equivalent engineering practices. That does not change Trello lifecycle authority or weaken the Work Unit acceptance criteria.

### Human users own

- Product intent and explicit constraints.
- Approval immediately before dangerous deletion or similarly irreversible data loss.
- Production-board policy and workflow-migration intent.
- Final portfolio review of Done cards.
- Manual archival of Done cards.

Neither an agent skill, Superpowers, nor the current CLI owns card archival.

Agents otherwise operate autonomously within the current Work Unit and
repository contract. Creating, clarifying, claiming, updating, transitioning,
reviewing, completing, recovering, committing, or pushing routine bounded work
must not create redundant permission prompts. Escalate when mandatory
credentials/access or another hard prerequisite is unavailable, authority is
irreconcilably contradictory, or the requirement cannot be satisfied honestly.
Do not mock away required live/E2E evidence merely to avoid escalation.

## 3. Canonical Work Unit and evidence

A Work Unit is one Trello card whose canonical description conforms to the Work Unit format documented by the installed CLI.

The canonical sections hold:

- The objective and bounded scope.
- Out-of-scope constraints.
- Observable acceptance criteria.
- Applicable verification expectations.
- Context needed to resume safely.
- Concise current evidence and links.

Detailed designs, plans, test logs, review reports, source changes, and CI evidence remain in the repository or their authoritative systems. The card links to them rather than duplicating them. Git and CI remain authoritative for their own state.

The CLI can read attachment metadata and download uploaded attachments. This protocol does not require or imply attachment upload support.

Evidence must be proportionate. Normal progress does not require an append-only journal. Record information that another agent or the human needs to understand current state, verify a gate, or recover from an exceptional outcome.

## 4. Canonical lifecycle

The built-in lifecycle is:

```text
Inbox → In Design → Ready → In Progress → Review → Done
                                  ↓          ↘
                               Blocked       In Progress
                                  ↘
                              Ready or In Progress
```

Normative transitions:

| From        | To          | Purpose                                                        |
| ----------- | ----------- | -------------------------------------------------------------- |
| Inbox       | In Design   | Select and begin clarifying the same card.                     |
| In Design   | Ready       | Confirm the canonical Work Unit is complete enough to claim.   |
| Ready       | In Progress | Claim the task for one owner.                                  |
| In Progress | Review      | Submit completed work and concise evidence for review.         |
| In Progress | Blocked     | Preserve a genuine blocker that prevents progress.             |
| Review      | Done        | Record the agent's justified completion judgment.              |
| Review      | In Progress | Address review findings or incomplete acceptance.              |
| Blocked     | Ready       | Release the task for a new claim after the blocker is removed. |
| Blocked     | In Progress | Resume with the existing or explicitly selected owner.         |

`Done` is terminal for agents. Human archival occurs later and outside this lifecycle.

A custom `TRELLO_TRANSITIONS_JSON` may replace the built-in graph. Agents must read effective configuration and never invent a permissive route. This protocol's semantic gates still apply to equivalent configured transitions.

## 5. Universal command discipline

For board-dependent operations:

1. Select the board explicitly with `--board <id-or-exact-name>`.
2. Prefer `--output json` for automation.
3. Read the Work Unit immediately before mutation.
4. Pass the latest observed version with `--if-version`.
5. Generate one durable, unique `--operation-id` for the intended operation.
6. Reuse that operation ID when recovering the same intent; never reuse it for different intent.
7. Execute the minimum required mutation.
8. Read back and verify the requested postcondition before proceeding.
9. Never blindly retry an ambiguous or partial result.

Trello does not provide atomic conditional writes. `--if-version` is a best-effort pre-write stale-read check, not a lock or transaction.

Use `--dry-run` when the target, policy, operation, or consequences need inspection. Do not require duplicate dry runs for routine, already-understood, reversible operations.

Before any description-writing mutation, inspect the CLI's exact final-payload preflight. Trello documents a 16,384-character card-description limit; byte counts and operation-record contribution are diagnostics, not substitute limits. A local `DESCRIPTION_BUDGET_EXCEEDED` result means no write occurred. After a remote deterministic description size/value rejection, read back before classifying the operation, preserve the same operation ID, and stop rather than blindly retrying, deleting card content, or replacing recovery markers. A dry-run rendering/wrapper error is also no-write unless read-back proves otherwise.

## 6. Intake, creation, and clarification

### Ordinary Inbox card

Humans may create an ordinary Trello card in Inbox. Agents discover it with `inbox list`. Selecting it for design must preserve that same card's Trello ID, comments, attachments, and history.

The design agent:

1. Reads the selected Inbox card and latest version.
2. Clarifies material uncertainty with the human or locally authoritative evidence.
3. Produces a canonical In Design Work Unit.
4. Runs `design start` with a durable operation ID and current version.
5. Reads back the same card and confirms canonical content, `in_design` status, and identity preservation.

### Agent-prepared Draft Work Unit

An agent may prepare a local canonical draft and validate it offline. It may then use `draft create` after explicit board selection and a dry run when the target or plan is not already established.

A dry run cannot predict `WU-N`. The server-assigned card identity is accepted only after creation and read-back.

### Clarification in In Design

In Design is intentionally resumable. Unresolved material content is marked explicitly with `Pending:` and, where useful, `Open Questions`.

Software-design exploration belongs to Superpowers when available. The Trello design skill owns only durable lifecycle coordination and canonical Work Unit completeness.

Before `In Design → Ready`, the agent confirms:

- Every required canonical section exists.
- Material `Pending:` entries are resolved.
- Material Open Questions are resolved.
- Scope, non-goals, acceptance criteria, and verification expectations are clear enough to claim.
- Known dependencies and blockers use Work Unit IDs where applicable.

After the guarded transition, the agent reads back and confirms `ready` status and the expected Ready list.

## 7. Claiming

Claiming is the intended postcondition:

- Status is `in_progress`.
- Owner is the stable identity of the claiming agent or harness worker.
- Both values refer to the latest task state.

The current CLI does not atomically combine owner metadata update and status transition. Therefore claiming is a recovery-aware multi-step operation, not an atomic lock.

### Claim algorithm

1. Read the Ready Work Unit immediately before claiming.
2. Stop if it is no longer Ready, is blocked, or already has a conflicting claim.
3. Choose a stable owner value and one durable claim identity. Derive distinct operation IDs for the owner update and transition while retaining the common claim identity in local recovery context.
4. Apply the owner update with the latest version and read it back.
5. Read again, then transition `Ready → In Progress` using the new latest version.
6. Read back once more.
7. Begin engineering work only when both `owner == expected owner` and `status == in_progress` are confirmed.

If any step is ambiguous, invoke the minimal recovery rule before another mutation. A partially applied owner update is not a completed claim. Another agent must not proceed merely because it attempted the transition first.

This protocol reduces duplicate work but does not claim a globally atomic lock. Work Units requiring stronger production allocation guarantees need a separately designed concurrency mechanism.

## 8. Work execution and updates

After a confirmed claim, engineering design, planning, implementation, tests, debugging, and review practice belong to Superpowers or equivalent harness practice.

Update the Work Unit when one of these materially changes:

- Scope or acceptance understanding.
- Owner or resumability.
- A dependency or blocker.
- The implementation/review frontier.
- Evidence needed for Review or Done.
- A recovery condition another actor must understand.

Do not rewrite system-managed status, IDs, or timestamps through generic description or metadata commands. Use lifecycle commands for status changes.

Concise evidence may include:

- Repository-relative design or plan paths.
- Commit, branch, or pull-request references.
- Test commands and summarized outcomes.
- CI run links or exact revision references.
- Review outcome and material unresolved findings.

The Work Unit need not contain every command or full log unless its own acceptance criteria require that detail.

## 9. Blocking

Use `In Progress → Blocked` only for a genuine condition that prevents useful progress, such as missing mandatory access, an unavailable mandatory dependency, contradictory or impossible authority, or a conflicting external state that cannot be safely reconciled. Consequence level alone is not a blocker; resolve routine scoped decisions autonomously from current Work Unit and repository authority.

Before or with the transition, record concisely:

- What is blocked.
- Why progress cannot continue.
- Who or what can unblock it.
- The safest next action.
- Relevant evidence or recovery identifiers.

After the blocker is removed:

- Use `Blocked → In Progress` when the existing claim remains valid and work resumes directly.
- Use `Blocked → Ready` when the previous claim is released and a fresh claim is required.

Read back the selected postcondition before resuming.

## 10. Review

Before `In Progress → Review`, the agent judges that:

- The Work Unit acceptance criteria appear satisfied.
- Applicable implementation verification has passed.
- No known blocker prevents review.
- Repository artifacts and Git/CI references are current.
- The card contains a concise evidence summary sufficient to evaluate or resume the task.

Superpowers review artifacts may be linked when useful. No specific review artifact, independent reviewer, or Superpowers internal phase is mandatory unless the Work Unit or repository requires it.

After transition, read back and confirm `review` status and the expected Review list.

Review outcomes:

- Material changes or failed acceptance: `Review → In Progress`, with concise findings.
- Accepted completion: `Review → Done`.

## 11. Completion

An agent may transition `Review → Done` when it judges that:

1. The current Work Unit acceptance criteria are satisfied.
2. Applicable verification has passed.
3. No known blocking issue remains.
4. Concise supporting evidence and durable links are present.

The protocol intentionally does not mandate an artifact format, tool, independent reviewer, pull request, or CI system unless the Work Unit or repository requires one.

Agent judgment cannot override failed acceptance criteria, required failing checks,
known blockers, a dangerous-deletion approval gate, or an unavailable hard
prerequisite.

After transition, read back and confirm `done` status and the expected Done list. The agent then stops lifecycle mutation. A human performs final portfolio review and manually archives the card when desired.

## 12. Minimal recovery rule

Use this rule after an interrupted, partial, timed-out, stale-version, or otherwise ambiguous operation:

1. **Read current state.** Preserve the intended postcondition, board ID, Work Unit/card ID, latest known version, and operation ID.
2. **Already satisfied:** if the intended postcondition exists and belongs to the same operation intent, treat it as recovered and continue.
3. **Unchanged:** if state is unchanged, retry once using the same operation ID and the newly read latest version.
4. **Conflicting:** if state conflicts with the intended result, do not overwrite it. Run `reconcile --dry-run` where applicable, then perform only an authorized repair or route the Work Unit to Blocked with a concise explanation.
5. **Still ambiguous:** stop mutation and preserve the CLI's non-secret recovery data for another actor.

Record recovery evidence only when the interruption changed task state, leaves uncertainty, or affects another agent. A successfully replayed routine operation needs no separate recovery artifact.

Never recreate a card merely because a response was lost. Never change an operation ID merely to bypass replay or collision detection.

## 13. Reconciliation

Use `reconcile` when the canonical description/status and Trello list may have drifted.

1. Read the Work Unit.
2. Run `reconcile --dry-run`.
3. Inspect the configured source-of-truth policy and proposed repair.
4. Execute only when the repair is authorized and its direction is understood.
5. Use the current version and a durable operation ID.
6. Read back and verify the repaired postcondition.

No skill may invent a reconciliation source or silently choose the list over the description.

## 14. Archival

For agents, Done is the end of the lifecycle.

The human user periodically reviews Done cards and manually archives selected cards. Agent skills must not:

- Automatically archive Done cards.
- Treat card archival as a completion gate.
- Close the Done list to simulate card archival.
- Reopen or delete cards as cleanup.

The CLI's guarded list-closing behavior concerns empty lists and is not a card-archival mechanism.

## 15. Cross-harness compatibility

All harnesses must preserve the same normative core:

- Explicit board selection.
- Canonical Work Unit format.
- Trello lifecycle authority.
- Read-before-write and read-back verification.
- Version and operation identity discipline.
- Minimal recovery behavior.
- Superpowers responsibility boundary.
- Human archival ownership.

Harness adapters may differ only in installation, skill discovery, tool invocation syntax, environment loading, and optional Superpowers integration.

### Claude Code

A Claude Code adapter may use plugin hooks and native Superpowers skills. Hidden hooks may improve discovery but must not be required for protocol correctness. The Trello skills still verify current state explicitly.

### Codex

A Codex adapter may use Codex plugin or skill packaging and available Superpowers integration. It must not depend on Claude-specific hook behavior or tool names.

### Pi

A Pi adapter may use Pi packages, native skills, and the Superpowers bootstrap extension. Optional subagent or task-list packages do not become protocol requirements.

### Hermes Agent

Current inspected Superpowers upstream documentation does not list native Hermes Agent support. A Hermes adapter must therefore:

- Use Hermes-compatible skill packaging for Trello lifecycle operations.
- Invoke available equivalent engineering-practice skills when Superpowers is unavailable.
- Never claim that native Superpowers execution occurred without evidence.
- Preserve the same lifecycle and evidence boundaries as supported harnesses.

## 16. Proposed follow-on skill set

Skill implementation is a separate work item. Keep the set to four responsibilities.

### `trello-work-orchestrator`

- **Trigger:** Resume, status, “what is next,” task selection, or uncertain lifecycle state.
- **Inputs:** Explicit board selector, current repository context, optional Work Unit reference.
- **Permitted mutations:** None.
- **Outputs:** Current state, blockers, evidence frontier, and exactly one routed next skill/action.
- **Does not own:** Design, claim, implementation, recovery mutation, Superpowers practice, or archival.

### `trello-work-design`

- **Trigger:** New draft, ordinary Inbox selection, or resumable In Design task.
- **Inputs:** Explicit board, selected card or validated draft, human intent, repository context.
- **Permitted mutations:** Draft creation; same-card `design start`; canonical metadata/section updates; guarded `In Design → Ready` transition.
- **Outputs:** Read-back-confirmed In Design or Ready Work Unit with resolved material questions.
- **Does not own:** Software-design methodology, implementation, Review/Done, production-board migration, or archival.

### `trello-work-deliver`

- **Trigger:** Ready task selected for claim, owned In Progress task, Blocked task eligible to resume, or Review task requiring disposition.
- **Inputs:** Explicit board, Work Unit reference, stable owner, repository instructions, available Superpowers/equivalent practice.
- **Permitted mutations:** Recovery-aware claim; concise metadata/section evidence updates; normal transitions among Ready, In Progress, Blocked, Review, and Done.
- **Outputs:** Read-back-confirmed lifecycle state with proportionate evidence.
- **Does not own:** Superpowers internal methodology, stronger-than-Trello locking, production migration, card archival, release, or destructive cleanup.

### `trello-work-recover`

- **Trigger:** Ambiguous or partial result, stale version, replay/collision signal, drift, or conflicting postcondition.
- **Inputs:** Intended postcondition, board and resource IDs, operation ID, current read, CLI recovery data.
- **Permitted mutations:** One same-operation retry after an unchanged read; authorized reconciliation or repair; Blocked routing when conflict prevents safe continuation.
- **Outputs:** Recovered postcondition, safe normal route, or explicit blocked recovery record.
- **Does not own:** Blind retries, new intent under an old operation ID, scope decisions, destructive cleanup, or archival.

No separate archival skill is proposed.

## 17. Follow-on verification strategy

Future skill implementation should verify:

| Area                 | Minimum evidence                                                                                                                                      |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Skill structure      | Valid frontmatter, bounded triggers, required inputs, permitted mutations, outputs, and non-responsibilities.                                         |
| Shared authority     | Every adapter preserves Trello authority and the Superpowers boundary.                                                                                |
| Command accuracy     | Examples match the versioned CLI catalog and use explicit board, JSON output, current version, operation ID, and read-back where applicable.          |
| Offline lifecycle    | Disposable fixtures cover ordinary Inbox and Draft intake, In Design completeness, Ready claim, progress, Blocked/resume, Review, and Done.           |
| Claim safety         | Owner update plus transition is treated as multi-step; work starts only after both postconditions are read back.                                      |
| Concurrency          | Stale-version rejection and competing claim observations never imply an atomic lock.                                                                  |
| Idempotency          | Same-operation replay is recognized; changed intent cannot reuse the operation ID.                                                                    |
| Recovery             | Already-satisfied, unchanged, stale, replayed, ambiguous, partial, and conflicting outcomes follow the minimal recovery rule.                         |
| Evidence             | Cards contain concise summaries and repository links without requiring attachment upload or full logs.                                                |
| Completion           | Agent judgment is bounded by acceptance, applicable verification, known blockers, and concise evidence.                                               |
| Archival             | Done terminates agent mutation; no skill archives cards or closes Done as a substitute.                                                               |
| Harness adapters     | Claude Code, Codex, Pi, and Hermes load or adapt the same normative core without hidden-behavior dependency.                                          |
| Superpowers boundary | Trello skills coordinate state and evidence but do not reimplement brainstorming, planning, TDD, debugging, code review, or verification methodology. |
| Safety               | Default verification performs no production-board mutation and contains no credentials or secret values.                                              |

Use offline or disposable test state by default. Any live test must be authorized
by the current bounded Work Unit or repository plan, explicitly allowlisted to a
testing board, recovery-aware, and isolated from production boards. Do not ask
again when that scoped authority already exists. If required credentials or
access are unavailable, escalate rather than substituting mocks for mandatory
live evidence.

Packing this protocol into the CLI, exposing it through `jz-trello-flow docs`, publishing a package, globally installing it, or implementing generated adapters each requires its own bounded work item and verification. Those work items proceed autonomously unless a narrow escalation condition applies.

## 18. Explicit exclusions

This protocol does not authorize:

- Production-board initialization or migration.
- Attachment upload through the current CLI.
- Atomic task allocation claims.
- Git Bash shim remediation.
- Package release, publication, or global installation.
- Automatic card archival.
- Skill implementation.
- Source deletion or destructive Trello cleanup.
