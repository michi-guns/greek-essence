# Customer Contact Recognition Contract

## Authority and Scope

This contract is normative for Request Processing and Communications D-002. It
defines how requests are grouped for internal staff context without customer
accounts.

It does not define correction, duplicate-submission, authentication, retention,
privacy-request verification, or staff-interface mechanics. D-003 and later
decisions own those boundaries.

## Contact Relationship

1. The normalized submitted email address identifies an internal
   customer-contact relationship.
2. Accepted requests using the same normalized email may be grouped for staff
   context across Consultation Request, Booking Request, and General Contact.
3. The relationship is not a customer account, login, verified identity, or
   proof that every grouped request came from one person.
4. Different email addresses remain separate unless authorized staff safely
   establish the relationship during manual follow-up.
5. The system must not automatically merge relationships using names,
   telephone numbers, or approximate matching.

Exact normalization mechanics remain an implementation contract, but they must
not apply provider-specific transformations that can change address ownership
or silently merge distinct mailboxes.

## Immutable Request Contact Snapshot

Every accepted request preserves the contact values submitted for that request.
A later request may add current information to the grouped relationship, but it
must not overwrite, rewrite, or detach the earlier request's snapshot.

This preserves what the visitor submitted and what the agency acted upon at the
time. D-003 must define corrections as explicit history rather than authorize
in-place replacement.

## Privacy Boundary

Public forms must not, based only on a submitted email address:

- reveal whether earlier requests exist;
- list or summarize earlier requests;
- prefill earlier personal information; or
- claim that the visitor is a recognized or verified customer.

Any later access to request history requires a separately accepted verification
boundary. Customer accounts and public request history remain deferred.