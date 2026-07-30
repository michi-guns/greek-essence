# Expanded Client Requirements Intake

## Status

Active intake. This document captures source material and confirmed outcomes;
it must not turn incomplete client statements into implementation decisions.

## Intake Rules

- Record each requirement with its source, confidence, and approval state.
- Separate requested outcomes from suggested technologies.
- Identify affected users, content, data, workflows, integrations, and
  operational owners.
- Mark conflicts with the archived PRD, prototype specification, technical
  design, and design system explicitly, without granting them current
  authority.
- Do not select architecture, migrate content, or change runtime paths until the
  relevant requirement set is sufficiently complete and approved.
- Do not place secrets, credentials, personal data, or raw client records here.

## Source Register

| ID | Source | Date | Authority | Notes |
| --- | --- | --- | --- | --- |
| SRC-001 | Operator report of materially expanded client requirements | 2026-07-28 | Direct operator instruction | Mentions CMS, Drizzle ORM, Supabase backend, and further requirements not yet captured |
| SRC-002 | `sources/07_PROJECT_ROADMAP.md` | 2026-07-29 | Operator-authored, agent-assisted working draft; client-unreviewed | Revised-v2 release roadmap, milestones, scope, and delivery principles |
| SRC-003 | `sources/06_DOMAIN_ARCHITECTURE.md` | 2026-07-29 | Operator-authored, agent-assisted working draft; client-unreviewed | Candidate domain ownership, entities, relationships, states, workflows, and invariants |
| SRC-004 | `sources/NEXTJS_LAYER_2_MIGRATION.md` | 2026-07-29 | Operator-authored, agent-assisted working draft; client-unreviewed | Candidate feature-based code-organization rules |
| SRC-005 | Operator confirmation in active session | 2026-07-29 | Direct operator instruction | End-of-August preview will be publicly accessible and is expected to receive real visitors |

## Requirement Capture Template

Use one record per independently testable need.

| Field | Value |
| --- | --- |
| Requirement ID | `REQ-###` |
| Source | `SRC-###` plus precise section, message, or artifact |
| Desired outcome | What the client or user must be able to accomplish |
| Actors and roles | Public visitor, client, editor, administrator, operator, integration, or other |
| Data involved | Entities, ownership, sensitivity, retention, and lifecycle |
| Content involved | Types, locales, workflow, preview, publishing, media, and SEO |
| Operational workflow | Who acts, in what order, with what failure/recovery behavior |
| Constraints | Legal, privacy, security, accessibility, performance, hosting, budget, or deadline |
| Suggested technology | Client suggestion, preference, or mandate; keep separate from the outcome |
| Conflicts | Earlier requirements or implementation assumptions affected |
| Acceptance evidence | Observable condition that proves the requirement is met |
| Status | Reported, clarified, approved, deferred, or rejected |

## Coverage Checklist

Capture the client material across these areas before architecture selection:

- product goals, launch scope, audiences, and user journeys;
- public routes, authenticated areas, roles, and permissions;
- CMS content types, editorial roles, draft/review/publish flow, preview,
  localization, media, SEO, and revision history;
- persistent domain entities, relationships, ownership, lifecycle, import, and
  retention;
- managed PostgreSQL responsibilities: Neon projects, branches, databases,
  roles, connections, provider recovery, exports, and environments;
- Drizzle responsibilities: schema ownership, migrations, query boundary,
  transactions, generated database-facing validation/types, handwritten Zod v4
  business validation, and interaction with Neon connections;
- forms, lead/customer workflows, notifications, assignment, auditability, and
  failure recovery;
- external integrations, webhooks, email, scheduling, analytics, search, and
  payments if requested;
- privacy, consent, security, data residency, legal, accessibility, and abuse
  controls;
- rendering, caching, freshness, preview, performance, availability, and SEO;
- deployment environments, secrets, observability, backups, restoration, and
  operational ownership;
- migration of prototype content/assets and explicit non-goals.

## Current Confirmed Direction

- The preview release is production-facing: it will be public and accept real
  visitor traffic and enquiries.
- The earlier static-first, local-JSON-only architecture is no longer an
  adequate basis for the expanded product.
- Sanity, Neon PostgreSQL, Drizzle, and the application/backend boundaries are
  locked directions whose exact responsibilities and integration model must be
  resolved through Foundation Design before feature/module boundaries are
  promoted.
- Use the latest Drizzle release candidate available when implementation begins
  with its first-party Zod integration and the latest Zod v4; pin exact resolved
  versions during implementation.

## Ingested Batches

- [Batch 01 synthesis](REQUIREMENTS_BATCH_01.md) — provisional internal planning
  baseline with 27 reported requirements, candidate domain ownership,
  former-prototype scope classification, and 15 conflicts or clarification
  needs derived from SRC-002 through SRC-004.
- [Public preview release validation](PREVIEW_RELEASE_VALIDATION.md) — operator-
  confirmed release classification, minimum client questions, internally owned
  technical decisions, and the production-facing Phase 1 gate.

## Intake Needed

Use the concise client-validation checklist to confirm visible and operational
scope while resolving the internal technical conflicts in Batch 01.
