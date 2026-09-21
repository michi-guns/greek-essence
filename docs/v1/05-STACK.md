# Greek Essence v1 — Stack Decisions

Written because the earlier D-010 recorded a stack it had **inherited from the v0
`package.json`**, not one anyone chose. This file is the actual decision, with the reasoning.

Verified against Next.js 16.3.5 docs and Cloudflare's current framework guidance, September 2026.

---

## S-001 ✅ Next.js 16, App Router, `output: 'export'`

**Chosen over Astro**, which is arguably the better technical fit for a 7-page static brochure
site (zero JS by default, islands, more stable API). Next wins on grounds that matter more here:

- You already run Next 16.3 on another repo, so knowledge moves both ways.
- The reference repo (`nextjs-todo-list-example`) is Next, and its agent context files, CI
  patterns and conventions are the ones we are borrowing.
- One framework across your projects is worth more than a marginally better fit on one of them.

*Honest counterweight:* Next 16 postdates agent training data — the reference repo's `AGENTS.md`
opens by warning exactly this. Agents must read `node_modules/next/dist/docs/` before writing
routing or config code. That obligation goes in `AGENTS.md`.

**Rendering: fully static.** `output: 'export'` produces an `out/` folder of HTML/CSS/JS. There
is no server, no runtime, nothing to attack and nothing to pay for.

## S-002 ✅ Cloudflare Pages

Closes D-015, which flagged Vercel's commercial-use terms as an unresolved launch risk and never
resolved it. Cloudflare Pages' free tier is unambiguous about commercial use, static performance
is excellent, and a static export needs nothing Pages lacks.

Cloudflare currently lists three Next.js paths: **vinext** (their recommended Workers route),
the **OpenNext adapter**, and **static Next.js on Pages**. We take the third. It is the simplest
of the three and the only one with no adapter in the dependency chain.

## S-003 ✅ Consequences of static export — read this before building

`output: 'export'` disables real features. All of these are fine for v1, but each needs a
deliberate answer rather than a discovery in week 5.

| Unsupported | Our answer |
|---|---|
| **ISR / `revalidate`** | Sanity webhook → **Cloudflare Pages deploy hook** → full rebuild (~1 min). Simpler than ISR and adequate for a brochure site |
| **`next/image` default loader** | **Custom Sanity loader.** Sanity's CDN does the transformation (`?w=&q=&fm=`), so we get real optimization without a server. Do *not* use `images.unoptimized` |
| **`redirects` / `headers` in `next.config`** | Cloudflare `_redirects` and `_headers` files. Security headers (CSP, HSTS, Referrer-Policy) live there |
| **Middleware / proxy** | Not needed. Nothing to intercept |
| **Route Handlers reading the request** | Not needed. `force-static` GET handlers still work if we want a generated JSON file |
| **Server Actions** | Not needed. All mutations are Google Forms |
| **Cookies** | Not needed. No auth, no session, no consent cookie (see S-007) |
| **Draft Mode** | ⚠️ **The one real loss.** See below |

### The Draft Mode problem
Static export cannot do Next's Draft Mode, so there is no "preview unpublished Sanity content on
the site" flow. The client will want to see a package before publishing it.

Options, in order of preference:
1. **Sanity Studio's own preview pane** — she reviews content in the Studio, not on the site.
   Free, zero build work, but it is not a true page preview.
2. **A preview branch deploy** — a second Cloudflare Pages environment building from the Sanity
   *draft* dataset perspective. Real page preview, roughly 2–3h of work.
3. **Publish and look** — she publishes, the rebuild runs, she checks the live site, she fixes.
   Crude, and on a site with a handful of visitors it is genuinely survivable.

**Decide this during M2**, not at launch. Start with (1), upgrade to (2) if she struggles.

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

## S-007 ✅ Analytics — Cloudflare Web Analytics

Supersedes the Plausible/Umami note in the roadmap. Since we are on Cloudflare anyway: free,
cookieless, no consent banner required, no extra vendor, no script from a third-party domain,
and no account for the client to own and forget. The host choice makes this the obvious answer.

## S-008 ✅ Everything else

| | |
|---|---|
| Package manager | pnpm, version pinned via `packageManager` |
| Node | 24 LTS, pinned in `.node-version` |
| Language | TypeScript, `strict: true` |
| Styling | Tailwind 4, CSS-first config in `globals.css` |
| Variants | `class-variance-authority` + `tailwind-merge` |
| Content | Sanity (D-011), Portable Text for rich text |
| Validation | Zod 4 — for Sanity response shapes and the form URL builder, not for forms we do not host |
| Testing | Vitest (logic) + Playwright (smoke) |
| CI | GitHub Actions |

---

## Component architecture

```
components/
  ui/          primitives — Button, Badge, Card, Breadcrumb, Dialog, Prose
  patterns/    composed, reusable — Gallery, PackageCard, DestinationCard
  sections/    page-level blocks — Hero, CardGrid, SplitFeature, CtaBand
app/           routes only; pages compose sections, never primitives directly
lib/           pure functions — buildFormUrl, sanity client, image loader
```

Rule: **a page assembles sections; a section assembles patterns and primitives.** If a page
reaches for a primitive directly, either the section is missing or the page is doing too much.

Second rule: **do not create a component for one caller.** Inline it until a second use appears.

---

## Open

- **S-004 verification** — T-00.1 spike must confirm shadcn + Base UI before M1 starts.
- **S-003 Draft Mode** — pick a preview approach during M2.
- Fonts and icons are overridable during M1 if the comps argue otherwise.
