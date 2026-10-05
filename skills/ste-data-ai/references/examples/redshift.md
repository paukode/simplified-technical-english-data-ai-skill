# Examples: Amazon Redshift

Each example shows text before and after the change to STE.
The rule IDs refer to `references/writing-rules.md`.

## 1. Select a distribution key

Type: mixed

Before:

~~~text
Since fact_sales and dim_customer are always joined on customer_id, we should probably use customer_id as the DISTKEY on both tables to avoid data redistribution at query time.
~~~

After:

~~~text
The `fact_sales` table and the `dim_customer` table join on the column `customer_id`. If both tables use `customer_id` as the distribution key, the rows with the same key are on the same slice. Then the join does not move data between the nodes.

Use `customer_id` as the distribution key of the two tables. Before you make the change, make sure that the values of `customer_id` do not cause data skew.
~~~

Changes: no "should" (V4), identifiers as inline code (T5), and the risk of the change (A2).

## 2. VACUUM and ANALYZE after a large delete operation

Type: procedure

Before:

~~~text
After the big monthly delete, run VACUUM DELETE ONLY and then ANALYZE on the table, otherwise query performance will tank because of all the dead rows and stale stats.
~~~

After:

~~~text
Do these steps after the delete operation of each month on the `events` table:

1. Remove the deleted rows:

   ```sql
   VACUUM DELETE ONLY events;
   ```

2. Update the statistics of the table:

   ```sql
   ANALYZE events;
   ```

If you do not do these steps, the queries on the table scan the deleted rows. As a result, the queries become slow.
~~~

Changes: one command in each step (P2, P5), the result of the risk (A2), and no slang (W9).

## 3. Concurrency scaling at the end of the month

Type: description

Before:

~~~text
During month-end, BI queries pile up in the WLM queue. Turning on concurrency scaling lets Redshift add transient clusters to handle the burst, and you get one hour of free credits per day.
~~~

After:

~~~text
At the end of each month, the business intelligence (BI) dashboards send more queries than the cluster can run at the same time. The queries then wait in the WLM queue.

Concurrency scaling adds temporary clusters when queries wait in the queue. The primary cluster gets 1 hour of free concurrency scaling credits for each 24 hours that it operates. After these free credits, the cost is for each second that the temporary clusters operate.
~~~

Changes: the full term before the acronym (W14), no phrasal verbs (V7), and specific values (W13).

## 4. Base capacity of Redshift Serverless

Type: mixed

Before:

~~~text
Be careful bumping the base RPUs on the serverless workgroup - going from 32 to 128 RPUs quadruples the hourly cost even if the queries don't need it.
~~~

After:

~~~text
CAUTION: Do not increase the base capacity of the `analytics` workgroup to 128 RPUs without approval. When queries run, the cost for each second is 4 times the cost at 32 RPUs.

Before you change the base capacity, compare the query times at 32 RPUs and at 64 RPUs.
~~~

Changes: the cost risk as a caution (A1), a command first (A2), and no slang (W9).

## 5. Load Parquet files with COPY

Type: procedure

Before:

~~~text
To load the daily parquet files, just run a COPY from the S3 prefix using the cluster's default IAM role; make sure the column order matches the table.
~~~

After:

~~~text
1. Make sure that the columns in the Parquet files have the same order as the columns of the `sales` table.
2. Load the files from Amazon S3:

   ```sql
   COPY sales
   FROM 's3://example-bucket/sales/2026-10-04/'
   IAM_ROLE DEFAULT
   FORMAT AS PARQUET;
   ```

3. Examine the `SYS_LOAD_ERROR_DETAIL` view for errors.
~~~

Changes: no semicolon in the text (T1), "make sure that" (S2), and the command in a code block (P5).
