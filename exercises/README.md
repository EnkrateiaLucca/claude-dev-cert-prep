# Hands-on exercises

The exam guide asks every candidate to "build and operate at least one Claude application that exercises the API, integrates one or more tools, applies basic prompt and context engineering, and includes simple security and evaluation practices." These four exercises cover that build in small steps. Each one starts from an official Anthropic notebook or repo, so you write the exam-relevant part yourself and skip the boilerplate.

You need an API key from [platform.claude.com](https://platform.claude.com) and the SDK (`pip install anthropic` or `npm install @anthropic-ai/sdk`). Use a current model ID such as `claude-sonnet-5-5`. Some older notebooks still use forced `tool_choice`, assistant prefill, or `budget_tokens`; current models return a 400 for all three.

## 01 · Stop reasons and streaming (D2 API Mechanics)

1. Build a multi-turn CLI chat that resends the full history every call.
2. Branch on every `stop_reason`: `end_turn`, `tool_use`, `max_tokens`, `stop_sequence`, `pause_turn`, `refusal`, `model_context_window_exceeded`. Treat `max_tokens` as truncated and `refusal` (HTTP 200) as no content.
3. Switch the call to streaming. Read `stop_reason` and `usage` from the `message_delta` event. Kill the connection mid-stream and make sure nothing partial lands in your history.

Start from: [`anthropics/courses` API fundamentals](https://github.com/anthropics/courses/tree/master/anthropic_api_fundamentals) (archived; swap in a current model ID).

**Check yourself:** what does your app do when an input is already larger than the context window?

## 02 · Prompt caching and Message Batches (D2 + D5 Cost)

1. Put a large, stable system prompt behind a `cache_control` breakpoint. Log `cache_creation_input_tokens` and `cache_read_input_tokens` on two calls in a row.
2. Add `Current time: {now}` to the top of the system prompt and watch the hit rate drop to zero. Move it after the breakpoint and watch it come back.
3. Submit 100 classification requests as one batch, each with a `custom_id`. Poll until `processing_status` is `ended`, then join results by `custom_id`.

Start from: [`claude-cookbooks/misc/prompt_caching.ipynb`](https://github.com/anthropics/claude-cookbooks/blob/main/misc/prompt_caching.ipynb) and [`misc/batch_processing.ipynb`](https://github.com/anthropics/claude-cookbooks/blob/main/misc/batch_processing.ipynb).

**Check yourself:** at what request count does the 5-minute cache pay for its 1.25× write?

## 03 · Tool-use loop with a guard (D1 + D8 + D7)

1. Write the loop that runs while `stop_reason == "tool_use"`. Keep every assistant content block in history.
2. Return all parallel tool results in one user message. Return a failed tool call as a `tool_result` with `is_error: true`.
3. Give one tool a dangerous side effect (a fake `delete_file`). Gate it behind a human approval step in your loop, then rebuild the same guard as a `PreToolUse` hook in the Claude Agent SDK.

Start from: [`claude-quickstarts/agents`](https://github.com/anthropics/claude-quickstarts/tree/main/agents) (a loop under 300 lines) and [`claude-agent-sdk-python/examples/hooks.py`](https://github.com/anthropics/claude-agent-sdk-python/tree/main/examples).

**Check yourself:** why does a system-prompt rule against deleting files fail where the hook succeeds?

## 04 · One MCP server, two transports (D8)

1. Build a server that exposes one tool, one resource, and one prompt.
2. Run it over stdio from Claude Code (`.mcp.json` at the repo root). Test it with the MCP Inspector.
3. Serve the same server over Streamable HTTP and call it from the Messages API with the MCP connector.

Start from: [`modelcontextprotocol/python-sdk` example servers](https://github.com/modelcontextprotocol/python-sdk/tree/main/examples/servers) and [`anthropics/skills/skills/mcp-builder`](https://github.com/anthropics/skills/tree/main/skills/mcp-builder).

**Check yourself:** when would you ship this capability as a Skill instead of an MCP server?

## More exercises by blueprint skill

| Skill | Exercise | Starting point |
|---|---|---|
| Output Handling (6.3) | Extract JSON with `output_config.format`, validate it, retry with the validation error | `claude-cookbooks/tool_use/extracting_structured_json.ipynb` |
| Agent Architecture (1.1) | Build one task as a prompt chain and as orchestrator-workers; compare cost and failures | `claude-cookbooks/patterns/agents/` |
| Agent Construction (1.2) | Managed agent with a human-approval gate and prompt versioning | `claude-cookbooks/managed_agents/` |
| Agentic Customization (8.3) | One capability built three ways: Skill, custom tool, MCP server | `anthropics/skills/skills/skill-creator` |
| Claude Code (3.1) | Compare strict vs lax `settings.json`, add a Bash-validator hook, run `claude -p` headless | `anthropics/claude-code/examples/` |
| Context Engineering (6.1) | Long agent run with and without compaction and tool-output pruning | `claude-cookbooks/tool_use/automatic-context-compaction.ipynb` |
| Security (7.1, 7.2) | Agent reads a page with hidden instructions; prove a prompt warning fails, then block with a hook | Pair `misc/building_moderation_filter.ipynb` with `managed_agents/CMA_gate_human_in_the_loop.ipynb` |
| Debugging (4.1) | Code-graded and model-graded eval for one prompt; trace a failing run to its layer | `claude-cookbooks/misc/building_evals.ipynb`, `observability/` |
