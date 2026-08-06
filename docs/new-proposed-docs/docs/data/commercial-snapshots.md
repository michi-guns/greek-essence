---
status: active
owner: product-and-engineering
related-adrs:
  - ADR-0004
---

# Commercial Snapshots

When a catalog offering enters a quote or booking, store its relevant commercial
data in PostgreSQL.

Snapshot at least:

- Source Sanity document ID
- Source revision when useful
- Title
- Relevant description
- Dates
- Quantity
- Unit price
- Tax
- Discount
- Total
- Currency
- Material cancellation terms

## Invariant

```text
Sanity price changes from €500 to €650.

Existing accepted quote: remains €500.
Existing booking: remains €500.
New quote: may use €650.
```

Historical records must remain understandable even if the source content is
withdrawn or deleted.
