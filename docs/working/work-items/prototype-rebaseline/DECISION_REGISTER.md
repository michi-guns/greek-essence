# Expanded Product Decision Register

## Status Model

- **Open:** evidence or requirements are incomplete.
- **Candidate:** a direction has been named but is not approved as architecture.
- **Approved:** the operator has accepted the decision and its consequences.
- **Deferred:** intentionally excluded from the current phase.
- **Superseded:** retained only for history.

## Decisions

| ID | Decision | Status | Current evidence | Remaining design or validation |
| --- | --- | --- | --- | --- |
| ADR-001 | Product capability and feature boundaries | Approved | Project decisions define eight business and operational feature grills; prior `discovery` proposal is withdrawn | Complete the feature grills, then decide code-module boundaries from accepted behavior |
| ADR-002 | CMS product and editorial model | Approved | Sanity is selected as public-content owner | Define localization, editorial entities and relationships, publication state, application integration, media/evidence records, revisions, recovery, and cost through Content Operations; keep named staffing as launch validation |
| ADR-003 | Managed transactional database boundary | Approved | Neon PostgreSQL supersedes the reported Supabase direction | Validate EU region and DPA, account access, serverless connections, backup/export, restore, monitoring, and upgrade limits |
| ADR-004 | Drizzle responsibility boundary | Approved | Drizzle is selected for Neon schema access and reproducible migrations | Decide schema/migration ownership, server query boundary, pooling, transactions, generated types, and restore interaction |
| ADR-005 | Data model and ownership | Candidate | Customer, Consultation, Payment, Meeting, Questionnaire, Booking Request, Contact Message, and optional Newsletter Subscriber are reported | Resolve state/cardinality conflicts, sensitivity, retention, deletion, audit, import, and ownership |
| ADR-006 | Authentication and authorization | Open | Phase 1 customers are unauthenticated; future customer auth is anticipated | Define Sanity editors, agency operators, future customers, invitations, sessions, and authorization rules |
| ADR-007 | Rendering, caching, and content freshness | Open | Sanity publishing and draft preview replace local build-only content | Decide publishing latency, preview, dynamic data, caching, invalidation, and SEO behavior |
| ADR-008 | Runtime and deployment topology | Approved | Vercel is the current host; Netlify remains an optional later replacement; Sanity and Neon are selected | Confirm commercial Vercel plan or validated Netlify move, regions, connections, migrations, secrets, monitoring, recovery, and rollback ownership |
| ADR-009 | Migration and archive boundary | Open | Prototype is archived; local JSON and prototype structure are superseded candidates | Decide which content/assets are recreated, migrated, or discarded after new models are approved |
| ADR-010 | Security, privacy, and recovery requirements | Open | Real public traffic, PII submissions, and persistent production data are confirmed | Classify data and workflows; define RLS, service roles, idempotency, abuse controls, privacy, retention, backups, restores, audit, and incidents |
| ADR-011 | Consultation lifecycle by release | Open | Phase 1 is unpaid/manual; domain state machine begins at `Pending Payment` | Define Phase 1 states and later migration into paid consultation workflow |
| ADR-012 | Booking Request versus Booking lifecycle | Open | Request must not be a confirmed Booking, but candidate request state is `Confirmed` | Rename/define request terminal states and introduce the separate Booking aggregate for Full MVP |
| ADR-013 | Sanity-to-transaction reference policy | Open | Booking Request references a Sanity Experience without duplicating content | Define immutable IDs, snapshots, unpublish/delete behavior, and historical display needs |
| ADR-014 | Search ownership and filter scope | Candidate | Sanity drives search; Phase 1 and full filter lists differ | Confirm Phase 1 indexed types, filters, price ownership, query approach, and scale |
| ADR-015 | Feature source root and public APIs | Open | Provided Layer 2 brief conflicts with earlier repo working guidance | Choose root versus `src/` feature placement and safe server/client public entry points |
| ADR-016 | Notification delivery and recovery | Approved | Nodemailer through the agency mail service is selected for agency notifications and visitor acknowledgements | Validate SMTP compatibility and sender authorization; define templates, retry/idempotency, diagnostics, privacy, and manual recovery |

## Superseded Direction

The prior static-first architecture and the withdrawn capability proposal are
not implementation authority. The former documentation baseline now lives
under `docs/archive/showcase-prototype-v0/` and remains historical input only.
Any useful decisions must be revalidated through grilling and then promoted
into new canonical product and technical documentation.

The reported Supabase direction is superseded by the accepted Neon PostgreSQL
decision in `docs/grilling/DECISIONS.md`.
