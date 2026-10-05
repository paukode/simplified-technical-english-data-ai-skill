# Examples: Microsoft Azure

Each example shows text before and after the change to STE.
The rule IDs refer to `references/writing-rules.md`.

## 1. Rotate the key of a storage account

Type: mixed

Before:

~~~text
The storage account key used by the ETL app needs rotating every 90 days. It's stored in Key Vault, so you just need to regenerate key2, update the secret, and then regenerate key1 once everything's switched over.
~~~

After:

~~~text
Rotate the access key of the storage account at intervals of 90 days. This procedure prevents an outage of the ETL application.

1. In the Azure portal, open the `etlprodstorage` storage account.
2. Generate a new value for `key2`.
3. In Azure Key Vault, write the new value of `key2` to the secret `etl-storage-key`.
4. Wait 10 minutes. The ETL application reads the secret again at intervals of 10 minutes.
5. Generate a new value for `key1`.
~~~

Changes: one instruction in each step (P2), the reason for the wait (P7), and no vague words (W13).

## 2. The hierarchical namespace of Azure Data Lake Storage

Type: mixed

Before:

~~~text
You'll want to enable the hierarchical namespace when creating the storage account, since it can't be turned on later without a migration, and it's what gives you real directories and POSIX ACLs, which Spark and Synapse rely on.
~~~

After:

~~~text
Azure Data Lake Storage Gen2 uses the hierarchical namespace of a storage account. The hierarchical namespace gives directories and access control lists (ACLs) for files and for directories.

Enable the hierarchical namespace when you create the storage account. If you do not enable it at that time, you must do a migration to enable it.
~~~

Changes: no contractions (S3), the full name before the acronym (W14), and the description and the instruction in separate paragraphs (D2).

## 3. Failure of a pipeline in Azure Data Factory

Type: procedure

Before:

~~~text
When the nightly ADF pipeline fails, check the activity run output in the Monitor tab to see which activity blew up and why. Most of the time it's the self-hosted IR being offline, so restart the IR service on the VM and rerun from the failed activity.
~~~

After:

~~~text
1. In Azure Data Factory, open the "Monitor" page.
2. Select the failed run of the `nightly_load` pipeline.
3. Find the activity that has the status "Failed".
4. Examine the error message of the activity.
5. If the self-hosted integration runtime is not available, go to step 6. If not, go to step 8.
6. On the VM of the integration runtime, restart the integration runtime service.
7. On the "Monitor" page, run the pipeline again from the failed activity.
8. Send the error message to the data platform team.
~~~

Changes: numbered steps with conditions (P6), the full name instead of an acronym (W14), and no slang (W9).

## 4. Private endpoint for Azure SQL Database

Type: mixed

Before:

~~~text
By using a private endpoint for the SQL database, traffic stays on the Microsoft backbone and never traverses the public internet, which basically eliminates exposure.
~~~

After:

~~~text
A private endpoint gives the Azure SQL Database a private IP address in the virtual network. Applications in the virtual network connect to the database through this IP address.

The traffic between the applications and the database does not go through the public internet.

Disable the public network access on the database server. This blocks all other connections.
~~~

Changes: the official product name (W8), no vague words (W13), and the instruction in a separate paragraph (D2).

## 5. Spark notebooks on a Fabric capacity

Type: mixed

Before:

~~~text
Heads up: if a big Spark notebook gets kicked off during business hours it can eat up the whole F64 capacity and everyone's Power BI reports will slow to a crawl due to throttling.
~~~

After:

~~~text
CAUTION: Do not start a large Spark notebook on the F64 capacity during business hours. The notebook can use all of the capacity. Then Fabric throttles the other workloads, and the Power BI reports become slow.

Start large Spark notebooks after 19:00 UTC, or use a separate capacity for them.
~~~

Changes: the risk as a caution (A1, A2), no slang or phrasal verbs (W9, V7), and a specific time (T7).
