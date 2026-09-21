# Greek Essence v1 — Decision Register

**Status:** Draft for operator approval · **Date:** 2026-09-21 · **Target:** public v1 in 4–6 weeks

One file. Every decision that shapes v1. If a decision is not here, it is not decided.
Format: `D-nnn` · **Decision** · *Why* · *Consequence* · Owner.

Legend: ✅ decided · 🟡 recommended, awaiting your OK · 🔴 blocked on client.

---

## Part A — Product boundary

### D-001 ✅ v1 is a brochure site with an off-site request funnel
No backend, no database, no auth, no payments. The site publishes content and hands
intent to Google Forms. Everything else is v2.

*Consequence:* the site is 100% statically renderable. Hosting is free and effectively
un-breakable. There is no "honest failure" engineering to do, no idempotency, no
duplicate protection, no retention policy in code — all of that moves to Google's
infrastructure and to the privacy policy.

### D-002 ✅ Two product types: Pre-defined Package and Personalized Package
- **Pre-defined Package** — a catalogue entry in Sanity. Browsable, filterable, has a
  detail page. Replaces the v0 "Experience".
- **Personalized Package** — *not* a catalogue entry. It is one always-available offer
  with a single landing page and its own form. It is the "we build it around you" path.

*Consequence:* one catalogue model, one offer page. No second catalogue to populate.

### D-003 ✅ Destinations survive as a real content type
Destinations get list + detail pages and are the primary filter on packages.

*Why:* destinations are the SEO surface and the browsing entry point. They are also the
cheapest content for the client to produce (she already knows Greece).

### D-004 🟡 Drop the v0 Consultation / Booking / General Contact three-journey split
v1 has **three forms, one mental model**: *Book this package*, *Plan something personal*,
*Ask a question*. Same wording family, same thank-you page, same email template.

*Why:* v0 grilled these as three separate features with distinct field sets, privacy
copy and failure semantics. That distinction only pays off when there is a backend
that treats them differently. There isn't one.

### D-005 ✅ English-only at launch
`next-intl` routing stays wired with `/en` as the only active locale so Greek is a later
content drop, not a rebuild.

*Why:* bilingual doubles copy, review and QA, and the v0 decisions require a named human
approver per language before publishing. That gate alone could eat two weeks.

### D-006 🟡 No price display at launch unless the client supplies the full qualification set
Carry over v0 D-004: a "from" price only ships with currency, charging basis, inclusions,
review date and a subject-to-confirmation note. Otherwise the package shows no price and
invites an enquiry.

*Why:* a bare number on a travel package is a consumer-law problem, not a design choice.

### D-007 🟡 Explicitly out of v1
Accounts · payments · custom calendar/date-picker · live availability · confirmed bookings ·
articles/blog · accommodation pages · attraction pages · newsletter · staff dashboard ·
Greek locale content · any database.

---

## Part B — Platform

### D-010 ✅ Stack
Next.js 16 (App Router, static export-friendly) · TypeScript strict · Tailwind 4 ·
shadcn + Base UI · Sanity (content) · Google Forms (intake) · Google Apps Script +
Resend (email) · Vercel (hosting) · pnpm.

*Why this shape:* it is the v0 stack minus Neon, Drizzle and the Route Handlers. Nothing
new to learn, and every removed piece removes a class of failure.

### D-011 ✅ Sanity stays
The client edits content herself. That is the one operational capability worth its setup
cost — without it every copy tweak is a developer task for the next year.

### D-012 🟡 Google Forms is the intake, but the site owns the moment before and after
Raw "click → leave site → Google" is the weakest point in the whole product. Mitigate with:
1. An on-site **interstitial** (`/packages/[slug]/request`) that restates what happens next
   and *then* hands off. The handoff is expected, not jarring.
2. **Pre-filled** form fields via `?entry.<id>=<value>` URL params, so the package name and
   type are already filled in. Fewer abandonments, cleaner data.
3. Forms configured to redirect back to a **branded `/thank-you`** page.
4. Form theming pushed as far as Google allows: header image, brand colour, matching font.

*Consequence:* one extra route template and a small `buildFormUrl()` helper. Cheap.

### D-013 🟡 Email: Apps Script → Resend for the customer, Apps Script native mail for the operator
On form submit, an Apps Script `onFormSubmit` trigger sends:
- **to the customer** — a branded acknowledgement from `hello@<domain>` via the Resend API
  (`UrlFetchApp.fetch`). Branded sender, real deliverability.
- **to the client/agency** — a plain notification with the submission summary and a link to
  the response row. `MailApp.sendEmail` is enough here; it costs nothing and needs no domain.

*Why not Resend for both:* the internal notification does not need branding, and splitting
it keeps you under Resend's free tier comfortably.

*Prerequisites:* a verified sending domain in Resend (DNS records — **client owns the
domain, so this is a client-blocked task, start it week 1**), and the Resend API key stored
in Apps Script Script Properties, never in the repo.

### D-014 🟡 The Google Sheet is the system of record
Responses live in the linked Sheet. Nightly Apps Script export to Google Drive as CSV is the
backup. No other durable store exists in v1.

*Consequence:* the privacy policy must state that enquiry data is processed by Google.
Set the Sheet to the client's own Google account from day one — never yours.

### D-015 🔴 Hosting eligibility
v0 flagged that Vercel's free plan may not permit commercial use. **Resolve this in week 1.**
A static v1 has no runtime, so Cloudflare Pages or Netlify are drop-in alternatives if
Vercel's terms don't fit. Do not discover this in week 5.

---

## Part C — Process

### D-020 ✅ Archive `main`, restart clean
Current `main` becomes `archive/v0-preview` (branch + tag). New history starts empty.
Carry forward *only*: `docs/v1/**`, the design tokens in `app/globals.css`, and
`.editorconfig` / `.prettierrc` / `.gitattributes`.

*Why:* the v0 repo has ~50,000 words of process documentation and ~400 lines of application
code. Every agent that reads it spends its budget on protocol, not product. The docs aren't
wrong — they're just priced for a project ten times this size.

### D-021 ✅ Backlog.md replaces Trello
The real [Backlog.md](https://github.com/MrLesk/Backlog.md) CLI. Tasks, milestones, decisions
and docs are markdown in `backlog/`, committed to the repo. It ships a Kanban TUI, a web UI,
native milestones and dependencies, and a configurable Definition of Done.

*Consequence:* we adapt our conventions to its model, not the reverse. Concretely: it owns task
IDs (`GE-1`, `GE-2`, … via `--task-prefix GE`), so our `T-03.4` roadmap references become
pointers in the task description rather than identifiers. Phases become labels. Agents use the
CLI and **never hand-edit the markdown**, which is the tool's own stated rule.

### D-021b ✅ Agents use the Backlog.md **CLI**, not its MCP server
MCP tool definitions are resident context that loads whether or not a session touches the
backlog; the CLI costs nothing until invoked, and models already know CLI syntax from training.
The published MCP-vs-CLI framework puts local, auth-free, has-a-CLI tools firmly on the CLI
side, and Backlog.md's own `backlog instructions overview` is an on-demand loading mechanism
that an always-on MCP surface would undercut. Full reasoning and the reversal condition in
[03-WORKFLOW.md](03-WORKFLOW.md) §3.

*Consequence:* applies to this project generally — default to CLIs, reach for MCP only for
remote/OAuth/no-CLI services.

### D-022 ✅ `auto_commit: true` + a backlog-only post-commit push hook
An earlier draft of this register invented a rule that `backlog/**` should be committed directly
to `main`, bypassing the branch flow, so every dev saw current task state. **That rule is
withdrawn.** Backlog.md's `check_active_branches` (on by default) already reconciles task state
across every branch active within `active_branch_days` — without punching a hole in the branch flow.

What we set instead, verified against v1.52.0:
- `auto_commit: true` — task changes commit themselves, no discipline required.
- **`auto_commit` commits but does not push**, confirmed by experiment. A `post-commit` hook that
  pushes only backlog-only commits closes that gap (see [03-WORKFLOW.md](03-WORKFLOW.md) §3).
  An earlier draft proposed `onStatusChange: git push`; **that config key does not exist in
  v1.52.0** and the proposal is withdrawn.
- `active_branch_days: 14` — our phase branches live ≤ 7 days, so the default 30 is wider than needed.
- Git identity must be configured or `auto_commit` aborts the task operation half-done.

### D-023 ✅ Phase/Task branch flow (your model, with guard rails)
```
main
 └── phase/<nn>-<slug>          created when the phase starts
      └── task/<nn.n>-<slug>    created when the task starts
      ← merge task into phase   when the task is done
 ← merge phase into main        when the phase is done
```
Guard rails that make it survivable:
- **One phase branch open at a time**, unless two phases touch disjoint directories.
- **A phase lives ≤ 7 days.** If it's longer, it's two phases.
- **Merge `main` into the phase branch daily** (not the reverse). A phase branch that has
  drifted a week from `main` is a rewrite, not a merge.
- Fast-forward or `--no-ff` merges, no squash — you want the task granularity in history.
- Agents have standing authority for: branch, commit, push, merge task→phase, delete merged
  branches. Merge phase→`main` also pre-authorised **once** checks are green.
- Force-push, history rewrite, `main` deletion, and deleting an unmerged branch always need you.

### D-024 ✅ Agent instructions are direction, not law
One `AGENTS.md` (with `CLAUDE.md` as a one-line pointer). Target: under 200 lines.
Standing rule at the top: *"These are conventions. If a convention blocks correct work,
deviate and say so in the PR body."*

### D-025 🟡 Documentation budget
Hard cap for v1: `AGENTS.md`, `README.md`, `docs/v1/*` (these five files), `backlog/`.
New doc ⇒ delete or merge another. Anything an agent won't read before a task doesn't exist.

---

## Part D — Open, needs you or the client

| # | Question | Owner | Needed by |
|---|---|---|---|
| Q1 | Domain name — registered? who owns it? DNS access? | Client | Week 1 (blocks Resend) |
| Q2 | Which Google account owns the Forms + Sheet? | Client | Week 1 |
| Q3 | Business inbox for notifications | Client | Week 1 |
| Q4 | Vercel commercial-use eligibility, or pick an alternative | You | Week 1 |
| Q5 | Launch package list — how many, which destinations? | Client | Week 2 |
| Q6 | Photography — owned, licensed, or stock? Who supplies? | Client | Week 2 (biggest schedule risk) |
| Q7 | Show prices, or "enquire for pricing"? | Client | Week 2 |
| Q8 | Exact questions on each of the three forms | Client | Week 2 |
| Q9 | Privacy policy + terms — template, or lawyer review? | Client | Week 4 |
| Q10 | Analytics — any, and which? (Plausible/Umami avoid a cookie banner) | Client | Week 4 |
