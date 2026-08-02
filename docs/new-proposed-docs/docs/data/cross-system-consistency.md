---
status: active
owner: engineering
---

# Cross-System Consistency

PostgreSQL and Sanity cannot participate in one shared atomic transaction.

For workflows touching both systems:

1. Choose one authoritative write.
2. Make follow-up actions idempotent.
3. Record enough state to retry or repair.
4. Prefer targeted synchronization.
5. Add an outbox, queue, or worker only when reliability requirements justify it.

Booking creation must not depend on successfully mutating Sanity.

Sanity webhooks may trigger cache invalidation or synchronization, but business
truth remains in PostgreSQL.
