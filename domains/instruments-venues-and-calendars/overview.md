# Instruments, venues and calendars: an introduction

## What this domain covers

This domain describes **what is traded, where it is traded, and on which day it counts**. Every other part of the business leans on it: an order names a contract, a trade happens on a venue, a give-up has a deadline on a given day, a fee is charged per contract. Misread the contract, the venue or the date, and every answer built on it is wrong.

## Who is involved

Trading venues list contracts, run sessions and publish trading calendars. Central counterparties decide what they can clear and publish clearing calendars. Numbering agencies issue identifiers. Payment systems publish the days each currency can be paid. Inside the firm, the reference-data team keeps these records; product owners and operations rely on them.

## How things flow in practice

A venue decides to list a new contract, for example a future on a stock index. It publishes a **contract specification**: the underlying index, the contract size, the price tick, the expiry months, the rule that fixes the last trading day, and whether the contract settles in cash or by delivery. From this template the venue creates tradeable **series**, one per expiry month (and, for options, one per strike and call or put). Each series is an **instrument** that people can buy and sell. Venues may also list **strategies**, such as a spread between two expiries, traded in one go.

Trading happens in **sessions**: an opening auction, continuous trading, sometimes an evening session. The venue's **calendar** says which days are open and which **business date** each session counts towards; an evening session often counts towards the next day. The CCP has its own calendar, and so does each currency's payment system. Every date in the business therefore has a **role** (trade date, clearing date, value date, last trading day) and is read against a named calendar in a named time zone. Unless someone asks otherwise, "today" means the clearing date of the relevant CCP.

Contracts change: venues publish notices that move a holiday, extend trading hours, adjust a contract after a corporate action or delist a series. Each change has an effective date and ripples into deadlines, margin runs and fees.

OTC derivatives usually have no listing and no series. A standard product, such as a fixed-to-floating swap in one currency, is classified and may carry a product identifier; each swap's own terms live in the trade.

## Ideas to hold apart

1. **Product family, contract specification, instrument and service.** "Product" can mean any of these; always ask which.
2. **The thing and its identifier.** An identifier points to a thing within one scheme; a classification code describes it but does not identify it.
3. **The venue, its operator, its group and the CCP.** "The exchange" can mean any of the first three.
4. **Listed, on-venue and cleared.** They are three separate questions.
5. **A date and its role.** Trade date, clearing date and the date on the clock can differ.
6. **One calendar per scope, not per country.** A venue may be open while one contract or one currency is closed.
7. **Eligible, mandatory and offered.** A CCP can clear it, a rule may require it to be cleared, the firm may or may not offer it.

## What is deliberately elsewhere

Memberships and access sit on the parties, execution and service-offering pages; clearing services, accounts and positions on the clearing pages; deadlines and events such as expiry and exercise in post-trade operations; venue types and clearing obligations in regulation. Which contracts and venues the firm covers is internal knowledge, never written into the public ontology.
