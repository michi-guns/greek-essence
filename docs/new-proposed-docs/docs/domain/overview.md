---
status: evolving
owner: product-and-engineering
---

# Domain Overview

The domain model captures the business-relevant parts of a small travel agency.

Initial areas:

- Customers
- Travelers
- Catalog offerings
- Quotes
- Bookings
- Payments and refunds
- Suppliers
- Documents

The model is intentionally incomplete. It should evolve from observed workflows
rather than assumptions about the entire travel industry.

## Domain rule

Business behavior belongs in domain objects or domain services, not in forms,
database schemas, or CMS documents.

## Uncertainty

Unverified behavior belongs in
[`assumptions/`](./assumptions/) or
[`open-questions.md`](./open-questions.md).
