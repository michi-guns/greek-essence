# Docs Management and Next.js Architecture Plan (Grilling-Locked)

**Status:** working plan for operator acceptance (WU-44)  
**Authority:** accepted decisions under `docs/grilling/` only  
**Inspiration only:** draft PR #50 / branch `docs/migration-v4` candidate tree and evaluation report  
**Not authority:** candidate labels such as `status: active` or ADR `Accepted` inside `docs/new-proposed-docs/`

This plan defines how Greek Essence manages documentation and grows the Next.js
codebase for the Public Preview. It does not install dependencies, move runtime
paths by itself, or reopen product grilling.

---

## 1. Purpose

1. Make docs authority obvious for humans and agents.
2. Fix the Next.js source layout and dependency direction so Neon/Drizzle,
   Sanity, and the first vertical slices land in the right seats.
3. Keep delivery proportional: vertical slices, no empty onion scaffolds, no
   post-preview commercial domain imported from external references.

---

## 2. Authority order

When anything conflicts:

1. Current operator instructions
2. Root `AGENTS.md` and the active work-item `NEXT.md` (workflow/continuation)
3. Accepted `docs/grilling/**/DECISIONS.md` and related accepted registers
4. `docs/grilling/CLASSIFICATION.md` (routing locked inputs; does not change meaning)
5. This plan and other `docs/working/` plans (implementation direction only)
6. Canonical promoted docs after an explicit promotion step
7. Code and draft PRs (evidence of current state, not product authority)

**Never authority for current GE product/runtime:**

- `docs/archive/**`
- `docs/new-proposed-docs/**` (candidate / evaluation)
- External travel-agency reference systems (method inspiration only)
- Prototype JSON/content behavior once replacement authority exists

---

## 3. What we take from migration-v4 (shape only)

| Keep as inspiration                                             | Reject as GE authority                                                                                                              |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Thin docs index + explicit authority categories                 | Candidate commercial modules: customers, travelers, quotes, bookings, payments, suppliers, documents as first-class preview modules |
| ADR / assumption / runbook patterns (later, when earned)        | Candidate ADRs marked Accepted without GE grilling                                                                                  |
| Domain-centered modules + inward dependency direction           | Mandatory empty `domain/application/infrastructure/presentation` folders                                                            |
| Vertical-slice delivery                                         | Big-bang `features/showcase` source move or wholesale docs replace                                                                  |
| Next.js as delivery framework; business rules out of components | Server Action auth/account assumptions not in preview                                                                               |
| `shared/` kept small                                            | Treating candidate runbooks as live ops procedure                                                                                   |

The evaluation report’s **Option C** direction is adopted in GE terms:

- preserve compatible governance and placement principles;
- do not execute obsolete prototype-only path moves;
- transition docs and code **incrementally** from accepted grilling;
- keep PR #50 as evaluation history until superseded by this plan and follow-on slices.

---

## 4. Documentation management

### 4.1 Tiers

| Tier                          | Location                                                                                      | Role                                              | May authorize implementation?                  |
| ----------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------- | ---------------------------------------------- |
| A. Workflow                   | Root `AGENTS.md`, `docs/GIT_WORKFLOW.md`, `docs/QUALITY_GATES.md`, `docs/AGENT_TOOLING.md`, … | How we work                                       | Workflow only                                  |
| B. Product / foundation truth | `docs/grilling/**` accepted decisions and registers                                           | What the service may be and do                    | Yes, when a bounded WU says so                 |
| C. Working plans and maps     | `docs/working/**`                                                                             | Selection, handoffs, migration plans, inventories | Direction only until promoted or cited by a WU |
| D. Candidate / evaluation     | PR branches, `docs/new-proposed-docs/` if retained                                            | Compare options                                   | No                                             |
| E. Archive                    | `docs/archive/**`                                                                             | Historical                                        | No                                             |

### 4.2 Management rules

1. **One writer per fact class** — product truth in grilling; task lifecycle in Trello; soft pull order in `docs/working/work-program/SEQUENCE.md`; multi-session handoff in root `NEXT.md` + work-item `NEXT.md`.
2. **Promote deliberately** — do not silently move candidate docs into tier A/B.
3. **Prefer links over duplication** — working plans cite DECISIONS; they do not rewrite them.
4. **Bilingual product claims** stay under grilling / future content ops authority; eng docs stay English unless a WU says otherwise.
5. **No secrets** in any tier.

### 4.3 Target docs navigation (incremental)

Keep `docs/README.md` as the human/agent entry map. Evolve it in small PRs:

1. **Now (with this plan):** link this plan from `docs/README.md` and the work-program map when refreshed.
2. **Next docs-transition slice (follow-on WU or later commit on a docs WU):**
   - clearer “Authority” section (tiers above);
   - “Architecture & platform” subsection pointing at foundation-design DECISIONS + this plan;
   - demote or clearly label Layer-2 inventory/migration files as historical evaluation once this plan is accepted;
   - do **not** merge raw `new-proposed-docs/` into `docs/`.
3. **Later, only if pain appears:** thin ADR folder for _GE-accepted_ engineering decisions that are not product grilling (e.g. exact folder aliases)—still subordinate to grilling.

### 4.4 Fate of PR #50 materials

After this plan is accepted:

- Close or mark PR #50 superseded (evaluation complete; GE plan is `docs/working/DOCS_AND_NEXTJS_ARCHITECTURE_PLAN.md`).
- Keep git history; do not require importing the candidate tree into `main`.
- Optional later: archive a short pointer note under `docs/working/` if agents keep rediscovering PR #50.

---

## 5. Next.js architecture (locked method + initial seats)

### 5.1 Locked method (already grilled)

From Application Architecture D-001 and related foundation decisions:

- One deployable Next.js App Router app (modular monolith).
- Organize primarily by **accepted business capability**, not by global technical layers.
- Deliver **complete vertical slices**.
- Inward dependencies: presentation → application behavior → domain rules/contracts where justified.
- Infrastructure adapters (Sanity, Drizzle/Neon, mail) stay server-only; no provider SDKs or secrets in the browser.
- Server Components default; Client Components only for real browser needs.
- Server Actions for visitor forms; Route Handlers for webhooks/machine callers.
- Explicit journey workflows (Consultation, Booking Request, General Contact)—no universal `submitRequest` god-module.
- **Do not** create empty architectural folders, generic repositories, or DI frameworks for symmetry.
- Import **none** of the external reference’s Customers/Travelers/Quotes/confirmed Bookings/Payments workflows.

### 5.2 Preview capability map (code ownership)

Grow modules only when a slice needs them:

| Capability (preview)                            | Owns                                                                                       | First real code arrives with                                    |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| `catalog` (name flexible)                       | Destination/Experience discovery reads, public catalogue view models                       | Catalogue / Sanity read slices                                  |
| `brand` or public pages                         | Home, About, shared brand presentation                                                     | Public brand page slices                                        |
| `consultation-request`                          | Consultation journey workflow + presentation adapter                                       | Consultation implementation slice                               |
| `booking-request`                               | Booking Request journey + Sanity eligibility + snapshot handoff                            | Booking Request slice                                           |
| `general-contact`                               | General contact journey                                                                    | Contact slice                                                   |
| `request-processing` (shared only where earned) | Shared Request envelope meaning, exact-retry, correction verify, mail intents coordination | When two journeys would otherwise duplicate accepted invariants |
| `content-operations` (eng support)              | Preview route, webhook revalidation hooks (as authorized)                                  | Content ops / webhook slices                                    |
| Platform seats (not business modules)           | `sanity/`, `db/` (or equivalent), mail adapter                                             | WU-45 / WU-46 connection proofs                                 |

**Explicit non-modules for Public Preview:** payments, supplier automation, staff CRM/dashboard, customer accounts, live availability engine, confirmed online booking lifecycle.

### 5.3 Responsibility names vs folders

`domain`, `application`, `infrastructure`, and `presentation` are **responsibility labels**.  
They become directories **only inside a capability that already has real code** needing that split.

Default for early slices:

```text
features/<capability>/
  // start flat or with 1–2 files
  // split inward only when a file owns a distinct rule or adapter
```

Avoid creating four empty layers per feature on day one.

### 5.4 Recommended initial repository seats

Compatible with current root Next.js layout; move only when a WU implements it.

```text
app/                         # App Router entry: locales, pages, route handlers
  [locale]/
features/                    # business capabilities (vertical slices)
  <capability>/
shared/                      # small: locale helpers, cn, truly shared Request types later
content/                     # transitional local JSON until Sanity cutover (existing)
lib/                         # shrink over time; do not grow as a second architecture
sanity/                      # Sanity config, schemas (minimal→grown), server client
db/                          # Drizzle client, schema, migrations (minimal→grown)
messages/                    # next-intl messages (existing)
docs/                        # documentation (this tree)
```

Notes:

- Prefer `features/` over `modules/` naming in GE to match “feature-first” language in AA; either name is fine if one is chosen and used consistently—**choose `features/`**.
- `db/` and `sanity/` are platform seats, not a place for journey business rules.
- Do not introduce `src/` wrapper unless a later WU proves root clutter requires it; current root App Router stays unless migration cost is justified.
- Existing `components/`, `lib/content.ts`, and JSON content remain valid **until** a slice replaces them; no forced big-bang delete.

### 5.5 Dependency rules (enforce proportionally)

Allowed:

```text
app (presentation adapters) → features/<capability> application API
features application → feature domain/contracts (if present)
features infrastructure adapters → feature contracts + db/sanity/mail seats
shared ← used by features only for stable shared meaning
```

Forbidden:

- domain/application importing Next.js, React, Drizzle, Sanity SDK, GROQ, or HTTP types
- Client Components importing server-only db/sanity/mail
- pages/actions containing acceptance transaction orchestration
- `shared/` becoming a junk drawer

Enforcement: code review + focused tests/lint only where violation is costly. No generic architecture police framework.

### 5.6 Platform connection seats (WU-45 / WU-46)

| WU                   | Lands in                                                        | Proof                                      | Must not do                                                          |
| -------------------- | --------------------------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------- |
| WU-45 Neon + Drizzle | `db/` + env placeholders + server-only client                   | Non-mutating connect                       | App request schema, migrations applied as product, journey code      |
| WU-46 Sanity         | `sanity/` + env placeholders + server client and/or Studio boot | Read-only or Studio proof                  | Full catalogue schema dump, content migration, private PII in Sanity |
| WU-47 Vertical proof | one `features/*` slice + thin `app` adapter                     | Synthetic Sanity read + synthetic db touch | Real enquiries, privacy launch, empty full module tree               |

Mail adapters appear only when a request-processing slice needs them (foundation already chose provider-neutral gateway).

---

## 6. Phased delivery (after this plan is accepted)

| Phase | Work                                  | Primary WU                                              | Exit                                                      |
| ----- | ------------------------------------- | ------------------------------------------------------- | --------------------------------------------------------- |
| 0     | Accept this plan                      | WU-44                                                   | Plan on `main` via PR; operator acceptance                |
| 1     | Docs nav/authority labels (small)     | follow-on docs slice or residual on WU-44 if still open | `docs/README.md` reflects tiers; PR #50 closed/superseded |
| 2     | Neon + Drizzle connection             | WU-45                                                   | Packages + connect proof in `db/`                         |
| 3     | Sanity connection                     | WU-46                                                   | Packages + connect proof in `sanity/`                     |
| 4     | Minimal dual-platform synthetic slice | WU-47 (blocked by 45+46)                                | One feature path proves both seats                        |
| 5+    | Real catalogue/brand/request slices   | future WUs                                              | Replace JSON content and add journeys per grilling        |

Soft order may run phase 1 parallel to 2/3. Hard order: 4 after 2 and 3.

---

## 7. Relationship to parent program

Parent: **Bootstrap Public Preview platform foundations (WU-43)**

```text
WU-43
├── WU-44 this plan (docs + architecture direction)
├── WU-45 Neon + Drizzle connect
├── WU-46 Sanity connect
└── WU-47 synthetic vertical proof  ← blocked_by WU-45, WU-46
```

---

## 8. Acceptance checklist (plan quality)

- [x] Grilling is sole product/architecture authority
- [x] migration-v4 limited to inspiration; rejections listed
- [x] Docs tiers and management rules explicit
- [x] Next.js method matches AA; initial seats named
- [x] Preview capabilities listed; commercial candidate modules excluded
- [x] WU-45/46/47 handoffs explicit
- [ ] Operator accepts this plan (required before Done on WU-44)

---

## 9. Operator decision

Accept, correct, or reject this plan.

If accepted, next engineering pull is **WU-45** or **WU-46** (connection proofs into the seats above), with optional small docs-nav PR as phase 1.
