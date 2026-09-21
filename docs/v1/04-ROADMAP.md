# Greek Essence v1 — Roadmap

Milestones → Phases → Tasks. Estimates are **minutes**, and they mean *agent wall-clock plus
your review of the result* — not pure generation time. For AI-agent work the review is usually
the larger half, and it is the part that doesn't parallelise.

`min` = it went right first time. `avg` = plan against this. `max` = one bad assumption or one
round of client feedback.

**On the IDs below:** `T-03.4` is a *planning reference into this document*, not a task ID.
Backlog.md assigns the real IDs (`GE-1`, `GE-2`, …) when T-00.10 seeds them. The planning ref
goes in the task description; the milestone is a native Backlog.md milestone; the phase is a
label. There is no native estimate field, so `est: 90/180/360 min` goes in the description too.

---

## Milestone map

| # | Milestone | Weeks | Exit criteria |
|---|---|---|---|
| **M0** | Reset & Foundation | 1 | New `main`, empty of v0, builds and deploys to a preview URL. Backlog seeded |
| **M1** | Design System & Shell | 1–2 | Client has said "yes, this is the look" on 2 real pages. Tokens + 8 components + 4 patterns extracted |
| **M2** | Content Platform | 2 | Client can log into Sanity and edit a destination that appears on a preview URL |
| **M3** | Public Site | 2–4 | All 9 templates live on preview with seed content |
| **M4** | Request Pipeline | 3–4 | A real submission on all 3 forms emails both parties and lands in the Sheet |
| **M5** | Launch Readiness | 5 | Live on the real domain, client trained, runbook handed over |
| **MC** | Client & Content *(parallel)* | 1–5 | Copy, photos, packages, prices, legal, form questions — all delivered |

M4 has **no code dependency on M1–M3** — the forms and Apps Script can be built any time from
week 1. Start it early and it stops being on the critical path.

---

## M0 — Reset & Foundation

### P0.1 — Repo reset & scaffold
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-00.1 | Salvage set, archive `main` → `archive/v0-preview`, orphan branch, force-push new `main` | 30 | 45 | 90 |
| T-00.2 | Scaffold Next 16 + TS strict + Tailwind 4 + shadcn/Base UI + pnpm | 45 | 90 | 180 |
| T-00.3 | Port design tokens from v0 `globals.css`, wire heading + body fonts | 30 | 60 | 120 |
| T-00.4 | Directory structure, path aliases, `lib/` skeleton | 20 | 40 | 80 |

### P0.2 — Tooling & CI
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-00.5 | eslint + prettier + commitlint + husky + lint-staged (thin: see 03-WORKFLOW §5) | 30 | 60 | 120 |
| T-00.6 | Vitest + Playwright config, one smoke test each | 40 | 75 | 150 |
| T-00.7 | GitHub Actions CI: typecheck, lint, test, build | 30 | 60 | 120 |
| T-00.8 | Vercel project, preview deploys, env var plumbing | 30 | 60 | 150 |

### P0.3 — Agent context & backlog
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-00.9 | Write `AGENTS.md` (<200 lines) + `CLAUDE.md` pointer | 45 | 90 | 180 |
| T-00.10 | `backlog init --task-prefix GE`, write `config.yml` (03-WORKFLOW §3), CLI-only (no MCP, see D-021b), seed all 6 milestones and 59 tasks via the CLI | 60 | 120 | 240 |
| T-00.11 | Install the 4 agent skills | 15 | 30 | 60 |

**M0: 375 / 730 / 1490 min**

---

## M1 — Design System & Shell

### P1.1 — Tokens & primitives
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-01.1 | Token validation: WCAG contrast audit, type scale, spacing rhythm, radii, motion | 45 | 90 | 180 |
| T-01.2 | `Button`, `Badge`, `Card`, `Prose` | 60 | 120 | 240 |
| T-01.3 | `Input`, `Select`, `Dialog`, `Breadcrumb`, `Gallery` | 60 | 120 | 240 |

### P1.2 — Shell
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-01.4 | Site header + navigation (desktop + mobile sheet) | 60 | 120 | 240 |
| T-01.5 | Site footer | 30 | 60 | 120 |
| T-01.6 | Root layout, metadata defaults, font loading, skip-link, landmarks | 30 | 60 | 120 |

### P1.3 — Direction comps and the sign-off gate
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-01.7 | Home comp at production quality, placeholder content | 120 | 240 | 480 |
| T-01.8 | Package detail comp at production quality | 90 | 180 | 360 |
| T-01.9 | Extract the 4 section patterns from those two pages | 60 | 120 | 240 |
| T-01.10 | **Client look-and-feel review + revision round** 🔴 | 120 | 240 | 600 |

**M1: 675 / 1350 / 2820 min** — T-01.10 is the widest band in the project. It is also the one
gate you cannot skip; everything downstream inherits its answer.

---

## M2 — Content Platform

### P2.1 — Sanity
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-02.1 | Sanity project on the **client's** account, embedded Studio route | 45 | 90 | 180 |
| T-02.2 | Schemas: `siteSettings`, `homePage`, `personalizedPage`, `page` | 60 | 120 | 240 |
| T-02.3 | Schemas: `destination`, `package` + publication-gate validation rules | 60 | 120 | 240 |
| T-02.4 | Studio desk structure, field grouping, preview config | 45 | 90 | 180 |

### P2.2 — Data layer
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-02.5 | Sanity client, GROQ queries, generated types | 60 | 120 | 240 |
| T-02.6 | Image pipeline: `@sanity/image-url` + `next/image`, LCP handling | 45 | 90 | 180 |
| T-02.7 | ISR revalidation webhook from Sanity | 30 | 60 | 120 |

### P2.3 — Seed
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-02.8 | Seed script: 3 destinations, 6 packages, all singletons, placeholder media | 60 | 120 | 240 |

**M2: 405 / 810 / 1620 min**

---

## M3 — Public Site

| ID | Task | Phase | min | avg | max |
|---|---|---|---|---|---|
| T-03.1 | `/` Home wired to Sanity | P3.1 | 60 | 120 | 240 |
| T-03.2 | `/destinations` list | P3.2 | 45 | 90 | 180 |
| T-03.3 | `/destinations/[slug]` detail + related packages | P3.2 | 60 | 120 | 240 |
| T-03.4 | `/packages` list + destination/type filters | P3.3 | 90 | 180 | 360 |
| T-03.5 | `/packages/[slug]` detail, gallery, includes, conditional price | P3.3 | 90 | 180 | 360 |
| T-03.6 | `/packages/[slug]/request` interstitial + `buildFormUrl()` prefill helper | P3.3 | 60 | 120 | 240 |
| T-03.7 | `/personalized` offer page | P3.4 | 60 | 120 | 240 |
| T-03.8 | `/about` + `/contact` | P3.4 | 45 | 90 | 180 |
| T-03.9 | `/thank-you` + `404` | P3.4 | 30 | 60 | 120 |
| T-03.10 | `/privacy` + `/terms` rendering | P3.5 | 30 | 60 | 120 |

**M3: 570 / 1140 / 2280 min**

---

## M4 — Request Pipeline *(no dependency on M1–M3 — start early)*

### P4.1 — Forms
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-04.1 | Build the 3 Google Forms on the client's account, theme them, link the Sheet | 90 | 180 | 360 |
| T-04.2 | Extract `entry.*` IDs, configure prefill + redirect to `/thank-you` | 45 | 90 | 180 |

### P4.2 — Email
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-04.3 | Resend account + sender domain verification + DNS records 🔴 | 30 | 60 | 240 |
| T-04.4 | Apps Script `onFormSubmit` → Resend customer acknowledgement | 90 | 180 | 360 |
| T-04.5 | Apps Script internal notification to the business inbox | 30 | 60 | 120 |
| T-04.6 | Email templates: customer ack (non-confirming wording) + internal summary | 60 | 120 | 240 |
| T-04.7 | Nightly CSV export of the response Sheet to Drive | 30 | 60 | 120 |

### P4.3 — Integration
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-04.8 | End-to-end submission test across all 3 forms, both emails, the Sheet row | 45 | 90 | 180 |

**M4: 420 / 840 / 1800 min**

---

## M5 — Launch Readiness

### P5.1 — SEO & analytics
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-05.1 | Per-page metadata from Sanity, OG images, `TouristTrip` JSON-LD | 60 | 120 | 240 |
| T-05.2 | `sitemap.xml`, `robots.txt`, canonicals | 30 | 60 | 120 |
| T-05.3 | Analytics (Plausible or Umami — cookie-banner-free) | 30 | 60 | 120 |

### P5.2 — Quality
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-05.4 | Accessibility audit (axe across 9 templates) + fixes | 90 | 180 | 360 |
| T-05.5 | Performance pass: LCP, image budgets, font loading | 60 | 120 | 240 |
| T-05.6 | Cross-browser + responsive QA | 60 | 120 | 240 |
| T-05.7 | Complete the Playwright smoke suite (9 templates + 3 CTA handoffs) | 60 | 120 | 240 |

### P5.3 — Production
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-05.8 | Domain, DNS, SSL 🔴 | 30 | 60 | 180 |
| T-05.9 | Production env, Sanity production dataset, first real deploy | 45 | 90 | 180 |
| T-05.10 | Final privacy + terms content, cookie decision 🔴 | 45 | 90 | 240 |

### P5.4 — Handover
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-05.11 | Client training: editing in Sanity, reading form responses | 60 | 120 | 240 |
| T-05.12 | Runbook: how to change X, what to do when Y, who to call | 45 | 90 | 180 |

**M5: 615 / 1230 / 2580 min**

---

## MC — Client & Content track *(runs weeks 1–5, in parallel)*

Not developer tasks, but they are on the critical path and belong in the backlog with owners
and dates. Track them or they will decide your launch date for you.

| ID | Item | Needed by |
|---|---|---|
| C-1 | Domain + DNS access | Week 1 |
| C-2 | Google account for Forms/Sheet; business inbox named | Week 1 |
| C-3 | Photography library, or a decision on licensed stock | Week 2 |
| C-4 | The launch package list: names, destinations, durations, inclusions | Week 2 |
| C-5 | Pricing decision — display with full qualification, or "enquire" | Week 2 |
| C-6 | The exact questions on each of the 3 forms | Week 2 |
| C-7 | Home / About / Personalized copy (drafted by you, approved by her) | Week 3 |
| C-8 | Destination and package copy | Week 3 |
| C-9 | Trust evidence: what may be claimed publicly, with proof | Week 3 |
| C-10 | Privacy + terms: template or legal review | Week 4 |

---

## Totals and what they mean

| | min | avg | max |
|---|---|---|---|
| **Total** | 3,060 min · **51 h** | 6,100 min · **102 h** | 12,590 min · **210 h** |

Against a 5-week window at a realistic 25–30 focused hours per week, you have **125–150 hours**
of capacity.

- **avg (102 h) fits**, with roughly 30% slack. That is the right amount — not generous.
- **max (210 h) does not fit.** Landing near max means a 7–8 week project.

The three things most likely to push you toward max, in order:
1. **T-01.10** — the client look-and-feel gate. One extra revision round is +4 hours and it
   blocks all of M3.
2. **C-3** — photography. There is no engineering answer to "she doesn't have images."
3. **C-7 / C-8** — copy. Draft it yourself and have her *approve* rather than *write*. This is
   the single highest-leverage thing you can do for the schedule, and the v0 decisions already
   concluded the same thing about how this client works.

### Suggested week shape
| Week | Focus |
|---|---|
| 1 | M0 complete · M1 P1.1–P1.2 started · M4 P4.1 in parallel · C-1, C-2 chased |
| 2 | M1 P1.3 comps → **client sign-off gate** · M2 in parallel · C-3, C-4, C-5, C-6 chased |
| 3 | M3 P3.1–P3.3 · M4 P4.2 · C-7, C-8 |
| 4 | M3 P3.4–P3.5 · M4 P4.3 · M5 P5.1 · C-9, C-10 |
| 5 | M5 P5.2–P5.4 · buffer · launch |

Week 5 being mostly quality and handover is deliberate. If you find yourself writing features
in week 5, cut scope rather than cut M5 — a site that launches slightly smaller beats one that
launches broken.
