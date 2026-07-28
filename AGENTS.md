# Greek Essence Agent Instructions

## Authority

Use the GitHub Flow strategy in [`docs/GIT_WORKFLOW.md`](docs/GIT_WORKFLOW.md) for every committed change. Keep `main` deployable, never commit or push directly to `main`, and deliver changes through a short-lived branch and pull request. Review approval is not required, but applicable checks must pass before merge. Continue to preserve unrelated and concurrent edits, and never discard or overwrite work without explicit authorization.

### Work-item continuation

At the start of project work, read the repository-root [`NEXT.md`](NEXT.md),
which is the router for active multi-session work. Detailed state and the next
recommended action belong in each work item's `NEXT.md` under
`docs/working/work-items/<work-item>/`.

If the user or spawning agent assigns a listed work item, read that work item's
`NEXT.md` completely before acting. If no work item is assigned, present the
available work items and ask the user which one to continue; do not select or
begin one autonomously. Current user instructions always take precedence over
handoff content.

Each work item has one primary owner. Claim it in its `NEXT.md` before changing
its scope, and do not act on an item claimed by another owner without explicit
coordination. Only the primary owner updates that work item's `NEXT.md`;
subagents report results to the owner unless explicitly given ownership. Before
creating or claiming work with overlapping paths or responsibilities, inspect
the other active work items and coordinate the overlap.

Verify a selected work item's current-state claims against the live repository
before following its next action. If they disagree, treat the handoff as stale
and reconcile or escalate it before continuing. Before handing off materially
advanced work, reconcile the operation document first and update the work
item's `NEXT.md` as the final documentation action. Record one next recommended
action, its completion condition, and immediate constraints or approval needs.

Create a work item's directory and add its root-router link in the same change.
When work completes, mark its `NEXT.md` complete and remove its root-router link
in the same change. The root router contains links only; it never owns task
details or a global next action.

[`TODO.md`](TODO.md) is the operator-managed backlog and idea inbox for pending work that is not active. It is not an execution queue, task contract, project-status ledger, or handoff, and an item appearing there does not authorize implementation. Agents may add clearly attributable pending work or clarify an item without changing its intent, but must not implement, delegate, schedule, or promote an item unless the operator or an authorized planning task selects it. Before execution, move the selected work into the appropriate plan, issue, task contract, or active work-item directory; record its immediate continuation only in that work item's `NEXT.md`. Do not store runtime state, process IDs, session IDs, raw logs, secrets, credentials, or detailed execution evidence in `TODO.md`; remove completed entries after their outcomes are reconciled into durable project history.

Read [the documentation entry point](docs/README.md) first. Project decisions take precedence in this order: Project Protocol, Product Requirements, Prototype Specification, Technical Design, then Design System. Agent-tooling documents govern tooling only; record and escalate conflicts rather than silently reinterpreting a higher-authority requirement.

## Architecture

Use standalone `pnpm` `11.17.0` directly; follow the repository `packageManager` version and do not substitute another package manager. Keep TypeScript strict. Build a static-first Next.js App Router prototype: local, schema-validated JSON content renders public pages at build time; the form-submission Route Handler is the sole server-side dynamic boundary. Prefer Server Components and add Client Components only for necessary interaction and minimal JavaScript.

Support explicit English and Greek routes. Follow the modular [prototype specification](docs/02_prototype_specification/index.md) for UX, accessibility, responsiveness, content, and form behavior, and the modular [technical design](docs/03_technical_design/index.md), including [testing and quality gates](docs/03_technical_design/18_testing_and_quality_gates.md). Prefer simple, maintainable, battle-tested solutions.

Do not add or imply a database, CMS, CRM, analytics provider, booking, availability, payments, accounts, dashboards, itinerary management, dynamic inventory, price comparison, customer reviews, marketing automation, or another deferred production capability without explicit approval.

## Proportional implementation

This repository is prototype-stage. Produce modern, maintainable code using established project patterns, but keep engineering effort proportional to the explicit task and current product stage.

Implement the smallest complete solution that satisfies the task contract and acceptance criteria. Prefer one clear code path over speculative flexibility. Reuse existing architecture, dependencies, and conventions before introducing new abstractions.

Do not add unsolicited abstraction layers, generalized frameworks, compatibility shims, fallback systems, migration machinery, production infrastructure, or handling for hypothetical future requirements. Do not broaden a task merely because a more enterprise-grade solution is possible.

An edge case is in scope only when it is named by the task or authoritative documentation, reasonably reachable through supported user behavior, required for security or data integrity, or reproduces an observed failure.

Test the requested behavior, important realistic boundaries, and identified regressions. Do not create exhaustive or combinatorial tests for implausible edge cases unless the task, a documented requirement, or an observed defect requires them.

When acceptance criteria and required verification pass, stop. Do not continue refactoring, polishing, documenting, or expanding adjacent functionality without a concrete task requirement. Material out-of-scope concerns may be reported briefly, but they must not be implemented automatically.

Correctness, accessibility, security, privacy, and explicit repository gates remain mandatory; proportionality must not be used to bypass them.

## Implementation depth

Every task operates at one of four engineering-depth tiers:

1. **Spike** — Temporary feasibility work. Prove the hypothesis with minimal implementation and verification.
2. **Prototype** — The smallest maintainable, complete implementation covering supported behavior, realistic boundaries, focused tests, and required gates.
3. **Product** — Production-facing implementation with documented failure handling, broader integration coverage, and justified operational safeguards.
4. **Critical** — Security-, privacy-, financial-, integrity-, or availability-critical work requiring fail-closed behavior, comprehensive realistic failure coverage, recovery considerations, and independent verification.

The assigned tier controls engineering breadth, defensive depth, and verification effort—not baseline code quality. Correctness, security, privacy, accessibility, maintainability, explicit acceptance criteria, and repository-required gates remain mandatory at every tier.

### Project default and tier resolution

**Project default engineering depth:** Tier 2 — Prototype

Resolve the engineering-depth tier for each task in this order:

1. A direct operator instruction for the current task.
2. An explicit `implementation_depth` value in the task contract.
3. The project default declared in this file.

The first applicable declaration is the **resolved tier**. A task-specific tier overrides the project default. Agents must not raise or lower the resolved tier based on speculation, hypothetical future requirements, perceived importance, or a desire for completeness.

Delegated subtasks inherit the parent task's resolved tier unless their brief explicitly assigns a different tier. The delegating agent must communicate the resolved tier in the subtask brief.

A task may override the project default with `implementation_depth: 3` in its YAML front matter. Accepted values are `1`, `2`, `3`, and `4`, corresponding to Spike, Prototype, Product, and Critical. The front-matter value is authoritative if the task body also displays a human-readable tier label.

When a task contains one sensitive component, apply a stronger tier narrowly to that component rather than raising the entire task. For example: **Implementation depth:** Tier 2 — Prototype; **Narrow exception:** Credential handling uses Tier 4 — Critical.

At every tier, stop when the tier-appropriate acceptance criteria and required verification pass.

### Calibration example

For a task such as “send an email notification after a contact-form submission”:

- **Tier 1 — Spike:** Prove that sample form data can reach the provider and produce a successful response. Implement only what is needed to answer the feasibility question.
- **Tier 2 — Prototype:** Implement the supported form flow with validation, clear success and failure behavior, realistic provider-error handling, and focused acceptance and regression tests. Do not add queues, delivery tracking, or generalized notification infrastructure.
- **Tier 3 — Product:** Address documented operational needs such as timeouts, duplicate submissions, abuse controls, provider failures, configuration validation, recovery behavior, and useful operational visibility. Add broader integration coverage where justified.
- **Tier 4 — Critical:** When delivery participates in a security-sensitive, financial, legal, privacy-sensitive, or similarly critical workflow, require strict authorization and data handling, idempotency, auditability, reconciliation, explicit recovery, fail-closed boundaries where appropriate, and independent verification.

The example illustrates relative depth only. Apply the assigned tier to the actual task contract and supported risks; do not copy example-specific requirements into unrelated work.

## Approved skills

Use only the repository-local skills approved in [the tooling baseline](docs/05_agent_skills/01_approved_tooling_baseline.md): Google Chrome Modern Web Guidance for modern-web implementation decisions; Vercel `vercel-react-best-practices` for React work; the official Playwright CLI Agent Skill for browser inspection; and `greek-essence-quality-review` for structured quality reviews. For Next.js-specific work, consult the documentation bundled with the installed Next.js version under `next/dist/docs/` and its approved generated agent rules; do not install the retired `next-best-practices` skill. Guidance complements, and never replaces, required executable checks.

## Browser inspection

Use Playwright CLI as the only interactive browser interface. Do not install, configure, or use Playwright MCP, `agent-browser`, Browser Use/Browser Use CLI, or another overlapping browser-agent tool.

## Required checks

Run the task-required checks plus applicable repository commands: `pnpm lint`, `pnpm typecheck`, `pnpm validate:content`, `pnpm build`, and the required Playwright, accessibility, metadata, and quality checks. Record exact commands, exit codes, and results; do not claim checks that did not run.

## Definition of done

A change is done only when it meets the authoritative requirements; preserves static-first and locale boundaries; has focused, passing required checks; has no console errors or failed critical network requests; protects personal/client data from Git, logs, screenshots, previews, and analytics; uses only approved visible claims/assets; records known production gaps; and receives required review approval.
