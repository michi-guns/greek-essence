# Public Preview Release Validation

## Release Classification

The operator confirmed on 2026-07-29 that the end-of-August preview release will
be publicly accessible and is expected to receive real visitors. Treat it as a
production-facing Phase 1 release, not a private client demonstration.

This confirmation does not by itself approve every feature, provider, public
claim, legal text, cost, or operational commitment in the working drafts.

## Market-Validation and Cost Boundary

The Public Preview is a real-data service operated as a market-validation
experiment. Its launch objective is zero new recurring platform spend: use free
provider plans and quotas wherever they meet the minimum production-facing
requirements, and do not buy hypothetical capacity before visitors demonstrate
demand.

Traffic that approaches or exceeds a free limit is successful validation and
triggers an evidence-led client decision about a bounded paid upgrade. Until
that decision, the service may degrade or stop the affected operation honestly,
but it must not silently lose accepted enquiries, misrepresent delivery, expose
personal data, or bypass an accepted privacy, security, accessibility, or
recovery boundary.

Before launch, verify that the selected free plans permit the intended public
and commercial use, identify their enforceable quotas, monitor those quotas, and
name who receives a threshold or failure alert. If no free route can satisfy a
mandatory safeguard, escalate the blocker rather than silently purchasing a
service or weakening the gate.

## Confirmed Internally

- Public access and real visitor traffic are in scope.
- Real consultation, booking-request, and contact submissions are expected.
- Personal and operational data must be handled as real production data.
- Preview shortcuts cannot weaken security, privacy, accessibility, data
  integrity, or truthful user communication.
- The archived prototype and former static-only architecture are not the launch
  implementation baseline.

## Minimum Client Validation Before Scope Freeze

Keep the client review short and outcome-focused. The client does not need to
approve code organization, ORM mechanics, or framework conventions.

1. **Launch scope and timing** — confirm the target date, public domain, launch
   markets, supported languages, and whether access is fully open.
2. **Public catalogue** — confirm Phase 1 Experience types, destinations, and
   whether Accommodation, Attraction, Article, Cruise, Transfer, and Newsletter
   surfaces are included or deferred.
3. **Consultation request** — confirm the fields collected, manual follow-up
   process, agency owner, response expectations, and notification recipients.
4. **Booking request** — confirm eligible Experiences, required fields, manual
   review process, and wording that makes clear no booking is confirmed online.
5. **Content operations** — identify Sanity editors, approvers, English/Greek
   ownership, preview needs, and who supplies launch-ready copy and licensed
   media.
6. **Trust and commercial claims** — approve public services, relationships,
   testimonials, credentials, package terminology, pricing language, and any
   response-time promise.
7. **Privacy and legal operation** — confirm controller identity, privacy and
   consent language, retention/deletion expectations, contact channels, cookie
   behavior, and required launch policies.
8. **Vendor and account ownership** — approve Sanity, Neon, Vercel, email,
   monitoring, domain, and other recurring provider accounts or costs owned by
   the client.

## Technical Decisions Owned Internally

Subject to the validated product outcomes above, the development process can
decide and document:

- Next.js folder and feature boundaries;
- Drizzle schema, migration, transaction, and validation mechanics;
- Neon connection, role, branch/database, and server-only access boundaries;
- Sanity query modules and preview implementation;
- validation, idempotency, rate limiting, and abuse-control mechanisms;
- caching, revalidation, observability, CI, and deployment mechanics;
- test strategy and quality-gate implementation.

Material cost, privacy, security, data residency, operational burden, or visible
product consequences must be escalated rather than treated as purely technical.

## Production-Facing Phase 1 Gate

Before public launch, require evidence that:

- production and preview environments are separated and correctly configured;
- database migrations are reproducible and recoverable;
- CMS draft content remains private and published content is validated;
- public submissions validate input, resist abuse, handle duplicates safely,
  and never expose personal data in URLs, logs, analytics, or screenshots;
- agency and customer notifications have failure handling and an operational
  recovery path;
- privacy, consent, legal, retention, and deletion behavior match approved
  policy;
- critical public journeys pass accessibility, security, responsive, browser,
  performance, and production-like end-to-end checks;
- monitoring, backups, restore ownership, incident contacts, and launch rollback
  are documented;
- catalogue and request language does not imply live availability, confirmed
  booking, or payment where those capabilities are absent.
