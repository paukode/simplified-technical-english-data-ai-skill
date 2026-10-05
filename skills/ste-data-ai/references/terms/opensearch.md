# Technical names: OpenSearch

These are technical names for OpenSearch, Amazon OpenSearch Service, and their features.
Use them as nouns, or as modifiers before a noun.
Do not use a technical name as a verb (rule W6).
Use the official spelling and case. Write API paths, field names, settings, and query clauses as inline code. For example, write the `should` clause and the `must_not` clause as inline code.
A name in parentheses is the short name or the acronym. Write the full name at the first use (rule W7).
This list is not complete. Any official OpenSearch name is a technical name (rule W5).

## Products and deployment

- OpenSearch, OpenSearch Project, OpenSearch Dashboards, OpenSearch UI, Amazon OpenSearch Service, OpenSearch Service, OpenSearch Service domain, domain, Amazon OpenSearch Serverless, OpenSearch Serverless
- collection, search collection, time series collection, vector search collection, OpenSearch Compute Unit (OCU), Amazon OpenSearch Ingestion, OpenSearch Ingestion, OpenSearch Ingestion pipeline, Data Prepper
- Elasticsearch, Elastic, Apache Lucene, Lucene, OpenSearch plugin, OpenSearch Benchmark

## Clusters and nodes

- cluster manager node, dedicated cluster manager node, data node, hot data node, warm node, UltraWarm node, coordinating node, ingest node, ML node, search node
- shard, primary shard, replica shard, shard allocation, shard rebalancing, shard size, unassigned shard, segment, segment merge, segment replication, document replication, remote-backed storage, zone awareness, Multi-AZ with Standby
- cluster health, cluster status, green status, yellow status, red status, JVM heap, JVM memory pressure, thread pool, search thread pool, write thread pool, rejected request, cluster settings, OR1 instance

## Indexes, documents, and mappings

- index, index name, index alias, alias, write index, data stream, backing index, index template, composable index template, component template, index pattern, document, document ID
- field, field type, mapping, dynamic mapping, explicit mapping, mapping explosion, keyword field, text field, date field, numeric field, nested field, object field, multi-field, field limit
- index settings, number of shards, number of replicas, refresh interval, refresh, flush, translog, merge policy, Reindex API, rollover, rollover alias, shrink operation, close index operation, snapshot repository

## Text analysis

- analyzer, standard analyzer, custom analyzer, tokenizer, token filter, character filter, normalizer, stemming, stemmer, stop word, synonym, synonym filter, n-gram, edge n-gram, lowercase filter, ASCII folding, language analyzer, ICU analysis plugin

## Search and queries

- Query DSL, full-text query, match query, match phrase query, multi-match query, term query, terms query, range query, Boolean query, bool query, filter context, query context, relevance, relevance score, BM25, TF-IDF, scoring, boosting, boost, function score query
- aggregation, bucket aggregation, metric aggregation, pipeline aggregation, terms aggregation, date histogram aggregation, cardinality aggregation, point in time (PIT), Point in Time API, highlighting, suggester, autocomplete, fuzzy query, wildcard query, regexp query, query string query, simple query string query
- score, Cluster Allocation Explain API, Search API, Multi-Search API, Count API, Explain API, Profile API, SQL plugin, OpenSearch SQL, Piped Processing Language (PPL), Dashboards Query Language (DQL), Lucene query syntax, search template
- search pipeline, search processor, search request processor, search response processor, normalization processor, score normalization, hybrid query, rerank processor, learning to rank (LTR), Learning to Rank plugin, search relevance, mean reciprocal rank (MRR), normalized discounted cumulative gain (nDCG)

## Vector and neural search

- k-NN plugin, k-NN search, k-nearest neighbors (k-NN), approximate k-NN, exact k-NN, script score k-NN, k-NN index, vector field, engine, Faiss engine, Lucene engine, NMSLIB engine, space type, efficient filtering, radial search
- byte vector, binary vector, disk-based vector search, on-disk mode, compression level, neural search, neural query, neural sparse search, semantic search, ML Commons, ML Commons plugin, model group, remote model, local model, ML connector, connector blueprint
- text embedding processor, sparse encoding processor, text chunking processor, Flow Framework, conversational search, OpenSearch Assistant

## Data ingestion

- Bulk API, bulk request, ingest pipeline, ingest processor, processor, grok processor, date processor, script processor, sink, buffer, pipeline configuration

## Index management and storage

- Index State Management (ISM), ISM policy, state transition, Index Management plugin, index rollup, index transform, hot storage, warm storage, UltraWarm, UltraWarm storage, cold storage, hot-warm-cold architecture, searchable snapshot, codec, index codec

## Security

- Security plugin, fine-grained access control (FGAC), role mapping, backend role, internal user database, document-level security (DLS), field-level security (FLS), field masking, node-to-node encryption, Amazon Cognito authentication, domain access policy, VPC access, public access
- data access policy, encryption policy, network policy

## Observability, alerting, and analytics

- visualization, saved object, Observability plugin, trace analytics, log analytics, Alerting plugin, monitor, per query monitor, per bucket monitor, per document monitor, composite monitor
- Anomaly Detection plugin, detector, anomaly grade, confidence score, Security Analytics plugin, detection rule, Sigma rule, query insights

## Operations

- slow log, search slow log, indexing slow log, service software update, Auto-Tune, rolling restart, cross-cluster search, cross-cluster replication, leader index, follower index, snapshot management
