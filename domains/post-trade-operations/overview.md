# Post-trade operations: overview

## What this domain covers

Post-trade operations is everything that happens to a trade after it is done and handed to clearing: the events that change it and the positions it creates, the deadlines each step must meet, the money and assets that must move, the checks that records agree, and the problems someone has to fix. It matters because this is where a missed deadline becomes a charge, a complaint or a risk, and where every status an operations agent reports comes from.

## Who is involved

The firm's operations teams, acting as clearing member toward the CCP and as clearing broker toward clients. The CCP, which registers trades, keeps positions and issues the daily reports and payment amounts. Executing and other clearing brokers on the other side of give-ups. Settlement banks and payment systems that move the cash. Clients and their investment managers, who send instructions.

## How it flows in practice

During the clearing day, trades and give-ups are registered at the CCP, each before its cut-off. Positions then change through new trades, take-ups, transfers, adjustments and, near expiry, through exercise, assignment and final settlement or delivery. At the end of the day (and at intraday cycles where the CCP runs them) the CCP reports trades, positions, margin and the cash due. Those amounts become settlement obligations, usually netted into one payment per currency, paid through a settlement bank before a settlement deadline. The firm passes the relevant amounts on to each client. Reconciliations compare the firm's records with the CCP's reports, broker statements, bank statements and client records. Any difference is a break. Breaks, rejected or lapsed give-ups, missed cut-offs and unpaid amounts raise operational exceptions, handled as cases until resolved. Nothing is deleted: a correction is a new event that points to the original.

## Ideas to hold apart

1. **What is owed, what was asked, what was paid.** A settlement obligation, a payment instruction and a cash movement are three different things with three different statuses.
2. **Break, exception, reject, fail.** A break says two records disagree, not which is right. An exception is a situation someone must act on. A rejected give-up is an event. A settlement fail is an amount not paid on time.
3. **The trade and its records.** One trade, many records of it (the firm's books, the CCP, the broker). Always say which source answered.
4. **Market cut-off and firm cut-off.** The CCP's deadline binds the firm; the firm sets earlier deadlines for clients and teams to meet it.
5. **Expiry, exercise, assignment, settlement.** The series ends; the holder uses the option; the exercise is allocated to short positions; the position is closed in cash or by delivery.
6. **Adjusting, transferring, amending.** Adjusting changes a position in the same account; transferring moves it to another account; amending changes or ends a trade.
7. **Dates have roles.** Trade date, clearing date, value date and due date can differ. "Today" means the CCP's clearing date unless stated.

## What is deliberately elsewhere

Orders, executions and allocation instructions sit with execution. The give-up line, take-up and CCP registration sit with clearing give-up and acceptance. Accounts, positions, position transfers and porting sit with clearing services and accounts. Margin requirements, margin calls and collateral sit with margin and collateral. Fee amounts and invoices sit with fees and revenue. Calendars, business dates and contract key dates sit with instruments, venues and calendars. How our own firm runs each of these steps is captured in the questions for our firm, never in the definitions.
