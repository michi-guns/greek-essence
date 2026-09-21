# Greek Essence v1 — Roadmap

**Revised after discovery and the stack decisions.** 7 milestones · 17 phases · 62 tasks ·
~133.2h average · ~8.5 weeks.
Architecture: [06-ARCHITECTURE.md](06-ARCHITECTURE.md). Stack rationale: [05-STACK.md](05-STACK.md).

Estimates are **minutes**, meaning *agent wall-clock plus the reviewing human's time*. For
AI-agent work the review is usually the larger half and it does not parallelise.
`min` = went right first time · `avg` = plan against this · `max` = one bad assumption or one
round of client feedback.

**On the IDs:** `T-03.4` is a planning reference into this document, not a task ID. Backlog.md
assigns real IDs (`GE-001`…) at seeding. Milestones are native milestones, **phases are parent
tasks** (D-028), and `est: 90/150/300` goes in the task description since there is no native
estimate field.

---

## Lanes

Two developers, two lanes, no shared phases (D-026).

| Lane | Owner | Milestones |
|---|---|---|
| **Product** | Operator | M0, M1, M2, M3, M5 P5.2–P5.3, M6 |
| **Pipeline** | Junior dev | M4, M5 P5.1 |

Both lanes run concurrently from week 1. This is why D-023's "one phase branch at a time" rule
is relaxed — two branches open by design, disjoint directories, one owning lane per phase.

---

## Milestone map

| # | Milestone | Lane | Weeks | avg h | Exit criteria |
|---|---|---|---|---|---|
| **M0** | Foundation | Product | 1 | 13.3 | New `main`, empty of v0, builds and deploys to a preview URL |
| **M1** | Design System & Shell | Product | 1–3 | 33.5 | Client has said "yes, this is the look" on two real pages |
| **M2** | Content Platform | Product | 3–4 | 16.0 | Client can edit a destination in the Studio and watch the page update live beside her |
| **M3** | Public Site | Product | 4–5 | 16.2 | All 7 templates live on preview with real content |
| **M4** | Request Pipeline | **Junior** | 1–3 | 16.2 | A real submission on all 3 forms emails both parties and lands in the Sheet |
| **M5** | Launch Readiness | Mixed | 6–7 | 19.0 | Live on the real domain, client trained, runbook handed over |
| **M6** | Content Production | Product | 2–6 | 17.5 | All copy approved, ~30 images curated and licence-logged |
| | **Total** | | **8** | **131.8** | |

---

## M0 — Foundation · Product lane

### P0.1 — Stack validation, reset, scaffold
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-00.1 | **Stack verification spike** (throwaway): Next 16 on **Netlify** + shadcn/Base UI Dialog + Sanity image loader + Draft Mode round-trip. Confirm S-004 or fall back to Radix and record it | 75 | 135 | 270 |
| T-00.2 | Salvage set, archive `main` → `archive/v0-preview`, orphan branch, real scaffold, port v0 design tokens, **directory structure per 06-ARCHITECTURE §3**, path aliases, `lib/env.ts` Zod validation. **No i18n** (D-005) | 105 | 195 | 390 |
| T-00.3 | eslint + prettier + commitlint + husky + lint-staged (thin) · **`no-restricted-imports` zones encoding the 06-ARCHITECTURE §4 dependency rules** · Vitest and Playwright configs with one smoke test each | 90 | 165 | 330 |
| T-00.4 | GitHub Actions CI · **Netlify** site with **auto-deploy of `main` to production disabled** (A-003), deploy previews per branch, credit alerts at 50/75%, security headers in `next.config`, env plumbing (server-only Sanity token) | 75 | 150 | 300 |

### P0.2 — Agent context and backlog
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-00.5 | `AGENTS.md` (<200 lines, incl. the read-`node_modules`-docs rule) + `CLAUDE.md` · agent skills: 4 project + Netlify's 4 (A-005) + `sanity-io/agent-toolkit` (A-006) · **`.claude/settings.json` permission allow/deny list and `.local/` scaffold (D-050, D-051)** · re-init Backlog.md in the new tree and seed · backlog-only `post-commit` push hook · git-identity preflight | 90 | 150 | 300 |

## M1 — Design System & Shell · Product lane

**Method: direction before system, diverge before converge.** Explore several genuinely
different visual answers cheaply, pick one, *then* extract the system from what you picked.
Systems designed in the abstract do not fit; systems extracted from a chosen design do.

### P1.1 — Direction
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-01.1 | Visual research: 8–12 annotated references from editorial / hospitality / boutique-hotel sites (not travel-agency templates). Extract *specifically* what works — type pairing, image treatment, whitespace ratio, colour restraint → written art-direction brief | 60 | 120 | 240 |
| T-01.2 | Design decisions record: component architecture per 05-STACK, styling conventions (CVA variant vs utility vs new component), breakpoints, fluid type via `clamp`, icon usage, motion policy, image aspect ratios and Sanity hotspot usage | 60 | 105 | 210 |
| T-01.3 | **Three divergent first-fold directions** — same content, deliberately different (type-led / image-led / editorial-grid), built as real code, screenshotted side by side | 150 | 270 | 540 |
| T-01.4 | 🔴 Pick a direction (operator, optionally with client input) | 30 | 60 | 120 |

### P1.2 — Foundations, extracted from the winner
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-01.5 | Token system: contrast-audit the ported palette, fluid type scale, spacing, radii, elevation, motion tokens. No dark mode | 60 | 105 | 210 |
| T-01.6 | Typography implementation: Fraunces + Inter self-hosted via Fontsource, `size-adjust` fallback metrics, Prose styles | 45 | 90 | 180 |
| T-01.7 | Primitives: `Button`, `Badge`, `Card`, `Breadcrumb` | 75 | 135 | 270 |
| T-01.8 | Composites: `Gallery`/lightbox, `Dialog`, Portable Text renderer | 75 | 135 | 270 |
| T-01.9 | Shell: header + nav (desktop and mobile), footer, root layout, metadata defaults, skip-link, landmarks | 90 | 180 | 360 |

### P1.3 — Comps and sign-off
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-01.10 | Home comp at production quality in the chosen direction | 105 | 195 | 390 |
| T-01.11 | Package detail comp at production quality | 90 | 165 | 330 |
| T-01.12 | Extract the 4 section patterns (`Hero`, `CardGrid`, `SplitFeature`, `CtaBand`) from those two pages | 60 | 120 | 240 |
| T-01.13 | **Content-shape stress test**: long headline, short body, missing image, no price, longest package name, 2 cards vs 3. Where designs die | 45 | 90 | 180 |
| T-01.14 | 🔴 **Client look-and-feel review + revision round** | 120 | 240 | 600 |

T-01.14 has the widest band in the project and gates all of M3. Deploy to preview and send
links, never descriptions. Ask closed questions.

## M2 — Content Platform · Product lane

### P2.1 — Sanity
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-02.1 | Sanity project on the **client's** account, Studio embedded at `/studio`, desk structure organised as Packages/Destinations/Pages/Settings, singletons locked (06-ARCH §13) | 75 | 135 | 270 |
| T-02.2 | Schemas: all six types with `defineType`/`defineField` · field-group tabs · plain-language descriptions · list previews · publication-gate validation with readable messages · required alt text (06-ARCH §13). **No localization** (D-005 / A-002) | 105 | 195 | 390 |

### P2.2 — Data layer, seed and preview
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-02.3 | Sanity client (`server-only`), GROQ queries, `sanity typegen`, **Zod schemas + `map.ts` domain-DTO mappers (D-040)**, custom image loader, webhook → `revalidateTag` | 120 | 210 | 420 |
| T-02.4 | Seed script: 2 destinations, 3 packages, all singletons, placeholder media | 45 | 90 | 180 |
| T-02.5 | **Draft Mode + Sanity Presentation tool**: enable/disable route handlers, draft-aware fetches, click-to-edit overlays, live preview in the Studio | 75 | 135 | 270 |
| T-02.7 | **Portable Text**: restricted editor config (06-ARCH §13) + serializers mapping every block type to design-system components, incl. embedded images through the Sanity loader | 60 | 120 | 240 |
| T-02.6 | **Draft-leak test**: Playwright assertion that an unauthenticated request to a page with unpublished changes returns the published version. Server-only token verified absent from the client bundle | 45 | 75 | 150 |

---

## M3 — Public Site · Product lane

### P3.1 — Catalogue
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-03.1 | `/packages/[slug]` page structure + Sanity data wiring | 75 | 120 | 240 |
| T-03.2 | Package media: gallery, hotspot-aware crops, lightbox, LCP handling | 60 | 105 | 210 |
| T-03.3 | Price / includes / excludes blocks. The D-006 qualification rule is enforced in `map.ts` (D-040), so this renders `price` or nothing — plus the unit test for the mapper | 45 | 90 | 180 |
| T-03.4 | `/destinations/[slug]` detail + packages in this destination | 60 | 105 | 210 |
| T-03.5 | `/packages/[slug]/request` interstitial + `buildFormUrl()` prefill helper | 60 | 105 | 210 |

### P3.2 — Brand and utility
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-03.6 | `/` Home wired to Sanity, carrying package and destination cards directly | 75 | 120 | 240 |
| T-03.7 | `/personalized` offer page | 60 | 105 | 210 |
| T-03.8 | Shared content-page template → `/about`, `/contact`, `/privacy`, `/terms` | 60 | 105 | 210 |
| T-03.9 | `/thank-you` + `404` | 30 | 45 | 90 |
| T-03.10 | **Unpublished-package page** (v0 D-005: former URL shows "no longer listed" with no stale claims, prices or media, and routes back to the catalogue) + internal linking and breadcrumb pass | 45 | 75 | 150 |

## M4 — Request Pipeline · **Junior lane** · no dependency on M1–M3

**Contracts first.** T-04.1 defines the interface between the site, Forms, the Sheet and the
emails. Every other task in this milestone implements against it.

### P4.1 — Contract and forms
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-04.0 | **`clasp` setup** (A-009): Apps Script project linked to the repo as TypeScript, push/pull workflow, `.clasp.json` and credentials handling documented | 45 | 90 | 180 |
| T-04.1 | **Intake contract spec** — one document. Per form: field list, types, required/optional, Sheet column mapping, `entry.*` ID map, prefill params, redirect params, and the validation each field carries | 60 | 120 | 240 |
| T-04.2 | Build the 3 Google Forms on the client's account to that spec, theme them, link the response Sheet | 75 | 150 | 300 |
| T-04.3 | Prefill + redirect to `/thank-you`, verified field-by-field against the spec | 45 | 90 | 180 |

### P4.2 — Email
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-04.4 | 🔴 Resend account + sender-domain verification + DNS records | 30 | 60 | 240 |
| T-04.5 | **Email content contract** — template variables, non-confirming wording, the personalized ack stating a call is arranged by email (D-031), internal notification format | 45 | 90 | 180 |
| T-04.6 | Apps Script `onFormSubmit` → Resend customer acknowledgement via `UrlFetchApp` | 75 | 135 | 270 |
| T-04.7 | Apps Script internal notification via `MailApp` to the business inbox | 30 | 60 | 120 |
| T-04.8 | **Failure and idempotency**: `onFormSubmit` double-fire guard (a processed-row marker), Resend error handling, operator alert on send failure. Without this the client gets duplicate enquiries and the customer gets two acknowledgements | 60 | 120 | 240 |

### P4.3 — Ops and verification
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-04.9 | Nightly CSV export of the response Sheet to Drive | 30 | 60 | 120 |
| T-04.10 | End-to-end verification against the contract spec: all 3 forms, both emails, Sheet rows, redirect | 45 | 90 | 180 |

**Junior-lane watch:** T-04.2 needs the client's Google account and T-04.4 needs her domain and
DNS. Chase both in week 1 or this lane idles.

## M5 — Launch Readiness · Mixed

### P5.1 — SEO and analytics · **Junior lane**
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-05.1 | Per-page metadata from Sanity, OG images, `TouristTrip` JSON-LD on packages | 60 | 120 | 240 |
| T-05.2 | `sitemap.xml`, `robots.txt`, canonicals, analytics (**Umami Cloud**, S-007 — cookieless, no banner; confirm the current free-tier limits and fall back to Cloudflare Web Analytics if they disappoint) | 45 | 90 | 180 |

### P5.2 — Quality · Product lane
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-05.3 | Accessibility audit (axe across the 7 templates) + fixes | 90 | 165 | 330 |
| T-05.4 | Performance pass: LCP, image budgets, font loading | 60 | 120 | 240 |
| T-05.5 | Cross-browser + responsive QA | 60 | 105 | 210 |
| T-05.6 | Playwright smoke suite: 7 templates + 3 CTA handoffs | 60 | 120 | 240 |

### P5.3 — Production and handover · Product lane
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-05.7 | Domain, DNS, SSL, production env, Sanity production dataset, first real deploy 🔴 | 75 | 150 | 300 |
| T-05.8 | Final privacy + terms content, cookie decision 🔴 | 45 | 90 | 240 |
| T-05.9 | Client training (editing in Sanity, reading form responses) + runbook incl. account-ownership table and the Netlify credit budget (A-003) | 105 | 180 | 360 |

---

## M6 — Content Production · Product lane · runs weeks 2–6

Real work, not a client checkbox (D-035). Agents draft **directly into Sanity as drafts**;
the client reviews in Presentation on the real page and publishes (A-008). Each task's `max`
assumes two approval rounds.

**Dependency:** every copy task needs M2 P2.1+P2.2+T-02.5 done. Photo curation does not.

### P6.1 — Photography
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-06.1 | Curate ~30 free-stock images per D-034, build the source/author/licence log, process and upload | 90 | 180 | 360 |

### P6.2 — Copy
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-06.2 | Home + `/personalized` copy: draft → edit → client approval | 120 | 240 | 480 |
| T-06.3 | Destination copy (1–2): draft → edit → approval | 90 | 165 | 330 |
| T-06.4 | Package copy (2–3): draft → edit → approval | 120 | 210 | 420 |
| T-06.5 | About, contact and trust-block copy — approved claims only, per v0 trust rules | 75 | 135 | 270 |
| T-06.6 | Form questions, email copy, thank-you copy | 60 | 120 | 240 |

---

## Totals

| | min | avg | max |
|---|---|---|---|
| **Total** | 4,320 min · **72.0 h** | 7,905 min · **131.8 h** | 16,140 min · **269.0 h** |

At ~15h/week combined (operator 8–12h + junior net of review): **~8.5 weeks at avg, ~4.5 weeks at
min, ~17.5 weeks at max.** The spread is wide because four tasks are client-gated.

### Suggested week shape

| Week | Product lane | Junior lane |
|---|---|---|
| 1 | M0 (stack spike → reset → scaffold → CI) | M4 P4.1 contract + forms — chase Google account + domain |
| 2 | M1 P1.1 direction → **direction pick** · M6 photos (T-06.1) | M4 P4.0 clasp → P4.1 |
| 3 | M1 P1.2 foundations · **M2 P2.1–P2.2 brought forward** (unblocks copy) | M4 P4.2 email |
| 4 | M1 P1.3 comps → **client sign-off gate** · T-02.5 Presentation · M6 copy starts in Sanity | M4 P4.3 → M5 P5.1 |
| 5 | M2 complete · M6 copy approvals | M5 P5.1 complete |
| 6 | M3 complete · content final | QA support |
| 7 | M5 P5.2 quality | — |
| 8 | M5 P5.3 · buffer · launch | — |

### The four things most likely to push toward max
1. **T-01.14** — the client look-and-feel gate. One extra round is +4h and blocks all of M3.
2. **M6 copy approvals** — five tasks, each with a client round trip. The long pole nobody plans for.
3. **T-04.2 / T-04.4** — the junior lane's client-gated start. Chase in week 1.
4. **D-030** — if the client picks "fixed itinerary, fixed price", M2 and M6 both grow and legal
   review joins the critical path.

Weeks 7–8 are quality, handover and buffer on purpose. If you are writing features in week 8,
cut scope rather than cutting M5.

**If 8 weeks is too long,** the cheapest week to claw back: drop T-01.3 from three directions to
two (−2h), cut T-01.13 the content-shape stress test (−1.5h), and drop T-03.2's hotspot crops
for plain aspect-ratio images (−1h). I would keep all three.
