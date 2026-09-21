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
No coverage percentage gate — see [03-WORKFLOW.md](03-WORKFLOW.md) §5 for why.

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

## 14. Two decisions that need your confirmation

### A-001 🟡 Drop `next-intl` from v1 entirely — revises D-005
D-005 said keep `next-intl` wired with a single active locale so Greek is a later content drop.
**I now think that is wrong.** It buys a `/en/` prefix on every URL of a single-language site —
uglier, and it carries routing machinery through every task in M3 for a benefit that arrives in v2.

The standard pattern is cheaper and SEO-safe: **English at the root now**, Greek added later at
`/el/` with English staying where it is. Nothing breaks, no URLs change, no redirects needed.

*Recommendation: no i18n in v1.* Saves roughly 2h across M0 and M3 and removes a concept from
every page task.

### A-002 🟡 Sanity localization: document-level later, none now
Three ways to hold two languages: localized fields (`{en, el}`), an `internationalizedArray`
plugin, or **document-level i18n** — a parallel document per language, linked, via Sanity's
`document-internationalization` plugin.

*Recommendation: document-level, added in v2.* v1 schemas carry no localization at all. Authoring
plain fields is far nicer for a non-technical client, and document-level i18n is additive — it
does not require rewriting the v1 schemas. This also matches what v0 concluded: store each
language's content separately rather than interleaving it.

The alternative — localized fields now — makes every field in the Studio a two-tab widget for a
client who will only ever fill one side of it for months.
