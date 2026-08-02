---
status: active
owner: engineering
---

# Availability

Strongly consistent availability belongs in PostgreSQL.

Examples:

- Remaining seats
- Room allocation
- Reservation holds
- Capacity
- Supplier confirmation state
- Booking status

These values may change concurrently and may require transactions or locking.

Sanity may display derived or editorial availability, but it must not be the
authority for a booking-critical decision.
