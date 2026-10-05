# Technical names: Amazon Redshift

These are technical names for Amazon Redshift features, objects, and concepts.
Use them as nouns, or as modifiers before a noun.
Do not use a technical name as a verb (rule W6).
Use the official spelling and case. Write SQL commands, system tables, and parameters as inline code.
A name in parentheses is the short name or the acronym. Write the full name at the first use (rule W7).
This list is not complete. Any official Redshift name is a technical name (rule W5).

## Clusters and nodes

- Amazon Redshift, Redshift, provisioned cluster, Redshift cluster, leader node, compute node, node slice, slice, node type, RA3 node, RA3 node type, DC2 node, Redshift Managed Storage (RMS), managed storage
- Amazon Redshift Spectrum, Redshift Spectrum, elastic resize, classic resize, concurrency scaling, concurrency scaling cluster, cluster parameter group, cluster subnet group, Redshift-managed VPC endpoint, enhanced VPC routing
- Amazon Redshift Data API, Redshift Data API, Amazon Redshift query editor v2, query editor v2, Redshift JDBC driver, Redshift ODBC driver, Redshift Python connector

## Redshift Serverless

- Amazon Redshift Serverless, Redshift Serverless, workgroup, namespace, Redshift Processing Unit (RPU), RPU-hour, base capacity, maximum capacity, AI-driven scaling and optimization, price-performance target, usage limit

## Table design

- distribution style, AUTO distribution, EVEN distribution, KEY distribution, ALL distribution, distribution key, DISTKEY, sort key, SORTKEY, compound sort key, interleaved sort key, AUTO sort key
- column encoding, compression encoding, AZ64, ZSTD, LZO, BYTEDICT, RUNLENGTH, automatic table optimization (ATO), data skew, row skew, skew, zone map, block
- SUPER data type, SUPER, PartiQL, VARBYTE, identity column, informational constraint, late-binding view, automatic materialized view, auto refresh, external schema, cross-database query, federated query

## Loading and unloading data

- COPY command, COPY, UNLOAD command, UNLOAD, manifest file, default IAM role, auto-copy, COPY JOB, streaming ingestion, deep copy, staging table

## Workload management and performance

- workload management (WLM), automatic WLM, manual WLM, WLM queue, query queue, query priority, query monitoring rule (QMR), short query acceleration (SQA), query group, user group, WLM slot
- disk-based query, EXPLAIN plan, Amazon Redshift Advisor, Redshift Advisor, result caching, table statistics, unsorted region, unsorted rows
- VACUUM, VACUUM DELETE ONLY, VACUUM SORT ONLY, VACUUM REINDEX, automatic vacuum delete, automatic vacuum sort, ANALYZE, automatic analyze, ANALYZE COMPRESSION

## Sharing and integration

- datashare, producer cluster, consumer cluster, producer namespace, consumer namespace, AWS Data Exchange datashare, multi-data warehouse writes, Amazon Redshift ML, Redshift ML, Amazon Q generative SQL

## Security

- database user, database group, database role, row-level security (RLS), column-level access control, column-level security, dynamic data masking, masking policy, audit logging, user activity log, connection log, user log, cluster encryption, IAM authentication

## Monitoring and system tables

- system table, system view, STL table, STV table, SVL view, SVV view, SYS view, SYS_QUERY_HISTORY, STL_QUERY, SVV_TABLE_INFO, STL_LOAD_ERRORS, SYS_LOAD_ERROR_DETAIL, query profiler

## Snapshots and recovery

- automated snapshot, manual snapshot, cross-Region snapshot copy, snapshot schedule, table restore, recovery point
