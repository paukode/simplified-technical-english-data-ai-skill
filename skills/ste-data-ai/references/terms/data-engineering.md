# Technical names: data engineering

These are technical names for data pipelines, processing, storage formats, and data platforms.
Use them as nouns, or as modifiers before a noun.
Do not use a technical name as a verb (rule W6).
Use the official spelling and case. Write table names, column names, and configuration keys as inline code.
A name in parentheses is the short name or the acronym. Write the full name at the first use (rule W7).
This list is not complete. Any official name is a technical name (rule W5).

## Pipelines and orchestration

- data pipeline, ETL, ELT, ETL process, ELT process, ETL job, reverse ETL, zero-ETL, orchestration, orchestrator, workflow orchestration, directed acyclic graph (DAG), DAG run, task instance, sensor, deferrable operator, hook, XCom
- Apache Airflow, Airflow, Airflow connection, Airflow variable, Astronomer, Astro, Dagster, Dagster asset, software-defined asset, asset materialization, Prefect, Prefect flow, Luigi, Kestra, Temporal, Apache NiFi
- upstream task, downstream task, trigger rule, retry delay, SLA miss, catchup, backfill, data interval, logical date, execution date, schedule interval, cron schedule, idempotent pipeline, pipeline run, job run, run, run ID, sync, connector sync, data freshness

## Batch and stream processing

- partitioning, indexing, batching, scheduling, processing, batch processing, stream processing, streaming, micro-batch, micro-batch processing, real-time processing, event time, processing time, ingestion time, watermark, late data, late-arriving data, out-of-order event
- window, tumbling window, sliding window, hopping window, session window, windowed aggregation, stateful processing, stateless processing, state store, checkpoint, checkpointing, savepoint
- exactly-once semantics, at-least-once delivery, at-most-once delivery, deduplication, Apache Flink, Flink, Flink SQL, Flink job, Apache Beam, Beam pipeline, PCollection, PTransform, Spark Structured Streaming, Kafka Streams, ksqlDB, Materialize, RisingWave, Apache Pulsar, Redpanda, Confluent, Confluent Cloud

## Apache Spark

- Apache Spark, Spark, PySpark, Spark SQL, Spark DataFrame, DataFrame, resilient distributed dataset (RDD), Spark application, Spark job, Spark stage, Spark task, driver, executor, executor memory, executor core, cluster manager, YARN, Spark on Kubernetes
- shuffle, shuffle partition, broadcast join, broadcast variable, sort-merge join, shuffle hash join, data skew, salting, Adaptive Query Execution (AQE), Catalyst optimizer, Tungsten, lazy evaluation, transformation, narrow transformation, wide transformation
- caching, spill, out-of-memory error (OOM error), Spark UI, Spark History Server, Spark Connect, Photon

## Apache Kafka

- Apache Kafka, Kafka, Kafka cluster, broker, KRaft, ZooKeeper, partition, in-sync replica (ISR), leader replica, follower replica, replication factor, offset, consumer offset, committed offset, offset commit, consumer group, consumer lag, lag, rebalance, partition assignment
- idempotent producer, transactional producer, message key, retention, log compaction, compacted topic, log segment, cleanup policy, Kafka Connect, source connector, sink connector, Single Message Transform (SMT)
- Schema Registry, Confluent Schema Registry, schema compatibility, full compatibility, MirrorMaker 2, dead-letter topic

## Change data capture and integration

- change data capture (CDC), log-based CDC, query-based CDC, trigger-based CDC, write-ahead log (WAL), binary log (binlog), redo log, transaction log, logical replication, replication slot, publication
- Debezium, Debezium connector, Fivetran, Airbyte, Stitch, Meltano, Singer tap, Qlik Replicate, Oracle GoldenGate, initial load, full load, incremental load, high-water mark, cursor field
- source system, source database, target database, destination, flat file, file transfer

## File formats and table formats

- file format, TSV, newline-delimited JSON (NDJSON), Apache Parquet, Parquet, Apache Avro, Avro, Apache ORC, ORC, Apache Arrow, Arrow, row-oriented format, columnar format, columnar storage
- compression codec, Snappy, Zstandard (zstd), LZ4, row group, column chunk, dictionary encoding, run-length encoding, predicate pushdown, projection pushdown, column pruning, bloom filter, statistics
- table format, open table format, Apache Iceberg, Iceberg, Iceberg table, Iceberg catalog, Iceberg REST catalog, Delta Lake, Delta table, Apache Hudi, Hudi, Apache Paimon, Delta Universal Format (UniForm)
- manifest file, manifest list, metadata file, time travel, schema evolution, partition evolution, hidden partitioning, Z-ordering, Z-order, liquid clustering, copy-on-write (COW), merge-on-read (MOR), deletion vector, equality delete, position delete, ACID transaction

## Storage layers and engines

- raw data, data lake, data lakehouse, lakehouse, data warehouse, cloud data warehouse, enterprise data warehouse (EDW), data mart, operational data store (ODS), staging area, staging table, staging layer, landing zone, raw zone, raw layer, curated zone, curated layer, consumption layer, presentation layer
- medallion architecture, bronze layer, silver layer, gold layer, managed table, metastore, Hive Metastore, Apache Hive, Hive, Apache Hadoop, HDFS, Trino, Presto, Starburst, Dremio, Apache Druid, Apache Pinot, ClickHouse, DuckDB, MotherDuck
- PostgreSQL, MySQL, MariaDB, Microsoft SQL Server, SQL Server, Oracle Database, IBM Db2, SQLite, MongoDB, Apache Cassandra, Couchbase, Teradata, Vertica, SAP HANA

## dbt and transformation

- dbt, dbt Core, dbt platform, dbt Fusion engine, dbt model, dbt project, dbt package, dbt test, data test, generic test, singular test, dbt source, seed, dbt snapshot, macro, Jinja, ref function, materialization, incremental model, ephemeral model
- dbt exposure, MetricFlow, dbt Semantic Layer, semantic layer, lineage graph, SQLMesh, Dataform

## SQL and queries

- query, SQL statement, data definition language (DDL), data manipulation language (DML), data control language (DCL), CREATE TABLE AS SELECT (CTAS), MERGE statement, join, inner join, left join, right join, full outer join, cross join, self-join, anti-join, semi-join, join key, join condition
- subquery, correlated subquery, common table expression (CTE), window function, aggregate function, scalar function, table function, clause, predicate, filter, primary key, foreign key, unique key, composite key
- B-tree index, hash index, bitmap index, covering index, query plan, execution plan, explain plan, cost-based optimizer, query optimizer, full table scan, index scan, table scan, view, materialized view, temporary table, stored procedure, user-defined function
- transaction, isolation level, read committed, repeatable read, serializable isolation, snapshot isolation, dirty read, phantom read, row lock, table lock, NULL value, numeric precision, cardinality, high cardinality, low cardinality, selectivity, query performance, slow query

## Data quality and observability

- duplicate, order line, breaking schema change, non-breaking schema change, data quality, data quality check, data quality rule, data quality dimension, accuracy, completeness, consistency, timeliness, validity, uniqueness, freshness, schema change, schema drift, data drift, anomaly, anomaly detection
- data observability, data downtime, data incident, data validation, data profiling, data contract, Great Expectations, Soda, Soda Core, Monte Carlo, Elementary Data, Deequ, Pandera, expectation, validation rule
- row count, null rate, null count, duplicate row, duplicate record, referential integrity, orphan record, outlier, reconciliation, quarantine table, error table

## Data operations and metadata

- DataOps, data platform, data infrastructure, data integration, data ingestion, data replication, data migration, data synchronization, data export, data import, data transfer, data movement, data processing, data transformation, data enrichment, data cleaning, data cleansing
- data normalization, data standardization, data anonymization, data sampling, data partitioning, data retention, data archival, data backup, data recovery, data versioning, data catalog, data discovery, data lineage, column-level lineage, OpenLineage, Marquez
- technical metadata, business metadata, operational metadata, data dictionary, business glossary, data asset, data product, table, column, row, record, catalog, dataset

## Platforms and tools

- Databricks, Databricks workspace, Databricks cluster, Databricks job, Lakeflow Jobs, Lakeflow Declarative Pipelines, Lakeflow Connect, Databricks SQL, SQL warehouse, Unity Catalog, Unity Catalog metastore, Delta Sharing, Databricks Asset Bundles, Databricks notebook, Databricks Runtime, Mosaic AI, Auto Loader
- business intelligence (BI), Talend, Informatica, Informatica PowerCenter, Matillion, Alteryx, SQL Server Integration Services (SSIS), Hightouch, Tableau, Apache Superset, Metabase, Hex, Sigma Computing, ThoughtSpot
- Apache Atlas, DataHub, OpenMetadata, Amundsen, Atlan, Collibra, Alation, Apache Ranger
