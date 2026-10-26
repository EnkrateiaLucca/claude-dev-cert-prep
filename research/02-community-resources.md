# Community Resources for the Claude Certified Developer – Foundations Exam (CCDV-F)

## Context

This file records community study material for **Claude Certified Developer – Foundations (CCDV-F)**: GitHub repos, exam-taker write-ups, hands-on exercises built on official Anthropic repos, and recurring distractor patterns. Each repo gets a quality judgment and a link recommendation for the course README. Many CCDV-F repos are AI-generated question dumps, copies of gated material, or banks keyed to API behavior that current docs have changed. This file flags those. Research date: 2026-10-26.

### Source key

| Alias | What it is | URL |
|---|---|---|
| `OG` | Official CCDV-F Exam Guide v1.0, effective July 2026 (8 pages; downloaded and text-extracted) | https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf |
| `BLOG` | Anthropic launch post for the four role-based certifications, 2026-07-23 | https://claude.com/blog/four-role-based-claude-certifications |
| `SKJ` | Anthropic Partner Academy (Skilljar) prep-course index | https://anthropic-partners.skilljar.com/page/claude-certification-exam-prep-courses |
| `VK` | vkorost book repo. Paths like `ch03` refer to `book/chapters/03-*.md` | https://github.com/vkorost/claude-certified-developer-guide |
| `CS` | CertSafari self-reported CCDV-F exam experiences (vendor-hosted) | https://www.certsafari.com/exam-experiences/anthropic/claude-developer-foundations |
| `IND` | Haider Rasool (Indicium AI), dev.to, "A Simple Guide to Passing…", score 941 | https://dev.to/indiciumai/a-simple-guide-to-passing-the-claude-certified-developer-exam-4g3c |
| `JR` | Jenisha Roshan, two Medium posts dated 2026-09-30, score 970. Read through the author's RSS feed because the article pages return HTTP 403. | https://medium.com/feed/@jenisharoshan |
| `BP` | "Blue Panda", dev.to, "I Cleared All 4 Anthropic Claude Certifications" | https://dev.to/bluepanda/i-cleared-all-4-anthropic-claude-certifications-what-you-actually-need-to-know-and-what-to-skip-224m |
| `D-ERR` | Claude API errors docs | https://platform.claude.com/docs/en/api/errors |
| `D-STOP` | Stop reasons docs | https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons |
| `D-CACHE` | Prompt caching docs | https://platform.claude.com/docs/en/build-with-claude/prompt-caching |
| `D-BATCH` | Batch processing docs | https://platform.claude.com/docs/en/build-with-claude/batch-processing |
| `MCP-T` | MCP spec 2025-11-25, transports | https://modelcontextprotocol.io/specification/2025-11-25/basic/transports |

Repo facts (stars, push dates, file trees, file contents) come from the GitHub API on 2026-10-26. The repo URL is the source.

## Findings

### 1. Official baseline used to judge community material

- Exam facts: 53 items, multiple-choice plus multiple-response ("each item states how many responses to select"), 120 minutes, 720 on a 100–1,000 scale, $125, valid 12 months. The score report shows percent-correct by domain. [source: OG §5]
- Blueprint weights: Agents and Workflows 14.7%, Applications and Integration 33.1%, Claude Code 3.1%, Eval/Testing/Debugging 2.6%, Model Selection and Optimization 16.8%, Prompt and Context Engineering 11.0%, Security and Safety 8.1%, Tools and MCPs 10.6%. [source: OG §6]
- The guide gives a weight per skill (25 skills). The largest are Claude Application Design 8.6%, Software Engineering Foundations 7.4%, Claude API Mechanics 6.8%, and Technical Fundamentals 6.1%. Claude Hooks is 1.0%. [source: OG §6]
- The guide lists frameworks by name ("Strands, LangGraph, PydanticAI") and MCP communication patterns as "stdio, sockets, client vs. server". [source: OG §6 Domain 1, Domain 8]
- The guide includes three sample questions (Batches vs sync, prompt injection, MCP server for a shared REST service). It states they are "not drawn from the live item bank". [source: OG §8]
- Exams are open only to members of the Claude Partner Network. Anthropic's prep courses live in the Anthropic Partner Academy. [source: BLOG]
- The official "Claude Certified Developer - Foundations Prep Course" path contains 5 courses. [source: SKJ]
- Candidates accept an NDA that covers "questions, answer options, and scenarios". [source: OG §13]

### 2. GitHub repos

`gh search repos` for "Claude Certified Developer", "CCDV-F", "claude-certified-developer", "claude developer foundations", and "ccdv" returned about 60 CCDV-F repos. Most have 0–1 stars and were created between July and October 2026. [source: GitHub search API, 2026-10-26] The repos below were opened and spot-checked.

#### Recommended

- **[vkorost/claude-certified-developer-guide](https://github.com/vkorost/claude-certified-developer-guide)**. 38★, pushed 2026-09-15. A 23-chapter book (about 75K words, PDF and EPUB) organized by decision. Each chapter ends with a "when the scenario says / answer / trap" table. [source: VK README.md] The author says he passed CCDV-F on 2026-09-14 and links a Credly badge. [source: VK README.md] Every behavioral claim has an endnote with a docs URL. Spot-checks match current docs: all seven `stop_reason` values, `refusal` arriving as HTTP 200, and batch facts (50%, 24 h expiry, 29-day retention, out-of-order results matched by `custom_id`). [source: VK ch03; D-STOP; D-BATCH] The README says Claude Code wrote the book under the author's direction. The book has no practice questions. [source: VK README.md] License: CC BY-NC-SA 4.0. Link to it; do not adapt its text into paid course material. [source: VK README.md "License"] One drift: ch09 keys "force that tool on the first request". Current docs return 400 for forced `tool_choice` on Opus 5.5, Sonnet 5.5, Fable 5.1, and Mythos 5.1. [source: VK ch09; D-ERR "Forced tool use not supported"]
- **[preporato/claude-certification-guide](https://github.com/preporato/claude-certification-guide)**. 178★, pushed 2026-10-13. Contains `ccdv-f/guide.md` (721 lines), 30 practice questions (7 multiple-response) with per-option explanations, a browser-based timed test, and PDF/EPUB downloads. [source: repo README.md; ccdv-f/practice-questions.md] Preporato, which sells six paid practice tests, maintains the repo. [source: repo README.md] The questions are specific and match the docs. One example: a cache prefix below the minimum length shows zeros for both cache token counters and returns no error. [source: ccdv-f/practice-questions.md Q5; D-CACHE] The guide is current on prefill (400 since Claude 4.6) and adaptive thinking. [source: ccdv-f/guide.md; D-ERR] Link it and label it vendor-maintained.
- **[gwythyr/ccdv-practice-exam](https://github.com/gwythyr/ccdv-practice-exam)**. 6★, pushed 2026-08-05. A static quiz app that repackages Matthew Purcell's 53-question PDF. Every item has a rationale and a "why not" for each distractor, and some items are "Select TWO". [source: repo README.md; questions.js] Purcell's disclaimer says the items are original and written against the public guide. [source: repo README.md] Spot-check: item 1.5 says the SDK retries rate-limited requests twice by default via `max_retries`. The docs confirm this. [source: questions.js; D-ERR] One 970 scorer named this question bank as the point where "things really clicked". [source: JR] The README credits Purcell. The repo does not say whether Purcell gave permission to republish his PDF. [unverified] Link it, and credit Purcell's LinkedIn profile next to it.
- **[asampath1/myClaudeLab](https://github.com/asampath1/myClaudeLab)**. 0★, pushed 2026-10-07. The author reports passing with 896. Contains per-domain briefs, worked examples, 20-item MCQ sets with separate answer keys, labs, a 53-item mock, and Claude Code mechanism notes (hooks, MCP, permissions, rules, skills, subagents). The README says it does not include the official guide and that every question is original. [source: repo README.md] Its API notes are current: `budget_tokens` returns 400 on new models, prefill is removed, and `pause_turn`/`refusal` are covered. [source: blueprint-prep/D2A-claude-api-mechanics.md; D-ERR; D-STOP] Link it as one candidate's notes.
- **[CorporateChittyChat/claude-certification-prep](https://github.com/CorporateChittyChat/claude-certification-prep)** + **[chittychat-studio/ccdvf-course](https://github.com/chittychat-studio/ccdvf-course)**. 3★ / 1★. A 12-video CCDV-F YouTube series, a 30-question mock with an HTML player, and runnable Python/TypeScript code for each episode (`ep01-models` … `ep09-failure-checker`, including `ep07-guard-hook`). [source: both repos' README.md and file trees] Questions are labeled original. [source: CorporateChittyChat README.md] Link it as the hands-on and video companion.

#### Optional (link with a caveat)

- **[kuljotSB/Claude-Certified-Developer-CCDV-F](https://github.com/kuljotSB/Claude-Certified-Developer-CCDV-F)**. 21★, 55 forks, pushed 2026-08-16. Lab notebooks: Messages API, batch processing, adaptive thinking, structured outputs (`output_config`), a FastMCP server on Streamable HTTP, Managed Agents, Agent SDK subagents and skills, LangChain, RAG. The code uses current APIs. The README is only a title and a course thumbnail, and the repo has no license. [source: repo file tree; README.md; notebook grep] It suits learners who want a lab path, but it has no explanations.
- **[Amey-Thakur/CLAUDE-CERTIFICATIONS](https://github.com/Amey-Thakur/CLAUDE-CERTIFICATIONS)**. 102★, pushed 2026-10-26. Has `developer-foundations/` (35 practice questions, 3 mocks, notes, cheat sheet), a 110-card flashcard deck for all four exams exported as `flashcards.tsv` for Anki, and a browser practice engine. [source: repo README.md; tree] The questions are generic. Q8 and Q9 closely paraphrase official samples 2 and 3. [source: developer-foundations/practice-questions.md; OG §8] `developer-foundations/exam-guide.pdf` matches the official guide byte for byte (SHA-256 prefix `8c52679323cb5467`). [source: repo file; OG] Every recent commit has the message "Claude Certifications". [source: GitHub commits API] Use it for the flashcards only.
- **[dnacenta/claude-certified-architect `certs/ccdv-f-developer.md`](https://github.com/dnacenta/claude-certified-architect/blob/main/certs/ccdv-f-developer.md)**. 135★. One overview page that maps CCDV-F domains to the repo's CCAR-F domain files and links the official PDF. Its exam facts match `OG`. [source: file content; OG §5–6] Useful for learners crossing over from the Architect exam.
- **[WorkflowtechAI/claude-cert-examprep](https://github.com/WorkflowtechAI/claude-cert-examprep)**. 3★. A Claude Code study-coach skill (diagnostic, drills, timed mocks) for CCAR-F, CCAR-P, and CCDV-F. Its questions are generated on the fly by design. The author links a Credly profile showing all three certs. [source: repo README.md] Use it as a "have Claude quiz you" example. IND reports this method worked (four Claude-generated mocks, score 941). [source: IND]
- **[NiravRVaghasiya/Claude-Developer-Foundations](https://github.com/NiravRVaghasiya/Claude-Developer-Foundations)**. 0★. A Next.js study site with spaced-repetition flashcards and a 53-question simulator weighted by domain. [source: repo README.md] Content accuracy was not checked. [unverified]

#### Do not link

- **[hoangminhq5310/CCDV-F_Dump](https://github.com/hoangminhq5310/CCDV-F_Dump)**. The repo is named "Dump". It holds 97 questions, and all 97 explanations read only "The correct answer is …". [source: CCDV-F_trainer.html, parsed] It has the shape of a brain dump and may contain NDA-covered material. [unverified]
- **[natsh/claude-developer-foundations-prep](https://github.com/natsh/claude-developer-foundations-prep)**. 3★. The README says it holds "Full course materials extracted from the Skilljar prep course (5 modules)". [source: repo README.md] The official prep path is gated behind the Partner Academy. [source: BLOG; SKJ] Linking it would point learners to redistributed Anthropic course content.
- **[Skillsoft-Content/Claude-Certified-Developer-Foundations-CCDE-F-Bootcamp](https://github.com/Skillsoft-Content/Claude-Certified-Developer-Foundations-CCDE-F-Bootcamp)**. 12★. One zip file. It uses the wrong exam code ("CCDE-F"), and its "Bootcamp.pdf" is the official exam guide renamed (same SHA-256). [source: zip listing and hash; OG] Its 200-question bank teaches outdated answers. Q1 keys forced `tool_choice` as the structured-output fix, Q15–16 key `budget_tokens`, and Q5 says the Messages API has no system role inside `messages`. [source: Claude_CCD_Foundations_200Q.md] Current docs reject forced `tool_choice` on Opus/Sonnet 5.5 and replace extended thinking with adaptive thinking on 4.7+. [source: D-ERR] Newer models also accept a mid-conversation `role: "system"` message. [source: VK ch03 endnote 1]
- **[mrKindly/claude-certified-developer](https://github.com/mrKindly/claude-certified-developer)** and **[hedge-hog-23/claude-developer-certificate-resources](https://github.com/hedge-hog-23/claude-developer-certificate-resources)**. A single README with 53 questions, and a notes file plus an MCQ file. [source: repo trees] hedge-hog-23's description calls the exam "associate". [source: repo description] Neither adds anything the recommended repos lack.
- **[paullarionov/claude-certified-architect](https://github.com/paullarionov/claude-certified-architect)**. It has no CCDV-F content. No file path or README line mentions "developer" or "CCDV". [source: repo tree and README grep] Link it only for Architect overlap.

#### Websites mentioned in the sibling research

- **claudecertificationguide.com** (run by AI Cert Guides) has a CCDV-F blueprint article published 2026-07-24 and updated 2026-10-01. Its weights and sub-skill weights match `OG`. The site advertises six mock exams and a free diagnostic. [source: https://claudecertificationguide.com/blog/claude-certified-developer-foundations-exam-guide] IND used it for scope and weights. [source: IND]
- CertSafari sells a CCDV-F practice bank. [source: CS] Search results also list paid CCDV-F banks on Tutorials Dojo, Udemy, and LinkedIn Learning. Those pages were not fetched and their items were not evaluated. [unverified]
- Search results list certempire.com pages titled "Anthropic CCDV-F Real Exam Dumps". Do not link them. The pages were not fetched. [unverified]

### 3. Exam-taker reports

| Report | Score | What they say | Source |
|---|---|---|---|
| Haider Rasool (Indicium AI) | 941 | Finished in about 70 minutes. "The real exam was nowhere near as difficult as the harder mocks." Questions "come down to thinking like a software engineer on the job." "The detail that decides the answer is often in the last line." "If an option is technically possible but nobody would ship it, it's probably a distractor." Prepared mainly with four Claude-generated mocks built from the exam guide. | `IND` |
| Jenisha Roshan | 970 | "CCDV-F is much more scenario-based than I expected." Advises against memorizing syntax from the course exercises. Prepared with the official learning path, Purcell's 53-question bank, and Anas Riad's six-test Claude artifact. Summary: "It's testing whether you can apply good software engineering principles when Claude is part of the system." | `JR` |
| "Blue Panda" (passed all four exams) | not in text | Ranks CCDV-F second-easiest after CCAO-F. Says the Messages API (payloads, streaming events, batches, tool schemas) is about a third of the exam. Says the exam "tests what happens when a tool returns an error code". Scenario-based, no negative marking. | `BP` |
| vkorost | pass (Credly) | "Nearly every wrong answer on this exam is a mechanism that works perfectly well somewhere else." "A third of this exam is not about Claude" (REST, versioning, review). | `VK` README.md |
| asampath1 | 896 | Built per-domain briefs, MCQ sets, and a 53-item mock. | asampath1 README.md |
| CertSafari aggregate (20 entries, Sep–Oct 2026) | 808–985 | Nearly every entry calls the real exam easier than CertSafari's practice. Heavy topics named: MCP, agent architecture, workflow vs agent, model selection, software engineering fundamentals, security, batch vs stream, hooks for validation, reasoning effort, SDK retry defaults. Several report no multi-select items. One reports only "5–10 questions" on parameters or configuration. Others say two options are usually easy to eliminate and warn about wording like "is not", "is best", and "fits better". | `CS` |

- CertSafari hosts these reports on its own sales site. Every listed entry is a pass, which points to selection bias. [source: CS]
- Several CertSafari entries say they saw no multi-select items. The official guide says the exam uses multiple-response items. [source: CS; OG §5] Preporato estimates about a quarter of items are multiple-response. [source: preporato README.md] The real share is unknown and may vary by exam form. [unverified]
- Failed or empty fetches: Medium article pages returned 403. Sridhar's post (https://medium.com/@sridharcloud/ccdv-f-claude-certified-developer-foundations-exam-and-how-i-prepared-for-it-c25dda15ba1a) shows only a teaser in RSS. Reddit blocks this crawler, so no r/ClaudeAI threads could be read. A YouTube "I Passed" video (https://www.youtube.com/watch?v=k5FYbKhfnyY) returned only page chrome. The Anas Riad artifact (https://claude.ai/public/artifacts/83eee27a-0509-45c1-be08-cc3e8b4cbfc8) renders client-side and returned no content. A search found no Hacker News threads. [unverified]

### 4. Hands-on exercises mapped to blueprint skills

Status of the official repos: `anthropics/anthropic-cookbook` now redirects to `anthropics/claude-cookbooks` (53.8k★, pushed 2026-10-24). [source: https://github.com/anthropics/claude-cookbooks] `anthropics/courses` is archived and recommends Claude 3 Haiku. Use it for concepts and swap in a current model ID. [source: https://github.com/anthropics/courses README.md; GitHub API `archived=true`] Most cookbooks spot-checked use `claude-sonnet-5-5` or `claude-opus-5-5`. `tool_use/tool_choice.ipynb` and `tool_use/extracting_structured_json.ipynb` use Haiku 4.5 with forced `tool_choice`, which fails on Opus/Sonnet 5.5. [source: notebook grep; D-ERR]

| Exam topic (blueprint skill, weight) | Exercise | Official starting point |
|---|---|---|
| Messages API, statelessness, `stop_reason` (API Mechanics 6.8%) | Build a multi-turn CLI that resends full history. Add a `match` on all seven stop reasons: continue `pause_turn` unchanged, treat `refusal` (HTTP 200) as non-content, treat `max_tokens` as truncated. [source: D-STOP] | `anthropics/courses/anthropic_api_fundamentals/02_messages_format.ipynb`, `04_parameters.ipynb` [source: https://github.com/anthropics/courses] |
| Streaming (API Mechanics 6.8%) | Stream a long answer. Read `stop_reason` from `message_delta`. Handle an error event that arrives after HTTP 200. [source: D-ERR; VK ch03] | `anthropics/courses/anthropic_api_fundamentals/05_Streaming.ipynb` [source: https://github.com/anthropics/courses] |
| Errors, retries, idempotency (SE Foundations 7.4%) | Set `max_retries`. Simulate 429 vs 529. Add an idempotency key to a side-effecting tool so a retry cannot double-charge. The SDK retries twice by default and honors `retry-after`. [source: D-ERR] | Docs `api/errors` (no notebook) [source: D-ERR] |
| Prompt caching (Cost and Token Mgmt 2.8%) | Cache a large system prompt and log `cache_creation_input_tokens` and `cache_read_input_tokens`. Reorder the tools and watch the hit rate drop to zero. Send a prompt below the minimum and confirm both counters are 0 with no error. Prefix order is tools → system → messages, with up to 4 breakpoints. [source: D-CACHE] | `claude-cookbooks/misc/prompt_caching.ipynb`, `misc/speculative_prompt_caching.ipynb` [source: https://github.com/anthropics/claude-cookbooks] |
| Message Batches (API Mechanics 6.8%) | Submit 100 classification requests with `custom_id`, then join results by `custom_id` because order is not guaranteed. Compare cost with sync calls (50% off). Try the 1-hour cache TTL on the shared prefix. [source: D-BATCH] | `claude-cookbooks/misc/batch_processing.ipynb` [source: https://github.com/anthropics/claude-cookbooks] |
| Tool-use loop (Tool Implementation 4.4%; Agent Construction 5.3%) | Write a loop that runs while `stop_reason == "tool_use"`. Return `is_error` tool results. Send parallel tool results back in one user message. | `claude-quickstarts/agents/agent.py` (under 300 lines, "NOT an SDK"); `claude-cookbooks/tool_use/customer_service_agent.ipynb`, `parallel_tools.ipynb` [source: https://github.com/anthropics/claude-quickstarts; https://github.com/anthropics/claude-cookbooks] |
| Structured output and defensive parsing (Output Handling 2.6%) | Extract JSON with `output_config.format` and validate it. On failure, retry with the validation error included. Contrast with prefill, which returns 400 on Claude 4.6+. [source: D-ERR] | `claude-cookbooks/tool_use/extracting_structured_json.ipynb`, `misc/how_to_enable_json_mode.ipynb` [source: https://github.com/anthropics/claude-cookbooks] |
| Workflow vs agent (Agent Architecture 4.5%) | Build the same task as a prompt chain and as an orchestrator-workers agent. Compare cost and failure modes. | `claude-cookbooks/patterns/agents/basic_workflows.ipynb`, `orchestrator_workers.ipynb`, `evaluator_optimizer.ipynb` [source: https://github.com/anthropics/claude-cookbooks] |
| Claude Agent SDK and hooks (Agent Construction 5.3%; Claude Hooks 1.0%) | Add a `PreToolUse` hook that denies `rm -rf`. Set turn and budget limits. Run one subagent. | `claude-agent-sdk-python/examples/hooks.py`, `max_budget_usd.py`, `tool_permission_callback.py`, `agents.py`, `streaming_mode.py`; `claude-cookbooks/claude_agent_sdk/00_…` to `08_Dynamic_workflows.ipynb` [source: https://github.com/anthropics/claude-agent-sdk-python; https://github.com/anthropics/claude-cookbooks] |
| Hosted vs self-hosted agents (Agent Construction 5.3%) | Deploy a managed agent with a human-approval gate and prompt versioning. | `claude-cookbooks/managed_agents/CMA_gate_human_in_the_loop.ipynb`, `CMA_prompt_versioning_and_rollback.ipynb`, `CMA_cap_session_spend.ipynb`; `claude-quickstarts/managed-agents` [source: https://github.com/anthropics/claude-cookbooks; https://github.com/anthropics/claude-quickstarts] |
| MCP server (MCP Server Dev 2.1%) | Build one server that exposes a tool, a resource, and a prompt. Run it over stdio, then over Streamable HTTP. The spec defines exactly these two standard transports. [source: MCP-T] | `modelcontextprotocol/python-sdk/examples/servers/simple-resource`, `simple-prompt`, `simple-streamablehttp`; `anthropics/skills/skills/mcp-builder` [source: https://github.com/modelcontextprotocol/python-sdk; https://github.com/anthropics/skills] |
| Built-in vs custom tool vs Skill vs MCP (Agentic Customization 4.1%) | Implement one capability three ways (a Skill, a custom tool, an MCP server) and write down when each fits. | `anthropics/skills/skills/skill-creator`, `template/`; `claude-cookbooks/skills/notebooks/01_skills_introduction.ipynb` to `03_skills_custom_development.ipynb` [source: https://github.com/anthropics/skills; https://github.com/anthropics/claude-cookbooks] |
| Claude Code config (Claude Code 3.1%; Config Mgmt 4.1%) | Compare project and user `settings.json`. Add a Bash-validator hook. Add a subagent and a custom command. Run `claude -p` headless with JSON output. | `anthropics/claude-code/examples/settings/settings-strict.json`, `settings-lax.json`, `settings-bash-sandbox.json`; `examples/hooks/bash_command_validator_example.py`; `claude-cookbooks/claude_agent_sdk/chief_of_staff_agent/.claude/` (agents, commands, output-styles, CLAUDE.md) [source: https://github.com/anthropics/claude-code; https://github.com/anthropics/claude-cookbooks] |
| Context engineering (Context Engineering 3.8%) | Run a long agent with and without compaction and tool-output pruning. Compare token use. | `claude-cookbooks/tool_use/automatic-context-compaction.ipynb`, `misc/session_memory_compaction.ipynb`, `tool_use/memory_cookbook.ipynb`, `tool_use/context_engineering/context_engineering_tools.ipynb` [source: https://github.com/anthropics/claude-cookbooks] |
| Prompt injection defense (AI App Security 3.2%; Guardrails 2.3%) | Give an agent a web page with hidden instructions and an email tool. Show that a system-prompt warning fails. Then block the tool with a hook or human gate, and deliver page text as a delimited tool result. This mirrors official sample 2. [source: OG §8] | No dedicated injection notebook appears in the cookbook tree. Pair `claude-cookbooks/misc/building_moderation_filter.ipynb` with `managed_agents/CMA_gate_human_in_the_loop.ipynb`. [source: https://github.com/anthropics/claude-cookbooks file tree] |
| Evals, tracing, cost tracking (Debugging 2.6%; Cost 2.8%) | Write a code-graded eval and a model-graded eval for one prompt. Trace a failing run and decide whether the fault sits in the integration layer or the model output. | `claude-cookbooks/misc/building_evals.ipynb`, `tool_evaluation/tool_evaluation.ipynb`, `observability/opentelemetry_tracing.ipynb`, `observability/usage_cost_api.ipynb`; `anthropics/courses/prompt_evaluations/` (archived) [source: https://github.com/anthropics/claude-cookbooks; https://github.com/anthropics/courses] |

### 5. Recurring distractor patterns

| Pattern | Typical wrong option | Typical right direction | Source |
|---|---|---|---|
| Prompt text offered as enforcement | "Add a line to the system prompt", or repeat the instruction more firmly | Hook, deterministic check, least-privilege tool access | `OG` §8 Sample 2; gwythyr Q1.4; `VK` ch21 |
| Model size offered as the fix | "Switch to a larger model", or "smallest model regardless of quality" | Match the mechanism to the requirement. A more instruction-following model "can be more susceptible" to injection. | `OG` §8 Samples 1–2 |
| A sampling knob aimed at a non-sampling problem | Raise or lower temperature, or lower `max_tokens` to cut cost | Name the real mechanism: capacity, batching, isolation | `OG` §8 Samples 1–2; `VK` ch01 |
| "Asynchronous" read as "fast" | Parallel synchronous calls for an overnight job | Message Batches when volume is high and nobody waits on a single result | `OG` §8 Sample 1; `VK` ch03 |
| Data pasted or logic hard-coded instead of an integration | Paste inventory into context; hard-code logic into each app's prompt | MCP server shared across apps | `OG` §8 Sample 3 |
| A capability the platform lacks | "Built-in tools can reach any internal REST API" | Custom tool or MCP server | `OG` §8 Sample 3 |
| A neighboring mechanism that works elsewhere | A Skill where a server is needed, a context file where a hook is needed, a retry for a permanent failure | Ask what must execute and who must reuse it | `VK` README.md, ch11 |
| A heavier mechanism than the material needs | Fine-tune or build retrieval when a few labeled examples exist | Few-shot examples in the prompt | `VK` ch01 |
| HTTP 200 treated as success | Parse the first content block unconditionally | Check `stop_reason`. `refusal` arrives as 200. | `D-STOP`; `VK` ch03 |
| Retries treated as safe for side effects | More retries or backoff after a duplicate charge | Idempotency key on the unit of work | `VK` ch17; `JR` |
| Confusable pairs | Anthropic SDK vs Agent SDK; Agent SDK vs Claude Code; prompt injection vs jailbreak; caching vs memory; streaming vs batch; `max_tokens` vs context window; 429 vs 529 | Know the one-line definition of each | `JR` |
| Qualifier words | Missing "first", "best", "is not", "fits better", or a constraint in the last line | Read the last line before the options | `CS`; `IND` |

### 6. Drift between community material and current docs

Banks written before the 5.5 model generation key answers that current APIs reject. The course should teach the exam's intent and add a "current docs" callout.

| Topic | What older community material teaches | Current docs |
|---|---|---|
| Forced `tool_choice` | Force a tool to get structured output or to make a step run first [source: Skillsoft 200Q Q1; `VK` ch09] | `any` and `tool` return 400 on Opus 5.5, Sonnet 5.5, Fable 5.1, Mythos 5.1. Use `auto` with strict tool use, or structured outputs. [source: D-ERR] |
| Prefill | Prefill the assistant turn to force a format | Returns 400 on Claude 4.6+ [source: D-ERR] |
| Extended thinking | `thinking: {type: "enabled", budget_tokens: N}` [source: Skillsoft 200Q Q15–16] | Removed on Claude 4.7+. Use adaptive thinking with `output_config.effort`. [source: D-ERR] |
| Cache read price | 0.1× base input [source: `JR` cheat sheet, labeled "historically documented"] | 0.05× on Opus 5.5 and Sonnet 5.5, 0.025× on Fable 5.1 and Mythos 5.1, 0.1× elsewhere [source: D-CACHE] |
| MCP transports | "stdio, sockets" [source: `OG` §6 Domain 8] | Two standard transports: stdio and Streamable HTTP, which replaced HTTP+SSE. Custom transports are allowed. [source: MCP-T] |

Whether live exam items still key the older behavior is unknown. The exam guide is v1.0 from July 2026. [unverified]

## Comparison

| Resource | Type | Accuracy | Currency | Practice items | Link in README |
|---|---|---|---|---|---|
| vkorost guide | Book (23 ch.) | High, docs-cited | Sep 2026 | None | Yes |
| preporato | Guide + 30 Qs + timed test | High | Oct 2026 | 30 | Yes (vendor) |
| gwythyr / Purcell | 53-Q interactive bank | High (spot-checked) | Aug 2026 | 53 | Yes (credit Purcell) |
| asampath1 | Notes + MCQ sets + mock | High (spot-checked) | Oct 2026 | 53 + domain sets | Yes |
| CorporateChittyChat + ccdvf-course | Videos + code + mock | Not deeply checked | Oct 2026 | 30 | Yes (hands-on) |
| kuljotSB | Lab notebooks | Code runs on current APIs | Aug 2026 | None | Optional |
| Amey-Thakur | Notes, mocks, flashcards | Generic | Oct 2026 | 35 + 3 mocks | Optional (flashcards) |
| dnacenta CCDV-F page | Overview | Matches OG | Oct 2026 | None | Optional |
| Skillsoft zip | Slides + 200 Qs | Outdated keys | Oct 2026 | 200 | No |
| natsh | Scraped official course | n/a | Aug 2026 | 153 | No |
| hoangminhq5310 "Dump" | Answer-only bank | No rationale | Sep 2026 | 97 | No |

[source: section 2 of this file]

## Decision

Recommended README links, ranked:

1. Official CCDV-F Exam Guide v1.0 (`OG`). Link to Anthropic's copy, not a re-hosted PDF.
2. vkorost/claude-certified-developer-guide. Best conceptual coverage and decision framing. Link only, because the license is NC-SA.
3. gwythyr/ccdv-practice-exam (Matthew Purcell's 53 questions). Best free practice set with distractor rationales.
4. preporato/claude-certification-guide. Accurate guide and 30 multi-response-aware questions. Label it vendor-maintained.
5. asampath1/myClaudeLab. Domain-by-domain MCQs and a mock from a candidate who passed.
6. anthropics/claude-cookbooks (specific notebooks from section 4). The lab spine for the course.
7. CorporateChittyChat/claude-certification-prep + chittychat-studio/ccdvf-course. Video and code companion.
8. Amey-Thakur `flashcards.tsv` for Anki users.

Reasoning: items 2–5 were spot-checked against current docs and every claim checked matched. Items 2, 3, and 5 come from people who report passing. The excluded repos redistribute gated material, carry answer-only dumps, or key answers that current APIs reject.

## Open questions

- **Purcell permission.** gwythyr republishes Purcell's PDF "with full attribution". Should the README link gwythyr, or only Purcell's own post? His original post URL was not found.
- **Exam keys vs current docs.** Should course questions follow the exam guide's framing (forced tool choice to make a step run first, "sockets") or current docs? The recommendation is current docs plus a callout. Lucas decides.
- **Multi-select share.** The guide says multiple-response items exist. Several candidates report none. Should course drills still include "Select TWO" items? The recommendation is yes, at about 15–25%.
- **Partner-only access.** Exams require Claude Partner Network membership. Should the course README say this up front?
- **Reddit and Medium gaps.** This crawler cannot read Reddit or Medium article pages. A manual pass over r/ClaudeAI may add reports.
