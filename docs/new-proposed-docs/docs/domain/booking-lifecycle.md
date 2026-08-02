---
status: draft
owner: product-and-engineering
---

# Booking Lifecycle

Initial proposal:

```text
Draft
→ PendingConfirmation
→ Confirmed
→ Completed

Applicable states
→ PartiallyCancelled
→ Cancelled
```

## Candidate rules

- A booking must contain at least one service.
- Confirmation records the agreed commercial snapshot.
- Current Sanity changes do not alter an existing booking.
- Cancellation preserves historical records.
- Supplier confirmation may be distinct from customer confirmation.

## Unverified questions

- Can bookings be created directly?
- What makes a booking confirmed?
- Are supplier confirmations required first?
- How are partial cancellations priced?
- Can a completed booking be reopened?
