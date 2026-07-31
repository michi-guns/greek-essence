# Editorial Content Platform Grilling

## Status

Active Foundation Design grill. This ledger does not authorize application
implementation, dependency installation, Sanity project configuration, schema
migration, deployment, or production access.

## Owning Layer and Purpose

Owner: Foundation Design — Editorial Content Platform.

Define the durable Sanity and Next.js foundations for representing, reviewing,
previewing, publishing, withdrawing, rendering, refreshing, and searching Greek
Essence's bilingual public content. Preserve accepted Product and Domain Truth
and the accepted System Boundaries and Domain Representation decisions without
reopening the selected technology stack.

## Accepted Inputs

- Next.js owns the public application and server-side orchestration.
- Sanity owns editable public and catalogue content. Private customer and Request
  data never enters Sanity.
- English and Greek are complete, separately represented, human-approved, and
  meaning-equivalent public experiences. Mixed-language, machine-only, and
  silent-fallback content is not finished public copy.
- Giorgos or an authorized agency delegate approves business content. The
  technical publisher checks technical preview and publication requirements but
  does not become responsible for approving agency facts, claims, prices, media
  rights, or commercial meaning.
- A useful standalone Destination may publish without a published Experience.
  Every published Experience requires at least one genuinely valid published
  Destination relationship, and all valid Destination relationships are equal.
- Every Experience has one immutable published Sanity document ID shared with
  accepted Booking Request records. Localized titles, slugs, and URLs are
  editable attributes rather than identity.
- Experience publication does not enable Booking Requests automatically.
  Requestability is an explicit per-Experience choice and never implies current
  availability or confirmation.
- A published Experience must satisfy its bilingual content, type,
  Destination, claim, media, requestability, and conditional indicative-price
  requirements.
- Withdrawn optional content leaves discovery and provides generic bilingual
  recovery at its former URL without stale claims, prices, or media. Required
  pages must be replaced or redirected, or their dependent journey must be
  disabled honestly.
- Named reviewers, publishers, production access holders, approved launch
  content, provider-account evidence, and completed operational proof remain
  Launch Readiness matters.

## Locked Technical Direction

Do not reopen Next.js or Sanity selection. Exact package versions and provider
configuration are implementation-time work. Current first-party Sanity guidance
recognizes field-level localization in one document and document-level
localization through linked documents as distinct modelling strategies; the
choice here must fit Greek Essence's already accepted identity, bilingual
publication, relationship, and withdrawal invariants.

Reference used for current Sanity capability context:
<https://www.sanity.io/docs/studio/localization>

## Explicit Boundaries

This track may define:

- Sanity document and reference structure;
- English/Greek representation and publication coupling;
- publication, requestability, and relationship validation contracts;
- approval and evidence metadata structure without assigning named people;
- preview, draft, revision, withdrawal, and recovery mechanisms;
- Next.js rendering, caching, revalidation, search, and freshness contracts; and
- durable Sanity roles and permission boundaries without assigning production
  accounts.

This track must not approve actual copy, claims, prices, media rights, legal
wording, named owners, credentials, quotas, account access, or launch evidence.
It must not define private Request storage, Drizzle schemas, application module
layout, deployment topology, or production operations owned by later tracks.

## Locked Decisions

### D-001 — One Bilingual Sanity Document per Public Content Item

Each public content item is represented by one Sanity document containing
separate English and Greek values for visitor-facing content. Shared facts and
relationships—such as Experience type, Destination references, requestability,
and the item's stable identity—exist once in that document rather than being
duplicated per language.

The document may publish only when both complete language experiences and their
applicable human approvals satisfy the publication gate. English and Greek
therefore publish, revise, and withdraw together at the document level rather
than operating on independent public schedules. The localized copy remains
separately written and approved, may be natural rather than literal, must be
meaning-equivalent, and cannot use silent fallback or machine-only text as
finished public content.

This preserves one accepted business item and one immutable published Sanity
document ID across editorial and Request boundaries. It also avoids duplicated
Destination relationships, requestability, withdrawal state, and
cross-language coordination. Exact localized field and object types remain for
the document-structure decision and bounded technical design.

Separate linked documents per language were rejected because they would make
identity, relationships, completeness, requestability, and withdrawal harder to
coordinate without providing a needed independent publication schedule. A
shared core plus separate English and Greek content documents was rejected
because three records per item would add joins, validation, and recovery paths
without proportionate launch value.

## Open Questions

- D-002: Which public surfaces require dedicated Sanity documents, reusable
  objects, or singleton records?
- D-003: Which validation and approval state must gate publication and
  requestability?
- D-004: How should claim, price, and media evidence metadata support technical
  publication checks without transferring business approval?
- D-005: How should drafts, preview, revisions, withdrawal, and former-URL
  recovery work together?
- D-006: How should Next.js rendering, caching, revalidation, localized search,
  and freshness preserve published Sanity truth?

## Next Question

ID: D-002

Owning layer: Foundation Design.

Topic:
Sanity document types, singleton pages, and reusable content objects.

Prompt:
How should Greek Essence divide its confirmed public content among repeatable
Sanity document types, one-off singleton page records, and reusable embedded
objects?

Options:

1. (recommended): **Use explicit document types for real public items, one
   controlled singleton record for each unique page or shared site concern, and
   reusable objects only inside those records.** Destinations and Experiences
   are repeatable documents. Confirmed one-off surfaces such as Home and About
   each have one editable record rather than an unlimited collection. Shared
   structures such as localized text, calls to action, media with approval
   metadata, and structured page sections are reusable object definitions
   embedded in the owning document, not independently publishable content.
2. **Use specialized Destination and Experience documents but one generic Page
   document type for all other public pages.** This reduces the number of schema
   types, but Home, About, request introductions, and required policy or service
   pages would rely more heavily on conditional fields and editor discipline,
   making page-specific publication rules less explicit.
3. **Build pages primarily from independently managed reusable section
   documents.** Home, About, and other pages assemble references to shared hero,
   text, media, or action records. This maximizes reuse and rearrangement, but
   creates more records, reference states, approval coordination, and withdrawal
   paths than the preview currently needs.

Why this matters:

This decision controls what the technical publisher sees in Sanity Studio and
where validation belongs. For example, the recommended model gives the
publisher a list of many Destination and Experience records but exactly one
Home record and one About record. A reusable call-to-action object defines a
consistent field shape inside those pages without creating a separate public
record that could be edited or withdrawn out of context.

The recommendation makes each editorial record correspond to something the
agency recognizes, allows specific validation for materially different content,
and prevents accidental duplicate Home or About pages. It still reuses field
structures where that reduces inconsistency, without turning small page sections
into a web of separately published records. Its tradeoff is a modest number of
clear schema types rather than one highly generic page builder.

After answer:

- Lock the public document, singleton, and embedded-object boundaries.
- Record only confirmed public surfaces; do not invent actual content or launch
  approval through the schema classification.
- Store D-003 as the next question.
