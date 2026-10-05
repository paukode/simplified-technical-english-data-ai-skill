# Examples: OpenSearch

Each example shows text before and after the change to STE.
The rule IDs refer to `references/writing-rules.md`.

## 1. Change the type of a field

Type: mixed

Before:

~~~text
You can't change the type of an existing field in OpenSearch, so if you need customer_id as a keyword instead of text you'll have to create a new index with the right mapping and reindex everything into it, then swap the alias.
~~~

After:

~~~text
You cannot change the type of an existing field. To change the type, make a new index and copy the documents into it.

1. Create the index `orders-v2` with the field `customer_id` as type `keyword`.
2. Copy the documents from `orders-v1` to `orders-v2` with the Reindex API.
3. Make sure that the document count of `orders-v2` is the same as the count of `orders-v1`.
4. Move the alias `orders` from `orders-v1` to `orders-v2`.
5. When the applications operate correctly, delete `orders-v1`.
~~~

Changes: no contractions (S3), one instruction in each step (P2), and a check of the result (P5).

## 2. The size of a shard

Type: description

Before:

~~~text
Shards should generally be kept between 10 and 50 GB. Too many tiny shards waste heap and too few giant ones make recovery and rebalancing painfully slow.
~~~

After:

~~~text
The recommended size of a shard is 10 GB to 30 GB for search workloads and 30 GB to 50 GB for log workloads.

Each shard uses JVM heap memory. If the cluster has many small shards, the heap usage increases. If a shard is very large, the recovery of the shard and the shard rebalancing are slow.
~~~

Changes: no "should" (V4), specific values (W13), and one topic in each sentence (S1).

## 3. Index State Management policy for logs

Type: description

Before:

~~~text
Our ISM policy rolls the log index over every day or at 50 GB, whichever comes first, then moves indexes to UltraWarm after 7 days and deletes them after 30.
~~~

After:

~~~text
The ISM policy `logs-policy` has three states: "hot", "warm", and "delete".

- In the "hot" state, the policy does a rollover of the write index after 1 day or at 50 GB. The first condition that occurs starts the rollover.
- After 7 days, the policy moves the index to UltraWarm storage.
- After 30 days, the policy deletes the index.
~~~

Changes: a vertical list for a sequence (S4), no phrasal verbs (V7), and state names in quotation marks (T6).

## 4. The cluster status is red

Type: mixed

Before:

~~~text
If the cluster goes red, don't panic. It usually means a primary shard is unassigned. Use the allocation explain API to figure out why and then fix the underlying problem (usually disk space or a node that dropped out).
~~~

After:

~~~text
A red cluster status shows that one or more primary shards are not assigned to a node. Searches on the indexes of these shards can return results that are not complete.

1. Find the shards that are not assigned:

   ```
   GET _cat/shards?v&h=index,shard,prirep,state,unassigned.reason
   ```

2. For each primary shard that is not assigned, get the reason from the Cluster Allocation Explain API:

   ```
   GET _cluster/allocation/explain
   ```

3. If the reason is a low disk space, increase the storage of the data nodes.
4. If the reason is a missing node, restart the node or replace it.
~~~

Changes: the meaning of the status first (D2), each command in a code block (P5), and each decision as a condition (P6).

## 5. Hybrid search with a normalization processor

Type: description

Before:

~~~text
Neither BM25 nor pure vector search was good enough on its own, so we set up a search pipeline with a normalization processor that blends both scores, weighted 0.3 lexical / 0.7 semantic.
~~~

After:

~~~text
The `products` index uses hybrid search. Each query runs a BM25 keyword query and a k-NN vector query together.

The scores of the two queries use different ranges. Thus, a search pipeline with a normalization processor changes each score to a value from 0 to 1. Then the processor calculates the sum of the two scores. The keyword score has a weight of 0.3, and the vector score has a weight of 0.7.

We did a test on 2026-09-15 with 400 questions. Hybrid search found the correct product in the top 5 results for 87% of the questions. Keyword search without vector search found it for 71% of the questions.
~~~

Changes: no phrasal verbs (V7), measured results with a date and a test set (M2), and one topic in each sentence (S1).
