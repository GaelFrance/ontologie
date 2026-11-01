# Listed derivatives execution: an introduction

## What this domain covers

This domain describes how a client's order to buy or sell listed futures and options becomes executed trades, split across the right accounts and handed to clearing, either the firm's own or another clearing broker through a give-up.

It matters because every execution fee and revenue figure depends on knowing what was executed, for whom and through which channel, and because most give-up problems start here: a wrong account, a late allocation or a missing clearing designation.

## Who is involved

- The **client**, often acting through an investment manager, who gives orders and says how to split the result across accounts.
- The **executing broker**, who takes responsibility to the client for working the order.
- The **venue member**, admitted to enter orders on the venue: the executing broker itself or another firm it uses (third-party execution).
- The **trading venue**, which matches orders or registers negotiated trades.
- The **clearing broker** that will carry the trade for the client, which may be a different firm.

## How things flow in practice

A client sends an order. The desk either works it by hand (care), passes it to one of the broker's algorithms, or lets the client route it electronically through the broker's infrastructure (direct market access) or straight to the venue under the broker's membership (sponsored access). Working the order usually creates several smaller child orders, each of which may be filled several times. A large trade may instead be negotiated privately and registered on the venue as a block trade, or as an exchange of futures against a related position.

The broker then reports executions back to the client, sometimes at one average price across all fills. The client, or a standing instruction agreed in advance, says how to split the quantity across its accounts. Each part goes either to an account the firm clears itself, or to another clearing broker through a give-up. From that point the clearing domain takes over. If the other clearing broker rejects the trade or does not take it up in time, the executing side keeps it.

## Ideas to keep apart

1. **The client's order and the orders the broker sends to the venue** are different orders, linked parent to child.
2. **A fill on the venue, a fill reported to the client and an allocation line** are three different records; their counts differ.
3. **An execution and a trade** are not the same: one is an event on an order, the other an agreement between two counterparties.
4. **How an order was worked (channel), what the client is allowed to do (access), and how the price was formed (execution method)** are three separate facts.
5. **The broker serving the client, the firm entering the order on the venue, the firm named in regulatory reports and the clearing member that first receives the trade** can be four different firms.
6. **Averaging and allocation**: one sets a single price, the other splits quantity.
7. **An internal allocation and a give-up**: only an allocation to another clearing broker's account starts a give-up.

## What is deliberately elsewhere

Clearing acceptance and CCP registration are on the clearing pages; fees, brokerage and revenue on the fees page; venues, contracts and trading calendars on the instruments page; client permissions for electronic access on the market access page; transaction reporting and best execution on the regulation page. Execution of OTC derivatives on swap facilities is not covered by any page yet.
