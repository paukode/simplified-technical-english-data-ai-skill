# Examples: Snowflake

Each example shows text before and after the change to STE.
The rule IDs refer to `references/writing-rules.md`.

## 1. Decrease the auto-suspend time of a warehouse

Type: mixed

Before:

~~~text
The TRANSFORM_WH warehouse has auto-suspend set to 30 minutes, which means we're paying for a lot of idle time. It should be lowered to 60 seconds since the dbt jobs run back to back anyway.
~~~

After:

~~~text
The `TRANSFORM_WH` warehouse stops 30 minutes after its last query. During these 30 minutes, the warehouse uses credits but does no work.

Set the auto-suspend time of the warehouse to 60 seconds:

```sql
ALTER WAREHOUSE TRANSFORM_WH SET AUTO_SUSPEND = 60;
```

The dbt jobs run one after the other. Thus, the warehouse does not stop between the jobs.
~~~

Changes: no "should" (V4), no vague words (W13), and the command in a code block (P5).

## 2. Time Travel and Fail-safe

Type: description

Before:

~~~text
Accidentally dropped a table? No worries, Time Travel lets you UNDROP it as long as you're still within the retention period, which defaults to 1 day but can be bumped up to 90 days on Enterprise.
~~~

After:

~~~text
Time Travel keeps the old versions of the data for a retention period. During this period, you can use the `UNDROP TABLE` command to restore a table that you dropped.

The default retention period is 1 day. In Enterprise edition, you can set the retention period to a value from 0 to 90 days.

After the retention period, Fail-safe keeps the data for 7 more days. Only Snowflake Support can recover data from Fail-safe.
~~~

Changes: full sentences (S2), the official edition name (W8), and no slang (W9).

## 3. A zero-copy clone for tests

Type: procedure

Before:

~~~text
Instead of copying prod data into the test environment, just clone the database - it's instant and doesn't cost extra storage until you start modifying data.
~~~

After:

~~~text
1. Make a zero-copy clone of the production database:

   ```sql
   CREATE DATABASE analytics_test CLONE analytics_prod;
   ```

2. Do the tests on the `analytics_test` database.
3. When the tests are complete, drop the `analytics_test` database.

NOTE: A zero-copy clone does not copy the data when you make it. The clone uses more storage only for the data that you change.
~~~

Changes: numbered steps (P6), no jargon (W9), and the facts in a note (P7).

## 4. Masking policy for PII columns

Type: specification

Before:

~~~text
PII columns like email and phone should be masked for everyone except the PII_READER role. The masking policy shall be applied via tags so new columns get covered automatically.
~~~

After:

~~~text
This specification uses the keywords MUST and MUST NOT as RFC 2119 gives them.

- MP-01: The data owner MUST apply the tag `pii=true` to each column that contains PII.
- MP-02: The tag `pii=true` MUST have the masking policy `pii_mask`.
- MP-03: The masking policy MUST show the value of the column only to the role `PII_READER`.
- MP-04: For all other roles, the masking policy MUST show the value `***MASKED***`.
- MP-05: A new column with the tag `pii=true` MUST get the masking policy automatically.
~~~

Changes: one requirement in each item with an ID (R2), the actor as the subject (R4), and MUST instead of "shall" (R1).

## 5. Snowpipe does not load new files

Type: procedure

Before:

~~~text
If files are landing in the stage but not showing up in the table, Snowpipe probably choked on a bad file. Check COPY_HISTORY for the pipe and look at the error, then fix the file and reload it.
~~~

After:

~~~text
Use this procedure if there are new files in the stage, but the table does not get new rows.

1. Show the load history of the table for the last 24 hours:

   ```sql
   SELECT file_name, status, first_error_message
   FROM TABLE(INFORMATION_SCHEMA.COPY_HISTORY(
     TABLE_NAME => 'RAW.ORDERS',
     START_TIME => DATEADD(hour, -24, CURRENT_TIMESTAMP())));
   ```

2. Find the files that have the status `LOAD_FAILED`.
3. Read the value of `first_error_message` for each file.
4. Correct the error in the file.
5. Upload the corrected file to the stage with a new file name.
~~~

Changes: one instruction in each step (P2), the query in a code block (P5), and no slang (W9).

## 6. Cortex Search

Type: description

Before:

~~~text
Cortex Search basically gives you a fully managed hybrid search service over your text data, so you don't have to stand up your own vector DB or worry about keeping embeddings in sync.
~~~

After:

~~~text
Cortex Search is a Snowflake service for search in text data. It uses vector search and keyword search together (hybrid search).

Cortex Search makes the embeddings and keeps the index current. You do not operate a separate vector database. The `TARGET_LAG` parameter sets the maximum time before a change in the source table shows in the index.
~~~

Changes: no vague words (W13), no phrasal verbs (V7), and the full term instead of jargon (W9).
