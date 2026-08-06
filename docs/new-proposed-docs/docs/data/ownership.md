---
status: active
owner: engineering
related-adrs:
  - ADR-0002
  - ADR-0003
  - ADR-0004
---

# Data Ownership

## Sanity owns

- Destination and offering descriptions
- Images and galleries
- Public itineraries
- SEO and marketing sections
- Publication state
- Bookability flags
- Simple current catalog pricing when appropriate

## PostgreSQL owns

- Customers and travelers
- Quotes and accepted prices
- Bookings and booking items
- Payments and refunds
- Supplier confirmations and obligations
- Capacity and reservation holds
- Historical commercial records
- Audit data

## Rule

> Sanity owns editable catalog content. PostgreSQL owns business truth.

When Sanity content becomes part of a quote or booking, copy the commercially
relevant data into PostgreSQL.
