# Greek Essence v1 — Scope, Sitemap, Content Model

Authority: [00-DECISIONS.md](00-DECISIONS.md). This file says *what gets built*.

---

## 1. The product in one paragraph

A static English-language marketing site for a boutique Greece travel-planning agency.
Visitors browse destinations and pre-defined packages, or learn about a personalized
planning service. Every conversion path ends in a Google Form. Submissions email the agency
and acknowledge the customer. Content is edited by the client in Sanity. Nothing is booked,
paid for, or confirmed on the site.

---

## 2. Sitemap

**Seven templates.** List pages are cut (D-033) — Home carries the catalogue directly. Routes
are structured so `/packages` and `/destinations` list pages are additive later, not a redesign.

| Route | Template | Source | Notes |
|---|---|---|---|
| `/` | Home | Sanity `homePage` + all packages + all destinations | Hero, value prop, **the 2-3 packages as cards**, **the 1-2 destinations as cards**, personalized CTA, trust block |
| `/packages/[slug]` | Detail | Sanity `package` | Gallery, what's included, itinerary outline, CTA → request |
| `/packages/[slug]/request` | Interstitial | static + package | Restates the process, then hands off to the pre-filled Form |
| `/destinations/[slug]` | Detail | Sanity `destination` | Story, gallery, packages in this destination |
| `/personalized` | Offer page | Sanity `personalizedPage` | How the bespoke service works, CTA → custom Form |
| `/about` + `/contact` | Content page | Sanity `page` / `siteSettings` | Same template, different content |
| `/thank-you` | Confirmation | static | Google Forms redirect target. Says what happens next |
| `/privacy`, `/terms` | Legal | Sanity `page` | Reuses the content-page template |
| `/404` | Not found | static | |

**Cut from v1, deliberately:** `/packages` and `/destinations` list pages, and **all catalogue
filters** (D-032 — two filters across three packages is theatre).

## 3. Sanity content model

```ts
siteSettings   // singleton
  siteName, tagline, logo
  contact { email, phone, address, hours }
  forms { packageRequestUrl, personalizedUrl, generalUrl }   // base Google Form URLs
  formEntryIds { packageName, packageType }                   // prefill param mapping
  social[], nav[], footerLinks[]

homePage       // singleton
  hero { headline, subhead, image, ctaLabel, ctaHref }
  intro { heading, body }
  featuredDestinations[] -> destination
  featuredPackages[]     -> package
  personalizedBlock { heading, body, ctaLabel }
  trustBlock { heading, points[] }        // approved facts only, see D-006 / v0 trust rules

personalizedPage // singleton
  hero, howItWorks[ { step, title, body } ], faq[], ctaLabel

destination
  title, slug, region, summary, body (PortableText)
  heroImage, gallery[]
  featured (bool), order (number)
  seo { title, description }

package
  title, slug
  type: 'tour' | 'activity' | 'travel-package'
  destinations[] -> destination            // required, min 1
  summary, body (PortableText)
  heroImage, gallery[]
  durationDays (number), groupSize (string)
  highlights[], includes[], excludes[]
  price?  { amount, currency, basis: 'per-person'|'per-group', includesNote, reviewedAt }
  requestable (bool, default false)        // carried over from v0 D-001
  formUrlOverride?                          // escape hatch for a package-specific Form
  featured (bool), order (number)
  seo { title, description }

page           // about / privacy / terms
  title, slug, body (PortableText), seo
```

**Launch volume (D-032):** 1–2 `destination` documents, 2–3 `package` documents, plus the four
singletons and the `page` documents. Roughly nine documents in total. Sanity is still worth its
setup cost because the client edits copy without a developer for the next year (D-011).

**Publication gate (carried from v0 D-005):** a `package` cannot be published without
title, slug, summary, body, one type, ≥1 published destination, a hero image, and — if
`price` is set — every field in the price object. Enforce in Sanity validation rules so
the client cannot publish a broken card.

---

## 4. The three forms

| Form | Entry point | Prefilled | Fields |
|---|---|---|---|
| **Package request** | `/packages/[slug]/request` | package name, type | name, email, preferred dates (or flexible), adults, children, notes, consent |
| **Personalized trip** | `/personalized` | — | name, email, party size, destinations/interests, rough dates, budget band, notes, consent |
| | | | *Flow (D-031): submit → acknowledgement email → she emails to arrange a call → call → quote. No phone number collected, no scheduling tool in v1.* |
| **General question** | `/contact` | — | name, email, subject, message, consent |

Rules that carry over from v0 and still apply:
- Never imply a booking, reservation or availability. The request page, the form intro,
  the submit button, the thank-you page and the customer email all say "request" / "enquiry".
- No telephone number collected, no passport/payment/medical fields, no blanket marketing consent.
- A short warning above free-text: *"Please don't include passport, payment or medical details."*
- One combined name field. No separate first/last.
- The personalized acknowledgement says a **call will be arranged by email**, and promises no
  response time without client approval.

---

## 5. Explicitly not built

Accounts, login, payments, Stripe, custom calendar/date picker, live availability, confirmed
bookings, cancellation/refund flows, staff dashboard, CRM, articles/blog, accommodation pages,
attraction pages, newsletter, Greek locale content, Neon/Drizzle/any database, Route Handlers,
rate limiting, idempotency keys, request reference codes, retry queues, catalogue list pages, catalogue filters, automated scheduling.

---

## 6. Non-functional bar for v1

| Area | Bar |
|---|---|
| Rendering | Every page prerendered via `generateStaticParams`; server used only for Draft Mode and on-demand `revalidateTag` from the Sanity webhook |
| Lighthouse | Performance ≥ 90 mobile, Accessibility ≥ 95, SEO 100 |
| A11y | WCAG 2.2 AA on the 7 templates. Keyboard-navigable, visible focus, real landmarks |
| Images | Free stock curated per D-034 with a source/author/licence log; served via Sanity CDN + `next/image`, AVIF/WebP, explicit dimensions, LCP preloaded |
| Browsers | Last 2 versions of Chrome, Safari, Firefox, Edge + iOS Safari |
| Testing | Vitest for pure logic (form URL builders, Portable Text helpers). Playwright smoke on the 7 templates + the 3 CTA handoffs. No exhaustive unit coverage gate |
| SEO | Per-page metadata from Sanity, sitemap.xml, robots.txt, OG images, JSON-LD `TouristTrip` on packages |
| Privacy | Draft content provably unreachable unpublished — asserted by a Playwright test, not by care |
