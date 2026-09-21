# Greek Essence v1 — Roadmap

**Revised after discovery.** 7 milestones · 16 phases · 44 tasks · ~104h average · ~7 weeks.

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
| **M0** | Foundation | Product | 1 | 10.8 | New `main`, empty of v0, builds and deploys to a preview URL |
| **M1** | Design System & Shell | Product | 1–3 | 21.5 | Client has said "yes, this is the look" on two real pages |
| **M2** | Content Platform | Product | 3–4 | 9.8 | Client can edit a destination in Sanity and see it on preview |
| **M3** | Public Site | Product | 4–5 | 12.2 | All 7 templates live on preview with real content |
| **M4** | Request Pipeline | **Junior** | 1–3 | 13.5 | A real submission on all 3 forms emails both parties and lands in the Sheet |
| **M5** | Launch Readiness | Mixed | 6–7 | 19.0 | Live on the real domain, client trained, runbook handed over |
| **M6** | Content Production | Product | 2–6 | 17.5 | All copy approved, ~30 images curated and licence-logged |
| | **Total** | | **7** | **104.2** | |

---

## M0 — Foundation · Product lane

### P0.1 — Reset, scaffold, tooling
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-00.1 | Salvage set, archive `main` → `archive/v0-preview`, orphan branch, scaffold Next 16 + TS strict + Tailwind 4 + shadcn/Base UI, port v0 design tokens, directory structure and path aliases | 120 | 210 | 420 |
| T-00.2 | eslint + prettier + commitlint + husky + lint-staged (thin, per 03-WORKFLOW §5) · Vitest and Playwright configs with one smoke test each | 90 | 150 | 300 |
| T-00.3 | GitHub Actions CI (typecheck, lint, test, build) · Vercel project, preview deploys, env plumbing | 75 | 135 | 270 |

### P0.2 — Agent context and backlog
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-00.4 | `AGENTS.md` (<200 lines) + `CLAUDE.md` pointer · install the 4 skills · re-init Backlog.md in the new tree and seed this roadmap · backlog-only `post-commit` push hook · git-identity preflight | 90 | 150 | 300 |

---

## M1 — Design System & Shell · Product lane

### P1.1 — Foundations
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-01.1 | Token validation: WCAG contrast audit of the ported palette, type scale, spacing rhythm, radii, motion. No dark mode | 45 | 90 | 180 |
| T-01.2 | Components: `Button`, `Badge`, `Card`, `Prose`, `Breadcrumb`, `Gallery`, `Dialog`. (No `Input`/`Select` — filters are cut) | 120 | 240 | 480 |
| T-01.3 | Shell: header + nav (desktop and mobile), footer, root layout, metadata defaults, font loading, skip-link, landmarks | 90 | 180 | 360 |

### P1.2 — Direction and the sign-off gate
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-01.4 | Home comp at production quality, placeholder content | 120 | 240 | 480 |
| T-01.5 | Package detail comp at production quality | 90 | 180 | 360 |
| T-01.6 | Extract the 4 section patterns (`Hero`, `CardGrid`, `SplitFeature`, `CtaBand`) from those two pages | 60 | 120 | 240 |
| T-01.7 | **Client look-and-feel review + revision round** 🔴 | 120 | 240 | 600 |

T-01.7 has the widest band in the project and gates all of M3. Deploy to preview and send links,
never descriptions. Ask closed questions.

---

## M2 — Content Platform · Product lane

### P2.1 — Sanity
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-02.1 | Sanity project on the **client's** account, embedded Studio route, desk structure, field grouping, preview config | 75 | 135 | 270 |
| T-02.2 | Schemas: `siteSettings`, `homePage`, `personalizedPage`, `page`, `destination`, `package` + publication-gate validation rules | 90 | 180 | 360 |

### P2.2 — Data layer and seed
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-02.3 | Sanity client, GROQ queries, generated types, image pipeline (`@sanity/image-url` + `next/image`), ISR revalidation webhook | 105 | 180 | 360 |
| T-02.4 | Seed script: 2 destinations, 3 packages, all singletons, placeholder media | 45 | 90 | 180 |

---

## M3 — Public Site · Product lane

### P3.1 — Catalogue
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-03.1 | `/packages/[slug]` detail: gallery, highlights, includes/excludes, conditional price per D-006 | 90 | 150 | 300 |
| T-03.2 | `/destinations/[slug]` detail + packages in this destination | 60 | 105 | 210 |
| T-03.3 | `/packages/[slug]/request` interstitial + `buildFormUrl()` prefill helper | 60 | 105 | 210 |

### P3.2 — Brand and utility
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-03.4 | `/` Home wired to Sanity, carrying the package and destination cards directly | 75 | 120 | 240 |
| T-03.5 | `/personalized` offer page | 60 | 105 | 210 |
| T-03.6 | Shared content-page template → `/about`, `/contact`, `/privacy`, `/terms` | 60 | 105 | 210 |
| T-03.7 | `/thank-you` + `404` | 30 | 45 | 90 |

---

## M4 — Request Pipeline · **Junior lane** · no dependency on M1–M3

### P4.1 — Forms
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-04.1 | Build the 3 Google Forms on the client's account, theme them, link the response Sheet | 90 | 180 | 360 |
| T-04.2 | Extract `entry.*` IDs, configure prefill and redirect to `/thank-you` | 45 | 90 | 180 |

### P4.2 — Email and backup
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-04.3 | Resend account + sender-domain verification + DNS records 🔴 | 30 | 60 | 240 |
| T-04.4 | Apps Script `onFormSubmit`: Resend customer acknowledgement + `MailApp` internal notification | 120 | 210 | 420 |
| T-04.5 | Email templates: non-confirming wording, and the personalized ack stating a call is arranged by email (D-031) | 60 | 120 | 240 |
| T-04.6 | Nightly CSV export of the response Sheet to Drive | 30 | 60 | 120 |

### P4.3 — Integration
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-04.7 | End-to-end: all 3 forms, both emails, Sheet rows, thank-you redirect | 45 | 90 | 180 |

**Junior-lane watch:** T-04.1 needs the client's Google account and T-04.3 needs her domain and
DNS. Chase both in week 1 or this lane idles.

---

## M5 — Launch Readiness · Mixed

### P5.1 — SEO and analytics · **Junior lane**
| ID | Task | min | avg | max |
|---|---|---|---|---|
| T-05.1 | Per-page metadata from Sanity, OG images, `TouristTrip` JSON-LD on packages | 60 | 120 | 240 |
| T-05.2 | `sitemap.xml`, `robots.txt`, canonicals, analytics (Plausible or Umami — no cookie banner) | 45 | 90 | 180 |

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
| T-05.9 | Client training (editing in Sanity, reading form responses) + runbook | 105 | 180 | 360 |

---

## M6 — Content Production · Product lane · runs weeks 2–6

Real work, not a client checkbox (D-035). Agents draft → operator edits → client approves.
Each task's `max` assumes two approval rounds.

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
| **Total** | 3,345 min · **55.8 h** | 6,255 min · **104.2 h** | 12,810 min · **213.5 h** |

At ~15h/week combined (operator 8–12h + junior net of review): **~7 weeks at avg, ~4 weeks at
min, ~14 weeks at max.** The spread is wide because four tasks are client-gated.

### Suggested week shape

| Week | Product lane | Junior lane |
|---|---|---|
| 1 | M0 complete | M4 P4.1 — chase Google account + domain |
| 2 | M1 P1.1 · M6 T-06.1 photos | M4 P4.2 |
| 3 | M1 P1.2 → **client sign-off gate** · M6 copy starts | M4 P4.3 → M5 P5.1 |
| 4 | M2 complete · M6 copy | M5 P5.1 complete · support |
| 5 | M3 complete · M6 copy approvals | QA support |
| 6 | M5 P5.2 · content final | — |
| 7 | M5 P5.3 · buffer · launch | — |

### The four things most likely to push toward max
1. **T-01.7** — the client look-and-feel gate. One extra round is +4h and blocks all of M3.
2. **M6 copy approvals** — five tasks, each with a client round trip. The long pole nobody plans for.
3. **T-04.1 / T-04.3** — the junior lane's client-gated start. Chase in week 1.
4. **D-030** — if the client picks "fixed itinerary, fixed price", M2 and M6 both grow and legal
   review joins the critical path.

Week 7 is quality, handover and buffer on purpose. If you are writing features in week 7, cut
scope rather than cutting M5.
