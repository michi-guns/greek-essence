
# 06_DOMAIN_ARCHITECTURE.md

# Greek Essence – Domain Architecture

> **Purpose**
>
> This document captures the business domain and architectural decisions of Greek Essence. It intentionally avoids implementation details, SQL schemas, or framework syntax. Its goal is to help AI agents and developers understand **how the business works**, **where data belongs**, and **how the system should evolve**.

---

# 1. Guiding Principles

- Model business concepts, not UI pages.
- Separate content from transactional data.
- Prefer reusable domain entities over duplicated models.
- Business workflows should be explicit.
- Every entity should have a single owner.
- Optimize for long-term maintainability while keeping the MVP simple.

---

# 2. System Responsibilities

## Sanity (Content Layer)

Owns editable marketing and catalogue content.

Documents include:

- Experience
- Destination
- Accommodation
- Attraction
- Interest
- FAQ
- Article
- SEO
- Navigation
- Homepage
- Site Settings

Sanity should never own transactional or customer-specific data.

## Supabase (Business Layer)

Owns transactional and operational data.

Entities include:

- Customer
- Consultation
- Payment
- Meeting
- Questionnaire
- Booking Request
- Contact Message
- Newsletter Subscriber

Supabase should never duplicate content already managed by Sanity.

---

# 3. Bounded Contexts

## Marketing

Owns:
- Pages
- Branding
- SEO
- Blog

Does not own:
- Customers
- Bookings
- Payments

## Catalogue

Owns:
- Experiences
- Destinations
- Accommodation
- Attractions
- Interests

Does not own:
- Pricing history
- Customer data

## Consultation

Owns:
- Consultation
- Payment
- Meeting
- Questionnaire

Does not own:
- Experiences
- SEO
- Articles

## Booking

Owns:
- Booking Requests

Consumes:
- Experience
- Customer

## CRM

Owns:
- Customer
- Contact Messages
- Newsletter Subscribers

---

# 4. Content Model (Sanity)

## Experience

Represents anything sold by the agency.

Types:

- Tour
- Activity
- Package
- Cruise
- Transfer

Relationships:

- Destination
- Accommodation
- Interest
- FAQ
- Images

## Destination

Represents countries, regions, islands and cities.

Relationships:

- Experiences
- Attractions
- Accommodation

## Accommodation

Hotels, villas, apartments and similar lodging.

## Attraction

Points of interest associated with destinations.

## Interest

Reusable taxonomy such as:

- Adventure
- Food
- Luxury
- Family
- Nature
- History
- Beach

## Supporting Content

- Articles
- FAQ
- SEO
- Navigation
- Homepage
- Site Settings

---

# 5. Business Model (Supabase)

## Customer

Represents every person interacting with the business.

Created from:

- Consultation
- Booking Request
- Contact Form

Future authentication will attach to an existing Customer instead of replacing it.

## Consultation

Represents the complete bespoke travel consultation lifecycle.

References:

- Customer
- Payment
- Meeting
- Questionnaire

## Payment

Tracks payment independently from consultations.

Designed so payment providers can change without affecting business logic.

## Meeting

Represents the scheduled consultation.

## Questionnaire

Stores consultation-specific questions and answers.

## Booking Request

Represents interest in an Experience.

A booking request is **not** a confirmed booking.

---

# 6. Domain Relationships

Customer
- has many Consultations
- has many Booking Requests
- has many Contact Messages

Consultation
- has one Payment
- has one Meeting
- has one Questionnaire

Experience
- belongs to Destination
- has many Interests
- has many FAQs

Booking Request
- belongs to Customer
- references one Experience

---

# 7. State Machines

## Consultation

Pending Payment
→ Paid
→ Questionnaire Pending
→ Scheduling
→ Scheduled
→ Completed

Alternative terminal state:

Cancelled

## Payment

Pending
→ Succeeded

or

Pending
→ Failed

Succeeded
→ Refunded

## Booking Request

Pending
→ Reviewed
→ Confirmed

or

Pending
→ Rejected

---

# 8. Core Workflows

## Consultation

1. Visitor submits consultation request.
2. Create (or reuse) Customer.
3. Create Consultation.
4. Redirect to payment.
5. Payment webhook confirms payment.
6. Send questionnaire.
7. Customer completes questionnaire.
8. Schedule meeting.
9. Consultation completed.

## Booking Request

1. Visitor selects an Experience.
2. Visitor submits booking request.
3. Create (or reuse) Customer.
4. Create Booking Request.
5. Agency reviews request.
6. Customer is contacted.

---

# 9. API Philosophy

Business operations should primarily be exposed through Route Handlers.

Reasons:

- Stable HTTP interface.
- Future AI agents can safely consume APIs.
- Business logic remains reusable.
- Decouples UI from business workflows.

Server Actions remain acceptable for purely UI-oriented interactions.

All public endpoints must enforce appropriate validation, authorization (when introduced), rate limiting, and security controls.

---

# 10. Search & Filtering

Searchable content:

- Experiences
- Destinations
- Accommodation

Primary filters:

- Destination
- Experience Type
- Duration
- Interest
- Difficulty
- Price

Catalogue search should be driven by Sanity content rather than transactional tables.

---

# 11. Domain Invariants

## Customer

- Exists before a Consultation.
- Exists before a Booking Request.
- May exist without authentication.

## Consultation

- Always belongs to one Customer.
- Cannot be scheduled before successful payment.

## Payment

- Always belongs to one Consultation.
- Successful payments are immutable except for refunds.

## Meeting

- Cannot exist before payment succeeds.
- Always belongs to one Consultation.

## Experience

- Exists only in Sanity.
- Never stores transactional information.

## Booking Request

- References an Experience.
- Never duplicates Experience content.

---

# 12. Future Considerations

The architecture intentionally leaves room for:

- Customer authentication
- AI-powered assistants consuming public APIs
- Automated booking workflows
- Additional payment providers
- CRM enhancements

These features should extend the existing domain model rather than replace it.
