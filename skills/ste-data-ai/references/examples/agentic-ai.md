# Examples: agentic AI

Each example shows text before and after the change to STE.
The rule IDs refer to `references/writing-rules.md`.

## 1. The agent loop

Type: description

Before:

~~~text
The agent basically thinks about what to do, calls a tool, looks at the result, and keeps going until it figures out it's done or hits the max of 20 steps.
~~~

After:

~~~text
The agent loop has these steps:

1. The model receives the task, the conversation history, and the tool definitions.
2. The model returns a tool call or a response.
3. If the model returns a tool call, the agent runtime runs the tool. Then the runtime adds the tool result to the conversation history and goes back to step 1.
4. If the model returns a response without a tool call, the loop stops.

The loop also stops after 20 tool calls. This step limit prevents a loop that does not stop.
~~~

Changes: no human qualities for the model (M1), the actor of each step (M5), and a specific limit (W13).

## 2. A tool description

Type: description

Before:

~~~text
get_order: This tool lets you look up an order. You can pass it an order ID and it'll give you back all the details about the order, like status, items, shipping info and so on.
~~~

After:

~~~text
`get_order`: Returns the status, the items, and the address of one order. Use this tool when the user gives an order ID. Do not use it to search for orders.

Input: `order_id` (string, mandatory). The ID of the order, for example `ORD-12345`.
~~~

Changes: what the tool returns and when to use it (M4), no phrasal verbs (V7), and no vague words (W13).

## 3. Approval gates for an agent

Type: specification

Before:

~~~text
The agent should ask for confirmation before doing anything destructive like deleting files or running migrations, and it shouldn't be able to push to main at all.
~~~

After:

~~~text
This policy uses the keywords MUST and MUST NOT as RFC 2119 gives them.

- AP-01: The agent MUST get the approval of the user before it deletes a file.
- AP-02: The agent MUST get the approval of the user before it runs a database migration.
- AP-03: The agent MUST NOT push commits to the `main` branch.
- AP-04: The agent harness MUST record each decision of the user in the audit log.
~~~

Changes: one requirement in each item with an ID (R2), the actor as the subject (R4), and no vague words (W13).

## 4. An incident report for an agent

Type: description

Before:

~~~text
The coding agent went rogue and decided to delete the staging database because it thought the tests needed a clean slate. It wasn't supposed to have those permissions anyway.
~~~

After:

~~~text
On 2026-09-22 at 10:14 UTC, the coding agent ran the command `dropdb staging` on the staging database server. The staging database was not available for 2 hours.

The agent selected this command after a test failed with a schema error. The command was not on the denylist. The credentials of the agent had the permission to drop databases.

Actions:

- We added `dropdb` and `DROP DATABASE` to the denylist of the agent.
- We removed the permission to drop databases from the credentials of the agent.
- The agent must get the approval of a person for each command that deletes data.
~~~

Changes: no human qualities for the agent (M1), facts with times in UTC (T7, M6), and the actions as a list (S4).

## 5. Connect an MCP server for GitHub

Type: procedure

Before:

~~~text
To hook up the GitHub MCP server, just drop the config into your settings file and restart the client. Make sure the token only has read access or the agent could accidentally modify repos.
~~~

After:

~~~text
WARNING: Use a token that has read-only access. If the token has write access, the agent can change the repositories.

1. Create a fine-grained personal access token in GitHub with read-only access to the repositories.
2. Add the GitHub MCP server to the configuration file of the MCP client.
3. Put the token in the environment variable `GITHUB_TOKEN`.
4. Restart the MCP client.
5. Make sure that the client shows the tools of the GitHub MCP server.
~~~

Changes: the security risk as a warning (A1, A2), no phrasal verbs (V7), and no jargon (W9).

## 6. Handoff between agents

Type: description

Before:

~~~text
The triage agent figures out what the customer wants and hands off to the billing or tech support agent, who then takes over the conversation.
~~~

After:

~~~text
The router agent reads the first message of the customer. It classifies the message as a billing question or a technical question.

Then the router agent transfers the conversation to the billing agent or to the technical agent. The agent that receives the conversation also receives the summary from the router agent. Then that agent answers the customer.
~~~

Changes: no human qualities for the agent (M1), the actor of each step (M5), and no phrasal verbs (V7).

## 7. Instructions for a coding agent

Type: procedure

Before:

~~~text
Hey! When working in this repo, please try to keep PRs small and always run the tests before committing. Don't touch the migrations folder unless you really have to, and ask before installing new dependencies.
~~~

After:

~~~text
Obey these rules in this repository:

1. Run the tests before each commit:

   ```bash
   make test
   ```

2. Keep each pull request to one change.
3. Do not change the files in `migrations/` without approval from the user.
4. Get the approval of the user before you add a new dependency.
~~~

Changes: the instructions as a procedure (M4), one rule in each item (P2), and no contractions or vague words (S3, W13).
