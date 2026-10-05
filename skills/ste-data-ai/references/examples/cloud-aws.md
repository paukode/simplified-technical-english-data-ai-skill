# Examples: Amazon Web Services (AWS)

Each example shows text before and after the change to STE.
The rule IDs refer to `references/writing-rules.md`.

## 1. Block public access to the S3 buckets of an account

Type: procedure

Before:

~~~text
To prevent data leaks, you should make sure that Block Public Access is turned on for all of your buckets. It can be enabled at the account level, which is recommended, so that new buckets are automatically protected.
~~~

After:

~~~text
WARNING: If a bucket is public, any person on the internet can read the data in the bucket.

1. Open the Amazon S3 console.
2. In the navigation pane, click "Block Public Access settings for this account".
3. Click "Edit".
4. Select "Block all public access".
5. Click "Save changes".

The setting applies to all the buckets in the account. It also applies to new buckets.
~~~

Changes: the risk first (A2), one action in each step (P2), the labels of the screen in quotation marks (T6), and no "should" (V4).

## 2. Least privilege for a Lambda function

Type: mixed

Before:

~~~text
The Lambda function's execution role has been given broad permissions, which isn't ideal. Ideally it should only be allowed to read from the specific S3 prefix and write to one DynamoDB table.
~~~

After:

~~~text
The execution role of the `export-orders` Lambda function has the `AmazonS3FullAccess` policy. This policy gives access to all the buckets in the account.

The function only reads objects from the prefix `exports/`. It only writes items to the `orders` DynamoDB table.

Replace the policy with a policy that gives only these two permissions.
~~~

Changes: the simple present tense (V2), specific names (W13), and the description and the instruction in separate paragraphs (D2).

## 3. Cold starts of a Lambda function

Type: description

Before:

~~~text
Users may experience slow responses on the first request after the function has been idle for a while, because Lambda has to spin up a new execution environment (a "cold start"). This can be mitigated using provisioned concurrency, although it does add cost.
~~~

After:

~~~text
If a Lambda function receives no requests for a period, Lambda removes its execution environments. The next request then starts a new execution environment. This cold start adds approximately 800 ms to the response time of the `checkout` function.

Provisioned concurrency keeps a specified number of execution environments ready. It prevents the cold start, but it increases the cost.
~~~

Changes: a measured value (M6), no "may" (V4), no phrasal verbs (V7), and no passive voice (V5).

## 4. Upgrade an EKS cluster

Type: procedure

Before:

~~~text
Before upgrading the EKS cluster, you'll want to make sure all the add-ons are compatible with the new Kubernetes version, otherwise pods might fail to schedule. Then upgrade the control plane first, followed by the managed node groups.
~~~

After:

~~~text
CAUTION: If an EKS add-on is not compatible with the new version, the pods can fail to start.

1. Make sure that each EKS add-on is compatible with Kubernetes version 1.33.
2. Upgrade the control plane of the EKS cluster to version 1.33.
3. Wait until the status of the cluster is `ACTIVE`.
4. Upgrade each managed node group to version 1.33.
~~~

Changes: the caution before the steps (A3), the sequence as numbered steps (P6), and "make sure that" (S2).

## 5. Stop the development instances at night

Type: mixed

Before:

~~~text
We're burning money on dev instances that sit idle overnight. Going forward, all non-prod EC2 instances should be shut down at 8pm and brought back up at 7am using an EventBridge schedule.
~~~

After:

~~~text
The EC2 instances in the development environment operate for 24 hours each day. Each night, the team does not use them for 11 hours.

To decrease the cost, make two EventBridge Scheduler schedules for the instances that have the tag `env=dev`:

1. Make a schedule that stops the instances at 20:00 UTC.
2. Make a schedule that starts the instances at 07:00 UTC.

CAUTION: Do not apply the tag `env=dev` to a production instance. The schedule stops each instance that has this tag.
~~~

Changes: no jargon (W9), no phrasal verbs (V7), times in 24-hour format with the time zone (T7), and a caution for the risk (A1).
