# Simplified Technical English skill for data and AI

An agent skill that writes, rewrites, and checks technical text in Simplified Technical English (STE).
The skill adapts STE to IT, cloud, data engineering, data architecture, machine learning, generative AI, and agentic AI.
It works in Claude, Codex, Kiro, [Whisper Studio](https://github.com/paukode/whisper-studio), and other agents that read `SKILL.md`.

This README is in STE.

## Install with one command

Copy the line for your agent to your terminal. The command uses `curl`, `tar`, and `python3`, and operates on macOS and on Linux.

Claude Code:

```bash
curl -fsSL https://raw.githubusercontent.com/paukode/simplified-technical-english-data-ai-skill/main/install.sh | sh -s -- claude
```

Codex:

```bash
curl -fsSL https://raw.githubusercontent.com/paukode/simplified-technical-english-data-ai-skill/main/install.sh | sh -s -- codex
```

Kiro:

```bash
curl -fsSL https://raw.githubusercontent.com/paukode/simplified-technical-english-data-ai-skill/main/install.sh | sh -s -- kiro
```

[Whisper Studio](https://github.com/paukode/whisper-studio):

```bash
curl -fsSL https://raw.githubusercontent.com/paukode/simplified-technical-english-data-ai-skill/main/install.sh | sh -s -- whisper
```

All four agents:

```bash
curl -fsSL https://raw.githubusercontent.com/paukode/simplified-technical-english-data-ai-skill/main/install.sh | sh -s -- all
```

The command downloads the skill to a temporary folder. Then it installs the skill and deletes the temporary folder.
Run the same command again to update the skill. To read the script before you run it, open `install.sh`.

## What the skill does

STE is a controlled form of English with a small vocabulary and strict writing rules.
Text in STE is short, clear, and easy to translate.
A reader who does not speak English as a first language can understand it.

Use the skill for these types of text:

- Runbooks, alerts, error messages, change requests, and incident reports.
- Data contracts, API specifications, service level agreements, and security policies.
- Architecture decision records (ADRs), pipeline documents, and schema documents.
- Model cards and evaluation reports.
- Prompts, agent instructions, and tool descriptions.

The skill gives the agent these items:

- 67 writing rules with examples. The rule IDs are W1 to G4.
- A core vocabulary of approximately 500 words, and approximately 200 technical verbs for IT, data, and AI.
- More than 6,000 technical names for 13 fields: IT, AWS, Google Cloud, Azure, Snowflake, Amazon Redshift, OpenSearch, vector databases, data engineering, data architecture, machine learning, generative AI, and agentic AI.
- Replacements for phrasal verbs, jargon, vague words, and former product names.
- Patterns for runbooks, incident reports, ADRs, data contracts, model cards, prompts, and agent instructions.
- 75 examples of text before and after the change to STE.
- A check script that finds the errors that a program can find. The script uses Python 3.8 or a newer version, and no other packages.

## Examples

### A runbook step

Before:

<!-- ste-check off -->

> If you're seeing the high memory alert for the payments API, you should first check the dashboard to figure out whether memory has been growing steadily. If it has, the service probably has a memory leak and you'll want to restart the pods one at a time so we don't take down the whole service.

<!-- ste-check on -->

After:

> CAUTION: Restart only one pod at a time. If you restart all the pods together, the `payments` API stops.
>
> 1. Open the "Payments API" dashboard in Grafana.
> 2. Examine the memory graph for the last 6 hours.
> 3. If the memory increases continuously, go to step 4. If not, go to step 7.
> 4. Restart one pod:
>
>    ```bash
>    kubectl delete pod <pod-name> -n payments
>    ```
>
>    Kubernetes starts a new pod.
> 5. Wait until the status of the new pod is `Running`.
> 6. Do steps 4 and 5 again for each pod.
> 7. Send a message to the `#payments-oncall` channel in Slack.

### An error message

Before:

<!-- ste-check off -->

> Oops! Something went wrong while uploading your file. It might be too big or the server could be having issues. Please try again later.

<!-- ste-check on -->

After:

> The system did not upload the file. The file is larger than the limit of 5 GB. Divide the file into parts. Then upload each part.

The folder `skills/ste-data-ai/references/examples/` has 75 examples for the 13 fields.

## Install from a clone

Use this method to change the skill, or to install the skill on Windows.
Clone the repository. Then run the install script for each agent that you use:

```bash
git clone https://github.com/paukode/simplified-technical-english-data-ai-skill.git
cd simplified-technical-english-data-ai-skill
python3 tools/install.py claude codex kiro whisper
```

| Agent | Target | Folder | How to start the skill |
|---|---|---|---|
| Claude Code | `claude` | `~/.claude/skills/` | Type `/ste-data-ai`, or ask for STE |
| Codex | `codex` | `~/.agents/skills/` | Type `$ste-data-ai`, or ask for STE |
| Kiro IDE and Kiro CLI | `kiro` | `~/.kiro/skills/` | Type `/ste-data-ai`, or ask for STE |
| [Whisper Studio](https://github.com/paukode/whisper-studio) | `whisper` | `~/.whisper/skills/` | Ask for STE |

Use `all` to install the skill for all four agents.
The script makes a copy of the skill. Run the script again after you update the repository.

Options of the install script:

- `--link`: make a symbolic link, not a copy. Then a change in the repository shows immediately in the agent.
- `--project PATH`: install the skill in a project folder, for example `PATH/.claude/skills/`.
- `--uninstall`: remove the skill.
- `--status`: show where the skill is installed.

The script does not remove or replace a folder that is not this skill.

### Other agents

- Claude.ai (web and desktop): make a ZIP file with `python3 tools/build.py zip`. Then upload `dist/ste-data-ai.zip` in the settings for skills.
- An agent that reads `SKILL.md` from a different folder: copy the folder `skills/ste-data-ai/` to the skills folder of the agent. Keep the folder name `ste-data-ai`.
- An agent or a chat tool without skills: make one prompt file. Then put the file in the system prompt or in the custom instructions.

```bash
python3 tools/build.py prompt --fields aws,data-engineering,genai --examples
```

The fields for `--fields` are `it`, `aws`, `gcp`, `azure`, `snowflake`, `redshift`, `opensearch`, `vector`, `data-engineering`, `data-architecture`, `ml`, `genai`, `agentic`, and `all`.

## Use the skill

Ask the agent for STE. Examples:

- "Rewrite this runbook in STE."
- "Write an incident report in Simplified Technical English from these notes."
- "Check this data contract against the STE rules."
- "Write the system prompt for the support assistant in STE."

The skill starts only when you ask for STE, Simplified Technical English, controlled English, or plain technical English.

## Use the check script

You can run the check script without an agent:

```bash
python3 skills/ste-data-ai/scripts/ste_check.py docs/runbook.md
python3 skills/ste-data-ai/scripts/ste_check.py --mode specification contracts/orders.md
cat draft.md | python3 skills/ste-data-ai/scripts/ste_check.py --strict
python3 skills/ste-data-ai/scripts/ste_check.py --format json docs/model-card.md
```

The script shows each error and each warning with its line and its rule ID.
It also gives a list of the words that are not in the vocabulary.
The exit status is 0 when there are no errors. Thus, you can use the script in a CI/CD pipeline.

To stop the check for a part of a file, put the line `<!-- ste-check off -->` before the part. Put the line `<!-- ste-check on -->` after the part.
This README uses these lines for the "Before" text of the examples.

The script cannot find all errors. It cannot tell if a word has its narrow meaning. A person must also read the text.

## Add the names of your project

Copy `skills/ste-data-ai/assets/ste-terms-template.md` to the root folder of your project. Give it the name `ste-terms.md`.
Add the names of your systems, tables, teams, and products, and the technical verbs of your project.
The check script reads `ste-terms.md` from the current folder. You can also give a file with the `--terms` option.

## Files in this repository

```text
skills/ste-data-ai/          the skill (the install scripts copy this folder)
  SKILL.md                   the primary instructions
  agents/openai.yaml         the display name for Codex
  references/                the rules, the vocabulary, the substitutions, and the patterns
  references/terms/          the technical names for each field
  references/examples/       the examples for each field
  scripts/ste_check.py       the check script
  assets/                    the template for the names of a project
install.sh                   installs the skill with one command
tools/install.py             installs the skill for each agent from a clone
tools/build.py               makes the ZIP file and the prompt file
tests/                       the tests
```

## Development

Run the tests:

```bash
python3 -m unittest discover -s tests
```

The tests make sure that `SKILL.md` and each example obey the rules of the skill.
The rules for changes to this repository are in `AGENTS.md`.

## ASD-STE100

This skill uses the principles of the ASD-STE100 specification.
It is not an official ASD document, and ASD did not approve it.
ASD-STE100 is a trademark of ASD.

The vocabulary and the rule IDs are our own. They are not the official STE dictionary or the rule numbers of the specification.
If your project must obey ASD-STE100, use the official specification. You can get it from ASD at no cost.

## License

MIT. Refer to `LICENSE`.
