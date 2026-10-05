# Writing rules

This file gives all the writing rules of this skill, with examples.
`SKILL.md` gives the most important rules in a short form.

The rule IDs are our own. They are not the rule numbers of the ASD-STE100 specification.
The rules use the principles of ASD-STE100 and adapt them to IT, data, and AI text.

In the examples, "Not STE" shows text to correct. "STE" shows correct text.

## Contents

- W: Words (W1 to W14)
- N: Noun clusters (N1 to N3)
- V: Verbs (V1 to V7)
- S: Sentences (S1 to S6)
- P: Procedures (P1 to P7)
- D: Descriptions (D1 to D4)
- R: Requirements and specifications (R1 to R4)
- A: Safety and risk notices (A1 to A4)
- T: Text format, punctuation, and word count (T1 to T8)
- M: Models, agents, and data statements (M1 to M6)
- G: General rules (G1 to G4)

## W: Words

**W1.** Use only these words: words from `core-vocabulary.md`, technical names, and technical verbs.

**W2.** Use a core word only as the part of speech that the vocabulary gives.
- Not STE: "Test the pipeline." ("test" is a noun)
- STE: "Do a test of the pipeline."
- Not STE: "Check the logs." ("check" is a noun)
- STE: "Examine the logs."

**W3.** Use a core word only with its narrow meaning. The list of narrow meanings is at the end of `core-vocabulary.md`.
- Not STE: "Follow the naming rules."
- STE: "Obey the naming rules."

**W4.** Use only the verb forms that the vocabulary gives.

**W5.** A technical name is the official name of an item. Technical names include:
- Products, services, and features: "Amazon S3", "BigQuery", "Snowpipe", "Microsoft Fabric".
- Data objects and code objects: "table", "schema", "partition", "column", "function", "endpoint".
- File formats, protocols, and standards: "Parquet", "JSON", "HTTPS", "OAuth 2.0", "RFC 2119".
- Roles, teams, and documents: "on-call engineer", "data owner", "runbook", "model card".
- Units, numbers, and time: "GB", "ms", "UTC", "p95".
- Quoted text from screens, buttons, logs, and messages: "Create bucket", "AccessDenied".

The files in `references/terms/` give the technical names of each field. The lists are not complete. Any official name is a technical name.

**W6.** Do not use a technical name as a verb.
- Not STE: "Snowpipe the files into the table."
- STE: "Use Snowpipe to load the files into the table."
- Not STE: "Slack the team."
- STE: "Send a message to the team in Slack."

**W7.** Use one name for one item. Do not change between names. If an official name is long, write the full name and the short name at the first use. Then use only the short name.
- STE: "Amazon Managed Workflows for Apache Airflow (Amazon MWAA)". Then: "Amazon MWAA".
- Not STE: "the orders table", "the order dataset", and "the sales data" for the same table.

**W8.** Use the current official name and spelling from the vendor. Write "PostgreSQL", "OpenSearch", "Kubernetes", "Microsoft Entra ID". `substitutions.md` gives former product names.

**W9.** Do not use slang or team jargon as a technical name.
- Not STE: "the big box", "the nightly thingy", "prod-ish data".
- STE: "the `etl-prod-01` server", "the nightly `orders_load` job", "a copy of the production data".

**W10.** Use a technical verb only when no core verb is sufficient. `technical-verbs.md` gives the technical verbs.
- Not STE: "Launch the job." STE: "Start the job."
- Not STE: "Detect the error in the log." STE: "Find the error in the log."

**W11.** Do not use a technical verb as a noun.
- Not STE: "The deploy failed."
- STE: "The deployment failed."

**W12.** Use American English spelling. Write "analyze", "color", "behavior", "canceled", "catalog".

**W13.** Do not use vague words. Give the specific value, name, or list.
- Not STE: "Increase the memory as needed."
- STE: "Increase the memory to 8 GiB."
- Not STE: "Use a large warehouse, etc."
- STE: "Use a warehouse of size Large or X-Large."

**W14.** Write the full term at the first use of an acronym. Then use the acronym. You can use these acronyms without the full term: API, CPU, GPU, RAM, SQL, JSON, CSV, HTTP, HTTPS, URL, DNS, IP, TLS, SSH, ID, UI, CLI, SDK, PDF, UTC, AI.

## N: Noun clusters

**N1.** Write a noun cluster of maximum three words. Articles and prepositions do not count. Use "of", "for", "in", or "on" to divide a long cluster.
- Not STE: "customer order fact table load job failure alert"
- STE: "the alert for the failure of the load job for the `fact_orders` table"

**N2.** A technical name counts as one unit in a cluster. If a technical name has more than three words, write it in full one time. Then use the short name (rule W7).

**N3.** Use an article ("a", "an", "the") or a demonstrative ("this", "these") before a noun. Do not use "the" before a noun that has an identifier.
- Not STE: "Restart service."
- STE: "Restart the service."
- STE: "Open port 443." "Run job 42."

## V: Verbs

**V1.** Use only these verb forms:
- the imperative
- the infinitive
- the simple present tense
- the simple past tense
- the future tense with "will"
- the past participle as an adjective.

**V2.** Do not use "has", "have", or "had" as a helping verb.
- Not STE: "The job has failed three times."
- STE: "The job failed three times."

**V3.** Do not use the "-ing" form of a verb. You can use an "-ing" word only when it is a technical name or a part of a technical name. Examples: "streaming", "partitioning", "embedding", "fine-tuning", "load balancing", "tool calling".
- Not STE: "The consumer is reading from the topic."
- STE: "The consumer reads from the topic."
- STE: "The streaming job reads from the topic."
- These "-ing" words are core words: during, existing, incoming, missing, outgoing, pending, remaining.

**V4.** Use only "can", "must", and "will" as helping verbs. Do not use "should", "would", "may", "might", "shall", or "ought to". Use "could" only as the past tense of "can".
- Not STE: "You should rotate the key every 90 days."
- STE: "Rotate the key every 90 days."
- Not STE: "The query may time out."
- STE: "If the query runs for more than 60 s, the query stops."

**V5.** Use the active voice. In a procedure, always use the active voice. In a description, use the active voice as much as possible. Make the agent the subject. If you do not know the agent, use "you" or "we".
- Not STE: "The file is uploaded by the job."
- STE: "The job uploads the file."
- Not STE: "The bucket must be encrypted."
- STE: "Encrypt the bucket."
- A past participle after "is" or "are" shows a condition. It is not the passive voice. STE: "The bucket is encrypted."

**V6.** Use a verb to show an action. Do not use a noun and a weak verb.
- Not STE: "Perform a restart of the service."
- STE: "Restart the service."
- Not STE: "The dashboard gives an indication of the error rate."
- STE: "The dashboard shows the error rate."

**V7.** Do not use phrasal verbs. A phrasal verb is a verb and a particle with a new meaning. `substitutions.md` gives replacements.
- Not STE: "Set up the cluster." STE: "Configure the cluster."
- Not STE: "Roll back the release." STE: "Revert the release."
- Not STE: "Spin up a new instance." STE: "Start a new instance."

## S: Sentences

**S1.** Write one topic in each sentence. Write short and clear sentences.

**S2.** Keep all the necessary words: the subject, the verb, the articles, and "that" after "make sure".
- Not STE: "If failed, rerun."
- STE: "If the job fails, run the job again."
- Not STE: "Make sure the file exists."
- STE: "Make sure that there is a file `orders.csv`."

**S3.** Do not use contractions. Write "do not", "cannot", and "it is".

**S4.** Use a vertical list for complex text. Put a colon at the end of the line before the list. In a list of commands with "not", write "not" in each item.
- STE: "Do not use these characters in a bucket name:" then one item for each character.

**S5.** Use connecting words to connect sentences: "and", "but", "then", "thus", "as a result", "if", "when".

**S6.** If a pronoun ("it", "this", "they") can refer to more than one noun, write the noun.
- Not STE: "The job reads the table and then it is locked."
- STE: "The job reads the table. Then the table is locked."

## P: Procedures

**P1.** Write maximum 20 words in each sentence of a procedure. This limit also applies to notices.

**P2.** Write one instruction in each sentence. Two actions are permitted only when they occur at the same time.
- Not STE: "Stop the job, rotate the key, and restart the job."
- STE: Three steps. "1. Stop the job." "2. Rotate the key." "3. Start the job."

**P3.** Write each instruction in the imperative.
- Not STE: "The engineer should then restart the pod."
- STE: "Restart the pod."

**P4.** When a condition comes before a command, put a comma after the condition.
- STE: "If the status is `FAILED`, examine the log of the task."

**P5.** Put each command in a code block after the step that uses it. Then give the expected result in a separate sentence.
- STE: "Show the status of the cluster." Then the command. Then: "The status is `ACTIVE`."

**P6.** Give each step a number. Write a decision as a condition. Write "If the test fails, go to step 7."

**P7.** A note gives information only. A note does not give an instruction. A note has maximum 25 words. If the information prevents damage or a loss, write a notice (rules A1 to A4).

## D: Descriptions

**D1.** Write maximum 25 words in each sentence of a description.

**D2.** Write one topic in each paragraph. Start the paragraph with a topic sentence. Write maximum six sentences in each paragraph.

**D3.** Use the same key word again in the next sentence. This shows the reader that the topic is the same.
- STE: "The job writes the data to a staging table. The staging table keeps the data for 7 days."

**D4.** Use a table to compare items or to give values, limits, and parameters.

## R: Requirements and specifications

Use these rules for data contracts, API specifications, service level agreements, security policies, and other requirements.

**R1.** Use "must" for a requirement and "must not" for a prohibition.
- A specification can use the keywords of RFC 2119 and RFC 8174.
- Write the keywords only in uppercase: MUST, MUST NOT, SHOULD, SHOULD NOT, MAY, REQUIRED, RECOMMENDED, OPTIONAL.
- Do not write "should" or "may" in lowercase.
- Use "MUST", not "SHALL".

**R2.** Write one requirement in each sentence. Give each requirement an ID.
- STE: "DC-03: The producer MUST send each event in less than 5 minutes."

**R3.** Give a value that you can measure.
- Not STE: "The API must be fast."
- STE: "The p95 latency of the API must be less than 300 ms."

**R4.** Make the actor the subject of the requirement: the producer, the consumer, the service, the data owner, the agent.

## A: Safety and risk notices

**A1.** Use the correct word for the level of risk:
- WARNING: one of these risks:
  - injury or death
  - a security or privacy breach
  - a loss of data that you cannot recover
  - a legal or compliance violation.
- CAUTION: a risk of damage that you can recover. Examples:
  - an outage or a decrease in performance
  - a large cost
  - a lock on a production table
  - a loss of data that you can restore from a backup.
- NOTE: information only. A note does not give a risk.

**A2.** Start the notice with a command or a condition. Then give the risk.
- STE: "WARNING: Do not delete the `prod-backups` bucket. The data in the bucket cannot be recovered."
- STE: "CAUTION: If you run this query on the production warehouse, the cost can be more than $500."

**A3.** Put the notice immediately before the step that has the risk.

**A4.** Write one risk in each notice.

## T: Text format, punctuation, and word count

**T1.** Do not use semicolons. Write two sentences.

**T2.** Use hyphens to connect words that make one unit. Examples: "read-only replica", "zero-copy clone", "multi-AZ deployment", "point-in-time recovery".

**T3.** Use parentheses for abbreviations, references, units, and short descriptions.

**T4.** Each of these items counts as one word:
- a number with its unit
- an identifier or an acronym
- quoted text or inline code
- a group of words with hyphens
- text in parentheses.

**T5.** Write code, commands, file names, paths, identifiers, keys, field names, and model IDs as inline code. The rules of this skill do not apply to code blocks.

**T6.** Write the text of the user interface in quotation marks. Do not change the text.
- STE: Click "Create bucket".

**T7.** Write numbers as digits with their units: "5 GB", "300 ms", "2 vCPU", "512 MiB". Write dates in ISO 8601: "2026-10-04". Write times in 24-hour format with the time zone: "14:30 UTC".

**T8.** Write a placeholder as inline code in angle brackets or in uppercase: `<bucket-name>`, `ACCOUNT_ID`. Tell the reader what value to use.

## M: Models, agents, and data statements

**M1.** Do not give human qualities to a model or an agent. Write what the system does.
- Not STE: "The model thinks that the answer is correct."
- STE: "The model returns the answer with a confidence score of 0.92."
- Not STE: "The agent decided to delete the files."
- STE: "The agent selected the `delete_files` tool."
- Not STE: "The model hallucinated a citation."
- STE: "The answer contains a citation that does not exist."
- "Hallucination" is a technical name. Use it only as a noun.

**M2.** Model output is not deterministic. Do not use the words "always" and "never" for model output. Give the measured value, the test set, and the date.
- Not STE: "The model is usually accurate."
- STE: "On 2026-09-30, the model gave a correct answer for 461 of 500 test questions (92%)."

**M3.** Give the full model ID and the version as inline code. Write `claude-sonnet-4-5`, not "the latest Claude model".

**M4.** Write prompts and agent instructions as procedures. Use the imperative, one instruction in each sentence, and conditions with a comma. The rules of this skill make instructions clear for a model and for a person.

**M5.** Name the actor in each step of an agent workflow: the user, the agent, the subagent, the tool, or the orchestrator.
- Not STE: "Then it calls the search tool."
- STE: "Then the agent calls the `search_orders` tool."

**M6.** When you give a fact from data, give the source, the time range, and the grain.
- Not STE: "Sales went up a lot."
- STE: "In the `fact_sales` table, the total sales for September 2026 increased by 12% from August 2026."

## G: General rules

**G1.** If a word-for-word replacement is not clear, write a new sentence. The reader must immediately understand each sentence.

**G2.** Use the same style in all the text. In a procedure, use the same words for the same type of step. Use the same name for the same item.

**G3.** The word "with" can have more than one meaning. Make the relation clear.
- Not clear: "Connect to the cluster with the admin role."
- Clear: "Use the admin role to connect to the cluster."

**G4.** If "this" can refer to more than one item, write the item again.
