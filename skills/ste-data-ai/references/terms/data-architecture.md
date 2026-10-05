# Technical names: data architecture

These are technical names for data architecture, data modeling, governance, and distributed systems.
Use them as nouns, or as modifiers before a noun.
Do not use a technical name as a verb (rule W6).
Use the official spelling and case.
A name in parentheses is the short name or the acronym. Write the full name at the first use (rule W7).
This list is not complete. Any official name is a technical name (rule W5).

## Architecture documents and decisions

- data architecture, enterprise architecture, solution architecture, reference architecture, target architecture, architecture diagram, architecture decision record (ADR), architecture decision, decision record, consequence, trade-off
- design principle, constraint, assumption, non-functional requirement (NFR), functional requirement, quality attribute, C4 model, context diagram, container diagram, component diagram, system context, data flow diagram (DFD), entity-relationship diagram (ERD), sequence diagram
- architecture review board (ARB), request for comments (RFC), TOGAF, DAMA-DMBOK, DAMA

## Data modeling

- data model, data modeling, conceptual data model, logical data model, physical data model, canonical data model, entity, entity type, relationship, one-to-one relationship, one-to-many relationship, many-to-many relationship, associative entity, junction table, bridge table, optionality
- data domain, subject area, business entity, business process, business key, natural key, surrogate key, candidate key, alternate key, unique constraint, check constraint, not-null constraint
- schema-on-read, schema-on-write, structured data, semi-structured data, unstructured data, polyglot persistence, erwin Data Modeler

## Dimensional modeling

- dimensional modeling, dimensional model, Kimball methodology, Kimball, Inmon, star schema, snowflake schema, galaxy schema, fact constellation, fact table, dimension table, dimension, fact, measure, additive measure, semi-additive measure, non-additive measure
- grain, declared grain, transaction fact table, periodic snapshot fact table, accumulating snapshot fact table, factless fact table, conformed dimension, role-playing dimension, junk dimension, degenerate dimension, outrigger dimension, mini-dimension, date dimension, time dimension
- slowly changing dimension (SCD), SCD Type 0, SCD Type 1, SCD Type 2, SCD Type 3, SCD Type 4, SCD Type 6, effective date, expiration date, current flag, hierarchy, ragged hierarchy, bus matrix, aggregate table, summary table
- online analytical processing (OLAP), OLAP cube, cube, online transaction processing (OLTP), hybrid transactional and analytical processing (HTAP), drill-down, roll-up

## Data Vault

- Data Vault, Data Vault 2.0, hub, link, satellite, hub table, link table, satellite table, hash key, hash diff, business vault, raw vault, point-in-time table, effectivity satellite, multi-active satellite, reference table, load date, record source

## Normalization

- normalization, denormalization, normal form, first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), update anomaly, insert anomaly, delete anomaly, functional dependency, wide table, one big table (OBT)

## Architecture patterns

- data mesh, data product, data product owner, domain-oriented ownership, self-serve data platform, federated computational governance, data fabric, lambda architecture, kappa architecture, hub-and-spoke architecture
- command query responsibility segregation (CQRS), microservices architecture, service-oriented architecture (SOA), data virtualization, data federation, logical data warehouse, operational analytics, embedded analytics, headless BI, metrics layer, feature store
- single source of truth (SSOT), system of record (SOR), golden record, master data, master data management (MDM), reference data, reference data management, transactional data, analytical data, operational data, historical data, hot, warm, cold, real-time data, streaming data, batch data, hot data, warm data, cold data

## Data governance and privacy

- governance, data governance, data governance council, data governance framework, data policy, data standard, data stewardship, data ownership, data access policy, data classification, data sensitivity level, public data, internal data, confidential data, restricted data
- personal data, sensitive personal data, special category data, data subject, data controller, data processor, data protection, data privacy, privacy by design, data minimization, purpose limitation, consent management, right to erasure, data subject access request (DSAR)
- data retention policy, retention schedule, data lifecycle, data lifecycle management, cross-border data transfer, data processing agreement (DPA), General Data Protection Regulation (GDPR), California Consumer Privacy Act (CCPA), EU AI Act, data ethics, data literacy
- metadata management, lineage, impact analysis, critical data element (CDE), key performance indicator (KPI), metric definition, data certification, certified dataset

## Quality attributes

- scalability, performance, maintainability, portability, interoperability, extensibility, usability, cost efficiency, total cost of ownership (TCO), return on investment (ROI), service level, data volume, data velocity, data variety, elasticity

## Integration patterns

- point-to-point integration, publish-subscribe pattern, request-response pattern, event-carried state transfer, outbox pattern, transactional outbox, inbox pattern, saga pattern, two-phase commit (2PC), dual write, idempotent consumer, competing consumers
- fan-out, fan-in, scatter-gather, strangler fig pattern, anti-corruption layer, backend for frontend (BFF), interface contract, service contract, contract

## Consistency and distributed systems

- CAP theorem, PACELC theorem, strong consistency, eventual consistency, eventually consistent, read-after-write consistency, causal consistency, linearizability, ACID, BASE, distributed system, distributed transaction, consensus, Raft, Paxos, quorum, leader election
- partition tolerance, network partition, split-brain, clock skew, vector clock, sharding, horizontal partitioning, vertical partitioning, replication, synchronous replication, asynchronous replication, primary-replica replication, multi-primary replication, conflict resolution, last-writer-wins (LWW), conflict-free replicated data type (CRDT)
