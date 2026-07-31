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

### D-002 — Explicit Documents, Controlled Singletons, and Embedded Objects

Greek Essence uses explicit Sanity document types for materially different
public content items. Destinations and Experiences are repeatable document
types. Each confirmed unique public page, including Home and About, has one
controlled singleton record so the publisher cannot create competing copies.
Any confirmed shared site concern that requires one authoritative editable
record may use the same singleton pattern.

Reusable structures—such as localized text, calls to action, media with
approval metadata, and structured page sections—are reusable object definitions
embedded within the document that owns their values. They are not independent
public documents with separate publication, approval, reference, or withdrawal
lifecycles.

This makes Sanity Studio correspond to content items the agency recognizes,
supports type-specific validation, and prevents accidental duplicate one-off
pages. It accepts a modest number of clear schema types instead of one generic
page builder. Only confirmed public surfaces may receive a document or singleton
type; the classification does not invent content, claims, or launch approval.

One generic Page document type was rejected because materially different pages
would depend on conditional fields and editor discipline rather than clear
page-specific structure and publication rules. Independently managed reusable
section documents were rejected because their extra records, references,
approval coordination, and withdrawal paths add complexity without
proportionate preview-release value.

## Open Questions

- D-003: Which validation and approval state must gate publication and
  requestability?
- D-004: How should claim, price, and media evidence metadata support technical
  publication checks without transferring business approval?
- D-005: How should drafts, preview, revisions, withdrawal, and former-URL
  recovery work together?
- D-006: How should Next.js rendering, caching, revalidation, localized search,
  and freshness preserve published Sanity truth?

## Next Question

ID: D-003

Owning layer: Foundation Design.

Topic:
Publication validation and approval state.

Prompt:
What must Sanity verify and record before a bilingual public document can be
published, and how should later edits affect that approval?

Options:

1. (recommended): **Require both automated publication validation and explicit
   current business approval.** Sanity blocks publishing until the document is
   structurally complete for both languages, all applicable relationships and
   conditional fields pass, required claim/media/price evidence is present, and
   the current public meaning has recorded agency approval. The technical
   publisher separately confirms preview and technical readiness. A material
   edit to approved public meaning makes the relevant approval stale and the
   changed draft cannot publish until it is reapproved. Requestability remains
   an explicit shared Experience choice and is effective only on a currently
   published, otherwise eligible Experience.
2. **Use automated validation plus one combined “ready to publish” state set by
   the technical publisher.** The publisher confirms that external approval was
   obtained and that technical checks pass, but Sanity does not preserve the
   business-approval boundary separately. This is simpler but makes it harder to
   show whether Giorgos or an authorized delegate approved the current meaning,
   and risks transferring practical approval responsibility to the publisher.
3. **Use automated structural validation only and keep approval outside
   Sanity.** Sanity blocks incomplete fields and relationships, while approval is
   coordinated through email or conversation and the publisher uses the normal
   Publish action. This has the least CMS workflow, but approval can become
   detached from the exact revision being published and later edits may retain
   no visible indication that reapproval is needed.

Why this matters:

Sanity normally keeps edits as a private draft until someone publishes them, and
its validation errors can block the standard Publish action. Validation can
prove facts such as “both titles exist” or “this Experience has a published
Destination reference,” but software cannot decide whether a commercial claim
is true or whether media use was approved. The document therefore needs a clear
boundary between automatic completeness checks, agency approval of business
meaning, and the publisher's technical preview check.

For example, an Experience draft may have complete English and Greek copy and a
valid Destination but contain a claim about local expertise. Automated
validation can confirm that required approval evidence is attached; Giorgos or
an authorized delegate must still approve the claim itself. If the claim is
later rewritten, the earlier approval must not silently authorize the changed
meaning. The recommendation keeps that distinction explicit without adding a
large editorial workflow system. Exact evidence fields, approver metadata, and
change-invalidation mechanics remain D-004 or bounded technical design.

After answer:

- Lock the publication validation, approval, edit-invalidation, and
  requestability gate boundaries.
- Preserve exact evidence fields and approver metadata for D-004.
- Store D-004 as the next question.
