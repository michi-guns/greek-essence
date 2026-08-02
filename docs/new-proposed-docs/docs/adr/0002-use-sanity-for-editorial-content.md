# ADR-0002: Use Sanity for Editorial Catalog Content

## Status

Accepted

## Context

Agency staff need to edit destinations, packages, images, SEO, and public
content without application deployments.

## Decision

Use Sanity as the source for editable catalog and editorial content.

Access Sanity through infrastructure adapters and validate query results before
mapping them into application models.

## Consequences

### Positive

- Editors can change and publish content quickly.
- Content workflows remain separate from transactional workflows.
- Public content can use Sanity's editorial capabilities.

### Negative

- The system has a second data store.
- Data ownership and synchronization must remain explicit.
- Sanity document shapes require validation and mapping.

## Related Documents

- [Sanity](../data/sanity.md)
- [Data ownership](../data/ownership.md)
