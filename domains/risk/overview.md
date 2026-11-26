# Risk: an introduction

## What this domain covers and why it matters

A broker that executes and clears derivatives for clients can lose money in three different places, and this domain keeps them apart:

1. **Risk we take on the clients we clear.** As clearing broker we guarantee our clients' trades to the CCP. If a client cannot pay a margin call, we still pay the CCP, and we may have to close out the client's positions at a loss.
2. **Execution risk.** Orders we send to venues can be wrong or too large, and trades we execute can stay with us if the clearing broker does not take them up.
3. **CCP risk.** As a clearing member we have money at each CCP (margin and default fund contributions) and we have promised more if another member defaults. If a member fails, or the CCP itself is in trouble, we can lose part of it.

The domain describes these risks in words: who could lose, toward whom, what limits apply and what happens when something goes wrong. It sets no risk model, scenario or limit value.

## Who is involved

- The **risk function** of the clearing broker or executing broker, which assesses clients and CCPs, sets limits and follows breaches. It is an internal team, not a party.
- The **client**, and the third parties that may guarantee it.
- The **executing broker** and the **trading venue member**, which control orders before they reach the venue.
- The **clearing member** and the **central counterparty**, with the CCP's default rules and resources.

## How it works in practice

**The clients we clear.** Before we clear for a client, the risk function reviews it, gives it an internal rating and sets limits: how much it may trade or how much exposure it may represent. Every day, and often during the day, we measure our exposure to the client after the collateral it gave us, and compare it with the limit. If the limit is exceeded, we warn, refer, ask for more margin or block new trades. If the client cannot pay, we declare it in default and close out, hedge or transfer its positions, using its collateral and any guarantee.

**Execution.** Each order is checked before it reaches the venue against limits such as a maximum size or a price collar. If something goes badly wrong, a kill switch cancels all of a participant's orders at once. When an order is executed wrongly by the executing side, the wrong part goes to an error account at the broker's own risk. And until the clearing broker takes up a given-up trade, the executing side keeps the trade and its risk.

**The CCPs.** Before joining a CCP and every year after, the risk function reviews it: its resources, its default rules and what it can ask from members. If a member defaults, the CCP uses resources in a fixed order, called the default waterfall: the defaulter's margin and default fund contribution, then its own capital, then the other members' contributions, then further calls on the surviving members. It auctions the defaulter's positions to the members. If all prefunded resources are used, it can pass losses on to members by other tools set in its rules.

## Ideas to hold apart

1. **Who could lose, toward whom.** Our exposure to a client, our exposure on trades not yet taken up, and our exposure to a CCP are three different measures; the CCP's exposure to us is what our margin covers.
2. **Exposure versus margin.** What we could lose is not the margin that must be posted.
3. **A firm limit versus a rule.** A limit our risk function sets is a decision; a position limit set by a regulator or venue is a rule; a concentration limit caps collateral.
4. **A check versus a breach.** A pre-trade check stops an order before a limit is exceeded; a breach is a limit already exceeded.
5. **Which default.** A client defaulting toward us, a clearing member declared in default by the CCP, and a CCP in recovery are three different events.
6. **Prefunded versus committed.** The default fund contribution is paid in advance; an assessment is a further payment the CCP may call after a default.
7. **Internal rating versus external rating.** Our grade of a client is not an agency rating or a regulatory classification.

## What is deliberately elsewhere

The clearing limit itself is on the give-up page, and the pre-trade control check on the execution page; both are shown here. Client default, clearing member default and porting are on the clearing services page. Margin, client margin uplifts and default fund contributions are on the margin page. Regulatory position limits are on the regulation page. Risk models, scenarios, limit values, risk appetite and capital requirements are not described at this phase.
