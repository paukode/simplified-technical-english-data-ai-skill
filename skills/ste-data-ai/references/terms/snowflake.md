# Technical names: Snowflake

These are technical names for Snowflake features, objects, and concepts.
Use them as nouns, or as modifiers before a noun.
Do not use a technical name as a verb (rule W6).
Use the official spelling and case. Write SQL keywords, functions, parameters, and object names as inline code.
A name in parentheses is the short name or the acronym. Write the full name at the first use (rule W7).
This list is not complete. Any official Snowflake name is a technical name (rule W5).

## Platform and accounts

- Snowflake, Snowflake AI Data Cloud, Snowflake account, account identifier, account locator, organization account, Snowsight, SnowSQL, Snowflake CLI, Snowflake Connector for Python, Snowflake JDBC driver, Snowflake ODBC driver
- Snowflake edition, Business Critical edition, Virtual Private Snowflake (VPS), cloud services layer, compute layer, storage layer, Snowflake Horizon Catalog, reader account, trial account, Snowflake Support

## Access control and governance

- role, system-defined role, ACCOUNTADMIN, SYSADMIN, SECURITYADMIN, USERADMIN, ORGADMIN, PUBLIC role, custom role, database role, role hierarchy, privilege, grant, future grant, ownership, OWNERSHIP privilege, access control
- discretionary access control (DAC), role-based access control (RBAC), service user, key pair authentication, programmatic access token, SCIM, network policy, network rule, authentication policy, password policy, session policy
- masking policy, row access policy, aggregation policy, projection policy, object tagging, tag-based masking policy, data classification, sensitive data classification, access history, Trust Center, Tri-Secret Secure

## Virtual warehouses

- virtual warehouse, warehouse, standard warehouse, Snowpark-optimized warehouse, Gen2 warehouse, multi-cluster warehouse, warehouse size
- X-Small, Small, Medium, Large, X-Large, 2X-Large, 3X-Large, 4X-Large, 5X-Large, 6X-Large
- auto-suspend, auto-resume, scaling policy, Standard scaling policy, Economy scaling policy, cluster count, credit, Snowflake credit, credit usage, resource monitor, queued query, statement timeout, query acceleration service (QAS), compute pool

## Storage and data objects

- database, schema, managed access schema, table, permanent table, transient table, temporary table, external table, Apache Iceberg table, Iceberg table, hybrid table, dynamic table, event table, directory table
- view, secure view, materialized view, secure materialized view, semantic view, column, VARIANT, OBJECT, ARRAY, GEOGRAPHY, GEOMETRY, VECTOR, semi-structured data
- micro-partition, clustering key, automatic clustering, clustering depth, pruning, partition pruning, Time Travel, Time Travel retention period, Fail-safe, zero-copy cloning, zero-copy clone, clone, sequence
- stage, internal stage, external stage, user stage, table stage, named stage, file format, storage integration, external volume, catalog integration, Snowflake Open Catalog, Apache Polaris

## Loading and unloading data

- COPY INTO, bulk loading, data loading, data unloading, Snowpipe, Snowpipe Streaming, auto-ingest, pipe, notification integration, Snowflake Connector for Kafka, Snowflake Openflow, Openflow, load history, schema detection, schema evolution

## Pipelines and development

- stream, standard stream, append-only stream, insert-only stream, change tracking, CHANGES clause, task graph, root task, child task, serverless task, triggered task, task history, target lag, refresh mode, incremental refresh, full refresh
- dbt Projects on Snowflake, Snowflake Notebooks, Streamlit in Snowflake, stored procedure, user-defined function (UDF), user-defined table function (UDTF), external function, external access integration, API integration
- Snowpark, Snowpark Python, Snowpark DataFrame, Snowpark pandas API, Snowpark Container Services, image repository, Snowflake Native App Framework, Snowflake Native App, application package, Snowflake Scripting, session variable, session parameter, account parameter, object parameter

## Performance

- query profile, query history, query ID, operator, spilling, local spilling, remote spilling, result cache, metadata cache, warehouse cache, local disk cache, search optimization service, search access path
- bytes scanned, partitions scanned, partitions total, execution time, compilation time, queued time

## Sharing, collaboration, and replication

- Secure Data Sharing, data sharing, share, data provider, data consumer, listing, private listing, public listing, Snowflake Marketplace, data exchange, data clean room, Snowflake Data Clean Rooms
- replication, database replication, account replication, replication group, failover group, primary database, secondary database, client redirect, Snowgrid

## Snowflake AI and ML

- Snowflake Cortex, Cortex AI, Cortex AISQL, AI_COMPLETE, AI_CLASSIFY, AI_FILTER, AI_AGG, AI_SUMMARIZE_AGG, AI_EMBED, AI_SENTIMENT, AI_EXTRACT, AI_TRANSLATE, AI_PARSE_DOCUMENT
- Cortex Search, Cortex Search service, Cortex Analyst, semantic model, Cortex Agents, Snowflake Intelligence, Document AI, Cortex Fine-tuning, Cortex Guard, Cortex Knowledge Extensions
- Snowflake ML, Snowflake Feature Store, Snowflake Model Registry, ML Functions, Snowflake Copilot, Snowflake Arctic, Arctic Embed

## SQL features

- QUALIFY, FLATTEN, LATERAL FLATTEN, MERGE, PIVOT, UNPIVOT, MATCH_RECOGNIZE, window function, common table expression (CTE), transaction, explicit transaction, anonymous block
