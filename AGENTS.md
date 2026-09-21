# Greek Essence — Agent Guide

These are conventions, not commands. They exist so that many agents produce one codebase.
**If a convention blocks correct work, deviate and say so in the commit or PR body.**

## What this is

A static-first marketing and enquiry site for a boutique Greece travel-planning agency.
No database, no auth, no payments, no customer data. Content comes from Sanity; every
conversion path hands off to a Google Form. The server exists only for Draft Mode and
on-demand revalidation.

## Read before working

1. `backlog instructions overview`, then your task: `backlog task view <id>`
2. [`docs/v1/00-DECISIONS.md`](docs/v1/00-DECISIONS.md) — every decision that shapes v1
3. [`docs/v1/06-ARCHITECTURE.md`](docs/v1/06-ARCHITECTURE.md) — layout, boundaries, data flow

That is the whole reading list. `docs/v1/` has four more files; open the one your task needs.

## Stack

Next.js 16 (App Router) · TypeScript strict · Tailwind 4 · Base UI · Sanity · Netlify · pnpm.
Full rationale in [`docs/v1/05-STACK.md`](docs/v1/05-STACK.md).

> **Next 16 is not the Next.js you know.** Read the relevant guide in
> `node_modules/next/dist/docs/` before writing routing or config code. The same caution
> applies to Tailwind 4 and Zod 4.

**The shadcn CLI does not work here** — `ui.shadcn.com` is blocked by egress policy. Write
components by hand against Base UI primitives. We need about seven of them.

## Conventions

- **Dependency direction:** `app → sections → patterns → ui`. `lib` and `types` are free for
  all. eslint enforces this; it is not a matter of care.
- **Components never see a Sanity document.** `lib/sanity/map.ts` maps to the DTOs in
  `types/domain.ts` at the boundary.
- **Server Components by default.** `'use client'` needs a reason; v1 has three.
- **Design tokens only.** No arbitrary Tailwind values (`text-[#17475f]`, `mt-[13px]`).
- **Do not create a component for one caller.** Inline it until a second use appears.
- Files kebab-case, components PascalCase, `@/` imports, no `useEffect` data fetching.

## Git

`main` → `phase/<nn>-<slug>` → `task/<nn.n>-<slug>`. Task merges into its phase, phase into
`main`. Rebase `main` into a phase branch daily; a phase lives ≤ 7 days. Conventional Commits.

Two lanes run concurrently (product, pipeline), so two phase branches may be open — one owning
lane each. Details in [`docs/v1/03-WORKFLOW.md`](docs/v1/03-WORKFLOW.md) §2.

**Merging to `main` does not ship.** `main` is the integration branch and gets a free Netlify
branch deploy you can review. Production is the `release` branch, reached only by an explicit
`git push origin main:release`, budgeted at ≤8/month (A-003). Netlify bills 15 credits per
production deploy against a hard 300/month limit, and exhausting it takes the site offline.

## Checks

`pnpm check` (format, lint, typecheck, unit) before pushing. `pnpm build` and `pnpm test:e2e`
at phase close.

**A green test is not enough for anything a person can see.** Walk the path a user would walk,
capture viewport and full-page screenshots plus console output into
`.local/evidence/<date>-<slug>/`, and file anything odd as a task rather than dropping it
(A-007). Skip the walk for pure refactors; still run the tests.

## Posture

Balanced commercial engineering. Deliver the accepted behaviour, make the main path reliable,
handle realistic failures, and stop when the checks support the result. Do not build
abstractions for one caller, and do not broaden a task into cleanup nobody asked for.

If the work requires reopening an accepted decision, stop and say so rather than quietly
choosing differently.

## Standing authorisations

The owner grants standing permission to use the Netlify, Sanity, Google and Resend dashboards
through the personal Chrome extension or Computer Use, for work already authorised — including
inspecting settings and applying routine configuration such as environment variables, webhooks
and integrations. Check the intended account and project before writing. No extra permission is
needed to reach the browser or save those changes.

This does not waive: the deny list in `.claude/settings.json`, a production deployment, sending
real email to a real customer address, deleting anything belonging to the client, or any paid
commitment.

## Local preferences

If `.local/preferences/user-profile.md` exists, read it before replying. It holds local
preferences; keep it untracked and never copy its contents into shared documentation.
Nothing in `.local/` is authoritative for the product — decisions live in `docs/v1/`, tasks in
`backlog/`.

<!-- BACKLOG.MD GUIDELINES START -->
<!-- backlog.md-instructions-version: 1.52.0 -->
<CRITICAL_INSTRUCTION>

## Backlog.md Workflow

This project uses Backlog.md for task and project management.

**At the beginning of each conversation in this project, run `backlog instructions overview` before answering or taking action. Re-read it only if you have not read it yet in the current conversation.**

Use the overview to decide whether to search, read, create, or update Backlog tasks.

Before task lifecycle actions, read the matching detailed guide:
- `backlog instructions task-creation` before creating or splitting tasks
- `backlog instructions task-execution` before planning, changing status or assignee, adding a plan or implementation notes, or implementing task work
- `backlog instructions task-finalization` before checking acceptance criteria, writing final summaries, or moving tasks to terminal statuses

Use `backlog <command> --help` before running unfamiliar commands. Help shows options, fields, and examples.

Do not edit Backlog task, draft, document, decision, or milestone markdown files directly. Use the `backlog` CLI so metadata, relationships, and history stay consistent.

</CRITICAL_INSTRUCTION>
<!-- BACKLOG.MD GUIDELINES END -->
