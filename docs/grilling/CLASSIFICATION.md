# Approved Grilling Classification

## Status and Purpose

The operator accepted this classification after reviewing the existing decision
landscape. It determines where accepted and pending material belongs across
Product and Domain Truth, Foundation Design, and Launch Readiness.
The operator amended the locked mail-provider input on 2026-08-04 through Runtime
and Production Foundations D-004; this classification reflects that explicit
reopening.

Classification does not change the meaning or authority of an accepted decision.
Existing accepted `DECISIONS.md` files and normative contracts remain
authoritative until their outcomes are promoted into canonical product, domain,
or technical documentation.

## Locked Foundation Inputs

Do not reopen these choices during Foundation Design:

- Next.js;
- Sanity for editable public and catalogue content;
- Neon PostgreSQL for private customer and request records;
- Drizzle ORM using the latest release candidate available when implementation
  begins;
- Drizzle's first-party Zod integration with the latest Zod v4;
- a provider-neutral transactional-email API gateway with Resend as primary and
  Brevo as the single launch fallback;
- Vercel as the current hosting direction, with Netlify only as the accepted
  fallback direction if Vercel fails a mandatory commercial or technical gate;
- zero new recurring platform spend until real visitor demand supports a
  separately approved upgrade.

Exact package versions must be pinned during implementation. Compatibility,
provider terms, quotas, regions, account access, and executable evidence remain
validation work; they do not reopen the selected direction by default.

## Product and Domain Truth

Retain the accepted product promise, scope, journeys, vocabulary, business
relationships, user-visible lifecycle meaning, information boundaries, and
truthful failure behavior. This includes:

- the public production-facing market-validation release;
- discovery, Consultation Request, Booking Request, and General Contact;
- Booking Request versus confirmed Booking and requestability versus availability;
- catalogue types, search/filter scope, request fields, and prohibited data;
- durable acceptance before receipt, immutable requests, explicit corrections,
  opaque references, and manual agency follow-up;
- twelve-month request retention and independent correction expiry;
- withdrawn Experience behavior and bounded historical request meaning;
- complete, meaning-equivalent English and Greek public experiences;
- accepted exclusions and deferrals.

The classification identified two product/domain gaps before the relevant
Sanity foundation:

1. the minimum publishable completeness for a Destination, after importing the
   already accepted contracts for Home, About, Experiences, request journeys,
   and visitor-visible system states;
2. withdrawal behavior for Destinations and other non-Experience public content.

Both gaps are accepted and resolved in
[`product-domain-truth/content-publication/DECISIONS.md`](product-domain-truth/content-publication/DECISIONS.md).
Accepted Experience completeness and withdrawal rules are imported unchanged.

## Foundation Design

Carry accepted system invariants forward and decide only their unresolved
technical realization. The dependency-ordered tracks are:

1. **System boundaries and domain representation** — service ownership, data
   classes, entities, relationships, identifiers, lifecycles, cross-service
   references, and immutable snapshots.
2. **Editorial content platform** — Sanity schemas and references, localization,
   publication, evidence metadata, preview, revisions, withdrawal, rendering,
   caching, revalidation, search, and freshness.
3. **Transactional data platform** — Neon and Drizzle schemas, constraints,
   transactions, migrations, Drizzle-Zod and handwritten Zod responsibilities,
   idempotency, audit, retention, deletion, and backup representation.
4. **Application architecture** — App Router, feature and shared boundaries,
   Route Handlers, server-only data access, browser/server entry points,
   dependency direction, and Server/Client Component boundaries.
5. **Runtime and production foundations** — environments, secrets, deployment,
   migrations, rollback, mail recovery, observability, quotas, backup, restore,
   and hosting-fallback implications.

Before each technology-dependent question, explain the relevant components and a
concrete Greek Essence workflow in plain language. The operator has light
Drizzle experience, moderate Zod experience mainly with v3, and no practical
Neon, Sanity, or CMS experience.

## Launch Readiness

Move assignments, approved inputs, provider facts, procedures, and executable
proof into a later owner/evidence/blocker register. This includes:

- named content reviewers, publishers, account owners, inbox recipients,
  incident contacts, and recovery owners;
- approved bilingual copy, catalogue records, claims, prices, media rights, and
  legal/privacy wording;
- provider terms, regions, agreements, quotas, account control, transactional-
  email sender authorization, API credentials, and access evidence;
- executed environment-isolation, migration, rollback, monitoring, backup,
  restore, accessibility, security, browser, performance, and end-to-end checks.

A readiness failure routes upstream only when it reveals a real product choice or
foundation constraint.

## Pending Mixed-Layer Ledgers

`content-operations/GRILLING.md` and `production-operations/GRILLING.md` are
preserved as classification sources but must not continue from their stored next
questions.

Content Operations D-001 remains a locked distinction: the client approves
business content and the technical publisher does not silently become the
business approver. Named people and the handoff belong to Launch Readiness. Its
remaining questions split into the product gaps, Editorial Content Platform
foundations, and Launch Readiness evidence.

Production Operations contains no separate active feature sequence. Account and
incident assignments belong to Launch Readiness. Environment, recovery,
monitoring, deployment, migration, rollback, secrets, and quota mechanisms belong
to Foundation Design, followed by launch proof. Vercel is validated before the
accepted Netlify fallback direction is activated.

## Drop, Defer, or Retain as History

Do not promote excluded, deferred, or superseded material into launch schemas or
architecture:

- Newsletter is excluded;
- customer accounts, payments, paid consultation, Meeting, Questionnaire,
  confirmed Booking, staff dashboards, and CRM are deferred;
- Supabase, Turso, Aiven, Nodemailer through agency SMTP, and the archived
  Resend-only prototype architecture are superseded;
- the three-provider quota-router draft is not adopted as authority;
- AhaSend, local cross-provider quota pooling, and a generic background email
  queue remain deferred until measured need supports a separate decision;
- Netlify implementation remains deferred unless Vercel fails a mandatory gate.

## Promotion Rule

Product/domain outcomes later promote into canonical product and domain
documentation. Foundation outcomes promote into canonical domain representation,
technical design, and normative integration contracts. Launch Readiness owns
external facts and evidence without duplicating or weakening upstream authority.
