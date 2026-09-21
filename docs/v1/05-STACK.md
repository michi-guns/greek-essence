# Greek Essence v1 — Stack Decisions

Written because the earlier D-010 recorded a stack it had **inherited from the v0
`package.json`**, not one anyone chose. This file is the actual decision, with the reasoning.

Verified against Next.js 16.3.5 docs and Cloudflare's current framework guidance, September 2026.

---

## S-001 ✅ Next.js 16, App Router, **server runtime** (no static export)

**Chosen over Astro**, which is arguably the better technical fit for a brochure site (zero JS by
default, islands, more stable API). Next wins on grounds that matter more here:

- You already run Next 16.3 on another repo, so knowledge moves both ways.
- The reference repo (`nextjs-todo-list-example`) is Next, and its agent context files, CI
  patterns and conventions are the ones we are borrowing.
- One framework across your projects is worth more than a marginally better fit on one of them.

*Honest counterweight:* Next 16 postdates agent training data — the reference repo's `AGENTS.md`
opens by warning exactly this. Agents must read `node_modules/next/dist/docs/` before writing
routing or config code. That obligation goes in `AGENTS.md`.

**Rendering: static by default, with a server available.** Every page uses
`generateStaticParams` and is prerendered at build; the server exists for Draft Mode and
on-demand revalidation, not to render pages per request. We get static performance *and*
preview.

**`output: 'export'` was considered and rejected.** It would have removed the server entirely —
attractive for simplicity — but it also removes Draft Mode, which is what Sanity's Presentation
tool needs. Losing live preview for a client who owns her own content was the wrong trade.

## S-002 ✅ Netlify — free plan

### Why not Vercel
Vercel's own docs state it plainly: *"the Hobby plan restricts users to non-commercial, personal
use only."* A client's business website is commercial, so Hobby is a terms violation rather than
a grey area — the exact risk v0 flagged in D-015 and never closed. Vercel therefore means Pro at
roughly $20/month billed to the client indefinitely, which fails the zero-recurring-spend goal
for no benefit Netlify does not also provide.

### Why not Cloudflare
Cloudflare Pages is free and commercially unambiguous, but its Next.js path is either a static
export (no Draft Mode) or an adapter — `vinext` or OpenNext on Workers — that adds a moving part
we would have to keep working. Netlify gets us the same for less risk.

### Why Netlify
- **Commercial use is explicitly permitted on the free plan.** Netlify staff, in their own
  forum: *"Yes, you can use the free plan for commercial projects… you can definitely charge
  your customers for your services in building and maintaining their websites."* The only
  restriction is reselling the hosting itself.
- **Next.js 16 deploys with zero configuration**, per Netlify's own changelog, via their
  OpenNext-based runtime — a maintained first-party path, not an experimental one.
- **`revalidateTag` / `updateTag` are supported**, which is precisely what a Sanity webhook needs
  for on-demand revalidation.
- Deploy previews per branch, which we rely on for every client review gate.

## S-003 ✅ What the server buys us, and what it costs

### Gained
| | |
|---|---|
| **Draft Mode** | The reason for this decision. Enables Sanity's **Presentation tool**: the client edits in the Studio and watches the real page update beside her, clicking an element to jump to its field. For a content owner this is a different product from "publish and go look" |
| **On-demand revalidation** | Sanity webhook → `revalidateTag` → the changed page updates in seconds. No full rebuild, no deploy hook |
| **`redirects` / `headers` in `next.config`** | Security headers (CSP, HSTS, Referrer-Policy) live in code and are reviewable, rather than in a platform-specific `_headers` file |
| **Route Handlers** | Not needed today, but the draft-mode enable/disable endpoints are exactly this |
| **`next/image` default loader** | Works now. We still use a **custom Sanity loader**: Sanity's CDN does the transformation for free and unmetered, which keeps us off Netlify's image quota entirely |

### Cost — two things that need real care
1. **Draft content must never leak to the public.** The Sanity read token is server-only and must
   never reach the client bundle; `draftMode()` must gate every draft fetch. This wants a
   Playwright test asserting that an unauthenticated request to a page with unpublished changes
   returns the published version. Not a matter of being careful — a matter of having a test.
2. **There is now a runtime.** A static export had nothing to attack and nothing to break. This is
   still a simple application, but env vars, a token, and a server path exist. Keep every page
   prerendered so the server is only doing preview and revalidation.

## S-004 ✅ shadcn + Base UI

Carried from v0 **with a verification gate**, not on faith. shadcn is historically Radix-based
and its Base UI support is comparatively new. T-00.1 is a spike that installs the combination
and builds a Dialog before the real scaffold exists.

If Base UI support turns out to be immature, fall back to **shadcn + Radix** — the well-trodden
path with far more training data — and record it here. Do not discover this in M1.

*Scope note:* we need seven components and only `Dialog` genuinely needs accessibility
primitives. The library earns its place through consistency and the CVA variant pattern, not
through breadth. Resist installing components we do not use.

## S-005 ✅ Typography — Fraunces + Inter, self-hosted

*Delegated pick.* Heading: **Fraunces** — a variable serif with real character (optical size and
"softness" axes), warm rather than corporate, and it carries the "well-made printed travel
journal" direction in 02-DESIGN-SYSTEM without costing anything.
Body: **Inter** — neutral, excellent at small sizes, enormous language coverage.

**Self-hosted via Fontsource**, not Google Fonts CDN: no third-party request, no privacy
disclosure to write, better LCP. Subset to `latin` + `latin-ext` (Greek comes with the locale,
later). Set `size-adjust` fallback metrics to kill layout shift.

Overridable in M1 — type is visible enough that you should judge it in the comps.

## S-006 ✅ Icons — `lucide-react`; Motion — CSS only

Icons: lucide. Tree-shakeable, matches shadcn conventions, consistent stroke weight.

Motion: CSS transitions and `tw-animate-css`. **No motion library.** The design direction is
"quiet premium" — the animation budget is hover states, focus rings, and gentle reveals. A
motion library would be 30KB in service of restraint. Use the View Transitions API for page
transitions if browser support allows; degrade silently if not.

## S-007 ✅ Analytics — Umami Cloud

Requirements: popular, real free tier, privacy-first, **not Google Analytics**.

**Umami Cloud.** Open source (MIT), widely adopted, **cookieless — so no consent banner**, which
matters for an EU-facing site and saves writing cookie-policy copy nobody reads. Supports custom
events if we want them. The escape hatch is real: if the free tier ever changes, Umami
self-hosts, so we are not trapped.

⚠️ **Verify the current free-tier limits at implementation time (T-05.2).** Their pricing page
did not render when this was written, and third-party listings citing ~100k events/month are not
a source I am willing to state as fact.

**Fallback if the free tier disappoints: Cloudflare Web Analytics** — genuinely free and
unlimited, cookieless, and works on any host via a JS beacon regardless of where the site runs.
Weaker on custom events, which matters less than usual here (see below).

Rejected: Google Analytics (excluded by you, and needs a consent banner); Plausible, Fathom and
Simple Analytics (no meaningful free tier); Netlify Analytics (paid $9/mo); Microsoft Clarity
(free and excellent, but cookies, a consent banner, and session recording on a page where people
type enquiry details is a privacy conversation we do not need).

### One design consequence worth noticing
The funnel ends off-site at Google Forms, so the last thing we can measure is the handoff. But
because D-012 put an **interstitial page** at `/packages/[slug]/request`, that conversion step
*is a pageview* — no custom event needed. Plain pageview analytics captures the main funnel for
free. Only the `/personalized` and `/contact` CTAs hand off without an interstitial; if we want
those measured, that is where a custom event earns its keep.

## S-008 ✅ Everything else

| | |
|---|---|
| Package manager | pnpm, version pinned via `packageManager` |
| Node | 24 LTS, pinned in `.node-version` |
| Language | TypeScript, `strict: true` |
| Styling | Tailwind 4, CSS-first config in `globals.css` |
| Variants | `class-variance-authority` + `tailwind-merge` |
| Content | Sanity (D-011), Portable Text for rich text, Presentation tool for live preview |
| Validation | Zod 4 — for Sanity response shapes and the form URL builder, not for forms we do not host |
| Testing | Vitest (logic) + Playwright (smoke) |
| CI | GitHub Actions |

---

## Component architecture

Moved to [06-ARCHITECTURE.md](06-ARCHITECTURE.md) §3–§4, which owns layout, dependency rules and
the data-flow boundary.

## Open

- **S-004 verification** — T-00.1 spike must confirm shadcn + Base UI before M1 starts.
- ~~S-003 Draft Mode~~ — **resolved.** Netlify's server runtime gives us Draft Mode and the
  Sanity Presentation tool. No preview workaround needed.
- **S-007 free tier** — confirm Umami Cloud's current limits during T-05.2.
- Fonts and icons are overridable during M1 if the comps argue otherwise.
