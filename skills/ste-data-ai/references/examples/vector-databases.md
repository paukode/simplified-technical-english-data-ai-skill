# Examples: vector databases

Each example shows text before and after the change to STE.
The rule IDs refer to `references/writing-rules.md`.

## 1. Select a distance metric

Type: description

Before:

~~~text
Since our embedding model outputs normalized vectors, cosine and dot product are basically equivalent, but dot product is faster so that's what we use.
~~~

After:

~~~text
The `text-embed-v3` model returns vectors that are normalized to a length of 1. For normalized vectors, cosine similarity and dot product give the same order of results.

The calculation of the dot product is faster than the calculation of the cosine similarity. Thus, the `docs` index uses dot product as the distance metric.
~~~

Changes: full technical names (W5), the reason for the decision (S5), and no vague words (W13).

## 2. Tune the HNSW parameter ef_search

Type: description

Before:

~~~text
Bumping ef_search from 64 to 256 got recall@10 up from 0.91 to 0.98 but roughly tripled p99 latency, so we settled on 128 as a compromise.
~~~

After:

~~~text
The `ef_search` parameter sets the number of candidate neighbors that the HNSW search examines. A higher value gives a higher recall and a higher latency.

We measured three values on 2026-09-20 with 1,000 test queries:

| `ef_search` | recall@10 | p99 latency |
|---|---|---|
| 64 | 0.91 | 12 ms |
| 128 | 0.96 | 19 ms |
| 256 | 0.98 | 35 ms |

We selected 128. This value gives a recall@10 of 0.96 and a p99 latency of less than 20 ms.
~~~

Changes: a table for the values (D4), the date and the test set (M2), and no slang (W9).

## 3. Change to a new embedding model

Type: procedure

Before:

~~~text
When we switch embedding models we can't just start writing new vectors into the existing index, since vectors from different models aren't comparable. We'll need to re-embed everything into a new index and cut over once it's done.
~~~

After:

~~~text
CAUTION: Do not put vectors from two different embedding models in the same index. The distance between vectors from two models has no meaning. As a result, the search results become incorrect.

1. Create a new index for the vectors of the new model.
2. Embed all the documents again with the new model.
3. Write the new vectors to the new index.
4. Do the evaluation of the new index with the ground truth set.
5. Compare the recall of the new index with the recall of the old index.
6. If the new recall is equal or better, move the alias to the new index.
7. After 7 days, delete the old index.
~~~

Changes: the risk as a caution (A1), one instruction in each step (P2), and no phrasal verbs (V7).

## 4. Metadata filtering

Type: mixed

Before:

~~~text
Post-filtering can return fewer than k results if most of the nearest neighbors get filtered out, so for selective filters like tenant_id you really want pre-filtering or a filterable index.
~~~

After:

~~~text
With post-filtering, the database finds the top k neighbors first. Then it removes the neighbors that do not match the filter. If the filter removes many neighbors, the query returns less than k results.

With pre-filtering, the database applies the filter first. Then it searches only the vectors that match the filter.

Use pre-filtering for a filter that removes most of the vectors, for example a filter on `tenant_id`.
~~~

Changes: one topic in each sentence (S1), the same key words in each paragraph (D3), and the instruction in a separate paragraph (D2).

## 5. An HNSW index with pgvector

Type: procedure

Before:

~~~text
To speed up similarity queries on the embeddings column, create an HNSW index with vector_cosine_ops; note it'll take a while to build on big tables and will block writes unless you use CONCURRENTLY.
~~~

After:

~~~text
CAUTION: Use the `CONCURRENTLY` keyword. If you do not use it, PostgreSQL does not let applications write to the table until the index is complete. On the `documents` table, the index build time is approximately 40 minutes.

1. Create the HNSW index:

   ```sql
   CREATE INDEX CONCURRENTLY documents_embedding_idx
   ON documents USING hnsw (embedding vector_cosine_ops);
   ```

2. Make sure that the index is valid:

   ```sql
   SELECT indisvalid FROM pg_index
   WHERE indexrelid = 'documents_embedding_idx'::regclass;
   ```

   The query returns `true`.
~~~

Changes: the risk as a caution before the steps (A3), no semicolon (T1), and the expected result (P5).
