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

### D-005 ✅ English-only at launch — **and no i18n machinery at all in v1**
*Revised.* This decision originally said to keep `next-intl` wired with a single active locale so
Greek would be a later content drop. That was wrong: it buys a `/en/` prefix on every URL of a
single-language site and carries routing machinery through every M3 task for a v2 benefit.

**English lives at the root.** Greek is added later at `/el/` with English staying where it is —
the standard pattern, SEO-safe, no URL changes and no redirects. Sanity schemas carry no
localization in v1; document-level i18n is added in v2 and is purely additive.

*Why English-only at all:* bilingual doubles copy, review and QA, and the v0 decisions require a
named human approver per language before publishing. That gate alone could eat two weeks.

*Saves ~2h across M0 and M3, and removes a concept from every page task.* Detail in
[06-ARCHITECTURE.md](06-ARCHITECTURE.md) A-001 / A-002.

### D-006 🟡 No price display at launch unless the client supplies the full qualification set
Carry over v0 D-004: a "from" price only ships with currency, charging basis, inclusions,
review date and a subject-to-confirmation note. Otherwise the package shows no price and
invites an enquiry.

*Why:* a bare number on a travel package is a consumer-law problem, not a design choice.

### D-007 🟡 Explicitly out of v1
Accounts · payments · custom calendar/date-picker · live availability · confirmed bookings ·
articles/blog · accommodation pages · attraction pages · newsletter · staff dashboard ·
Greek locale content · any database.

### D-030 🔴 What a Pre-defined Package *is* — client must choose from a menu
Still unconfirmed, and it drives the content model, the package page and the legal exposure.
Do **not** ask her to define it. Give her these four and ask her to pick one (or two):

1. **Fixed itinerary, fixed price** — "7 days Paros & Antiparos, €2,400pp", named hotels and
   transfers. A product with a SKU. Richest content, highest legal exposure.
2. **Curated template, customized per customer** — "Cyclades Island Hop, ~8 days". Sells the
   shape of the trip; price indicative or absent. *Current working assumption.*
3. **Thematic inspiration** — "Honeymoon in the Cyclades". No fixed duration, hotels or price.
   Lightest content, pure lead-gen.
4. **Single day activity or excursion** — a boat day, a cooking class.

The content model in [01-SCOPE.md](01-SCOPE.md) is built for (2) and degrades gracefully to (3).
If she picks (1), the price qualification rules in D-006 become mandatory, not optional, and
`includes`/`excludes` become required fields with legal review attached.

### D-031 ✅ Personalized Package = free consultation call, then a quote
No money changes hands on the site. Flow: form → acknowledgement email → **she emails the
customer to arrange a call** → call → quote.

*Consequence:* the acknowledgement email must say a call will be arranged by email and must not
promise a response time without client approval. No phone number is collected, so the v0
no-telephone rule survives intact. Automated scheduling stays out of v1 — but a free scheduling
link (Google Calendar appointment schedules) is the obvious v1.1 upgrade if her inbox gets busy.

### D-032 ⚠️ **REVISED** — launch catalogue is small, but the catalogue is dynamic and filterable
*Original:* 1–2 destinations, 2–3 packages, **filters cut**, list pages cut.

*Revised 2026-09-22, client requirement:* the client will not have fixed, static packages. He
creates and edits **both destinations and packages in Sanity**, on his own, as opportunities
appear — "finds a deal, makes a Mykonos package for 4–6 people, for these dates". So:

- **Filters are back in.** Destination and group size at minimum; the facet list is configurable
  in Sanity rather than hard-coded.
- **Budget is NOT a filter** (D-032b). A budget facet needs published prices, which D-006
  forbids without full qualification. Decided: drop it rather than weaken D-006.
- **Dates are display text only** (D-032c). A package may read "15–22 Ιουνίου" as content. There
  is no expiry logic, no availability matching, no date filter. This was the single largest cost
  avoided in this change.
- Launch *volume* is still deliberately small. Small catalogue, real catalogue machinery.

*Consequence:* +6 tasks, +9.3h. The estimate moves 133.2h → **142.5h**. Recorded openly rather
than absorbed.

### D-033 ⚠️ **REVISED** — list pages are back
`/packages` returns as a filterable catalogue page; `/destinations` returns as a list. A
catalogue without a list page is not a catalogue. Eight page templates, not seven.

*Consequence for the architecture:* the filter UI is the **fourth** `'use client'` component,
alongside MobileNav, Gallery and Dialog (06-ARCHITECTURE §6). Filtering happens client-side over
the already-prerendered set — no query params round-tripping to a server, since every package
ships in the payload at this catalogue size.

### D-034 ✅ Free stock photography, curated defensively
Unsplash/Pexels. Licences are permissive for commercial use, but images with recognisable faces
or private property can still carry model/property-release issues, and Unsplash's terms shifted
after the Getty acquisition.

Rules: prefer landscape, architecture, food and detail shots over identifiable people; log
source URL, author and licence for every image in a sheet; avoid anything that could read as a
claim about a specific hotel or supplier she has no relationship with.

### D-035 ✅ Copy is drafted by agents, edited by the operator, approved by the client
She starts from concrete drafts, never a blank page — the approach the v0 decisions already
concluded fits how she works.

*Consequence:* copywriting is **real work in the roadmap**, roughly 22h including photo
curation. The earlier roadmap omitted it entirely and was wrong by that amount.

### D-036 ✅ ⚠️ **REVISED** — target is ~8.5 weeks, and the client is told now
At ~141.5h average and ~15h/week combined capacity, ~8.5 weeks is the honest number. *(Was
~7 weeks at ~108h; the estimate rose through the catalogue scope-in — see D-032 — not through
any change to the rate or the capacity assumption.)* The client's
expectation is reset during planning rather than at a missed deadline. Scope and quality are
preserved; Sanity stays (D-011).

*Why cutting the catalogue didn't help much:* the design system, request pipeline and launch
readiness are **fixed costs** — identical for 3 packages or 30. Only M2 and M3 scaled down, and
the previously-omitted copywriting absorbed the savings.

---

## Part B — Platform

### D-010 ✅ Stack — see [05-STACK.md](05-STACK.md)
**This decision was previously inherited, not made.** The earlier version of D-010 recorded the
v0 `package.json` as if it were a choice. [05-STACK.md](05-STACK.md) is the actual decision record.

Summary: Next.js 16 App Router, **static by default with a server runtime** (prerendered pages,
server used for Draft Mode and on-demand revalidation) · TypeScript strict · Tailwind 4 ·
shadcn + Base UI *(pending a verification spike)* · Sanity with the Presentation tool ·
Google Forms · Apps Script + Resend · **Netlify free plan** · pnpm · Fraunces + Inter
self-hosted · lucide · CSS-only motion · Umami Cloud analytics.

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

### D-015 ✅ Resolved — Netlify free plan, with a server runtime
v0 flagged that Vercel's free plan may not permit commercial use and left it open. **Confirmed
and closed.** Vercel's own docs: *"the Hobby plan restricts users to non-commercial, personal
use only."* A client's business site is commercial, so Hobby is a terms violation and Vercel
means Pro at ~$20/mo billed to her forever.

**The host is Netlify's free plan**, where commercial use is explicitly permitted (S-002), and
we run **with a server rather than a static export**.

*Why the server matters:* `output: 'export'` disables Next's Draft Mode, which is what Sanity's
**Presentation tool** needs — the client editing in the Studio while watching the real page
update beside her, clicking an element to jump to its field. For a client who owns her own
content, losing that was the wrong trade. Pages are still prerendered; the server only handles
preview and on-demand revalidation.

**And the free plan is only viable because we kept the server.** Netlify bills 15 credits per
production deployment against a hard 300/month budget. On a static export every Sanity publish
would fire a rebuild — the client would pause her own website after twenty typo fixes. See
[06-ARCHITECTURE.md](06-ARCHITECTURE.md) §14 and A-003.

*Knock-ons:* ISR via `revalidateTag` replaces a full rebuild, so Sanity edits appear in seconds ·
security headers live in `next.config` rather than a platform file · **and draft content must be
provably unreachable by the public**, which needs a test, not care (S-003).

### D-040 ✅ Domain DTOs at the Sanity boundary
Components never see a Sanity document. `lib/sanity/map.ts` maps raw GROQ results into plain
types in `types/domain.ts`, and nothing downstream knows Sanity exists.

*Why this is worth its hour:* it makes **the D-006 price rule structural**. The mapper returns
`price: undefined` unless currency, basis, inclusions, review date and the confirmation note are
all present — so a partially-qualified price becomes impossible to render, rather than something
a component has to remember to check. Business rules belong at the boundary, not in JSX.

Also: components become testable with object literals, and restructuring the CMS is contained to
one file. Full rules in [06-ARCHITECTURE.md](06-ARCHITECTURE.md) §4–§5.

### D-041 ✅ Dependency rules are enforced by eslint, not by review
`app → sections → patterns → ui`, one direction, with `components/**` forbidden from importing
`lib/sanity/**`. Encoded as `no-restricted-imports` zones in T-00.3.

*Why:* a convention an agent can violate silently is not a convention. With 60 tasks and two
developers, the boundary has to fail the build.

### D-042 ✅ No error-monitoring service in v1
Netlify function logs cover a site with no mutations and no customer data. The failure that
actually matters — an enquiry email not sending — is alerted from Apps Script (T-04.8). Revisit
if the server ever does more than Draft Mode and revalidation.

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

### D-026 ✅ Two developers, two lanes, phase-level review
Operator + one junior developer, both using Claude Code (Opus 5).

| Lane | Owner | Scope |
|---|---|---|
| **Product** | Operator | M0, M1 design system, M2 content platform, M3 pages, M5 quality + handover |
| **Pipeline** | Junior | M4 (Forms, Apps Script, email) and M5 P5.1 (SEO, sitemap, metadata, analytics) |

*Why this split:* M4 is the best-isolated chunk in the project — self-contained, testable, zero
dependency on the design system. M5 P5.1 is well-defined and verifiable with a low taste
requirement. Neither blocks the other lane.

*Consequence for D-023:* "one phase branch open at a time" **no longer holds** — two lanes means
two concurrent phase branches by design. The disjoint-directories exception is now the normal
case. Each phase has exactly one owning lane; cross-lane edits need a word first.

*Watch:* the junior's lane is the one most exposed to client-blocked items (Google account,
domain, DNS for Resend). Chase those in week 1 or he idles.

### D-027 ✅ Review at phase close, not per task
Tasks are 3–6h and agents run a whole phase before the operator reviews a preview URL.
Roughly 20–25 tasks total rather than 40–50.

*Why:* at 8–12h/week the operator's hours are the scarcest resource in the project. Per-task
review would spend most of them on inspection rather than direction.

### D-028 ✅ Phases are parent tasks in Backlog.md
Milestone → parent task per phase → subtasks, via `-p/--parent`. Mirrors the Phase/Task branch
flow exactly and gives roll-up progress. `phase:` labels are not used.

### D-050 ✅ Low-friction agentic development is an explicit goal
Agents should be able to do the work. An approval prompt for `pnpm test` is not a safety control —
it trains everyone to click "allow" without reading, which is how the prompt that *should* have
stopped something gets waved through too.

The shape: **pre-authorise the routine surface broadly in a committed
`.claude/settings.json`, deny the genuinely destructive specifics, and keep prompts rare enough
that each one still means something.** Standing authorisation extends to provider dashboards
(Netlify, Sanity, Google, Resend) via the personal Chrome extension or Computer Use for work
that is already authorised.

The deny list is deliberately short — history destruction, file destruction, and deleting the
client's dataset or site. Everything else is recoverable from Git. Production deploys stay
deliberate for a different reason (A-003: credit budget, not safety).

Detail in [03-WORKFLOW.md](03-WORKFLOW.md) §5.

### D-051 ✅ `.local/` convention for personal preferences and evidence
Gitignored `.local/` holding `preferences/user-profile.md` (how the owner wants to be talked to)
and `evidence/<date>-<slug>/` (screenshots, logs, run output). Matches the convention already in
use in `marine-engineer-cv` and `agentic-wave`.

`AGENTS.md` carries a one-line pointer. Two rules: never committed, and never authoritative for
the product — decisions live in `docs/v1/`, tasks in `backlog/`.

---

### D-052 ✅ Internal reports are a separate product from the website — `report-kit/`

Documents that pass between the developer and the client (the M7 executive brief, and the
phase reports that follow it) are built by `report-kit/` at the repo root. It is **totally
isolated** from the website: its own palette, its own components, no imports in either
direction. Different audience, different job.

*Why not share tokens:* the brief is dense with charts and needs colours validated for
colourblind-safe data encoding; the site is photographic and needs a warm ground. Convergence
was evaluated and rejected on coupling grounds, not feasibility — see D-053.

`report-kit/` is self-contained so `git subtree split` can lift it into its own repo if a
second project ever needs it. A submodule was considered and rejected: known friction for
agents, and no second consumer exists.

### D-053 ✅ The brief's palette stays as it is — the convergence analysis, for the record

A converged palette using the website's tokens **was tested and does work**, so if this is ever
revisited, the answer is already computed. `--ge-blue-800 #17475f` / `--ge-teal-700 #34767a` /
`--ge-warning-800 #7a5725` clears white-text AA on all three (9.99 / 5.23 / 6.53) and clears
ΔE 38+ for every pair under both protanopia and deuteranopia — comfortably better than the
current palette, whose weakest pair is 20.7. One constraint found: `--ge-sand-500 #9b7c55`
cannot be a data fill (white on it is 3.88:1, under AA); sand stays a surface colour.

Rejected anyway: the two products are uncoupled by decision, and re-skinning a signed-off
document to serve a consistency nobody asked for is not worth the risk.

### D-054 ✅ Report documents are built with Preact, rendered to a string at build time

`preact` + `preact-render-to-string` + `esbuild`, TypeScript, output is inert light-DOM HTML
with zero runtime framework. Chosen against Astro (wants routing and split assets — we need
one inlined file), Eleventy (SSG machinery for a single page), and raw template literals
(loses escaping, typing and editor support). JSX is also the operator's and the agents' native
idiom.

*Constraint that drove it:* an Artifact page blocks every external origin but
`fonts.googleapis.com`, so the published form must be a single file with inlined CSS and
base64 assets. That is a publish constraint, not an authoring one — hence the build step.

Native HTML composition was researched and does not solve the problem: Declarative Shadow DOM
(Widely Available since Aug 2026) and `@scope` (Newly Available since Jan 2026) give
encapsulation, but nothing in HTML renders a component N times from data. Shadow DOM is also
ruled out because the client feeds the document to an AI to audit the hours.

## Part D — Open, needs you or the client

| # | Question | Owner | Needed by |
|---|---|---|---|
| Q1 | Domain name — registered? who owns it? DNS access? | Client | Week 1 (blocks Resend) |
| Q2 | Which Google account owns the Forms + Sheet? | Client | Week 1 |
| Q3 | Business inbox for notifications | Client | Week 1 |
| Q4 | ~~Hosting eligibility~~ — resolved: Netlify free plan (D-015 / S-002) | — | done |
| Q5 | **What a package IS** — pick from the D-030 menu; plus which 1-2 destinations and 2-3 packages | Client | Week 1 |
| Q6 | ~~Photography~~ — resolved: free stock, curated by us (D-034) | — | done |
| Q7 | Show prices, or "enquire for pricing"? | Client | Week 2 |
| Q8 | Exact questions on each of the three forms | Client | Week 2 |
| Q9 | Privacy policy + terms — template, or lawyer review? (no cookie banner needed — analytics is cookieless) | Client | Week 4 |
| Q10 | ~~Analytics~~ — resolved: Umami Cloud, cookieless, no consent banner (S-007) | — | done |
