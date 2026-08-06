# ADR-0004: Snapshot Commercial Data

## Status

Accepted

## Context

Sanity prices, descriptions, availability labels, and content may change after
a customer accepts a quote or completes a booking.

## Decision

Copy commercially relevant offering data into PostgreSQL when it becomes part
of a quote or booking.

## Consequences

### Positive

- Accepted prices and terms remain historically correct.
- Withdrawn CMS content does not break old records.
- Bookings are understandable without reading current Sanity state.

### Negative

- Intentional data duplication exists.
- Snapshot rules and mappings must be maintained.
- Corrections may require explicit versioning or amendments.

## Related Documents

- [Commercial snapshots](../data/commercial-snapshots.md)
- [Cross-system consistency](../data/cross-system-consistency.md)
