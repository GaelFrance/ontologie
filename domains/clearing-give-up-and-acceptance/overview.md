# Clearing: give-up and acceptance — an introduction

## What this domain covers and why it matters

Many clients execute listed futures and options with one broker and clear them with another. The step that moves a trade from the broker that executed it to the broker that will clear it is the **give-up**. Seen from the receiving side, the same step is a **give-in**. This domain describes that hand-over, the decisions that accept or refuse it, and the moment a central counterparty (CCP) legally steps into the trade.

It matters because the firm offers execution-only, clearing-only and execute-and-clear services. A late, rejected or partly accepted give-up leaves margin, risk and fees with the wrong firm until fixed.

## Who is involved

- The **client**, often acting through an investment manager, who decides where each part of a trade should be cleared.
- The **executing broker**, which fills the order, and its **giving clearing member**, which holds the trade at the CCP until the hand-over is done.
- The **clearing broker** and its **receiving clearing member**, which accept or refuse the trade.
- The **CCP**, which registers the trade and becomes the counterparty to each side.
- The **give-up agreement** signed by the client, the executing broker and the clearing broker, which says what may be given up, within which limits, and who bears a trade nobody takes up.

## How it flows in practice

The trade is executed on a venue. At many listed CCPs it is first registered to the executing side's clearing member (the exact sequence differs by CCP and is to be confirmed for each reference CCP). The client's allocation splits it into lines; each line meant for another clearing member becomes a give-up line. The receiving member checks the agreement, the account and its limit, then takes up all of the quantity, part of it, or none, before the CCP's deadline. The CCP then records the accepted quantity in the receiving member's account. The give-up is complete only when the full quantity is recorded there, and the CCP's record decides. If the line is rejected or lapses, the trade stays with the giving member.

On some markets the receiving member is named in advance and the CCP registers the trade straight to it. In OTC clearing there is no listed-style give-up: the trade is submitted for clearing, each side's clearing broker consents, and the CCP registers it.

## Ideas to hold apart

1. **Naming a clearing broker is not acceptance.** Only the receiving member's take-up or consent is.
2. **Member acceptance, CCP registration and the legal moment of clearing** are three steps. They sometimes happen at once, but not always.
3. **"Cleared" is a legal state.** A trade can be cleared while its give-up is still pending; the give-up changes who holds it.
4. **Complete, partial, rejected, lapsed** are different outcomes, and "no record" is not "pending".
5. **Give-up is not position transfer, porting or an OTC prime-brokerage give-up.**
6. **Novation is one way a CCP steps in, not the only one;** many listed CCPs use open offer.
7. **The give-up agreement allows give-ups; it does not oblige anyone to accept a given trade.**
8. **The executed trade, the CCP-facing trade and the member-client trade** are different agreements.

## What is deliberately elsewhere

Orders, executions, average pricing and allocation instructions are on the execution page. Clearing services, clearing members, CCP accounts, positions, client clearing agreements, position transfer and porting are on the clearing services page. Deadlines, exceptions and breaks are on the post-trade operations page; give-up fees and executing brokerage on the fees page. The firm's own deadlines, limits and practices are collected through company questions and kept in an internal layer, never in the ontology.
