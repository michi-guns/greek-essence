# System in Five Minutes

We are building a web application for a small Greek travel agency.

It has two main faces:

1. A public travel website.
2. An internal system for customers, quotes, bookings, payments, suppliers,
   and documents.

The architecture is a **domain-centered modular monolith with vertical slices**.

## Responsibilities

```text
Domain:
What the business means and what is valid.

Application:
What the system allows someone to do.

Infrastructure:
How databases, CMSs, files, and external services are used.

Presentation:
How users and external systems interact with the application.
```

## Main technologies

- Next.js and React deliver the application.
- PostgreSQL stores transactional business truth.
- Drizzle maps the relational persistence model.
- Sanity manages editable catalog and editorial content.
- Zod validates untrusted input and external data.
- React Hook Form is used for forms that justify client-side complexity.
- TanStack Query is added only when client-side server-state behavior requires it.

## Most important rule

> Sanity owns editable catalog content. PostgreSQL owns business truth.

When a catalog offering enters a quote or booking, its commercially relevant
data is copied into PostgreSQL as a snapshot.

Current CMS changes must never rewrite accepted commercial history.

## Initial workflow

```text
Customer
→ Travelers
→ Quote
→ Sanity offering
→ Commercial snapshot
→ Acceptance
→ Booking
→ Payment
→ Confirmation
```

The exact workflow remains subject to business verification.
