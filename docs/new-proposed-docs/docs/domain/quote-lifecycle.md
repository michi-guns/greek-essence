---
status: draft
owner: product-and-engineering
---

# Quote Lifecycle

Initial proposal:

```text
Draft → Sent → Accepted
             ↘ Rejected
             ↘ Expired
```

## Candidate rules

- A draft quote can be edited.
- A sent quote may require versioning before material changes.
- An accepted quote preserves its commercial snapshot.
- An expired quote cannot be accepted without reactivation or a replacement.
- Acceptance should record actor, time, and accepted version.

## Unverified questions

- Can staff create a booking without a quote?
- Can an accepted quote be changed?
- How is customer acceptance recorded?
- Are partial acceptances possible?

Do not treat candidate rules as confirmed requirements until verified.
