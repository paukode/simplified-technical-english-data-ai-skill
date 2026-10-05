# Examples: data engineering

Each example shows text before and after the change to STE.
The rule IDs refer to `references/writing-rules.md`.

## 1. Backfill a table after duplicate events

Type: procedure

Before:

~~~text
We need to backfill the orders_daily table for the last week since the upstream source was sending duplicate events. Make sure you clear the affected partitions first or you'll end up double counting.
~~~

After:

~~~text
CAUTION: Delete the data in each partition before you load it again. If you do not delete it, the table will contain duplicate rows.

1. Pause the `orders_daily` DAG in Airflow.
2. Delete the partitions of the `orders_daily` table for the days from 2026-09-27 to 2026-10-03.
3. Run the backfill for the same days:

   ```bash
   airflow backfill create --dag-id orders_daily --from-date 2026-09-27 --to-date 2026-10-03
   ```

4. Make sure that the row count of each day is the same as the row count in the source system.
5. Resume the `orders_daily` DAG.
~~~

Changes: the risk as a caution before the steps (A3), specific dates (T7), and no "-ing" verb forms (V3).

## 2. An idempotent pipeline

Type: description

Before:

~~~text
The pipeline is idempotent, meaning you can rerun it as many times as you want without messing up the data, because each run overwrites the target partition instead of appending to it.
~~~

After:

~~~text
The pipeline is idempotent. If you run it again for the same date, the result in the target table is the same.

Each run overwrites the partition for its date. It does not append rows to the partition. Thus, a second run does not make duplicate rows.
~~~

Changes: short sentences (D1), one topic in each sentence (S1), and no slang (W9).

## 3. A DAG run failed in Airflow

Type: procedure

Before:

~~~text
When the DAG fails, have a look at the task logs in the Airflow UI. If it's a transient error like a timeout, just clear the task so it retries; otherwise escalate to the data platform team.
~~~

After:

~~~text
1. In the Airflow UI, open the DAG run that failed.
2. Find the task that has the status `failed`.
3. Read the log of the task.
4. If the error is a timeout or a connection error, select the task and click "Clear". Airflow then runs the task again.
5. If the error is a different error, send the log to the data platform team in Slack.
~~~

Changes: no semicolon (T1), each decision as a condition (P6), and the label of the screen in quotation marks (T6).

## 4. Consumer lag on a Kafka topic

Type: mixed

Before:

~~~text
Consumer lag on orders-events is spiking because the consumer group can't keep up; we should probably scale out the consumers, but first check if a partition is stuck.
~~~

After:

~~~text
The lag of the `order-processor` consumer group on the `orders-events` topic is 250,000 messages. The limit is 50,000.

1. Find the lag of each partition.
2. If the lag is high on only one partition, examine the consumer that reads that partition.
3. If the lag is high on all the partitions, increase the number of consumers.

NOTE: The number of active consumers in the group cannot be more than the number of partitions. The topic has 12 partitions.
~~~

Changes: the value and the limit (M6), no phrasal verbs (V7), no semicolon (T1), and a note that gives a limit (P7).

## 5. A data contract for the orders data

Type: specification

Before:

~~~text
The orders feed should land in the raw zone by 6am UTC daily, order_id must never be null and should be unique, and any breaking schema change needs at least two weeks' notice to downstream consumers.
~~~

After:

~~~text
This contract uses the keywords MUST, MUST NOT, and SHOULD as RFC 2119 gives them.

- DC-01: The producer MUST send the data for each day to the raw zone before 06:00 UTC.
- DC-02: The column `order_id` MUST NOT be null.
- DC-03: Each value of `order_id` MUST be unique in the table.
- DC-04: The producer MUST give the consumers a notice of 14 days before a breaking schema change.
- DC-05: The producer SHOULD send the data for each day before 04:00 UTC.
~~~

Changes: one requirement in each item with an ID (R2), RFC 2119 keywords in uppercase (R1), and values that you can measure (R3).

## 6. Change data capture with Debezium

Type: description

Before:

~~~text
We use Debezium to stream changes from the Postgres WAL into Kafka, which gives us near-real-time replication without hammering the source DB with queries.
~~~

After:

~~~text
Debezium reads the changes from the write-ahead log (WAL) of the `orders` PostgreSQL database. It sends each change as an event to a Kafka topic.

This method does not send queries to the source database. Thus, it adds almost no load to the database. In September 2026, the p95 time between a change in the database and its event in Kafka was 1.4 seconds.
~~~

Changes: the full term before the acronym (W14), a measured value (M2), and no slang (W9).

## 7. A dbt test failed

Type: procedure

Before:

~~~text
If the not_null test on stg_payments.payment_id fails, it's almost always because the upstream Stripe sync had a hiccup. Rerun the sync and then rerun dbt build for that model and its children.
~~~

After:

~~~text
1. Make sure that the last sync of the `stripe` connector in Fivetran is complete.
2. If the sync failed, run the sync again.
3. Run the model and the models that use it:

   ```bash
   dbt build --select stg_payments+
   ```

4. Make sure that the `not_null` test on `stg_payments.payment_id` passes.
~~~

Changes: one instruction in each step (P2), the command in a code block (P5), and no slang (W9).
