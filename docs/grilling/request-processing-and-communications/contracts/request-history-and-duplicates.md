# Request History and Duplicate Contract

## Authority and Scope

This contract is normative for Request Processing and Communications D-003. It
defines chronological request history, explicit corrections, and exact
technical-retry behavior.

It does not define staff lifecycle states, detailed audit fields, retry windows,
retention, deletion, or a public request-history interface. D-004 and later
decisions own those boundaries.

## Chronological Request History

1. Every accepted new submission has one immutable request record and opaque
   reference in the D-002 email-based contact relationship.
2. The record preserves its request type, submitted snapshot, and durable
   acceptance time.
3. Later records append to the relationship's chronology. They do not overwrite,
   rewrite, or detach earlier records.
4. Similar content, close timing, or reused contact details do not by themselves
   prove that a later submission is a correction or duplicate.
5. The chronology is private agency context. It is not a customer account or a
   public request-history feature.

## Explicit Correction

1. A submission is a correction only when the visitor explicitly selects that
   intent and supplies the earlier request's opaque reference.
2. The submitted normalized email must belong to the same contact relationship
   as the referenced request.
3. A valid correction creates a new immutable request record linked to the
   corrected request.
4. The earlier record remains intact because it may already have been notified,
   read, or acted upon by agency staff.
5. A failed reference-and-email match must not reveal whether either value
   exists or identify any prior request.

## Exact Technical Retry

Repeated transport of the same submission must resolve idempotently to the same
accepted request and opaque reference. It must not create another chronological
record, another correction, or another intentional email dispatch.

The implementation contract must define a bounded, non-sensitive idempotency
identity. It must not infer duplication merely from similar visitor content or
reuse one idempotency identity for a visitor's later intentional request.

## Minimum Preserved Relationship

Each chronological record must retain enough relationship information to show:

- whether it is a new request or explicit correction;
- which earlier request it corrects, when applicable; and
- the processing and delivery-state history accepted by D-004 and D-005.