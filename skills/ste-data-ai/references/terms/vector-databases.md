# Technical names: vector databases and vector search

These are technical names for vector databases, vector search, and their concepts.
Use them as nouns, or as modifiers before a noun.
Do not use a technical name as a verb (rule W6).
Use the official spelling and case. Write parameter names as inline code, for example `ef_search`.
A name in parentheses is the short name or the acronym. Write the full name at the first use (rule W7).
This list is not complete. Any official name is a technical name (rule W5).

## Products and services

- vector database, vector store, vector search engine, vector index, Pinecone, Pinecone serverless index, pod-based index, Pinecone Assistant, Weaviate, Weaviate Cloud, Milvus, Zilliz Cloud, Qdrant, Qdrant Cloud, Chroma, ChromaDB, pgvector, pgvectorscale
- LanceDB, Lance format, Vespa, Turbopuffer, Faiss, Annoy, ScaNN, hnswlib, DiskANN, Redis, Redis Query Engine, Valkey, Elasticsearch, OpenSearch, Amazon S3 Vectors, Amazon OpenSearch Serverless, Amazon MemoryDB, Amazon DocumentDB, Amazon Neptune Analytics
- Azure AI Search, Azure Cosmos DB, Vertex AI Vector Search, AlloyDB AI, BigQuery vector search, MongoDB Atlas, MongoDB Atlas Vector Search, Neo4j, Neo4j vector index, Apache Cassandra, DataStax Astra DB, Astra DB, SingleStore, ClickHouse, Oracle AI Vector Search, Marqo, Vald, Mosaic AI Vector Search

## Core concepts

- vector, embedding, embedding vector, dense vector, sparse vector, multi-vector, vector dimension, dimensionality, vector space, embedding space, point, record, metadata, metadata field, namespace, collection, partition, segment, tenant, multi-tenancy
- upsert, query vector, neighbor, candidate, nearest neighbor, k-nearest neighbors (k-NN), approximate nearest neighbor (ANN), approximate nearest neighbor search, exact search, brute-force search, flat index, top-k, top-k results, similarity search, semantic search, vector search
- similarity score, distance, distance metric, similarity metric, score threshold, similarity threshold, recall, recall@k, precision@k, query latency, queries per second (QPS), index build time, ingestion rate, freshness

## Distance and similarity

- cosine similarity, cosine distance, dot product, inner product, maximum inner product search (MIPS), Euclidean distance, L2 distance, squared L2 distance, Manhattan distance, L1 distance, Hamming distance, Jaccard similarity, Jaccard distance
- normalized vector, unit vector, vector normalization, L2 normalization

## Index types and parameters

- Hierarchical Navigable Small World (HNSW), HNSW graph, HNSW index, graph-based index, graph index, inverted file index (IVF), IVF index, IVF_FLAT, IVF_PQ, IVF_SQ8, nlist, nprobe, centroid, cluster centroid, k-means clustering, Vamana, locality-sensitive hashing (LSH), tree-based index
- index type, index parameter, build parameter, search parameter, ivfflat index, hnsw index, halfvec, sparsevec, lists parameter, probes parameter

## Quantization and compression

- quantization, vector quantization, scalar quantization (SQ), product quantization (PQ), binary quantization (BQ), int8 quantization, float32, float16, bfloat16, int8, uint8, rescoring, oversampling
- Matryoshka embedding, Matryoshka Representation Learning (MRL), dimension reduction, dimensionality reduction, principal component analysis (PCA), compression ratio, memory footprint

## Filtering and search modes

- metadata filtering, metadata filter, filtered search, pre-filtering, post-filtering, filter expression, payload index, payload, hybrid search, keyword search, lexical search, full-text search, BM25
- sparse-dense search, sparse-dense vector, SPLADE, learned sparse retrieval, reciprocal rank fusion (RRF), score fusion, reranking, reranker, rerank model, cross-encoder, bi-encoder, ColBERT, late interaction, multi-vector retrieval
- maximal marginal relevance (MMR), faceted search, geo filter

## Embeddings and chunking

- embedding model, text embedding, image embedding, multimodal embedding, sentence embedding, Sentence Transformers, embedding dimension, embedding drift, re-embedding
- chunk, chunking, chunk size, chunk overlap, fixed-size chunking, recursive chunking, semantic chunking, late chunking, parent-child chunking, parent document retrieval, context window, token

## Operations and quality

- index build, index refresh, compaction, tombstone, soft delete, hard delete, dual write, shadow index, index alias, ground truth, ground truth set, evaluation set, relevance judgment, query set
- benchmark, ANN benchmark, VectorDBBench, tail latency, memory-mapped file, on-disk index, in-memory index, tiered storage
