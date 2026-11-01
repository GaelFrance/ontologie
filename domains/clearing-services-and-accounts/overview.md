# Clearing services, accounts and client clearing: an introduction

## What this domain covers and why it matters

Once a derivative trade is executed, a central counterparty (CCP) steps in between buyer and seller and guarantees it. This domain describes where that cleared trade lives and on what terms: which clearing service clears it, which firm answers to the CCP, which firm clears for the client, which CCP account holds the position, how the client's assets are kept apart from others, and what happens when a client moves or a member fails. Getting this right answers two pilot questions: "can we clear for client X at CCP Z, and how?" and "where does this trade land?"

## Who is involved

The CCP, which runs one or more clearing services. Clearing members, admitted to a service in a category that says whether they may also clear for clients. Clearing brokers, who clear for clients, as members or through one. Clients, and sometimes their own clients (indirect clients). In the US, the clearing broker is usually registered as a futures commission merchant (FCM).

## How things flow in practice

A client signs a client clearing agreement with a clearing broker. The agreement fixes the legal model (the broker deals with the CCP as principal and faces the client back-to-back, or acts as agent and guarantor), and the client elects how its positions are segregated: in an omnibus account shared with other clients, or in an individually segregated account. The clearing member opens the matching account at the CCP for each clearing service. The CCP registers the client's trades into that account, where they form positions; the broker maps its own client account to it. If the client changes broker, its open positions can be transferred. If the clearing member defaults, the CCP tries to port the client's positions and collateral to a back-up member, or else closes them out.

## Ideas to keep apart

1. **A clearing service is not the CCP.** Membership, accounts, margin and default funds are set per service.
2. **Clearing member, clearing broker and FCM are three different things:** admission at a CCP, a service to a client, and a US registration.
3. **Four separate answers describe a client's clearing:** the access route, the legal model, the segregation election and the CCP account kind. None of them alone says what legal protection the client has; only Legal concludes that.
4. **The CCP account, the broker's internal client account and the give-up reference are three levels.** The reference is a code, not an account.
5. **Omnibus means different things** in the EU, in the US and in a broker's own books.
6. **One position, several records.** The CCP statement and the internal books describe the same position; a difference is a break to resolve.
7. **Give-up, position transfer and porting differ:** a new trade attributed to a member, a requested move of open positions, and a default-triggered move of positions and collateral.
8. **Clearing creates new trades.** The executed trade is replaced by trades with the CCP and, under the principal model, a back-to-back trade between broker and client.

## What is deliberately elsewhere

Give-up and acceptance are on the give-up page; margin, collateral and default funds on the margin page; regulatory statuses such as FCM on the regulation page; access arrangements and the firm's service offering on the market access page; transfer and porting fees on the fees page. Which services, models and accounts the firm actually offers is an internal fact, captured through the company questions, never in the ontology itself.
