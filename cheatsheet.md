# CCDV-F Cheat Sheet

## The exam

53 items · 120 min (~2 min 15 s each) · multiple choice + multiple response · pass 720 / 1,000 scaled · $125 · Pearson VUE online or test center · valid 12 months · registration needs a Claude Partner Network email.

| Domain | Weight |
|---|---|
| D2 Applications and Integration | 33.1% |
| D5 Model Selection and Optimization | 16.8% |
| D1 Agents and Workflows | 14.7% |
| D6 Prompt and Context Engineering | 11.0% |
| D8 Tools and MCPs | 10.6% |
| D7 Security and Safety | 8.1% |
| D3 Claude Code | 3.1% |
| D4 Eval, Testing, and Debugging | 2.6% |

**Reading an item:** read the last line first, underline the deciding constraint, then strike options that match a distractor pattern: swap the model · prompt as policy · misses the constraint · stuff the context · overclaims a feature.

## API mechanics (D2)

| stop_reason | Your code |
|---|---|
| `end_turn` | Use the answer |
| `tool_use` | Run the tool, return `tool_result`, loop |
| `max_tokens` | Truncated: don't parse; raise the cap or continue |
| `stop_sequence` | Expected cut |
| `pause_turn` | Send back unchanged to continue |
| `refusal` | HTTP 200, no content; handle, don't retry |
| `model_context_window_exceeded` | Trim or compact history |

| Request shape | When |
|---|---|
| Synchronous | Short calls, backend jobs |
| Streaming (SSE) | A user is watching; long outputs; avoids HTTP timeouts |
| Async client | Concurrency without blocking |
| Message Batches | Bulk, offline: 50% off, up to 24 h, up to 100,000 requests, results keyed by `custom_id` |

**Streaming:** act only on complete blocks; tool input arrives as partial JSON; `stop_reason` and usage arrive in `message_delta`; discard partial turns on a dropped stream.

**Structured output:** `output_config.format` (JSON schema) for responses; `strict: true` for tool inputs; still check `stop_reason`; prefill returns 400 on current models.

## Cost and models (D5)

**Caching:** exact prefix, order `tools → system → messages` · `cache_control: {type: "ephemeral"}` · max 4 breakpoints · TTL 5 min (default) or 1 h · write 1.25× / 2×, read ~0.1× · model-dependent minimum length · verify with `cache_read_input_tokens` · timestamps or IDs in the prefix kill the hit rate.

**Cost levers, cheapest first:** cache → batch → trim input → effort → model tier → track cost per completed task.

**Models:** start on Sonnet; move to Opus or Fable only when an eval shows a miss; move to Haiku only when an eval shows quality holds. Pin exact model IDs in production; rerun evals before you move.

**Reasoning:** adaptive thinking + `effort` (low → max) per request. `budget_tokens` is deprecated (400 on newest models). Thinking bills as output. Sampling parameters are rejected on the newest models; temperature 0 never guaranteed identical output anyway.

## Agents and tools (D1 + D8)

- Workflow if you can draw the flowchart. Agent only when the task is complex, valuable, viable, and errors are recoverable.
- Claude asks; your code runs the tool. Pair every `tool_use` with a `tool_result` in the next user turn; all parallel results in one message; failures as `is_error: true`.
- Thinking blocks go back unchanged.
- Tool descriptions: what, when to use, when not to use, what it returns. Overlapping tools get exclusion conditions or merge into one tool with a type parameter.
- Manual loop · Tool Runner · Claude Agent SDK (harness, you host) · Managed Agents (Anthropic hosts loop + sandbox).
- Built-in tool (already shipped) · custom tool (one app, one action) · Skill (packaged procedure) · MCP server (reusable connection across apps).
- MCP: tools, resources, prompts · stdio (local) or Streamable HTTP (remote) · the API connector reaches remote servers only · tool definitions cost context.

## Prompting, context, security (D6 + D7)

| Symptom | Missing piece |
|---|---|
| Wrong shape | Output constraint / structured outputs |
| Scope drift | Specific system prompt |
| Invented structure | Few-shot examples in tags |
| Breaks on a variant | Constraint or example for the variant |

**Context levers:** prune tool output · compaction · subagents · external memory · clear history between tasks · attach only the MCP servers you use.

**Security:** untrusted input is data, never instructions · least privilege first · layer guardrails (input screening, output validation, tool permissions, hooks, human approval) · keys in a secret manager behind a backend, separate per environment, rotated on exposure.

## Claude Code and debugging (D3 + D4)

- CLAUDE.md = always-on context. Settings = enforcement: managed → user → `.claude/settings.json` (shared) → `.claude/settings.local.json` (personal). Deny beats allow.
- Hooks: `PreToolUse` blocks (exit code 2); `PostToolUse` audits.
- Modes: default · acceptEdits · plan · auto · dontAsk · bypassPermissions (isolated containers only). Headless: `claude -p --output-format json`.
- Errors: 400 fix the request · 401/403 fix auth · 429 back off and honor `retry-after` · 500/529 retry with backoff. Read the trace before touching the prompt.
