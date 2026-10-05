# Document patterns

This file gives a pattern for each frequent type of document in IT, data, and AI.
Each pattern gives the sections, the rules that apply, and a short example.
Use the pattern as a start. Your team can add sections.

## Runbook

A runbook tells the on-call engineer how to correct one problem.

Sections:

1. Title: the problem as a noun phrase. Example: "Consumer lag on the `orders` topic".
2. Symptoms: the alert, the dashboard, or the error message that the reader sees.
3. Effect: the effect of the problem on systems and on users.
4. Before you start: the access, the tools, and the permissions that the reader must have.
5. Procedure: a numbered list of steps, with one instruction in each step.
6. Escalation: the team and the channel to contact if the procedure does not correct the problem.
7. Rollback: the steps that revert each change.

Rules: P1 to P7, A1 to A4, and T5.
Put each command in a code block after its step. Then give the expected result.
Write each decision as a condition: "If the lag is more than 10,000 messages, go to step 6."

## Incident report

An incident report gives the facts of an incident and the actions that prevent it again.

Sections:

1. Summary: what occurred, the effect, and the duration. Use three to five sentences.
2. Timeline: one row for each event, with the time in UTC.
3. Root cause: the technical cause, in short sentences.
4. Contributing factors: a list.
5. Detection: how the team found the incident.
6. Resolution: the actions that stopped the incident.
7. Action items: one row for each action, with an owner and a date.

Rules: D1 to D4, M6, and V5.
Use the simple past tense for the events. Name the system or the team that did each action.
Give the facts of the system and of the process. Do not write the name of a person as the cause.

## Alert text

An alert tells the on-call engineer the problem and the first action.

Pattern: the condition, the value, the limit, and the first action.

Example: "The consumer lag on the `orders` topic is 25,000 messages. The limit is 10,000. Open the runbook for consumer lag."

Rules: P1, M6, and T7. Write maximum three sentences. Put a link to the runbook in the alert.

## Error message

An error message tells the user what failed and what to do.

Pattern:

1. What failed.
2. The cause of the failure, if you know it.
3. What the user can do.

Example: "The upload failed. The file is larger than 5 GB. Divide the file into parts and upload each part."

Rules: P1 and P3. Do not write that the user caused the error. Do not show the stack trace to the user. Write the trace to the log.

## Change request

A change request tells the reviewers what will change, the risk, and how to revert the change.

Sections:

- The change and the reason for the change.
- The systems that the change applies to.
- The risk and the test.
- The steps and the rollback steps.
- The time window in UTC.

Rules: P1 to P7 for the steps, and A1 to A4 for the risk.

## Architecture decision record (ADR)

An ADR records one architecture decision and the reasons for it.

Sections:

1. Title: the decision as a short statement. Example: "Use Apache Iceberg for the lakehouse tables".
2. Status: "Proposed", "Accepted", "Superseded", or "Deprecated".
3. Context: the problem, the requirements, and the constraints.
4. Decision: one or two sentences. Use "we will". Example: "We will use Apache Iceberg for all the tables in the lakehouse."
5. Consequences: the results of the decision, as a list. Give the good results and the bad results.
6. Alternatives: each alternative and the reason that we did not select it.

Rules: the basic level of STE. Obey the rules for verbs, sentences, and words. Keep each reason and each trade-off.
Give one reason in each sentence. Use "because" to connect a decision to its reason.

## Data contract

A data contract gives the requirements for a dataset between a producer and its consumers.

Sections:

1. Dataset: the name, the owner, and the purpose.
2. Schema: a table with one row for each column. Give the name, the data type, a description, and if the column can be null.
3. Grain: one sentence. Example: "The table has one row for each order line."
4. Requirements: one requirement in each row, with an ID.
5. Quality checks: the checks and their limits.
6. Change policy: how the producer tells the consumers that a change will occur.

Rules: R1 to R4 and M6.
Example requirement: "DC-01: The producer MUST deliver the data for each day before 06:00 UTC."

## Model card

A model card tells the reader what a model does, how the team measured it, and its limits.

Sections:

1. Model: the name, the full model ID, the version, the owner, and the date.
2. Intended use: the tasks and the users for the model.
3. Out-of-scope use: the tasks that the model must not do.
4. Training data: the source, the time range, and the size.
5. Evaluation: the test set, the metrics, the values, and the date of the test.
6. Limitations: the known errors and the conditions that cause them.
7. Risks and controls: each risk and the control that decreases it.

Rules: M1 to M3 and M6. Give measured values. Do not write "always" or "never" for model output.

## Pipeline document

A pipeline document tells the reader what a data pipeline does and how to operate it.

Sections: the source, the target, the schedule, the grain, the keys, the freshness target, the owner, the quality checks, and the runbooks.

Rules: D1 to D4 and M6. Use a table for the schedule, the targets, and the limits.

## Prompt and system prompt

A prompt tells a model what to do. Write it as a procedure. Clear instructions give better output from a model. They also help the persons who update the prompt.

Pattern:

1. The role and the task, in one or two sentences.
2. The input that the model receives.
3. The steps, as a numbered list.
4. The rules, as a list. Write one rule in each item.
5. The output format, with an example.

Rules: M4, P2, P3, and P4.
Example rule: "If the document does not contain the answer, write: The documents do not contain this information."

## Agent instructions

Agent instructions tell an agent how to work in a project. Examples: `AGENTS.md`, `CLAUDE.md`, a steering file, or the text of a `SKILL.md` file.

Pattern:

1. The purpose of the project, in two or three sentences.
2. The commands to build, test, and check the code. Put each command in a code block.
3. The rules, as a list. Write one rule in each item. Give the reason for a rule that is not clear.
4. The actions that the agent must not do without approval.

Rules: M4, M5, P2, P3, and V4.

## Tool description

A tool description tells a model when to call a tool and what the tool returns.

Pattern:

1. What the tool does and what it returns. Use one sentence.
2. When to use the tool.
3. When not to use the tool.
4. Each input parameter: the name, the type, the unit, and the permitted values.

Example: "Returns the status of one order. Use this tool when the user gives an order ID. Do not use it to search for orders."

Rules: M1, M4, and T5.
