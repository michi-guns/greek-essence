# Public Preview Release Decisions

## Status and Authority

Accepted by the operator on 2026-07-29 after project-level grilling.
The operator amended the mail-provider direction on 2026-08-04 through Runtime
and Production Foundations D-004; this document reflects that superseding choice.

This document defines the high-level product boundary, agency workflow, feature
map, platform direction, client-validation method, and explicit exclusions for
the Greek Essence Public Preview Release. It is product and design authority for
the feature grills that follow.

It does not authorize application implementation, dependency installation,
schema migration, deployment, or destructive path changes. Those require later
accepted feature decisions, promoted canonical documentation where needed, and
explicit bounded implementation contracts.

Use the terms in [GLOSSARY.md](GLOSSARY.md). The archived showcase prototype and
its documentation remain historical reference only.

## Release Definition

The Public Preview Release is a real public service expected to receive real
visitors and enquiries. It is not a private demonstration, even though
controlled demonstrations may be used during development and client review.

Its commercial purpose is market validation: learn whether the public site
attracts meaningful visitors and genuine enquiries before asking the client to
fund expanded capacity. Launch should therefore use free provider plans and
quotas wherever they satisfy the minimum real-data, privacy, security,
reliability, and truthful-failure requirements. Do not buy capacity in advance
for hypothetical traffic.

Approaching or exceeding a free limit because of real visitor activity is a
positive demand signal and triggers an evidence-led client discussion about a
bounded paid upgrade. Non-traffic exhaustion remains an operational constraint,
not evidence of demand. Neither case may silently lose an accepted enquiry or
weaken a required safeguard. If durable saving is unavailable, the site reports
an honest temporary failure and alerts the named operational owner rather than
pretending that the request was received.

The release remains targeted for the end of August in the current working
roadmap. The exact date, public domain, served markets, and languages require
example-led client confirmation before scope freeze.

## Product Promise

Greek Essence will help visitors discover destinations and Experiences and
provide two managed ways to express travel intent:

1. A **consultation request** asks the agency to help plan a trip.
2. A **booking request** expresses interest in a specific Experience.

Submitting a booking request does not reserve anything or confirm a booking.
The agency checks the request manually and follows up through its existing
email and telephone process.

The release does not promise live availability, instant confirmation, payment,
automated scheduling, or a custom agency dashboard.

## Required Visitor Capabilities

The launch must include:

- Home, About, and Contact pages;
- destination and Experience lists and detail pages;
- catalogue text search;
- useful catalogue filters, with the exact filters decided during the catalogue
  feature grill;
- a consultation-request journey;
- a booking-request journey with clear non-confirming wording;
- a general contact form for questions outside the two travel-request journeys;
  and
- the privacy and legal pages required for the real public service.

Articles, Accommodation pages, and Attraction pages are deferred unless
example-led client validation proves that a specific surface is necessary for
launch. Greek Essence does not have a newsletter; newsletter signup and
newsletter operations are not part of the product.

## Agency Request Workflow

For consultation requests, booking requests, and general contact messages:

1. The website must validate and safely save every accepted request before it
   treats the request as received.
2. The agency must receive a useful notification at its chosen business inbox.
3. The visitor must receive a simple acknowledgement that the request arrived.
   A booking-request acknowledgement must not imply confirmation.
4. Agency staff follow up manually through their existing email and telephone
   process.

Saving and email delivery are separate responsibilities. A notification failure
must not destroy an already accepted visitor request. The feature grills must
define honest visitor messaging, monitoring, retry or recovery behavior, and
duplicate-request protection.

Before scope freeze, the client must name the inbox owner, notification
recipients, normal response expectation, and recovery contact.

## Accepted Feature Areas and Order

Grill one feature at a time in this order:

1. **Public brand pages** — Home, About, and their shared brand promise.
2. **Catalogue discovery** — destinations, Experiences, search, filters, and
   detail pages.
3. **Consultation request** — the trip-planning help journey.
4. **Booking request** — interest in a specific Experience without confirmation.
5. **General contact** — messages outside the two travel-request journeys.
6. **Request processing and communications** — shared customer contact details,
   saving, validation, privacy and security, duplicate protection, and email
   delivery.
7. **Content operations** — editing, English/Greek ownership, preview, review,
   publishing, media, and content recovery.
8. **Production operations** — hosting, environments, monitoring, backup,
   restore, incidents, and launch ownership.

Dependencies:

- Public brand pages and catalogue discovery depend on content operations.
- The three submission journeys depend on request processing and
  communications.
- Every public feature depends on production operations.
- Shared foundations must follow the needs established by the individual
  business journeys rather than forcing those journeys into one generic form.

## Platform Direction

The current selected direction is:

- **Next.js** for the application;
- **Sanity** for editable public and catalogue content;
- **Neon Free PostgreSQL** for private customer and request records;
- **Drizzle** for the PostgreSQL schema, reproducible migrations, and application
  access;
- **Vercel** as the current host;
- a provider-neutral transactional-email API gateway using **Resend** as primary
  and **Brevo** as one failover provider for agency notifications and visitor
  acknowledgements; and
- **Netlify** as a possible later replacement for Vercel, not a current
  requirement.

Neon supersedes the working roadmap's Supabase proposal. The preview needs a
focused managed relational database and does not currently need Supabase Auth,
Storage, Realtime, or its other bundled capabilities.

Before accepting real visitor data, validate for Neon:

- an appropriate EU data region and privacy agreement;
- client-owned account and controlled developer access;
- Drizzle migrations and the full customer-and-request transaction;
- duplicate protection;
- monitoring and alert ownership;
- restore behavior; and
- secure off-provider export and a tested recovery procedure.

Neon Free's six-hour restore window cannot be the only recovery plan.

Vercel may be used for development and controlled demonstrations. If its terms
require a commercial plan for this public use, it is not the zero-cost launch
host unless the client later approves that cost. The public preview must use a
validated commercially eligible free-hosting route, such as a validated
Netlify Free replacement, or return the cost decision to the client. Provider
terms, quotas, and technical fit must be checked before launch.

The launch target is zero new recurring platform spend using compliant free
quotas and client-controlled services. Free limits must be monitored, and no paid
upgrade may be introduced without a later explicit client decision. If no free
option can meet a mandatory privacy, security, durability, or truthful-service
boundary, surface that launch blocker rather than silently paying or weakening
the requirement.

Application features depend on one provider-neutral transactional-email
interface. Resend is the primary provider and Brevo is the only launch fallback.
The submission handler waits for required initial email work to finish after the
Request commits. Failover occurs only after a provider result is proven to mean
definite non-acceptance; an ambiguous handoff stops automatic redispatch. The
Public Preview does not pool free quotas, run a generic background mail queue, or
enable AhaSend without a later evidence-backed decision.

Before launch, validate both providers' client-controlled accounts, privacy and
commercial terms, sender-domain authorization, API behavior, quotas, credentials,
and failure recovery. If either provider cannot satisfy a mandatory boundary,
return the constraint to the operator; do not silently add a third provider, pay
for an upgrade, or weaken truthful delivery behavior.

## Client Collaboration and Approval

Client validation must be example-led because the client has limited technical
knowledge and finds open-ended requirements communication difficult.

Prepare realistic examples, draft content, sample form answers, page mockups,
and short approval templates. Ask the client to correct, approve, or reject
concrete proposals rather than invent complete requirements from a blank page.

The client must confirm:

- launch date, domain, served markets, and languages;
- launch destinations, Experiences, and catalogue content;
- the questions asked by each form and the manual follow-up process;
- agency inbox ownership, notification recipients, response expectations, and
  recovery contact;
- content editors and English/Greek content ownership;
- approved copy, licensed images, testimonials, pricing wording, partnerships,
  credentials, and other public claims;
- privacy, cookies, data retention, contact details, and required legal
  documents; and
- ownership, access, acceptable cost, and operational responsibility for
  Sanity, Neon, Vercel or a later Netlify replacement, the domain, monitoring,
  and the Resend and Brevo accounts.

The development team owns Drizzle mechanics, code organization, validation
libraries, runtime configuration, and test implementation, subject to accepted
product and risk decisions.

### Draft and Placeholder Boundary

- Draft material must be clearly marked for review and must not be represented
  as client-approved fact.
- Do not publish unapproved legal or privacy wording, prices, testimonials,
  credentials, supplier relationships, response promises, or licensed-media
  claims.
- Privacy and cookie drafts must reflect what the finished site actually
  collects and uses; do not add a generic cookie banner without that evidence.
- Legal, privacy, tax, and commercial wording may require an appropriately
  qualified professional. A realistic placeholder is not proof of compliance.
- The operator's personal Gmail may be used only for a controlled demonstration
  with synthetic test enquiries. It must not receive real public visitor data or
  become the production agency inbox.

## Explicitly Deferred or Excluded

The following are deferred beyond the Public Preview Release:

- customer accounts, sign-in, and customer request history;
- online payments and paid consultations;
- post-enquiry questionnaires;
- automated appointment scheduling;
- live supplier availability;
- confirmed online bookings;
- online cancellation and refund handling;
- a private staff dashboard;
- a separate customer-management system;
- automated supplier connections;
- advanced automated customer communication; and
- articles, Accommodation pages, and Attraction pages unless client validation
  proves a specific launch need.

Newsletter functionality is excluded rather than deferred.

## Material Risks and Launch Gates

The public release must not accept real enquiries until the applicable feature
decisions and launch evidence establish:

- truthful distinction between inspiration, enquiry, booking request, and
  confirmed booking;
- secure handling of personal and free-text visitor data;
- working duplicate protection and request persistence;
- honest behavior when database or email delivery fails;
- named agency ownership and response process;
- client-controlled production accounts and secrets;
- validated Neon privacy, region, backup, restore, and recovery boundaries;
- validated Resend and Brevo account control, sender-domain authorization,
  privacy terms, API behavior, quotas, and delivery recovery;
- approved English/Greek content, licensed media, and public claims;
- required privacy and legal review;
- accessible, responsive, localized visitor journeys;
- passing security, metadata, performance, browser, and repository checks; and
- monitoring, incident, rollback, and recovery ownership.

## Superseded Directions

- The private prototype framing is superseded by the public production-facing
  preview.
- Supabase is superseded by Neon for preview transactional data.
- Turso and Aiven Free were considered and rejected in favor of Neon's
  PostgreSQL, Drizzle, serverless connection, and future-workflow fit.
- A custom staff dashboard, separate customer-management service, combined
  generic enquiry feature, and early booking operations are not launch scope.
- The archived prototype's Resend-only architecture and the later Nodemailer/
  agency-SMTP direction are superseded. Neither is current implementation
  authority.

## Unresolved External Validations

No unresolved high-level product decision remains. The following validations
have named owners or later feature grills and may still change launch details:

- Client: public scope, content, workflows, owners, claims, media, policies,
  accounts, and acceptable costs.
- Operator and development team: a validated commercially eligible zero-cost
  launch host; any later paid Vercel or other upgrade requires traffic evidence
  and explicit client approval.
- Development team with client account owner: Neon region, privacy agreement,
  access, recovery, and upgrade limits.
- Development team with client mail-provider owner: Resend and Brevo account
  control, API credentials, sender domain, terms, limits, delivery, and failure
  recovery.
- Qualified reviewers where applicable: legal, privacy, tax, commercial, and
  travel-industry claims.

These are validation gates, not permission to invent missing facts.
