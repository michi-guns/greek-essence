# Foundation Design Track Map

This file defines the dependency order for Foundation Design. It is structural
routing, not a progress tracker. Root `NEXT.md` and the active work-item handoff
own current status and continuation.

## Sequence

### 1. System Boundaries and Domain Representation

Establish which service owns each data class, the launch entities and value
objects, relationships, cardinalities, identifiers, lifecycle invariants,
cross-service references, and immutable snapshots.

### 2. Editorial Content Platform

Define Sanity documents, references, English/Greek representation, publication
contracts, evidence metadata, preview, revisions, withdrawal, rendering,
caching, revalidation, search, and freshness.

### 3. Transactional Data Platform

Define Neon and Drizzle schemas, constraints, indexes, transactions, migrations,
connection handling, Drizzle-Zod and handwritten Zod responsibilities,
idempotency, audit, retention, deletion, and backup representation.

### 4. Application Architecture

Define App Router composition, feature and shared module boundaries, Route
Handlers, server-only data access, browser/server entry points, dependency
direction, and Server/Client Component boundaries.

### 5. Runtime and Production Foundations

Define development/preview/production topology, secrets, deployment and migration
ordering, rollback compatibility, mail recovery, observability, quota behavior,
backup, deletion-safe restore, and hosting-fallback implications.

## Dependency Rule

A track may expose a missing upstream product or foundation decision. Route that
issue back to its owner and resolve it before continuing; never encode a
convenient assumption in a downstream schema or provider configuration.

The locked stack and full classification are recorded in
[`../CLASSIFICATION.md`](../CLASSIFICATION.md).
