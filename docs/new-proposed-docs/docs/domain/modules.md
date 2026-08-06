# Domain Modules

## Customers

Owns customer identity, contact information, and commercial relationship data.

## Travelers

Owns traveler identity and travel-specific personal details.

## Catalog

Represents sellable offerings exposed by an application-facing catalog port.
Sanity is the initial adapter.

## Quotes

Owns commercial proposals, quote items, pricing, validity, and acceptance.

## Bookings

Owns operational commitment, booking state, booked services, and historical
commercial records.

## Payments

Owns customer payments, refunds, and allocation against bookings.

## Suppliers

Owns providers, supplier references, obligations, confirmations, and payable
amounts.

## Documents

Owns metadata and generation workflows for quotations, confirmations, vouchers,
tickets, itineraries, invoices, and cancellation records.

These boundaries may change through ADRs as real business behavior becomes
clearer.
