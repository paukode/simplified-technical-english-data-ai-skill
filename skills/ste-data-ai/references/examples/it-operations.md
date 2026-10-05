# Examples: IT operations

Each example shows text before and after the change to STE.
The rule IDs refer to `references/writing-rules.md`.

## 1. Restart the pods after a memory alert

Type: procedure

Before:

~~~text
If you're seeing the high memory alert for the payments API, you should first check the dashboard to figure out whether memory has been growing steadily. If it has, the service probably has a memory leak and you'll want to restart the pods one at a time so we don't take down the whole service.
~~~

After:

~~~text
CAUTION: Restart only one pod at a time. If you restart all the pods together, the `payments` API stops.

1. Open the "Payments API" dashboard in Grafana.
2. Examine the memory graph for the last 6 hours.
3. If the memory increases continuously, go to step 4. If not, go to step 7.
4. Restart one pod:

   ```bash
   kubectl delete pod <pod-name> -n payments
   ```

   Kubernetes starts a new pod.
5. Wait until the status of the new pod is `Running`.
6. Do steps 4 and 5 again for each pod.
7. Send a message to the `#payments-oncall` channel in Slack.
~~~

Changes: a caution before the steps (A1, A3), one instruction in each step (P2), each decision as a condition (P6), and no phrasal verbs (V7).

## 2. Incident summary

Type: description

Before:

~~~text
On Tuesday we had a pretty bad outage where customers couldn't log in for about 45 minutes. It turned out that a config change to the auth service, which had been pushed without being reviewed, broke token validation. The on-call engineer rolled back the change once the issue was identified and things went back to normal.
~~~

After:

~~~text
On 2026-09-29 from 14:05 to 14:50 UTC, all the sign-in requests to the web application failed. The duration of the outage was 45 minutes.

The cause was a configuration change to the authentication service. After the change, the service did not validate the access tokens. The team deployed the change without a code review.

At 14:42 UTC, the on-call engineer reverted the change. At 14:50 UTC, the error rate of the sign-in requests was 0%.
~~~

Changes: dates and times in UTC (T7), the simple past tense (V2), the active voice (V5), and no jargon (W9).

## 3. Alert text

Type: procedure

Before:

~~~text
CRITICAL!!! Disk space is running really low on db-prod-03, please look into this ASAP before the database goes down!!
~~~

After:

~~~text
The free disk space on `db-prod-03` is 4%. The limit is 10%. Open the runbook "Low disk space on a database server".
~~~

Changes: the value and the limit (M6), the first action (P3), and no vague words (W13).

## 4. Error message for a failed upload

Type: procedure

Before:

~~~text
Oops! Something went wrong while uploading your file. It might be too big or the server could be having issues. Please try again later.
~~~

After:

~~~text
The system did not upload the file. The file is larger than the limit of 5 GB. Divide the file into parts. Then upload each part.
~~~

Changes: the cause and the action (P3), one instruction in each sentence (P2), and no "might" (V4).

## 5. Change request for a database upgrade

Type: mixed

Before:

~~~text
We're planning to upgrade the Postgres cluster from 14 to 16 this Saturday night. There may be a few minutes of downtime while the failover happens. Rollback plan: if anything breaks we'll restore from the snapshot taken right before the upgrade.
~~~

After:

~~~text
Change: upgrade the `orders-db` PostgreSQL cluster from version 14 to version 16.
Time window: 2026-10-10, from 22:00 to 23:00 UTC.
Risk: the database is not available for approximately 5 minutes during the failover.

Steps:

1. Make a manual snapshot of the cluster.
2. Upgrade the cluster to version 16.
3. Do the smoke test for the orders API.

Rollback: if the smoke test fails, restore the cluster from the snapshot of step 1.
~~~

Changes: the official product name (W8), a specific time window (T7), numbered steps (P6), and no "may" (V4).

## 6. Rotate a leaked access key

Type: procedure

Before:

~~~text
Someone accidentally committed an AWS access key to the repo. We need to rotate it ASAP and scrub it from the git history, otherwise attackers could use it to spin up resources in our account.
~~~

After:

~~~text
WARNING: Do the steps that follow immediately. An attacker can use the access key to create resources in the AWS account.

1. Make the access key inactive in the IAM console.
2. Create a new access key for the IAM user.
3. Write the new key to the secret `ci/aws-deploy` in AWS Secrets Manager.
4. Delete the old access key.
5. Remove the key from the history of the Git repository.
~~~

Changes: a warning for a security risk (A1, A2), one instruction in each step (P2), and no phrasal verbs or jargon (V7, W9).
