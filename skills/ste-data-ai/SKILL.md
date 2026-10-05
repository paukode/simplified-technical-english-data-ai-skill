---
name: ste-data-ai
description: Writes, rewrites, and checks technical text in Simplified Technical English (STE), a controlled English with a small vocabulary and strict rules for clear and short text. Use it when the user asks for STE, Simplified Technical English, controlled English, or plain technical English, or asks to check text against STE rules. Covers IT operations, AWS, Google Cloud, Azure, data engineering, data architecture, Snowflake, Amazon Redshift, OpenSearch, vector databases, machine learning, generative AI, and agentic AI. Typical text is runbooks, incident reports, ADRs, data contracts, model cards, prompts, and agent instructions.
license: MIT (see LICENSE.txt)
compatibility: Agent Skills format. Works in Claude, Codex, Kiro, Whisper Studio, and other agents that read SKILL.md. The optional check script needs Python 3.8 or later and no other packages.
metadata:
  version: "1.0.0"
  standard: "ASD-STE100 principles, not an official ASD document"
---

# Simplified Technical English for IT, data, and AI

This skill makes you write technical text in Simplified Technical English (STE).
STE is a controlled form of English with a small vocabulary and strict writing rules.
Text in STE is short, clear, and easy to translate.
A reader who does not speak English as a first language can understand it.

This skill adapts STE to IT, cloud, data, machine learning, generative AI, and agentic AI.
The rules in this file are the most important rules.
The full rules, with examples, are in `references/writing-rules.md`.

## When to use STE

Use STE for these types of text:

| Type of text | Level |
|---|---|
| Runbooks, procedures, setup steps, alerts, and error messages | Strict: obey all the rules |
| Incident reports, postmortems, and change requests | Strict |
| Data contracts, API specifications, SLAs, and security policies | Strict, with the rules for specifications |
| Model cards, pipeline documents, and schema documents | Standard: obey all the rules, and use tables for values |
| Architecture decision records (ADRs) and design documents | Basic: obey the rules for verbs, sentences, and words |
| Prompts, agent instructions, and tool descriptions | Standard |

Do not apply STE to:

- Code, commands, configuration, identifiers, file paths, and log output.
- Quoted text, for example the text of a screen or of an error message.
- The official names of products, services, documents, and persons.
- Marketing text, fiction, and conversation.

If the user asks for a different style, obey the user.

## Step 1: Identify the type of text

Before you write, identify the type of each part of the text:

- A procedure tells the reader what to do. Example: "Restart the service."
- A description gives information. Example: "The job loads the data each hour."
- A specification gives requirements. Example: "The producer must send each event in less than 5 minutes."

Each type has a different limit for the length of a sentence.
Do not put a procedure and a description in the same paragraph.

## Step 2: Obey the verb rules

- Use only these verb forms:
  - the imperative
  - the infinitive
  - the simple present tense
  - the simple past tense
  - the future tense with "will"
  - the past participle as an adjective.
- Do not use "has", "have", or "had" as a helping verb. Write "the job failed", not "the job has failed".
- Do not use the "-ing" form of a verb. Write "the consumer reads the topic", not "the consumer is reading the topic".
- You can use an "-ing" word in a technical name. Examples: "streaming", "partitioning", and "fine-tuning".
- Use only "can", "must", and "will" as helping verbs. Do not use "should", "would", "may", "might", or "shall".
- Use the active voice. Write "the job writes the file", not "the file is written by the job".
- In a procedure, use the imperative. Write "Rotate the key."
- A past participle after "is" or "are" shows a condition. It is permitted. Write "the bucket is encrypted".
- Do not use phrasal verbs. Write "configure", not "set up". Write "revert", not "roll back".

## Step 3: Obey the sentence rules

- Write maximum 20 words in each sentence of a procedure.
- Write maximum 25 words in each sentence of a description or a specification.
- Write maximum 6 sentences in each paragraph. Write one topic in each paragraph.
- Write one instruction in each sentence. Two actions are permitted only when they occur at the same time.
- When a condition comes before a command, put a comma after the condition. Write "If the job fails, examine the log."
- Keep the articles, the subject, the verb, and the word "that" after "make sure".
- Do not use contractions. Write "do not", not "don't".
- Do not use semicolons. Write two sentences.
- Use a vertical list for complex text. In a list of commands with "not", write "not" in each item.

## Step 4: Obey the word rules

- Use only these words: the core words in `references/core-vocabulary.md`, technical names, and technical verbs.
- A technical name is the official name of an item. Examples: a product, a service, a data object, a file format, a protocol, or a role.
- The files in `references/terms/` give the technical names of each field. The lists are not complete. Any official name is a technical name.
- A technical verb shows a process that a core verb cannot show. The technical verbs are in `references/technical-verbs.md`.
- Use a core verb when it is sufficient. Write "start the job", not "launch the job".
- Use a word only as its part of speech. The words "test" and "check" are nouns. Write "do a test of the pipeline" and "examine the logs".
- Do not use a technical name as a verb. Write "use Snowpipe to load the files", not "Snowpipe the files".
- Use one name for one item. Do not change between names for the same table, service, or model.
- Use the current official name of a product. Write "Microsoft Entra ID", not "Azure AD".
- Write a noun cluster of maximum three words. Use "of", "for", "in", or "on" to divide a long cluster.
- Do not use vague words. Give the value, the name, or the list. Write "8 GiB", not "more memory as needed".
- Use American English spelling.
- The file `references/substitutions.md` gives replacements for frequent words that are not permitted.

## Step 5: Obey the rules for IT, data, and AI

- Write code, commands, file names, paths, identifiers, field names, and model IDs as inline code. The rules do not apply to code blocks.
- Put each command in a code block after the step that uses it. Then give the expected result in a separate sentence.
- Write the text from a screen in quotation marks. Do not change the text. Example: Click "Create bucket".
- Write numbers as digits with their units: 5 GB, 300 ms, 2 vCPU. Write dates as 2026-10-04 and times as 14:30 UTC.
- At the first use of a long name or an acronym, write the full name and then the short name in parentheses. Then use only the short name.
- Do not give human qualities to a model or an agent. Write what the system does. Write "the model returns", not "the model thinks".
- Model output is not deterministic. Do not use the words "always" and "never" for model output. Give the measured value, the test set, and the date.
- Give the full model ID as inline code. Example: `claude-sonnet-4-5`.
- In an agent workflow, name the actor of each step. Examples: the user, the agent, a subagent, or a tool.
- When you give a fact from data, give the source, the time range, and the grain.
- Write prompts and agent instructions as procedures. Use the imperative, one instruction in each sentence, and a comma after each condition.
- In a specification that uses RFC 2119, you can write MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY in uppercase. Do not write these words in lowercase.

## Step 6: Write the safety and risk notices

Use the correct word for the level of risk:

- WARNING: a risk of injury, a security or privacy breach, a loss of data that you cannot recover, or a legal or compliance violation.
- CAUTION: a risk of damage that you can recover. Examples: an outage, a large cost, or a lock on a production table.
- NOTE: information only. A note does not give an instruction.

Start the notice with a command or a condition. Then give the risk.
Put the notice immediately before the step that has the risk.

Example: "WARNING: Do not delete the `prod-backups` bucket. You cannot recover the data in the bucket."

## Step 7: Check the text

After you write, check the text:

1. If you can run a script, run the check script. The path starts at the folder of this skill.

   ```bash
   python3 scripts/ste_check.py --mode auto FILE
   ```

2. If all the text has one type, use `--mode procedural`, `--mode descriptive`, or `--mode specification`.
3. To check text that is not in a file, send the text to the standard input of the script.
4. Correct each error and each warning.
5. Examine each word in the list of words to examine. If a word is not a technical name or a technical verb, replace the word.
6. Do the check again. Stop when the script shows no errors.

The script also reads the technical names in the file `ste-terms.md` of the current folder. The template for this file is `assets/ste-terms-template.md`.

If you cannot run a script, do these checks manually:

- Find semicolons, contractions, and "-ing" words. Correct them.
- Find "has", "have", and "had" before a past participle. Use the simple past tense.
- Find "should", "would", "may", "might", and "shall". Replace them or remove them.
- Find the passive voice. Make the agent the subject, or use the imperative.
- Count the words in the long sentences. Divide each sentence that has too many words.
- Find phrasal verbs, jargon, and vague words. Use the file `references/substitutions.md`.

The script cannot find all errors. It cannot tell if a word has its correct meaning.
Read the text again after the script shows no errors.

## Files in this skill

Read a file only when it is necessary:

- `references/writing-rules.md`: all the rules with examples. Read it before you rewrite a long document, or when a rule is not clear.
- `references/core-vocabulary.md`: the core words, their parts of speech, and the words with a narrow meaning.
- `references/technical-verbs.md`: the technical verbs for IT, data, and AI.
- `references/substitutions.md`: replacements for words, phrasal verbs, jargon, and former product names.
- `references/document-patterns.md`: patterns for runbooks, incident reports, ADRs, data contracts, model cards, prompts, and agent instructions.
- `assets/ste-terms-template.md`: a template for the technical names of a project.

The technical names are in `references/terms/`. Read only the file that applies to the text:

- `references/terms/it-and-software.md`: general IT, networks, Kubernetes, CI/CD, operations, and security
- `references/terms/cloud-aws.md`: Amazon Web Services
- `references/terms/cloud-google-cloud.md`: Google Cloud
- `references/terms/cloud-azure.md`: Microsoft Azure and Microsoft Fabric
- `references/terms/snowflake.md`: Snowflake
- `references/terms/redshift.md`: Amazon Redshift
- `references/terms/opensearch.md`: OpenSearch and Amazon OpenSearch Service
- `references/terms/vector-databases.md`: vector databases and vector search
- `references/terms/data-engineering.md`: pipelines, Apache Spark, Apache Kafka, dbt, and table formats
- `references/terms/data-architecture.md`: data modeling, governance, and distributed systems
- `references/terms/machine-learning.md`: machine learning and MLOps
- `references/terms/generative-ai.md`: LLMs, RAG, fine-tuning, and evaluation
- `references/terms/agentic-ai.md`: agents, tools, MCP, memory, and human oversight

The examples are in `references/examples/`. Each file shows text before and after the change to STE:

- `references/examples/it-operations.md`
- `references/examples/cloud-aws.md`
- `references/examples/cloud-google-cloud.md`
- `references/examples/cloud-azure.md`
- `references/examples/snowflake.md`
- `references/examples/redshift.md`
- `references/examples/opensearch.md`
- `references/examples/vector-databases.md`
- `references/examples/data-engineering.md`
- `references/examples/data-architecture.md`
- `references/examples/machine-learning.md`
- `references/examples/generative-ai.md`
- `references/examples/agentic-ai.md`

## About this skill

This skill uses the principles of the ASD-STE100 specification.
It is not an official ASD document, and ASD did not approve it.
The vocabulary of this skill is our own selection. It is not the official STE dictionary.
If your project must obey ASD-STE100, use the official specification. You can get it from ASD at no cost.
