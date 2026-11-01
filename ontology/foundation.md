# Foundational concept catalogue

Status: Draft for all entries (LD-C0001 to LD-C0074). Type assignments and definitions are proposals.

This catalogue is the single index of concept IDs: one row per ID, including later additions and any future deprecations. It does not claim to complete the [full concept template](../templates/concept-template.md). IDs are stable across future renaming, relocation and format migration. Common means shared stewardship, not exclusive domain use.

Definitions changed by the 2026-11 expert review are listed with their rationale in the [change log](../CHANGELOG.md) and the [arbitration record](../governance/reviews/2026-11-expert-review/ARBITRATION.md). Aliases, specialisations, usage notes, French labels and standard alignments are kept in [concept annotations](concept-annotations.md) so that this table keeps its five-column layout.

## Phase 1 foundation (LD-C0001 to LD-C0050)

| ID | Canonical English name | Owning module | Proposed type | Working business definition |
|---|---|---|---|---|
| LD-C0001 | Party | Common | Entity | Identifiable actor that can participate in a business relationship. |
| LD-C0002 | Legal Entity | Common | Entity | Organisation or structure recognised as a legal entity under the applicable framework. |
| LD-C0003 | Party Role | Common | Role | Contextual, time-bounded holding of a function by a party (party-in-role) toward identified counterparties, within a service and, where applicable, under an agreement; role kinds such as Client or Clearing Member are its specialisations. |
| LD-C0004 | Client | Common | Role | Role of a party receiving a service from an identified provider; contractual and commercial attribution must be distinguished. |
| LD-C0005 | Broker | Common | Role | Role of a party that acts on behalf of others to execute orders and/or to clear or carry their trades under an identified agreement. |
| LD-C0006 | Executing Broker | Common | Role | Role of the party providing the execution service concerned. |
| LD-C0007 | Clearing Member | Common | Role | Role of a party admitted to a clearing service (LD-C0051) under a membership category, entitling it to have transactions registered in its name in CCP accounts within that category's clearing scope. |
| LD-C0008 | Central Counterparty | Common | Role | Role of an entity interposed as counterparty through the applicable legal mechanism. |
| LD-C0009 | Trading Venue | Common | Entity | Organised trading facility or framework, distinguished from its legal operator and reporting facilities. |
| LD-C0010 | Account | Common | Entity | Business structure for attribution and recording, with an explicit function, maintaining party and relevant holders. |
| LD-C0011 | Segregation Model | Common | Reference Concept | Rules for separating positions, assets or records under a specified legal and operational framework. |
| LD-C0012 | Agreement | Common | Agreement | Arrangement governing services, rights and obligations between parties. |
| LD-C0013 | Product Family | Common | Reference Concept | Classification grouping of instruments or trades sharing economic and contractual characteristics, independent of any venue; not a venue's contract specification (LD-C0062) and not a service offering (LD-C0052). |
| LD-C0014 | Instrument | Common | Entity | Standardised derivative specification, identifiable independently of any counterparty pair and any single trade, at the level at which it is listed or assigned an instrument identifier (for listed derivatives, the series); a bespoke OTC contract is not an instrument and its terms belong to the Trade. |
| LD-C0015 | Business Date | Common | Reference Concept | Date assigned to a business object or event under a stated date role, resolved against a named business calendar (LD-C0066) and time zone. |
| LD-C0016 | Order | Execution | Instruction | Instruction from one party to another, or to a trading venue, to buy or sell a specified quantity of an instrument under stated execution conditions. |
| LD-C0017 | Execution | Execution | Event | Event fulfilling all or part of a trading instruction. |
| LD-C0018 | Trade | Common | Agreement | Agreed derivative transaction, distinguished from operational records and subsequent legal transformations. |
| LD-C0019 | Transaction | Common | Event | Business operation affecting rights, obligations or balances; this broad working definition requires validation and must not become a catch-all synonym. |
| LD-C0020 | Allocation | Common | Process | Assignment of a quantity or amount to target beneficiaries or accounts; instruction and completed event are later specialisations. |
| LD-C0021 | Average Price Group | Common | Entity | Grouping of eligible executions or trades subject to a specified average-pricing method. |
| LD-C0022 | Give-up / Take-up Process | Common | Process | Process by which all or part of an executed listed-derivative trade is attributed for clearing from the executing side to a receiving clearing member, through a give-up instruction and that member's acceptance or rejection; depending on the clearing service it occurs at or after CCP registration. Instructions, acceptance events and legal effects remain distinct. |
| LD-C0023 | Clearing Acceptance | Common | Event | Acceptance or registration of a trade by a central counterparty into a specified clearing service under defined criteria; evidence of, not identical to, CCP interposition (LD-C0054). A clearing member's take-up is LD-C0053. |
| LD-C0024 | Novation | Common | Event | Legal replacement of an obligation or contract by new obligations; applicability and effect depend on the governing framework. |
| LD-C0025 | Lifecycle Event | Common | Event | Occurrence affecting the existence, characteristics or obligations of a business object. |
| LD-C0026 | Position | Common | State | Resulting exposure or quantity for a defined scope, aggregation basis and as-of time. |
| LD-C0027 | Portfolio | Common | Entity | Delimited collection of business objects used for management, calculation or reporting. |
| LD-C0028 | Settlement Obligation | Common | Obligation | Duty to transfer cash or an asset under specified terms and due date. |
| LD-C0029 | Cash Movement | Common | Event | Observed movement of funds, distinct from the preceding obligation or instruction; booking and settlement evidence require context. |
| LD-C0030 | Operational Exception | Common | State | Situation requiring handling because an expected rule or outcome is not met. |
| LD-C0031 | Fee Charge | Common | Obligation | Chargeable or charged amount for a service or event, with identified debtor and creditor; stage and enforceability must be qualified. |
| LD-C0032 | Fee Schedule | Common | Reference Concept | Tariff and rules used to determine charges. |
| LD-C0033 | Client Execution Fee | Execution | Obligation | Fee owed by a client to a provider for execution services. |
| LD-C0034 | Client Clearing Fee | Common | Obligation | Fee owed by a client to a provider for ETD or OTC clearing services. |
| LD-C0035 | Executing Broker Brokerage Charge | Common | Obligation | Remuneration owed to an executing broker in an identified payment relationship. |
| LD-C0036 | Exchange Fee Charge | Common | Obligation | Charge attributable to an exchange service, with service nature and beneficiary specified. |
| LD-C0037 | CCP Fee Charge | Common | Obligation | Charge attributable to a CCP service, distinct from margin requirements. |
| LD-C0038 | Commission | Common | Reference Concept | Contractual remuneration category whose boundaries and overlap with fee types require business validation. |
| LD-C0039 | Revenue | Common | Measure | Income attributable to business activity from an observing entity perspective under an explicit management measurement basis; not automatically profit or cash received. |
| LD-C0040 | Cost | Common | Measure | Cost attributed to an observing entity or activity under an explicit management basis; inclusion in contribution or profitability measures requires a defined cost perimeter. |
| LD-C0041 | Execution Revenue | Execution | Measure | Revenue attributable to execution services under a defined semantic contract. |
| LD-C0042 | Clearing Revenue | Common | Measure | Revenue attributable to clearing services under a defined semantic contract. |
| LD-C0043 | Margin Requirement | Common | Measure | Amount of margin that a margin provider is required to provide to a margin taker for an identified account or risk scope, determined under an identified methodology or contractual rule at a stated as-of time and currency basis; distinct from the call that demands it and the collateral that covers it. |
| LD-C0044 | Initial Margin Requirement | Common | Measure | Margin requirement intended to cover potential future exposure over an assumed close-out period at a stated confidence level under the applicable methodology, including the add-ons that methodology applies. |
| LD-C0045 | Variation Margin Requirement | Common | Measure | Amount payable or receivable reflecting the change in value of positions since the previous margin cycle, with direction stated from the observing party; under settled-to-market treatment it gives rise to a Settlement Obligation, under collateralised-to-market treatment to collateral that must be returned as exposure changes. |
| LD-C0046 | Margin Call | Common | Instruction | Demand issued by a margin taker to a margin provider, in a scheduled or ad hoc run and with a settlement deadline, to satisfy a specified margin obligation; its amount derives from the uncovered requirement, not from the requirement alone. |
| LD-C0047 | Collateral | Common | State | Quantity of a collateral asset provided by a collateral provider to a collateral taker under an identified collateral arrangement, by title transfer or security interest, for an account as of a time, with market value and value after haircut; distinguished from merely eligible assets. |
| LD-C0048 | Collateral Asset | Common | Entity | Identifiable asset that may be mobilised as collateral; eligibility and actual commitment are separate. |
| LD-C0049 | Collateral Movement | Common | Event | Observed transfer of collateral assets (delivery, return, substitution or reallocation between accounts) under a specified arrangement; a cash collateral transfer is also a Cash Movement and is counted once. |
| LD-C0050 | Reconciliation | Common | Process | Comparison of representations expected to be consistent, of a stated type (trade, give-up, position, cash, margin, collateral, fee), scope, business date, matching keys and tolerance, in order to identify matches and discrepancies. |

## Additions from the 2026-11 expert review (LD-C0051 to LD-C0074)

All Draft and priority P1 for the pilot use cases (change impact, market onboarding, give-up and clearing acceptance) or the management revenue priority. Source reviews and decisions: [arbitration record](../governance/reviews/2026-11-expert-review/ARBITRATION.md).

| ID | Canonical English name | Owning module | Proposed type | Working business definition |
|---|---|---|---|---|
| LD-C0051 | Clearing Service | Common | Entity | Distinct clearing offering of a central counterparty for a defined product scope, governed by identified rule provisions, with its own admission categories, account structures, margin methodology, fee schedule and default-management arrangements; default resources may be shared across services. |
| LD-C0052 | Service Offering | Common | Entity | Defined execution, clearing or related post-trade service that a provider offers to clients, scoped by service kind (execution-only, clearing-only, execute-and-clear), product scope, the trading venues or clearing services it relies on, handling channel and client segment; distinct from a CCP's Clearing Service. |
| LD-C0053 | Clearing Member Acceptance | Common | Event | Decision by a clearing member to accept, wholly or partly, or to reject clearing responsibility for an identified trade or allocated quantity, for an identified client or account in a specified clearing service; explicit (take-up or claim) or automatic within a limit agreed before execution. Distinct from CCP acceptance (LD-C0023) and CCP interposition (LD-C0054). |
| LD-C0054 | CCP Interposition | Common | Event | Event by which a central counterparty becomes counterparty to each side of a trade under a clearing service's rules, at the moment and by the mechanism (novation, open offer or other) that those rules define; the legal meaning of "cleared", of which acceptance or registration messages are evidence. |
| LD-C0055 | Give-up Agreement | Common | Agreement | Agreement among a client, one or more executing brokers and one or more clearing brokers governing how executions are given up and taken up: acceptance conditions and limits, responsibility for trades not taken up, brokerage terms, billing and payment. |
| LD-C0056 | Client Clearing Agreement | Common | Agreement | Agreement under which a clearing member or clearing broker clears a client's transactions in one or more clearing services, setting the client clearing legal model (principal-to-principal, agency or guarantee, indirect chain), segregation election, margin and collateral terms, and default and porting provisions. |
| LD-C0057 | Clearing Broker | Common | Role | Role of a party that provides clearing of a client's transactions in a clearing service and is responsible to that client for them, either as a clearing member of that service or through another clearing member; distinct from admission at the CCP and from regulatory registrations. |
| LD-C0058 | Trading Venue Member | Common | Role | Role of a party admitted under a trading venue's rules, as member or participant, to enter orders and register trades in its own name; distinct from clearing membership and from the client-facing Executing Broker role. |
| LD-C0059 | Market Access Arrangement | Common | Agreement | Arrangement, documented by one or more agreements, by which a party can execute on a trading venue or clear in a clearing service, with an access model (direct membership by category, through a third-party member, direct electronic access, client clearing, indirect clearing, sponsored or direct-client model), any intermediary, a status and an effective period. |
| LD-C0060 | Allocation Instruction | Common | Instruction | Instruction, given before or after execution by a client or its investment manager, specifying how an executed or average-priced quantity is split across target accounts and, where relevant, clearing brokers; versioned and amendable until the applicable cut-off. |
| LD-C0061 | Order Handling Channel | Execution | Reference Concept | Governed classification of how an order is worked and reaches the venue: care (worked by a person at the broker), broker algorithm, direct market access through the broker's infrastructure, or sponsored access; whether the client itself uses an algorithm is a separate attribute. |
| LD-C0062 | Contract Specification | Common | Reference Concept | Versioned set of standard terms, defined by a trading venue, under which a derivative contract is listed and from which its tradeable instruments are created: underlying, size or multiplier, currency, tick, expiry cycle and key-date rules, settlement method and trading hours. |
| LD-C0063 | Rule Provision | Common | Reference Concept | Versioned, citable unit of a regulation, technical standard, guidance, CCP or venue rulebook or procedure, or the firm's own procedure, with issuer, scope and effective period, that imposes a requirement, defines a term or sets a parameter. |
| LD-C0064 | Rule Change | Common | Event | Proposal, adoption, amendment, withdrawal or replacement of a rule provision or of another published versioned specification (fee schedule, contract specification, business calendar, margin methodology, eligibility schedule), with a status and role-qualified dates; the trigger object of change-impact analysis. |
| LD-C0065 | Cut-off | Common | Reference Concept | Rule provision setting the time by which a process step must be completed, expressed as a local time relative to a business date of a named business calendar, with the consequence of missing it (rejection, lapse, late handling, charge) and the authority that sets it. |
| LD-C0066 | Business Calendar | Common | Reference Concept | Versioned set of business and non-business days, and where relevant trading or processing sessions with their business-date assignment rule, published by an identified calendar owner (venue, CCP, payment system or the firm) in a stated time zone. |
| LD-C0067 | Regulatory Regime | Common | Reference Concept | Body of binding rules identified by issuing authority, jurisdiction and legal instruments, applicable during an effective period; regimes may be related by equivalence or recognition decisions. |
| LD-C0068 | Regulatory Classification | Common | State | Time-bounded status of a legal entity, role assignment, account, trading venue, CCP or clearing service under a named regulatory regime, with its basis (self-assessment, notification, authority decision, calculation), asserting source and evidence; "unknown" is a value, never a default. |
| LD-C0069 | CCP Account | Common | Entity | Account opened by a CCP within a clearing service in a clearing member's name, of a defined type (house; omnibus client, net or gross; individually segregated client; indirect-client variants; other regimes' customer account classes), in which positions, margin and collateral are recorded. |
| LD-C0070 | Margin Methodology | Common | Reference Concept | Versioned rules and parameters by which a margin taker determines margin requirements for a scope: model family, confidence level, close-out period, look-back, offsets, add-ons and anti-procyclicality measures; at the member-client tier, CCP replication, replication with a multiplier or add-on, or an own model. |
| LD-C0071 | Collateral Arrangement | Common | Agreement | Terms under which collateral is provided, valued, substituted, remunerated and returned between a collateral provider and a collateral taker: legal form (title transfer or security interest), secured obligations, applicable eligibility schedule, haircut, valuation and interest terms; standalone or part of a CCP rulebook or client clearing agreement. |
| LD-C0072 | Collateral Eligibility Schedule | Common | Reference Concept | Versioned list, published by a collateral taker for a service, account type and tier, of the assets acceptable as collateral, with their haircuts (including FX haircuts), concentration limits and wrong-way restrictions. |
| LD-C0073 | Commercial Group | Common | Entity | Grouping of parties that a provider manages as one commercial relationship; distinct from legal or regulatory consolidation groups and carrying no legal or regulatory status. |
| LD-C0074 | Contribution | Common | Measure | Management revenue attributable to a target (client relationship, commercial group, service offering, venue or clearing service) less the costs within an explicitly approved cost perimeter, for a stated observing entity, period and currency; no formula or default cost perimeter is approved. |

## Proposed specialisations

- Legal Entity is a specialisation of Party, subject to validation of the wider Party scope.
- Client, Broker, Clearing Member, Central Counterparty and Trading Venue Member specialise Party Role.
- Executing Broker and Clearing Broker specialise Broker.
- Client Execution Fee, Client Clearing Fee, Executing Broker Brokerage Charge, Exchange Fee Charge and CCP Fee Charge specialise Fee Charge.
- Execution Revenue and Clearing Revenue specialise Revenue.
- Initial Margin Requirement and Variation Margin Requirement specialise Margin Requirement.
- Give-up Agreement, Client Clearing Agreement, Market Access Arrangement and Collateral Arrangement specialise Agreement.
- CCP Account specialises Account. Cut-off specialises Rule Provision.
- Execution, Clearing Acceptance, Clearing Member Acceptance, CCP Interposition and Novation specialise Lifecycle Event (proposed by the 2026-11 review).

The full specialisation table, with status and source, is in [concept annotations](concept-annotations.md#specialisations). Service Offering and Clearing Service are deliberately not given a common "Service" parent (see LD-A0020).

Do not infer that these categories are mutually exclusive or that fee categories are additive. One economic charge may have multiple classifications; aggregation requires an explicit identity and double-counting policy. Commission is deliberately not assigned a fee parent until its intended meaning is validated.

## Coverage and deferred detail

The absence of domain-owned ETD/OTC entries here does not exclude those domains: they initially reuse shared clearing concepts. Domain-specific acceptance, lifecycle and legal rules require later specialisation.

Currencies, units and date roles are required reference vocabularies; Business Calendar (LD-C0066) is now a concept because circulars change calendars and cut-offs are expressed against them. Compression, porting, position transfer, default fund, expiry, exercise, assignment, reporting, connectivity and clearing submission remain in the roadmap; their status is tracked in the [review backlog](../governance/reviews/2026-11-expert-review/ARBITRATION.md#6-backlog). No additional concept IDs are implied by this list.
