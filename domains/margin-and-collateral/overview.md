# Margin and collateral: an introduction

## What this domain covers and why it matters

When a derivatives trade is cleared, the central counterparty (CCP) guarantees it. To protect itself if a clearing member fails, the CCP asks each member for **margin**, and the member in turn asks its clients. Margin is paid in cash or delivered as securities, called **collateral**. This domain describes how much margin is required, how it is demanded, which assets may cover it, at what value, under which legal terms, and how collateral moves, earns interest and is returned.

It matters to the business in three ways. Margin calls carry strict deadlines: a missed call can lead to a default procedure under the CCP's rules or the client agreement. Collateral ties up the client's and the firm's balance sheet, so it drives cost and client experience. And collateral produces income, such as interest on client cash, which management needs to see apart from fees.

## Who is involved

- The **CCP**, which sets its margin model, publishes the assets it accepts and calls its members.
- The **clearing member or clearing broker**, which pays the CCP and calls its clients, often with its own uplift.
- The **client**, and sometimes the client's own clients (indirect clients).
- Banks, custodians and settlement systems that hold and move the assets.

## How it works in practice

Every day, and often several times a day, the CCP runs its margin model over each account's positions. The run gives an initial margin figure (enough to close out the positions if the member defaults) and a variation margin figure (the day's gain or loss). The CCP compares what is required with the collateral it already holds, after cutting each asset's value by a haircut. If there is a shortfall, it issues a margin call with a deadline. The member pays cash or delivers eligible securities. The member then does the same with each client, under the terms of its client clearing agreement. Excess collateral can be returned on request, and one asset can be swapped for another. Interest accrues on cash collateral, and a separate price alignment amount neutralises the interest effect of variation margin flows.

## Ideas to hold apart

1. **Requirement, call, collateral and movement** are four different things: what is owed, the demand, what is held, and the transfer.
2. **Tier**: what the CCP requires from the member is not what the member requires from the client.
3. **Initial margin versus variation margin**: protection against future loss versus settlement of today's change in value.
4. **Settled versus collateralised variation margin**: a final payment, or collateral to be returned.
5. **Eligible versus held**: an asset on the accepted list is not collateral until it is delivered.
6. **Methodology versus margin levels**: a new model is not the same as new daily rates.
7. **Margin versus default fund**: the defaulter's own protection versus a shared pool.
8. **Price alignment versus interest on cash**: two different amounts with different purposes.

## What is deliberately elsewhere

The accounts in which margin is recorded, the segregation choices and porting are on the clearing services page. Payments, deadlines as operational events and reconciliations are on the post-trade page. Whether collateral income counts as revenue is on the fees page. CCP circulars that change models or eligible assets are on the regulation page. Margin for uncleared bilateral trades is out of scope.
