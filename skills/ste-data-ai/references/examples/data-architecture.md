# Examples: data architecture

Each example shows text before and after the change to STE.
The rule IDs refer to `references/writing-rules.md`.

## 1. An architecture decision record

Type: description

Before:

~~~text
Context: We've been struggling with vendor lock-in and our Spark and Snowflake workloads can't easily share data. Decision: We're going to adopt Apache Iceberg as our table format going forward. Consequences: It'll take some effort to migrate existing Hive tables, but long term this should give us way more flexibility.
~~~

After:

~~~text
Context: The Spark jobs and Snowflake cannot use the same copy of the data. Each platform keeps its own copy in its own format. This increases the cost of storage and the risk of differences between the copies.

Decision: We will use Apache Iceberg as the table format for all the tables in the lakehouse. Spark and Snowflake will read and write the same Iceberg tables.

Consequences:

- We must migrate 140 Hive tables to Iceberg. The estimate of the data team is 6 weeks of work.
- Each engine reads the same data. Thus, there are no differences between copies.
- We must operate an Iceberg catalog.
~~~

Changes: "we will" for the decision, specific values instead of vague words (W13), and no "-ing" verb forms (V3).

## 2. The grain of a fact table

Type: mixed

Before:

~~~text
fact_orders is at the order line level, so if you sum revenue without grouping by order you'll be fine, but count(*) will overcount orders.
~~~

After:

~~~text
The grain of the `fact_orders` table is one row for each order line. An order with three products has three rows.

To count the orders, use `COUNT(DISTINCT order_id)`. Do not use `COUNT(*)`. It counts the order lines, not the orders.
~~~

Changes: the grain as a fact (M6), identifiers as inline code (T5), and the instruction in a separate paragraph (D2).

## 3. A slowly changing dimension of Type 2

Type: mixed

Before:

~~~text
dim_customer is an SCD2, so whenever a customer's address changes we close out the old row by setting valid_to and is_current = false and insert a new row.
~~~

After:

~~~text
The `dim_customer` table is a slowly changing dimension (SCD) of Type 2. It keeps the history of each customer.

When the address of a customer changes, the load job does these actions:

1. It sets `valid_to` of the current row to the date of the change.
2. It sets `is_current` of the current row to `false`.
3. It inserts a new row with the new address and with `is_current` set to `true`.

To get the current address of each customer, use the filter `is_current = true`.
~~~

Changes: the full term before the acronym (W14), a sequence as a list (S4), and no phrasal verbs (V7).

## 4. The layers of the medallion architecture

Type: description

Before:

~~~text
Bronze is just raw dumps of source data, silver is cleaned and conformed, and gold is business-level aggregates that BI tools hit directly.
~~~

After:

~~~text
The lakehouse has three layers:

- The bronze layer contains the raw data from the source systems. The data is not changed.
- The silver layer contains data that is cleaned, deduplicated, and changed to standard types and names.
- The gold layer contains aggregate tables for business intelligence (BI) dashboards and reports.

Only the gold layer is available to the BI tools.
~~~

Changes: a vertical list (S4), no jargon (W9), and the full term before the acronym (W14).

## 5. Recovery targets for a database

Type: specification

Before:

~~~text
For the customer DB, we'd like to be able to recover from a regional outage within an hour or so, losing no more than 5 minutes of data.
~~~

After:

~~~text
This document uses the keyword MUST as RFC 2119 gives it.

- DR-01: If the primary region fails, the `customers` database MUST operate in the secondary region in less than 60 minutes (RTO).
- DR-02: For the `customers` database, the maximum data loss MUST be 5 minutes of changes (RPO).
- DR-03: The platform team MUST do a test of the failover at intervals of 3 months.
~~~

Changes: values that you can measure (R3), one requirement in each item (R2), and no vague words (W13).

## 6. Ownership in a data mesh

Type: description

Before:

~~~text
In our data mesh, each domain team owns its data products end to end, including quality and SLAs, while the platform team just provides the self-serve infrastructure.
~~~

After:

~~~text
In the data mesh, each domain team is the owner of its data products. The domain team controls the quality, the schema, and the service level objectives (SLOs) of each data product.

The platform team supplies the self-serve data platform. It does not control the data products.
~~~

Changes: core words instead of "provide" (W1), the full term before the acronym (W14), and one topic in each sentence (S1).
