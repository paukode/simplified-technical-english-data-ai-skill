# Examples: Google Cloud

Each example shows text before and after the change to STE.
The rule IDs refer to `references/writing-rules.md`.

## 1. A partitioned table in BigQuery

Type: description

Before:

~~~text
The events table is partitioned by event_date and clustered by user_id, so queries that filter on date only scan the relevant partitions, which keeps costs down significantly.
~~~

After:

~~~text
The `events` table has one partition for each day, on the column `event_date`. The table also has clustering on the column `user_id`.

If a query has a filter on `event_date`, BigQuery reads only the partitions for those days. In the test on 2026-09-30, a query for one day read 2.1 GB instead of 640 GB.
~~~

Changes: identifiers as inline code (T5), the active voice (V5), and a measured value instead of a vague word (W13, M6).

## 2. Deploy a service to Cloud Run

Type: procedure

Before:

~~~text
Once your container image is built and pushed to Artifact Registry, you can go ahead and deploy it to Cloud Run with gcloud, making sure to set the min instances to 1 so you don't hit cold starts.
~~~

After:

~~~text
1. Build the container image.
2. Push the image to Artifact Registry.
3. Deploy the image to Cloud Run:

   ```bash
   gcloud run deploy orders-api --image=IMAGE_URL --region=europe-west1 --min-instances=1
   ```

   The command shows the URL of the service.
4. Open the URL. Make sure that the service returns the status code 200.

NOTE: The setting `--min-instances=1` keeps one instance ready. This prevents a cold start, but it increases the cost.
~~~

Changes: one instruction in each step (P2), the command and the expected result (P5), and a note for information only (P7).

## 3. Use Workload Identity Federation for CI/CD

Type: mixed

Before:

~~~text
Downloading service account keys is a big security risk since they never expire and can easily be leaked. It's much better to use Workload Identity Federation so that GitHub Actions can authenticate without any long-lived credentials.
~~~

After:

~~~text
A service account key does not expire. If a person gets a copy of the key, the person can use the key until you delete it.

Workload Identity Federation lets GitHub Actions get short-lived credentials from Google Cloud. This method does not use a key. Thus, there is no key to store or to protect.

WARNING: Do not make a service account key for a CI/CD pipeline. Use Workload Identity Federation.
~~~

Changes: no "-ing" verb forms (V3), short sentences (D1), the risk as a warning (A1), and no contractions (S3).

## 4. Dead-letter topic for Pub/Sub

Type: description

Before:

~~~text
If a subscriber keeps failing to process a message, Pub/Sub will keep redelivering it forever unless you configure a dead-letter topic, which is where messages end up after max delivery attempts is reached.
~~~

After:

~~~text
If a subscriber does not acknowledge a message, Pub/Sub sends the message again.

A dead-letter topic sets a limit for these attempts. After the maximum number of delivery attempts, Pub/Sub sends the message to the dead-letter topic. The subscriber then receives the next message.

For the `orders-sub` subscription, the maximum number of delivery attempts is 5.
~~~

Changes: one topic in each sentence (S1), no phrasal verbs (V7), and a specific value (W13).

## 5. Cost model of GKE Autopilot

Type: description

Before:

~~~text
With Autopilot, Google manages the nodes for you, so you only pay for the resources your pods actually request instead of for whole VMs, which is great for spiky workloads.
~~~

After:

~~~text
In GKE Autopilot, Google Cloud controls the nodes of the cluster. The cost is for the CPU, the memory, and the storage in the resource requests of the pods. The cost is not for the nodes.

Thus, GKE Autopilot is a good selection for workloads that change frequently.
~~~

Changes: the official product name (W8), no vague words (W13), and no jargon (W9).
