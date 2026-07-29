# 07_PROJECT_ROADMAP.md

# Greek Essence — Project Roadmap

**Status:** Revised v2  
**Audience:** Developer, AI agents, and technical reviewers  
**Purpose:** Define the full delivery path from discovery to the Phase 1 Release and then to the complete MVP.

---

## 1. Roadmap Structure

Greek Essence will be delivered in two major releases:

### Phase 1 Release

Target: end of August.

This is the first public version of the platform. It is intentionally limited but fully usable and presentable.

It includes:

- Project and repository restructuring
- Technical foundation
- Sanity, Supabase, and Drizzle setup
- Core domain implementation
- Public website
- Editorial homepage
- Destinations and packages
- Basic consultation request flow
- Basic booking request flow
- Production deployment

It excludes:

- Consultation payment
- Questionnaire
- Automated scheduling
- Full booking confirmation flow
- Advanced operational tooling

### Full MVP

The complete first production version.

It extends the Phase 1 Release with:

- Paid consultation flow
- Questionnaire workflow
- Scheduling
- Booking review and confirmation
- Booking payments where applicable
- More complete customer communications
- Production hardening
- Full launch and handover

---

## 2. Delivery Principles

- Scope is frozen per milestone.
- Sanity owns public content.
- Supabase and Drizzle own transactional data.
- Customers can interact without authentication.
- Route Handlers are preferred for business operations.
- Public APIs must include validation, rate limiting, idempotency, and other appropriate safety controls.
- Quality, testing, documentation, and deployment automation are part of delivery.

---

# Phase 0 — Discovery and Product Definition

## Objective

Turn the client’s ideas into an implementable product direction.

## Deliverables

- Product requirements
- Sitemap
- UX and prototype specification
- Technical design
- Domain architecture
- Content ownership decisions
- Consultation workflow
- Booking workflow
- Repository and AI-agent conventions
- MVP boundaries
- Delivery roadmap

## Status

Substantially completed.

## Acceptance Criteria

- Product scope is documented.
- Core workflows are documented.
- Major architectural decisions are recorded.
- Phase 1 and MVP boundaries are clear.

---

# Phase 1 Release — End-of-August Public Version

## Objective

Deliver a polished, production-deployed first release that Greek Essence can present publicly and use to collect real enquiries.

---

## Milestone 1 — Repository and Architecture Foundation

### Deliverables

- Feature-based application structure
- Next.js project cleanup and reorganization
- TypeScript strict setup
- Environment validation
- GitHub Actions
- Vercel integration
- Supabase setup
- Drizzle setup and migrations
- Sanity setup
- Test infrastructure
- Repository documentation
- Agent instructions, skills, and tooling configuration
- Gitleaks, Knip, linting, formatting, and build checks

### Acceptance Criteria

- Project builds locally and in CI.
- Preview deployments work.
- Database migrations are reproducible.
- Sanity Studio connects correctly.
- Repository structure and documentation are understandable to future agents.
- Mandatory checks block invalid changes.

---

## Milestone 2 — Core Domain and Data Foundation

### Deliverables

Implement the initial transactional domain required for the Phase 1 Release.

Core entities:

- Customer
- Consultation
- Booking Request
- Contact Message
- Newsletter Subscriber where included

Sanity-owned catalogue concepts:

- Destination
- Experience
- Accommodation
- Attraction
- Interest
- Article
- FAQ
- Testimonial
- Global site content

### Relationships

- Customer has many Consultation records.
- Customer has many Booking Requests.
- Consultation belongs to one Customer.
- Booking Request belongs to one Customer.
- Booking Request references one Sanity Experience.
- Experience references destinations, interests, FAQs, images, and related content.

### Acceptance Criteria

- Core relationships are implemented.
- Customer creation and reuse rules are defined.
- Sanity content identifiers can be safely referenced from transactional records.
- Content and business data are not duplicated unnecessarily.

---

## Milestone 3 — Design System and Editorial Homepage

### Objective

Create a visually strong first impression and a reusable UI foundation.

### Deliverables

- Design tokens
- Typography
- Layout system
- Header
- Footer
- Mobile navigation
- Reusable buttons, cards, forms, alerts, and loading states
- Editorial homepage
- Featured destinations
- Featured packages
- Brand story
- Trust-building content
- Consultation call to action
- Testimonials
- Responsive behaviour

### Editorial Direction

The homepage should feel closer to a high-quality travel publication than a generic agency template.

It should prioritize:

- Strong visual storytelling
- High-quality photography
- Clear hierarchy
- Premium spacing
- Curated package presentation
- Emotional and aspirational content
- Immediate understanding of the agency’s value

### Acceptance Criteria

- Homepage is polished on mobile and desktop.
- Key content is manageable through Sanity.
- The page communicates brand, services, and next steps clearly.
- Shared components are reusable throughout the website.

---

## Milestone 4 — Sanity Content Platform

### Deliverables

Sanity document types for:

- Homepage
- Destination
- Experience
- Accommodation
- Attraction
- Interest
- Article
- FAQ
- Testimonial
- About page
- Contact page
- Consultation page
- Navigation
- Footer
- Site settings
- SEO

### Experience Types for Phase 1

The initial Experience types should reflect services Greek Essence actually offers.

Expected initial types:

- Tour
- Activity
- Travel package

Additional types should be introduced only when required.

### Acceptance Criteria

- Client can create and edit the required public content.
- Content relationships work correctly.
- Draft preview works.
- Invalid essential content is blocked.
- Public content can be queried through reusable application modules.

---

## Milestone 5 — Public Website and Package Catalogue

### Deliverables

- Homepage
- About page
- Contact page
- Destination listing
- Destination detail pages
- Package or Experience listing
- Experience detail pages
- Consultation landing page
- Basic travel inspiration or article pages if content is ready
- Legal and policy pages required for launch
- Responsive layout
- SEO baseline
- Sitemap and robots configuration

### Phase 1 Search and Filtering

Include a practical first version:

- Search by text
- Filter by destination
- Filter by Experience type
- Filter by interest where content is ready

Advanced filtering may remain for the full MVP.

### Acceptance Criteria

- Published content renders correctly.
- Draft content remains private.
- Core pages are navigable.
- Packages are clearly presented.
- Search and basic filters work.
- Mobile experience is production-ready.

---

## Milestone 6 — Basic Consultation Request Flow

### Objective

Allow visitors to request a consultation without payment, questionnaire, or automated scheduling.

### Workflow

1. Visitor opens the consultation page.
2. Visitor submits personal and travel information.
3. Customer is created or reused.
4. Consultation is created.
5. Agency receives a notification.
6. Customer receives confirmation.
7. Agency follows up manually.

### Data Captured

- First name
- Last name
- Email
- Phone
- Country
- Preferred language
- Travel dates or flexibility
- Traveller count
- Budget range
- Main interests
- Notes
- Consent records

### Acceptance Criteria

- Request can be submitted without authentication.
- Customer and Consultation records are created consistently.
- Duplicate submissions are handled safely.
- Agency receives the enquiry.
- Customer receives acknowledgement.
- Personal data is not exposed in logs or URLs.

---

## Milestone 7 — Basic Booking Request Flow

### Objective

Allow visitors to express intent to book an eligible tour or package.

### Workflow

1. Visitor opens an Experience.
2. Visitor selects “Request Booking.”
3. Visitor submits dates, party size, and contact details.
4. Customer is created or reused.
5. Booking Request is created.
6. Agency receives notification.
7. Customer receives acknowledgement.
8. Agency continues manually.

### Acceptance Criteria

- Booking request can be submitted without authentication.
- Request references the correct Experience.
- Customer and request records are stored safely.
- Agency and customer notifications are sent.
- Request is clearly not presented as a confirmed booking.

---

## Milestone 8 — Phase 1 Quality and Deployment

### Deliverables

- Unit and integration tests for core domain logic
- Playwright coverage for critical Phase 1 journeys
- Security review
- Accessibility review
- Performance review
- Production deployment
- Environment verification
- Error monitoring
- Client content guidance
- Launch checklist

### Critical Journeys

- Browse homepage
- Browse destinations
- Browse packages
- Search and filter Experiences
- Submit consultation request
- Submit booking request
- Submit contact form

### Acceptance Criteria

- CI passes.
- Critical journeys pass in a production-like environment.
- No known launch-blocking security issue remains.
- Production site is available.
- Client can edit required content.
- Phase 1 scope is complete.

---

# Full MVP — Post-Phase-1 Expansion

## Milestone 9 — Paid Consultation Workflow

### Deliverables

- Payment session creation
- Payment provider integration
- Verified webhooks
- Idempotent payment handling
- Payment success and failure states
- Consultation state machine
- Payment confirmations
- Refund baseline

### Acceptance Criteria

- Consultation cannot progress to scheduling before successful payment.
- Payment events are verified and idempotent.
- Duplicate events do not create duplicate side effects.
- Payment state is auditable.

---

## Milestone 10 — Questionnaire Workflow

### Deliverables

- Secure questionnaire link
- Optional questionnaire configuration
- Structured and free-text responses
- Submission persistence
- Agency review
- Completion notifications

### Acceptance Criteria

- Questionnaire is accessible without account creation.
- Link is secure and non-guessable.
- Another customer’s responses cannot be accessed.
- Duplicate submissions are handled safely.

---

## Milestone 11 — Consultation Scheduling

### Deliverables

- Availability definition
- Time-zone handling
- Meeting scheduling
- Double-booking prevention
- Calendar invite
- Meeting link storage or generation
- Rescheduling and cancellation
- Reminder emails

### Acceptance Criteria

- Scheduling is available only after successful payment.
- Time-zone conversion is correct.
- Double-booking is prevented.
- Meeting status is traceable.

---

## Milestone 12 — Full Booking Workflow

### Deliverables

- Booking Request review
- More-information-required state
- Offer or adjustment workflow
- Accepted and rejected states
- Confirmed Booking record
- Deposit, full-payment, or no-payment modes
- Booking payments where applicable
- Cancellation and refund baseline
- Booking confirmations

### Acceptance Criteria

- Booking Request and Booking are distinct.
- Accepted requests can become Bookings.
- Historical pricing and selected terms remain understandable.
- Payment cannot confirm the wrong Booking.
- Customer communications reflect the correct state.

---

## Milestone 13 — Communications and Operational Controls

### Deliverables

- Complete transactional email set
- Internal workflow visibility
- Pending-action views
- Failure diagnostics
- Audit information
- Manual recovery documentation
- Basic reporting or exports where required

### Acceptance Criteria

- Agency can identify pending consultations and booking requests.
- Failed communications can be diagnosed.
- Critical transitions are traceable.
- Duplicate events do not send duplicate critical messages.

---

## Milestone 14 — Full Production Hardening and Handover

### Deliverables

- Final unit, integration, and E2E suite
- Coverage review
- Security hardening
- Accessibility validation
- Performance optimization
- SEO validation
- Browser and device checks
- Backup and recovery review
- Client training
- Technical handover
- Stabilization period

### Acceptance Criteria

- Full MVP workflows pass end-to-end.
- Coverage meets the agreed threshold or documented exceptions.
- No known critical issue remains.
- Client can operate the platform.
- Documentation is complete.

---

## 3. Indicative Schedule

### Phase 1 Release

Estimated effort: approximately 130–200 hours.

With focused work, this is realistic for an end-of-August target, provided:

- Scope is frozen.
- Content arrives on time.
- Client feedback is prompt.
- Payment, questionnaire, and automated scheduling remain excluded.
- No major custom admin panel is added.

### Remaining MVP

Estimated effort after Phase 1: approximately 220–320 hours.

Actual duration depends on provider choices, policies, and review speed.

---

## 4. Scope Control

New requirements must be classified as:

- Clarification
- Replacement
- Additional scope
- Future enhancement

Additional scope affects timeline and price.

The end-of-August date should be protected by postponing non-essential work rather than reducing quality across every feature.

---

## 5. Definition of Phase 1 Completion

Phase 1 is complete when:

- The public website is live.
- Homepage is polished and editorial.
- Destinations and packages are manageable through Sanity.
- Visitors can browse and search the catalogue.
- Visitors can submit consultation requests.
- Visitors can submit booking requests.
- Customer and request data are stored correctly.
- Agency notifications work.
- CI/CD and quality checks are active.
- The client can present the platform publicly.

---

## 6. Definition of Full MVP Completion

The full MVP is complete when:

- Paid consultations work.
- Questionnaire workflow works.
- Consultation scheduling works.
- Booking requests can become confirmed Bookings.
- Booking payments work where required.
- Full communications are operational.
- Critical workflows are tested.
- Production hardening and handover are complete.
