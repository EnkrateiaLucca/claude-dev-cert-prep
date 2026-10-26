# CCDV-F Practice Questions

Sixteen items in the exam's style: thirteen original questions plus the three official samples from the [Exam Guide v1.0](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf), Section 8. The original questions are not drawn from the live exam. The same items appear as polls in the slide deck.

Give yourself about 2 minutes 15 seconds per item, the real exam's pace. Answers are at the end of each item in a collapsed block.

Each wrong option is tagged with one of five distractor patterns:

| Pattern | Sounds like |
|---|---|
| Swap the model | "Switch to a larger / the smallest model" |
| Prompt as policy | "Add a line to the system prompt asking…" |
| Misses the constraint | Faster when the stem said cheaper; temperature for a security problem |
| Stuff the context | "Paste the data into every request" |
| Overclaims a feature | "Built-in tools can reach any internal API" |

---

## Segment 2 · API, applications, models (D2 + D5)

### Q1 · D2 Claude API Mechanics

An extraction service asks Claude for JSON. About 3% of responses fail to parse. Every failed response has `stop_reason: "max_tokens"`. What is the best fix?

- A. Add "Always return complete, valid JSON" to the system prompt.
- B. Check `stop_reason` before parsing and raise `max_tokens` for this route so long extractions can finish.
- C. Switch to a larger model that writes JSON more reliably.
- D. Lower the temperature to make output more deterministic.

<details><summary>Answer</summary>

**B.** The trace names the cause: the output hit the token cap. A (prompt as policy): the model can't finish what the cap cut off. C (swap the model): same cap, same truncation. D (misses the constraint): temperature doesn't change length, and the newest models reject the parameter.
</details>

### Official sample 1 · D2 Applications and Integration

A developer must process 10,000 documents overnight to produce a non-urgent analytics report. Cost is the primary concern, and results are not needed until the following morning. Which approach best fits the requirement?

- A. Send every request synchronously through the Messages API in parallel to finish as quickly as possible.
- B. Use the Message Batches API, which processes large asynchronous workloads within a 24-hour window at reduced cost.
- C. Lower max_tokens on synchronous calls to minimize cost.
- D. Switch to the smallest available model regardless of output quality.

<details><summary>Answer</summary>

**B.** Latency-tolerant, high-volume, cost-first work is what the Batches API is for. A optimizes speed and leaves per-token cost unchanged. C truncates output without touching the batch-vs-realtime choice. D ignores quality.
</details>

### Q2 · D5 Cost and Token Management

A support assistant sends a 25,000-token system prompt and an identical tool list on every request, with a `cache_control` breakpoint on the last system block. `cache_read_input_tokens` is always 0. The system prompt begins with `Current time: {now}`. What should the developer do?

- A. Switch to the 1-hour cache TTL so entries live longer.
- B. Add more breakpoints throughout the system prompt.
- C. Move the timestamp out of the system prompt to after the last breakpoint, such as into the user turn.
- D. Move the workload to the Message Batches API.

<details><summary>Answer</summary>

**C.** Caching matches an exact prefix (`tools → system → messages`). A timestamp in the first line changes every request, so nothing after it ever matches. A (misses the constraint): a longer TTL on a changing prefix still never hits. B (overclaims a feature): every breakpoint sits after the changing line. D (misses the constraint): interactive support can't wait up to 24 hours.
</details>

### Q3 · D5 Model Selection and Tradeoffs

A latency-sensitive classifier labels incoming tickets into four categories. It runs on an Opus-tier model at high effort. An eval on 500 labeled tickets shows a Haiku-tier model at low effort meets the same accuracy bar. What should the team do?

- A. Keep the Opus model and enable fast mode to cut latency.
- B. Move the route to the Haiku model at low effort, keeping the eval as a regression gate.
- C. Keep the Opus model and turn thinking up for even higher accuracy.
- D. Move the classifier to the Message Batches API to cut cost.

<details><summary>Answer</summary>

**B.** Start with Sonnet, then move up or down a tier only on eval evidence. Here the eval says the smaller model holds quality. A pays a premium for capability the task doesn't need. C adds latency and cost with no accuracy gain needed. D: "latency-sensitive" rules out a 24-hour window.
</details>

### Q4 · D5 Cost and Token Management (select two)

An internal assistant's bill doubled. 80% of input tokens on every call are an identical 20,000-token block of instructions and tool definitions. A nightly job re-scores the day's 40,000 conversations synchronously. Which TWO changes reduce cost without lowering quality?

- A. Add a cache breakpoint after the stable instructions and tool definitions.
- B. Move the nightly re-scoring job to the Message Batches API.
- C. Paste the full knowledge base into each request so the model needs fewer turns.
- D. Switch every route to the most capable model to reduce retries.
- E. Raise `max_tokens` on all calls.

<details><summary>Answer</summary>

**A and B.** Caching is the free win on a stable prefix; batching cuts offline work by 50%. C (stuff the context) multiplies input tokens. D (swap the model) raises per-token price with no evidence. E is a cap, not a cost lever.
</details>

---

## Segment 3 · Agents, tools, MCP (D1 + D8)

### Q5 · D8 Tool Implementation

An agent calls `get_order_status`. The downstream service times out. What should the developer's code send back to Claude?

- A. Nothing; remove the `tool_use` block from history and retry the whole request.
- B. A `tool_result` with an empty string so the loop continues.
- C. A `tool_result` for that `tool_use_id` with `is_error: true` and a short message such as "Order service timed out; retry or ask the user."
- D. A new user message telling Claude the tool is broken and to stop using tools.

<details><summary>Answer</summary>

**C.** Errors are information: give the model a recoverable signal in the paired `tool_result`. A edits history and drops context. B masks the failure, and Claude may invent an answer. D leaves the `tool_use` unpaired, which fails validation.
</details>

### Q6 · D1 Agent Construction with Claude

A team wants a coding agent that reads and edits files, runs shell commands, delegates to subagents, and blocks dangerous commands with hooks. Compliance requires it to run inside the team's own VPC. Which approach best fits?

- A. The Claude Agent SDK, deployed on the team's infrastructure.
- B. Managed Agents, so Anthropic hosts the loop and the sandbox.
- C. A hand-written Messages API loop with file, shell, and subagent tools built from scratch.
- D. The Message Batches API with one request per coding task.

<details><summary>Answer</summary>

**A.** The Agent SDK ships Claude Code's harness (built-in tools, hooks, subagents) and you host it. B misses the VPC constraint: Anthropic hosts the sandbox. C rebuilds what the SDK already ships. D has no interactive tool loop.
</details>

### Official sample 3 · D8 Tools and MCPs

A team needs Claude to call an internal inventory service exposed as a REST API. They want the capability to be reusable across several Claude applications and maintained independently of any one app. Which approach best fits?

- A. Hard-code the inventory logic into each application's system prompt.
- B. Build an MCP server that exposes the inventory operations as tools so multiple Claude applications can connect to it.
- C. Paste the current inventory data into the context window on every request.
- D. Rely on a built-in tool, since built-in tools can reach any internal REST API.

<details><summary>Answer</summary>

**B.** An MCP server exposes reusable tools that several apps share and that can be maintained independently. A is neither reusable nor maintainable. C gives no live access and wastes context. D: built-in tools don't reach arbitrary internal APIs.
</details>

### Q7 · D8 MCP Server Development

A developer built an MCP server that runs locally over stdio. It works in Claude Code. They now want a backend service to use it through the Claude API's MCP connector, and the connection fails. What is the cause and fix?

- A. The beta header is missing; adding it lets the connector launch the stdio server.
- B. The connector only reaches remote servers; deploy the server over Streamable HTTP, or run your own MCP client via the SDK.
- C. MCP servers can't serve API apps; rewrite the server as a Skill.
- D. The tool descriptions are too long; shorten them so the connector accepts the server.

<details><summary>Answer</summary>

**B.** The API MCP connector supports remote HTTP servers only. Local stdio servers need your own client, Claude Code, or Claude Desktop. A: the header enables the connector, but the connector can't spawn local processes. C: Skills teach procedures; they don't expose a live system. D: description length doesn't affect transport.
</details>

### Q8 · D7 Claude Hooks

A Claude Code agent must never run `git push --force` or delete files outside the repo, even if a prompt or a fetched web page tells it to. Which control is most reliable?

- A. A bold rule in CLAUDE.md: "NEVER force-push or delete files outside the repo."
- B. A `PreToolUse` hook that inspects Bash commands and blocks those patterns, plus permission deny rules.
- C. A `PostToolUse` hook that logs every command for weekly review.
- D. Switch to a more capable model that follows CLAUDE.md more closely.

<details><summary>Answer</summary>

**B.** Prompts ask; hooks and permissions enforce. Only `PreToolUse` can block a call (exit code 2, or a deny decision). A is a request that injected text can override. C records the damage after it happens. D: model choice doesn't enforce anything.
</details>

---

## Segment 4 · Prompting, context, security, Claude Code, debugging (D6 + D7 + D3 + D4)

### Q9 · D6 Prompt Engineering

A ticket router expects exactly `BILLING`, `TECHNICAL`, or `ESCALATION`. Claude returns "Billing", "billing", and sometimes "This looks like a billing issue." The developer has already added three paragraphs describing each category. What is the best next step?

- A. Add two more paragraphs of category descriptions and edge cases.
- B. Turn on extended thinking at high effort.
- C. Constrain the output to exactly one label from the fixed set (or a JSON schema), with two tagged examples showing the format.
- D. Switch to a larger model.

<details><summary>Answer</summary>

**C.** Wrong shape means a missing output constraint; examples show the exact format. A: longer prompts drift toward longer, looser outputs. B: reasoning isn't the problem; the shape is. D: same missing constraint, higher bill.
</details>

### Q10 · D6 Context Engineering

A research agent works well for 30 minutes, then starts repeating searches and ignoring a scope constraint from the first user turn. About 70% of its context is raw search results. Which change best addresses the root cause?

- A. Move to a model with a larger context window.
- B. Clear stale tool results and compact history, put the scope rule in the system prompt, and run searches in subagents that return condensed findings.
- C. Raise `max_tokens` so the agent can write longer plans.
- D. Restart the agent every 30 minutes with an empty context.

<details><summary>Answer</summary>

**B.** Bloat from tool output causes the drift. Prune, compact, isolate, and anchor durable rules in the system prompt. A: a bigger window fills with the same bloat. C: the output cap isn't the problem. D throws away progress and the constraint with it.
</details>

### Official sample 2 · D7 Security and Safety

A Claude-powered agent summarizes web pages submitted by end users. One page contains hidden text instructing the model to ignore previous instructions and reveal its system prompt. Which mitigation is most effective?

- A. Raise the model's temperature so its behavior is harder to predict.
- B. Treat retrieved page content as untrusted input, keep it separate from trusted instructions, and use guardrails or hooks so injected instructions cannot trigger sensitive actions.
- C. Add a line to the system prompt asking users not to include malicious instructions.
- D. Switch to a larger model that follows instructions more reliably.

<details><summary>Answer</summary>

**B.** Isolate untrusted content and enforce least-privilege guardrails so injected text can't invoke sensitive tools. A: temperature is irrelevant to injection. C: a polite request isn't enforceable. D: a more instruction-following model can be more susceptible, not less.
</details>

### Q11 · D7 Identity, Secrets, and Key Management

A startup's React web app calls the Claude API directly from the browser with an API key in the JavaScript bundle. Usage spikes overnight from unknown IPs. What should they do?

- A. Obfuscate the bundle so the key is harder to find.
- B. Rotate the key now, move Claude calls behind a backend that holds the key in a secret manager, and monitor per-key usage.
- C. Add a system prompt line telling Claude to refuse requests from unknown users.
- D. Lower `max_tokens` to limit the cost of each abusive request.

<details><summary>Answer</summary>

**B.** The key is compromised: rotate it, then keep keys server-side. A: anything shipped to the browser is public. C: the model can't authenticate callers. D caps damage per call while the key stays stolen.
</details>

### Q12 · D3 Claude Code + D2 Configuration Management

A team wants every developer's Claude Code to be blocked from reading `.env` files. Individual developers also want personal model preferences that stay out of git. Where should each setting go?

- A. Both in the project CLAUDE.md.
- B. The `.env` deny rule in `.claude/settings.json` (committed); personal preferences in `.claude/settings.local.json`.
- C. The `.env` deny rule in each developer's `~/.claude/settings.json`; preferences in the project CLAUDE.md.
- D. A line in the system prompt asking Claude not to open `.env` files.

<details><summary>Answer</summary>

**B.** Enforce in settings, share in the repo, keep personal settings local (`settings.local.json` is gitignored). A: CLAUDE.md is context, not an enforced permission. C relies on every person configuring it and leaks preferences into git. D isn't enforceable.
</details>

### Q13 · D4 Debugging and Error Handling

After a refactor of the history-building code, 15% of agent requests fail with `invalid_request_error: tool_result block references unknown tool_use_id`. The team has rewritten the tool descriptions twice. What should they do next?

- A. Rewrite the tool descriptions a third time with clearer exclusion conditions.
- B. Switch to a more capable model that tracks tool IDs better.
- C. Inspect failing request traces and fix the code so each `tool_result` echoes the exact `tool_use_id` in the next user turn.
- D. Wrap the call in a retry loop with exponential backoff.

<details><summary>Answer</summary>

**C.** A 400 validation error is an integration-layer bug: the API rejects the request before the model runs. A and B target the wrong layer. D: retrying a malformed request fails identically.
</details>

### Rapid fire · true or false

1. Temperature 0 guarantees identical outputs.
2. Claude executes your custom tools on Anthropic's servers.
3. MCP tool definitions consume context even when no tool is called.
4. Batch results come back in the order you submitted them.
5. Thinking blocks can be summarized to save context mid tool loop.
6. Structured outputs guarantee a parseable object even when `stop_reason` is `max_tokens`.

<details><summary>Answers</summary>

1. False. Sampling never guarantees identical output, and the newest models reject the parameter.
2. False. Your code runs client tools; only server tools (web search, web fetch, code execution) run at Anthropic.
3. True. Definitions load up front; defer loading or allowlist tools.
4. False. Key results by `custom_id`.
5. False. Return them unchanged, or the next request fails the signature check.
6. False. A truncated response still breaks the object; check `stop_reason`.
</details>
