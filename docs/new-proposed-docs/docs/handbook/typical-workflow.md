# Typical Workflow

This is the initial working model, not a final business requirement.

```text
1. Create or find a customer.
2. Add the actual travelers.
3. Create a draft quote.
4. Select catalog offerings from Sanity.
5. Snapshot commercial details into PostgreSQL.
6. Apply prices, taxes, and discounts.
7. Send the quote.
8. Record acceptance or rejection.
9. Create or confirm the booking.
10. Record customer payments.
11. Track supplier confirmations and obligations.
12. Produce confirmations, vouchers, or itineraries.
```

## Important distinctions

- The customer pays or owns the commercial relationship.
- Travelers receive the travel services.
- A quote is a proposal.
- A booking is an operational and commercial commitment.
- Catalog content may change.
- Historical quote and booking data must not change with it.

## Verification status

This workflow is a starting hypothesis. Open questions belong in
[`../domain/open-questions.md`](../domain/open-questions.md), and uncertain
rules belong in [`../domain/assumptions/`](../domain/assumptions/).
