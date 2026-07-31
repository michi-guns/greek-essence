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

None yet.

## Open Questions

- D-001: How should one public content item represent its English and Greek
  content in Sanity?
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

ID: D-001

Owning layer: Foundation Design.

Topic:
Bilingual Sanity representation and publication coupling.

Prompt:
How should one Greek Essence public content item—such as an Experience,
Destination, Home, or About—represent its English and Greek content in Sanity?

Options:

1. (recommended): **Keep one Sanity document per content item, with localized
   English and Greek values inside it.** Shared facts and relationships—such as
   Experience type, Destination references, and requestability—exist once, while
   title, summary, detail copy, slug, labels, and other visitor-facing wording
   have separate English and Greek values. The document publishes only when both
   complete language experiences and their approvals satisfy the relevant gate.
2. **Keep a separate linked Sanity document for each language.** English and
   Greek can have independent drafts and publication timing, but identity,
   references, withdrawal, requestability, completeness, and cross-language
   consistency must be coordinated across multiple documents. This adds a
   translation relationship and makes the already accepted single shared
   Experience identity harder to preserve cleanly.
3. **Use a shared core document plus separate English and Greek content
   documents.** Shared facts and relationships live in the core while each
   language has its own linked content record. This separates responsibilities
   explicitly but creates three records and additional joins, validation, and
   recovery paths for every bilingual item.

Why this matters:

This decision becomes the base for every later Sanity schema, relationship,
publication check, preview, revision, query, and search index. For example, if a
technical publisher corrects a Greek Experience summary, the chosen model
controls whether they edit one bilingual Experience or a separate Greek record,
how the English equivalent and shared requestability state are checked, and
which immutable Sanity ID a later Booking Request uses.

The recommendation keeps one accepted business item and one stable identity,
avoids duplicated relationship and withdrawal state, and matches the release
rule that both English and Greek must be complete before the item is public. It
still permits natural, non-literal copy in each language. Its tradeoff is that
English and Greek publish together rather than on independent schedules, which
is consistent with the current two-language launch boundary.

After answer:

- Lock the bilingual document representation and publication coupling.
- Preserve exact field types and Studio implementation for bounded technical
  design unless they are required by the chosen foundation.
- Store D-002 as the next question.
