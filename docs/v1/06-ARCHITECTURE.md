# Greek Essence v1 — Technical Design

Stack decisions live in [05-STACK.md](05-STACK.md). This file is the **architecture**: the
boxes and arrows, the layout, the boundaries, and the conventions every agent follows so that
60 tasks produce one codebase rather than sixty.

---

## 1. System context

```
                    ┌───────────────┐
   client edits ───▶│  Sanity       │  content: packages, destinations, pages
                    │  Studio + CDN │
                    └───────┬───────┘
                            │ GROQ (build) · webhook → revalidateTag (on publish)
                            ▼
  visitor ──────▶  ┌────────────────────┐  ──▶ Umami  (pageviews, cookieless)
                   │  Next.js on        │
                   │  Netlify           │
                   │  prerendered pages │
                   └─────────┬──────────┘
                             │ CTA → prefilled URL
                             ▼
                   ┌────────────────────┐
                   │  Google Form       │
                   └─────────┬──────────┘
                             │ onFormSubmit
                   ┌─────────▼──────────┐
                   │  Google Sheet      │──▶ nightly CSV ──▶ Drive
                   │  + Apps Script     │
                   └────┬──────────┬────┘
                        │          │
              Resend ───┘          └─── MailApp
            (customer ack)          (agency notification)
```

**The site never receives a form submission.** It has no database, no mutation endpoint and no
customer data. Everything after the CTA is Google's. That single property removes most of what
would otherwise be the security, privacy and reliability surface.

The only server-side capability the site has is **Draft Mode and revalidation** — see §7.

---

## 2. Environments and infrastructure

| Environment | Where | Content source | Purpose |
|---|---|---|---|
| **local** | `pnpm dev` | Sanity `production` dataset, draft perspective | Development |
| **preview** | Netlify deploy preview, per branch | Sanity `production`, draft perspective | Every client review gate |
| **production** | Netlify, custom domain | Sanity `production`, published only | The live site |

**One Sanity dataset, two perspectives.** A separate `staging` dataset would double the client's
content work for a site with nine documents. Draft vs published is the distinction that matters,
and the Presentation tool gives it to us.

### Account ownership — all client-owned, operator-administered
| Service | Owns | Note |
|---|---|---|
| Domain + DNS | Client | Blocks Resend verification — chase week 1 |
| Sanity | Client | Operator added as admin |
| Google (Forms, Sheet, Apps Script, Drive) | Client | **Never the operator's personal Gmail** — carried from v0 |
| Resend | Client | Sender domain must be hers |
| Netlify | Operator initially, transferred at handover | Free plan |
| Umami | Operator initially, transferred at handover | |

Write this table into the runbook (T-05.12). The most common way a small project like this fails
a year later is that nobody can get into an account.

---

## 3. Project layout

```
app/
  layout.tsx                    root: fonts, metadata defaults, skip-link, landmarks
  page.tsx                      /
  not-found.tsx  error.tsx
  packages/[slug]/
    page.tsx                    /packages/[slug]
    request/page.tsx            /packages/[slug]/request   (interstitial)
  destinations/[slug]/page.tsx
  personalized/page.tsx
  [...slug]/page.tsx            about, contact, privacy, terms — one template
  thank-you/page.tsx
  api/draft-mode/
    enable/route.ts  disable/route.ts
  api/revalidate/route.ts       Sanity webhook target
  sitemap.ts  robots.ts
  studio/[[...tool]]/page.tsx   embedded Sanity Studio

components/
  ui/            Button Badge Card Breadcrumb Dialog Prose
  patterns/      Gallery PackageCard DestinationCard PriceBlock
  sections/      Hero CardGrid SplitFeature CtaBand

lib/
  sanity/
    client.ts        server-only
    queries.ts       GROQ strings
    schemas.ts       Zod schemas for raw query results
    map.ts           raw Sanity → domain DTO   ◀── the boundary
    image.ts         custom next/image loader
  forms/
    build-url.ts     buildFormUrl(): the site ↔ Google Forms contract
  seo/metadata.ts
  utils.ts           cn() and nothing ambitious

types/
  domain.ts          Package, Destination, SitePage, SiteSettings

sanity/
  schemas/           document + object definitions
  structure.ts       desk customization

tests/
  unit/              colocated is fine too; pure functions only
  e2e/               Playwright specs
```

---

## 4. Module boundaries — the dependency rules

One direction only. **`app` → `sections` → `patterns` → `ui`**, and everything may use `lib` and
`types`.

| Rule | Why |
|---|---|
| `components/**` must **never** import from `lib/sanity/**` | Components take DTOs. A component that knows what `_ref` means is welded to the CMS |
| `components/ui/**` imports nothing from `patterns` or `sections` | Primitives are leaves |
| `app/**` composes **sections**, not primitives | If a page reaches for a `Button` directly, either a section is missing or the page is doing too much |
| `lib/**` imports nothing from `components/**` | Logic is testable without React |
| Only `lib/sanity/client.ts` imports `server-only` and reads the token | One place to audit |

**Enforce it in eslint**, not in review — `no-restricted-imports` zones, added in T-00.3. A
convention an agent can violate silently is not a convention.

**Second rule, equally important: do not create a component for one caller.** Inline it until a
second use appears. The failure mode of agent-built UI is forty single-use components.

---

## 5. Data flow and DTOs

This is the most important decision in this document.

```
Sanity document  →  GROQ query  →  Zod parse  →  domain DTO  →  RSC page  →  section props
   (raw)            queries.ts     schemas.ts      map.ts        app/         components/
```

**Components never see a Sanity document.** `lib/sanity/map.ts` maps raw query results into the
plain types in `types/domain.ts` at the boundary, and nothing downstream knows Sanity exists.

```ts
// types/domain.ts — what the rest of the app knows about
export type Package = {
  slug: string
  title: string
  type: 'tour' | 'activity' | 'travel-package'
  summary: string
  body: PortableTextBlock[]
  hero: Img                 // { url, alt, width, height, lqip }
  gallery: Img[]
  destinations: DestinationRef[]
  durationDays?: number
  highlights: string[]
  includes: string[]
  excludes: string[]
  price?: Price             // only present when FULLY qualified — see below
  requestable: boolean
  formUrl: string           // already resolved: override ?? siteSettings default
  seo: Seo
}
```

Three things this buys, in order of how much they matter:

1. **The D-006 price rule becomes structural.** `map.ts` returns `price: undefined` unless
   currency, basis, inclusions, review date and the confirmation note are *all* present. A
   partially-qualified price is then impossible to render — not because a component remembered
   to check, but because it does not exist. Business rules belong at the boundary, not in JSX.
2. **Components are testable with object literals.** No Sanity fixtures, no mocking a client.
3. **Swapping or restructuring the CMS is contained** to one file.

The cost is one mapping function per document type. At six types that is an hour, and it is the
best hour in the project.

`formUrl` shows the same idea: resolving the override-vs-default fallback once in `map.ts` means
no component ever writes `pkg.formUrlOverride ?? settings.forms.packageRequestUrl`.

### The Google Forms contract
`lib/forms/build-url.ts` is the single interface between the site and M4's work:

```ts
buildFormUrl(base: string, prefill: Record<string, string>): string
```

Entry IDs live in `siteSettings.formEntryIds` (Sanity), **not** in code — so when the junior
rebuilds a form and the IDs change, the client-editable config changes, not a deploy. This is
the one place the two lanes touch; T-04.1's contract spec defines the key names.

---

## 6. Server / client boundary

**React Server Components by default.** `'use client'` is an exception that needs a reason, and
in v1 there are exactly three:

| Component | Why |
|---|---|
| `MobileNav` | Open/close state |
| `Gallery` | Lightbox state, keyboard handling |
| `Dialog` | Base UI primitive, inherently client |

Everything else — every page, every section, every card — is a Server Component. If a fourth
appears, it is a design conversation, not a quick fix.

`lib/sanity/client.ts` imports `server-only` so a mistaken client import fails the build rather
than shipping a token to the browser.

---

## 7. Rendering and caching

- **Every route is prerendered.** All dynamic routes use `generateStaticParams`. The server
  exists for Draft Mode and revalidation, not to render pages per request.
- **Tagged caching.** Fetches tag by document type and slug — `package:paros-7day`,
  `destination:paros`, `settings`.
- **On publish**, the Sanity webhook hits `/api/revalidate`, which verifies the webhook secret
  and calls `revalidateTag` for the affected tags. Changed pages update in seconds; nothing else
  rebuilds.
- **Draft Mode** flips fetches to the draft perspective for that session only. §5 of
  [05-STACK.md](05-STACK.md) covers the leak risk; T-02.6 is the test.

---

## 8. Configuration and secrets

```
NEXT_PUBLIC_SANITY_PROJECT_ID     public
NEXT_PUBLIC_SANITY_DATASET        public
NEXT_PUBLIC_SITE_URL              public — canonical URLs, OG, sitemap
NEXT_PUBLIC_UMAMI_WEBSITE_ID      public
SANITY_API_READ_TOKEN             SERVER ONLY — draft content
SANITY_REVALIDATE_SECRET          SERVER ONLY — webhook verification
SANITY_STUDIO_PREVIEW_URL         Studio only
```

Rules: anything without `NEXT_PUBLIC_` must never appear in a client component. `.env.example`
is committed with every key and no values. **Validate env at startup with a Zod schema** — a
missing token should fail the build loudly, not produce a site that silently serves published
content when it should serve drafts.

The two Resend and Apps Script secrets live in **Apps Script Script Properties**, never in this
repo and never in Netlify — that lane does not touch the site.

---

## 9. Conventions

| | |
|---|---|
| Files | kebab-case: `package-card.tsx` |
| Components | PascalCase, named exports; no default exports outside `app/` |
| Props | `type Props = {...}` local to the file; exported only when reused |
| Styling | Tailwind utilities; CVA for variants; **design tokens only** — no arbitrary values like `text-[#17475f]` or `mt-[13px]` |
| Ordering | `cn()` wraps every conditional class; `prettier-plugin-tailwindcss` sorts |
| Imports | `@/` alias everywhere; no deep relative paths |
| Async | Server Components fetch directly; no `useEffect` data fetching anywhere |
| Dates | Intl API. No date library — we format about three dates |
| State | None. There is no global state in this app. If a task needs a store, escalate it |

---

## 10. Error, loading and empty states

| State | Convention |
|---|---|
| Not found | `not-found.tsx`, localized copy, routes back to home and catalogue |
| Unpublished package | Its old URL renders the D-005 "no longer listed" page — no stale price, media or claims (T-03.10) |
| Runtime error | `error.tsx` at root only. Plain, branded, no stack traces |
| Loading | Pages are prerendered, so `loading.tsx` is unnecessary. Do not add skeletons for content that is already in the HTML |
| Empty catalogue | Home and destination pages must render sensibly with zero packages. With a 2–3 package launch this is one bad publish away |

---

## 11. Testing strategy

**Unit (Vitest)** — pure functions only: `buildFormUrl`, `map.ts` mappers (especially the price
qualification rule), the Sanity image loader, SEO metadata builders.

**E2E (Playwright)** — the 7 templates render; the 3 CTA handoffs produce correctly prefilled
URLs; axe on every template; the draft-leak assertion (T-02.6).

**Not tested**: component snapshots, Sanity itself, Google's infrastructure, styling.
No coverage percentage gate — see [03-WORKFLOW.md](03-WORKFLOW.md) §6 for why.

---

## 12. Remaining library picks

| Need | Choice | Note |
|---|---|---|
| Portable Text | `@portabletext/react` | Custom serializers in `components/ui/prose.tsx` |
| Sanity types | `sanity typegen` (official) | Generates from schema + GROQ; no third-party query builder |
| Boundary validation | Zod 4 | At the Sanity boundary and env only. Not for forms we do not host |
| Env validation | Small Zod schema in `lib/env.ts` | `@t3-oss/env-nextjs` is more machinery than seven variables deserve |
| Sitemap | Next's native `sitemap.ts` | No `next-sitemap` |
| A11y testing | `@axe-core/playwright` | |
| Bundle analysis | `@next/bundle-analyzer` | Dev-only, run before launch |
| Error monitoring | **None in v1** | Netlify function logs cover a site with no mutations. The failure that actually matters — an enquiry email not sending — is alerted from Apps Script (T-04.8). Revisit if the server does more |

---

## 13. Sanity — concepts, content modelling, and Studio UX

Written because the operator is new to Sanity. Agents follow this section as standards, not
suggestions. **Nothing here is Sanity's default** — the defaults produce a working Studio that is
unpleasant to use, and this client will be using it for years.

### The five concepts you need

| Term | What it means |
|---|---|
| **Dataset** | A content database. We have one: `production` |
| **Document** | One editable thing — a package, a destination, the site settings |
| **Schema** | The typed definition of a document's fields, written in TypeScript with `defineType` / `defineField` |
| **GROQ** | Sanity's query language. Like SQL for JSON documents. Queries live in `lib/sanity/queries.ts` |
| **Portable Text** | Rich text stored as typed JSON blocks rather than HTML, rendered by components we supply |

**Studio** is the editing UI. We embed it at `/studio` on the same domain, so the client has one
URL to remember and the Presentation tool works without cross-origin setup.

### Portable Text — restrict the editor

The single biggest Studio UX decision. By default the block editor offers styles that will make
the site look wrong. Allow only:

| Allowed | Excluded, deliberately |
|---|---|
| Normal, **H2**, **H3** | **H1** — the page owns its one `h1` |
| Bold, italic | Underline — reads as a broken link |
| Link (external + internal reference) | Code, code block — not a dev blog |
| Bullet and numbered lists | Text colour, font size — the design system owns appearance |
| Image block, with **required** alt text | Blockquote, unless a designed treatment exists after M1 |

Constraining the editor is what stops a non-technical client accidentally producing a page that
looks broken. It is also fewer serializers for agents to write.

### Studio UX standards — every schema, no exceptions

1. **Field groups as tabs** — `Content` · `Media` · `SEO`. She should never scroll past meta
   description to reach the body.
2. **A plain-language `description` on every field.** Not "Slug" — *"The web address for this
   package. Lowercase, words joined by hyphens. Changing it breaks existing links."*
3. **List previews with `title`, `subtitle` and `media`.** A list of "Untitled" documents is the
   most common way a Studio feels broken.
4. **Validation messages that say what to do.** Not *"Required"* — *"Add a short summary; it
   appears on the package card on the home page."*
5. **Character limits with a reason.** `summary` capped at ~160 so cards never break — this is
   what makes T-01.13's content-shape stress test hold in practice, instead of relying on her
   restraint.
6. **Singletons locked**: `siteSettings`, `homePage`, `personalizedPage` cannot be created,
   duplicated or deleted from the Studio. Only edited.
7. **Alt text required on every image.** Accessibility, and WCAG 2.2 AA is in our non-functional
   bar. Required at the schema level so it cannot be skipped.
8. **Desk structure organised the way she thinks**: *Packages · Destinations · Pages · Site
   settings* — not a flat alphabetical list of document types.
9. **Initial values** on new documents so nothing starts fully blank.

### The publication gate, restated as schema
v0's D-005 says a package cannot be published incomplete. Enforce it as Sanity validation rules
so the Studio blocks it with a readable reason: title, slug, summary, body, one type, at least
one published destination, hero image with alt — and if a price exists at all, every D-006
qualification field with it.

The price rule is enforced **twice on purpose**: in the Studio so she cannot publish a bad one,
and in `map.ts` (D-040) so the site cannot render one. Belt and braces, because it is the rule
with actual legal consequences.

### Agent DX standards

| | |
|---|---|
| Types | `sanity typegen` generates from schema + GROQ. Never hand-write a Sanity type |
| Queries | One named query per page in `lib/sanity/queries.ts`. No inline GROQ in components |
| Schemas | `defineType` / `defineField` throughout, for autocomplete and type safety |
| Mapping | Every query result passes through `map.ts` (D-040) before leaving `lib/` |
| Fixtures | `tests/fixtures/domain.ts` exports plain DTO literals, so component tests never touch Sanity |
| Images | Always through `lib/sanity/image.ts`. Never construct a CDN URL by hand |

## 14. Netlify free-plan economics — the constraint that shapes deployment

Verified against Netlify's own docs, September 2026. **This changes how we deploy**, so it is
architecture, not billing trivia.

The free plan is **300 credits/month, a hard limit**. There is no auto-recharge and no overage
charge — instead, **every project on the account pauses until the next billing cycle.** Credit
exhaustion is an *outage*, not a bill.

| Consumes credits | Rate | In our terms |
|---|---|---|
| **Production deployment** | **15 credits each** | **20 production deploys/month, maximum** |
| Web bandwidth | 20 credits / GB | 15 GB/month if we spent everything on it |
| Web requests | 2 credits / 10,000 | |
| Function compute | 10 credits / GB-hour | Draft Mode + revalidation. Negligible at our size |
| **Deploy previews** | **free, unlimited** | |
| **Branch deploys** | **free, unlimited** | |
| **Failed deploys** | **free** | |

### A-003 ✅ Production deploys are a deliberate, batched act — not automatic on merge

Because deploys and traffic draw on the same 300 credits, deploying carelessly takes the site
down later in the month. So:

- **`main` does not auto-deploy to production.** Production releases are manual and batched.
- **Budget ≤ 8 production deploys/month**, reserving ~180 credits (≈9 GB) for actually serving
  visitors.
- **Deploy previews on every branch, used freely** — they cost nothing and they are how every
  client review gate works anyway (T-01.4, T-01.14).
- Act on Netlify's 50% / 75% notifications. At 75% with real traffic, stop deploying and talk to
  the client.

### Two earlier decisions that turn out to protect us

**1. Dropping static export was not just about preview.** On a static export, a Sanity publish
fires a deploy hook and rebuilds the site — **15 credits every time the client fixes a typo.**
She would pause her own website after twenty edits. Because we have a server,
`revalidateTag` handles content updates as function compute, which is effectively free at our
volume. The Netlify free plan is only viable *because* we kept the server.

**2. Serving images from Sanity's CDN protects the bandwidth budget.** Netlify only ever
transfers HTML, CSS and JS — roughly 100–150 KB per page. That is on the order of 100,000
pageviews inside budget. Had we served images from Netlify, a page with 2 MB of photography
would exhaust 15 GB in about 7,500 pageviews, which an Instagram spike could produce in a day.

Both decisions were made for other reasons. Note the near miss.

### A-004 ✅ Team access: the junior works through Git, not the Netlify console
The free plan allows **one team member** (Git contributors are unlimited only on public repos,
and ours is private). The operator holds that seat.

This is workable because the junior's lane is Google Forms and Apps Script — outside Netlify
entirely — plus SEO plumbing that ships through Git like any other code. He does not need
console access; if he needs a deploy log, the operator pulls it. Revisit only if it becomes a
real bottleneck.

### Paid plans, for when the free plan stops fitting

| | Free | **Personal** | **Pro** |
|---|---|---|---|
| Price | $0 | **$9/mo** | **$20/mo** |
| Credits | 300 (hard stop) | **1,000** | 3,000–20,000 |
| Team members | 1 | 1 | **Unlimited** |
| Adds | — | Smart secret detection, priority email support | Private org repos, shared env vars, 3+ concurrent builds, 30-day analytics, team management, 7-day audit logs, extended function logs |

**Escalation path: Free → Personal ($9).** 1,000 credits is 3.3× headroom and effectively removes
the pause risk. It does *not* add a second seat, so A-004 still holds. Pro ($20) is only worth it
for unlimited members — and at that price the honest comparison is against Vercel Pro, which
costs the same but which Netlify Free beat on the only question that mattered: being usable at
all without paying.

Ask for $9 only with evidence — real visitor traffic pushing credits past 50% — which is the
evidence-led upgrade conversation v0's decisions already described.

### A-005 ✅ Netlify agent tooling: official skills + CLI, no MCP

Netlify has an unusually complete agent ecosystem: an official MCP server, an official **agent
skills** repo ([netlify/context-and-tools](https://github.com/netlify/context-and-tools)), Agent
Runners, an AI Gateway, and Claude Code as a first-class supported client.

We take **the skills and `netlify-cli` (v27), not the MCP** — consistent with D-021b. Netlify's
skills *are* the lazy-loaded pattern we endorsed: documentation an agent pulls when it needs it,
versioned by Netlify, costing nothing resident.

Install only the four that match this project (T-00.5):

```bash
npx skills add netlify/context-and-tools \
  --skill netlify-config \
  --skill netlify-cli-and-deploy \
  --skill netlify-frameworks \
  --skill netlify-caching --yes
```

Deliberately skipped: `netlify-functions`, `netlify-edge-functions`, `netlify-blobs`,
`netlify-db`, `netlify-ai-gateway` (we use none of these), `netlify-image-cdn` (Sanity's CDN
instead — §14 explains why), `netlify-forms` (see below).

**Agent Runners are not for v1.** They let agents make repository changes on Netlify's
infrastructure, and they bill against the same 300-credit budget as our deployments and our
traffic. Agents run locally, where they cost nothing.

### Noted but not reopened: Netlify Forms
Netlify Forms handle submissions with no backend code, and the credit table lists form
submissions as free and unlimited. That would keep visitors on-site and remove the Google Forms
handoff that D-012 exists to paper over.

**Not reopening it.** The client chose Google Forms, and her choice also puts the submission data
in a Sheet she owns, on an account she controls, with no dependency on us. Worth knowing if she
ever asks why visitors leave the site to enquire — the answer is a real trade she made, not a
limitation.

### When to reopen the hosting decision
A sustained draw above ~50% of credits **from real visitor traffic** is a demand signal, and it
triggers exactly the evidence-led client conversation v0's decisions described: real people are
arriving, so a bounded paid upgrade is now justified. Exhaustion from deploys or mistakes is an
operational failure, not a demand signal — fix the process instead.

If the client declines to pay and traffic genuinely outgrows the plan, **Cloudflare Workers with
the OpenNext adapter** is the fallback: a more generous free tier that keeps Draft Mode, at the
cost of an adapter in the dependency chain. Do not go back to a static export — it trades the
client's live preview away and, as above, makes her own edits expensive.

### A-006 ✅ Sanity agent tooling: skills + CLI, **and deliberately not the MCP**

Sanity's ecosystem mirrors Netlify's: official agent skills, an official MCP server, and a mature CLI.

**Take:**
- **Agent skills** — `npx skills add sanity-io/agent-toolkit` (development best practices, content
  modelling, SEO). Lazy-loaded, versioned by Sanity, free when unused. Claude Code supported.
- **The CLI** — `npx sanity@latest` for typegen, schema deploy, dataset operations and document
  queries during debugging.

**Skip the MCP**, and here for a stronger reason than D-021b.

The Sanity MCP is remote (`https://mcp.sanity.io`, OAuth) and its tools are
`create_documents`, `patch_documents`, `publish_documents`, `unpublish_documents`,
`discard_drafts`, `version_discard`. Its entire value proposition is **write and delete access to
the client's content.**

**Agents do not write the client's content.** They write schemas, queries, mappers and a seed
script. The seed script (T-02.4) uses a write token deliberately, in a reviewable file, against
placeholder data — that is a different thing from an agent reaching into a live dataset mid-task
and patching a document nobody asked it to touch.

There is no capability lost: the CLI queries documents for debugging just as well. What is
avoided is an entire class of incident where an agent "helpfully" tidies the client's content.

### A-007 ✅ Visual work is proved by a live walk, not by a green test
Adopted from `agentic-wave`'s `references/verification.md`, whose rule we take verbatim:

> **A green unit test is not enough. You must walk the same path a user would walk.**

For any user-visible change, before a task is done:
1. Run the app (or open the Netlify deploy preview) and drive it with Playwright like a person.
2. For each step — load, interact, refresh, empty state, error state — capture a **viewport
   screenshot** and a **full-page screenshot**, and read the console and failed network calls.
3. Save to `.local/evidence/<date>-<slug>/`, named by step: `01-load-viewport.png`,
   `01-load-full.png`, `01-console.txt`.
4. Check the other screens sharing the same data.
5. File anything odd as a Backlog.md task — `spike`+`triage` if unsure, `bug` if a defect,
   `external` if outside our control. A dated note plus an evidence path is enough.

Skip the walk for pure refactors with no screen change; still run the tests.

*Why this earns ~15 minutes per UI task:* the operator reviews at **phase** boundaries (D-027) on
8–12h a week. Without per-task visual evidence, a wrong direction is found at the gate with three
more tasks built on top of it. This is the cheapest insurance in the project.

### A-008 ✅ Copy is drafted directly into Sanity and reviewed in Presentation
M6's five copy tasks do **not** produce documents. Agents write copy straight into Sanity as
**drafts**; the client reviews it in place, on the real page, through the Presentation tool;
she edits or approves; then she publishes.

*Why:* it deletes the transcription step. The Google-Docs loop is draft → approve → someone
retypes it into Sanity — effort, delay, and a place to introduce errors into copy that was
already approved. Here, approved copy is already in the CMS, in the right field, on the right page.

It also puts the client in the Studio repeatedly during weeks 3–6, which is the best possible
training for T-05.9 — she will have been using it for a month before anyone calls it training.

**Scheduling consequence:** M6's copy tasks now depend on **M2 P2.1 + P2.2 + T-02.5** (schemas and
Presentation working). Photo curation (T-06.1) has no such dependency and still starts in week 2.

### A-009 ✅ Apps Script is version-controlled in the repo via `clasp`
Google's official CLI (`@google/clasp` v3.4.1). The junior's `onFormSubmit` handler, email
templates and backup script live in the repo as TypeScript and go through the normal branch flow.

*Why this is not optional:* without it, the entire M4 output exists only inside a Google editor —
unreviewable, unversioned, un-diffable, with no rollback, and gone if the client's Google account
has a problem. It is also the one part of the codebase the operator would otherwise never see.

`clasp` pushes to the client's Apps Script project; the junior owns the workflow, and credentials
stay in Apps Script Script Properties, never in the repo.

## 14. Accepted architecture decisions

### A-001 ✅ No i18n machinery in v1 — accepted 2026-09-21
Revises D-005. `next-intl` is **not** installed. English lives at the root with no locale prefix.
Greek is added in v2 at `/el/`, English stays where it is — no URL changes, no redirects, nothing
breaks. Saves ~2h across M0 and M3 and removes a concept from every page task.

### A-002 ✅ No Sanity localization in v1 — accepted 2026-09-21
v1 schemas carry plain, single-language fields. Greek arrives in v2 through Sanity's
`document-internationalization` plugin — a parallel document per language, linked — which is
purely additive and does not require rewriting the v1 schemas.

Rejected: localized fields (`{en, el}`) and `internationalizedArray`, both of which would turn
every field in the Studio into a two-tab widget the client only ever fills one side of, for
months, for nothing.

This also matches what v0 concluded independently: store each language's content separately
rather than interleaving it.

