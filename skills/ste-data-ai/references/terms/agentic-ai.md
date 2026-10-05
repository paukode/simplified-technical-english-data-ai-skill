# Technical names: agentic AI

These are technical names for AI agents, tools, agent protocols, memory, human oversight, and agent platforms.
Use them as nouns, or as modifiers before a noun.
Do not use a technical name as a verb (rule W6).
Use the official spelling and case. Write tool names, file names, and settings as inline code.
A name in parentheses is the short name or the acronym. Write the full name at the first use (rule W7).
This list is not complete. Any official name is a technical name (rule W5).
Do not give human qualities to an agent (rule M1).

## Agents and architectures

- actor, assistant, AI assistant, AI agent, agent, autonomous agent, agentic AI, agentic system, agentic workflow, agent workflow, agent architecture, single-agent system, multi-agent system (MAS), orchestrator agent, supervisor agent, worker agent, subagent, specialist agent
- planner agent, executor agent, critic agent, reviewer agent, router agent, conversational agent, background agent, long-running agent, coding agent, browser agent, computer use agent, research agent, customer service agent
- agent runtime, agent harness, agent framework, agent platform, agent SDK, agent run, agent session, agent ID, agent registry, agent marketplace

## Agent loop and control

- loop, agent loop, agentic loop, reasoning loop, tool loop, round, step budget, step limit, iteration limit, maximum iterations, maximum turns, turn limit, time budget, cost budget, stop condition, termination condition, exit condition
- success criteria, objective, subtask, task decomposition, task queue, task status, cancellation, loop detection, loop guard, infinite loop, fallback, handoff, control flow, router, conditional edge
- graph, edge, state graph, workflow graph, deterministic workflow, dynamic workflow, long-running task, background task, parallel execution, sequential execution

## Tools and actions

- tool, tool call, tool use, tool calling, function calling, function call, tool definition, tool schema, tool name, tool description, input schema, tool parameter, tool argument, tool result, tool output, tool error, tool choice, parallel tool calls
- tool registry, tool catalog, toolset, toolkit, built-in tool, custom tool, server tool, client tool, tool server, tool permission, tool allowlist, tool denylist, read-only tool, write tool, destructive action, side effect
- action space, observation, code interpreter, code execution, code execution tool, bash tool, terminal tool, file system tool, text editor tool, web search, web search tool, web fetch, web fetch tool, browser tool, browser automation, computer use, computer use tool
- memory tool, retrieval tool, search tool, calculator tool, API tool, OpenAPI tool, skill, Agent Skills, skill folder, slash command, custom command, hook, pre-tool hook, post-tool hook, lifecycle hook

## Protocols and standards

- Model Context Protocol (MCP), MCP server, MCP client, MCP host, MCP tool, MCP resource, MCP prompt, MCP transport, stdio transport, Streamable HTTP transport, MCP Inspector, MCP registry, remote MCP server, local MCP server
- Agent2Agent protocol, Agent2Agent (A2A), A2A protocol, agent card, Agent Communication Protocol (ACP), AGENTS.md, CLAUDE.md, GEMINI.md, llms.txt, JSON-RPC, JSON-RPC 2.0

## Memory and state

- memory, agent memory, short-term memory, long-term memory, working memory, episodic memory, semantic memory, procedural memory, memory store, memory file, conversation memory, session memory, user memory, shared memory, scratchpad
- agent state, shared state, state persistence, session state, context management, context rot, conversation summary, thread ID, transcript, trajectory, Mem0, Letta, MemGPT

## Planning and reasoning patterns

- planning, plan, task plan, plan-and-execute, plan-and-solve, ReAct, reasoning and acting, tree of thoughts (ToT), reflection, self-reflection, self-critique, self-correction, self-consistency, verifier, evaluator, evaluator-optimizer
- parallelization, orchestrator-workers, MapReduce, Reflexion, decomposition, backtracking, Monte Carlo tree search (MCTS)

## Multi-agent systems

- multi-agent collaboration, multi-agent orchestration, agent team, crew, agent role, delegation, task delegation, agent-to-agent communication, message passing, blackboard architecture, hierarchical agents, supervisor, swarm, agent swarm, voting, group chat

## Human oversight and safety

- human-in-the-loop (HITL), human-on-the-loop, human approval, approval request, approval policy, permission mode, permission prompt, plan mode, read-only mode, least agency, excessive agency, policy engine
- sandboxing, network isolation, file system isolation, egress control, scoped token, short-lived credential, kill switch, emergency stop, spending limit
- tool poisoning, tool shadowing, confused deputy problem, unsafe action, irreversible action, destructive command, blast radius, dry run

## Evaluation and observability

- agent evaluation, agent eval, task success rate, task completion rate, success rate, pass rate, tool call accuracy, tool selection accuracy, trajectory evaluation, cost per task, end-to-end evaluation, simulated user, user simulator
- SWE-bench Verified, Terminal-Bench, tau-bench, GAIA, WebArena, OSWorld, AgentBench, agent trace, GenAI semantic conventions, AgentOps, W&B Weave, Helicone, session replay

## Agent frameworks and platforms

- LangGraph, LangGraph Platform, CrewAI, AutoGen, AG2, LlamaIndex Workflows, smolagents, OpenAI Agents SDK, OpenAI Assistants API, AgentKit, Agent Development Kit (ADK), Strands Agents, Agentforce, Salesforce Agentforce
- n8n, Zapier, Dify, Flowise, Langflow, Mastra

## Coding agents and developer tools

- AI coding assistant, AI pair programmer, Codex, OpenAI Codex, Codex CLI, GitHub Copilot coding agent, Copilot agent mode, Devin, Kiro CLI, Gemini CLI, Jules, Aider, Cline, Roo Code, Continue, OpenCode, Amp, Droid, Goose, Warp, Zed, Kilo Code, Replit Agent, Lovable, Bolt.new, v0
- spec-driven development, steering file, Kiro steering, Kiro spec, Kiro hook, Kiro powers, headless mode, non-interactive mode, allowed tools, disallowed tools, custom agent, agent profile, prompt file, instructions file, rules file

## Agent instructions and configuration

- agent instructions, system instructions, custom instructions, project instructions, user instructions, front matter, frontmatter, YAML front matter, progressive disclosure, invocation, implicit invocation, explicit invocation, skill description, definition of done
