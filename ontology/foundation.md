# Foundational concept catalogue

Status: Draft for all 50 entries. Type assignments and definitions are proposals.

This catalogue identifies concepts for Phase 1; it does not claim to complete the [full concept template](../templates/concept-template.md). IDs are stable across future renaming, relocation and format migration. Common means shared stewardship, not exclusive domain use.

| ID | Canonical English name | Owning module | Proposed type | Working business definition |
|---|---|---|---|---|
| LD-C0001 | Party | Common | Entity | Identifiable actor that can participate in a business relationship. |
| LD-C0002 | Legal Entity | Common | Entity | Organisation or structure recognised as a legal entity under the applicable framework. |
| LD-C0003 | Party Role | Common | Role | Function held by a party within a specified relationship, service and effective period. |
| LD-C0004 | Client | Common | Role | Role of a party receiving a service from an identified provider; contractual and commercial attribution must be distinguished. |
| LD-C0005 | Broker | Common | Role | Intermediation role whose activities and responsibilities require specification. |
| LD-C0006 | Executing Broker | Common | Role | Role of the party providing the execution service concerned. |
| LD-C0007 | Clearing Member | Common | Role | Role of a party admitted to a specified clearing service of a CCP. |
| LD-C0008 | Central Counterparty | Common | Role | Role of an entity interposed as counterparty through the applicable legal mechanism. |
| LD-C0009 | Trading Venue | Common | Entity | Organised trading facility or framework, distinguished from its legal operator and reporting facilities. |
| LD-C0010 | Account | Common | Entity | Business structure for attribution and recording, with an explicit function, maintaining party and relevant holders. |
| LD-C0011 | Segregation Model | Common | Reference Concept | Rules for separating positions, assets or records under a specified legal and operational framework. |
| LD-C0012 | Agreement | Common | Agreement | Arrangement governing services, rights and obligations between parties. |
| LD-C0013 | Product | Common | Reference Concept | Family defined by shared economic and contractual characteristics. |
| LD-C0014 | Instrument | Common | Entity | Identifiable specification of a derivative that can be traded or contracted; the boundary with a bespoke OTC contract requires validation. |
| LD-C0015 | Business Date | Common | Reference Concept | Date interpreted under a specified business function, calendar and operational context. |
| LD-C0016 | Order | Execution | Instruction | Instruction to trade subject to specified execution conditions. |
| LD-C0017 | Execution | Execution | Event | Event fulfilling all or part of a trading instruction. |
| LD-C0018 | Trade | Common | Agreement | Agreed derivative transaction, distinguished from operational records and subsequent legal transformations. |
| LD-C0019 | Transaction | Common | Event | Business operation affecting rights, obligations or balances; this broad working definition requires validation and must not become a catch-all synonym. |
| LD-C0020 | Allocation | Common | Process | Assignment of a quantity or amount to target beneficiaries or accounts; instruction and completed event are later specialisations. |
| LD-C0021 | Average Price Group | Common | Entity | Grouping of eligible executions or trades subject to a specified average-pricing method. |
| LD-C0022 | Give-up / Take-up Process | Common | Process | Coordinated process of delivering and accepting a trade for clearing under applicable rules; instructions, acceptance events and legal effects remain distinct. |
| LD-C0023 | Clearing Acceptance | Common | Event | Acceptance of a trade into a specified clearing service under defined criteria; legal effect must be stated separately. |
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
| LD-C0043 | Margin Requirement | Common | Measure | Calculated margin requirement for a defined scope, relationship and point in time, distinct from its call and satisfaction. |
| LD-C0044 | Initial Margin Requirement | Common | Measure | Margin requirement intended to cover potential future exposure under the applicable methodology. |
| LD-C0045 | Variation Margin Requirement | Common | Measure | Requirement associated with valuation changes, with legal treatment and direction explicitly specified. |
| LD-C0046 | Margin Call | Common | Instruction | Demand addressed to a party to satisfy a specified margin obligation. |
| LD-C0047 | Collateral | Common | Entity | Cash or assets committed as security for obligations under an identified arrangement, distinguished from merely eligible assets. |
| LD-C0048 | Collateral Asset | Common | Entity | Identifiable asset that may be mobilised as collateral; eligibility and actual commitment are separate. |
| LD-C0049 | Collateral Movement | Common | Event | Transfer, allocation or return of collateral under a specified arrangement. |
| LD-C0050 | Reconciliation | Common | Process | Comparison of representations expected to be consistent in order to identify discrepancies. |

## Proposed specialisations

- Legal Entity is a specialisation of Party, subject to validation of the wider Party scope.
- Client, Broker, Clearing Member and Central Counterparty specialise Party Role.
- Executing Broker specialises Broker.
- Client Execution Fee, Client Clearing Fee, Executing Broker Brokerage Charge, Exchange Fee Charge and CCP Fee Charge specialise Fee Charge.
- Execution Revenue and Clearing Revenue specialise Revenue.
- Initial Margin Requirement and Variation Margin Requirement specialise Margin Requirement.

Do not infer that these categories are mutually exclusive or that fee categories are additive. One economic charge may have multiple classifications; aggregation requires an explicit identity and double-counting policy. Commission is deliberately not assigned a fee parent until its intended meaning is validated.

## Coverage and deferred detail

The absence of domain-owned ETD/OTC entries here does not exclude those domains: they initially reuse shared clearing concepts. Domain-specific acceptance, lifecycle and legal rules require later specialisation.

Currencies, units, calendar policies and date roles are required reference vocabularies. Compression, portability, default fund, expiry, exercise, assignment, transfers, reporting, market access, connectivity, algorithms and execution channels remain in the roadmap. No detailed taxonomy or additional concept IDs are implied by this list.
