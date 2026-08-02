---
status: active
owner: content-and-engineering
related-adrs:
  - ADR-0002
---

# Sanity

Sanity is the content and catalog management system.

## Suitable data

- Destinations
- Travel package pages
- Accommodation and excursion descriptions
- Images
- Public itinerary copy
- SEO
- Homepage content
- FAQs
- Publication state
- Bookability state
- Marketing prices

## Integration rule

Application code depends on a catalog port. A Sanity adapter performs GROQ
queries, validates results with Zod, and maps them into application-friendly
models.

Raw Sanity documents must not flow through booking domain code.

## Not authoritative for

- Accepted prices
- Booking state
- Payment state
- Strongly consistent availability
- Supplier confirmation
- Historical commercial truth
