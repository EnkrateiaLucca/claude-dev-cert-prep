# Claude Certified Developer – Foundations (CCDV-F): Exam Prep

Course materials for the O'Reilly live training [*Claude Certified Developer – Foundations Exam Prep: A Two-Hour Crash Course*](https://learning.oreilly.com/live-events/claude-certified-developer-foundations-exam-prep-a-two-hour-crash-course/0642572438371/). The official [Exam Guide v1.0](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf) is the compass for everything here.

## What's inside

| Path | What it is |
|---|---|
| `presentation/claude-dev-foundations-exam-prep.html` | Live slide deck (remark.js). Open in a browser; press `P` for presenter notes. |
| `presentation/claude-dev-foundations-exam-prep.pdf` | PDF export of the deck |
| `questions/practice-questions.md` | 13 original exam-style questions, the 3 official samples, and a rapid-fire round, with answers and distractor analysis |
| `cheatsheet.md` | The whole course on one page |
| `exercises/` | Four hands-on builds that cover the exam guide's "build one Claude application" advice, plus a map of official notebooks by blueprint skill |
| `research/` | Sourced notes on the exam guide and community resources |

## Schedule (120 min)

| Segment | Time | Exam domains |
|---|---|---|
| 1. The exam and the blueprint | 15 min | All |
| 2. API mechanics, application design, model choice | 40 min | D2 (33.1%) + D5 (16.8%) |
| 3. Agents, tools, and MCP | 30 min | D1 (14.7%) + D8 (10.6%) |
| 4. Prompting, context, security, Claude Code, debugging | 25 min | D6 (11.0%) + D7 (8.1%) + D3 (3.1%) + D4 (2.6%) |
| 5. Readiness map and study plan | 10 min | All |

## Exam at a glance

Exam code CCDV-F · 53 items · 120 minutes · multiple choice and multiple response · scaled score 720/1,000 to pass · $125 · Pearson VUE (online or test center) · valid 12 months, free on-time renewal · no prerequisites. Registration requires a Claude Partner Network organization email.

## Official resources

- [Exam Guide v1.0 (PDF)](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf): blueprint, 25 weighted skills, 3 sample questions
- [Official prep path](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations) (Partner Academy): five lessons, about 13 hours
- [Certification FAQ](https://anthropic-partners.skilljar.com/page/faq-certifications)
- [Claude API docs](https://platform.claude.com/docs) · [Claude Code docs](https://code.claude.com/docs) · [MCP docs](https://modelcontextprotocol.io)
- [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) · [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) · [anthropics/skills](https://github.com/anthropics/skills)

## Community resources

Spot-checked against current docs in October 2026. Community material is unofficial; verify anything that disagrees with the docs.

| Resource | What it offers |
|---|---|
| [vkorost/claude-certified-developer-guide](https://github.com/vkorost/claude-certified-developer-guide) | 23-chapter study book by a candidate who passed; every claim cites the docs; trap tables per chapter |
| [preporato/claude-certification-guide](https://github.com/preporato/claude-certification-guide) | CCDV-F guide plus 30 questions with per-option explanations, including multiple response |
| [gwythyr/ccdv-practice-exam](https://github.com/gwythyr/ccdv-practice-exam) | 53-question interactive practice exam with a "why not" for every distractor |
| [asampath1/myClaudeLab](https://github.com/asampath1/myClaudeLab) | Per-domain question sets, labs, and a 53-item mock from a candidate who scored 896 |
| [chittychat-studio/ccdvf-course](https://github.com/chittychat-studio/ccdvf-course) | Runnable code for a 12-episode CCDV-F video series |
| [kuljotSB/Claude-Certified-Developer-CCDV-F](https://github.com/kuljotSB/Claude-Certified-Developer-CCDV-F) | Lab notebooks: Messages API, batches, structured outputs, MCP, Agent SDK |

Watch out for older question banks that key forced `tool_choice`, assistant prefill, or `budget_tokens` as correct answers. Current models return a 400 for all three.

## Before the session

1. Clone this repo.
2. Skim the official exam guide.
3. Optional: an Anthropic API key and the SDK (`pip install anthropic` or `npm install @anthropic-ai/sdk`) for the exercises.
4. Optional: Claude Code, to follow the configuration segment hands-on.

Practice questions are original and are not drawn from the live exam, except the three official samples quoted from the public exam guide. Platform facts (models, pricing, feature availability) were checked against Anthropic's documentation in October 2026 and will change; the exam tests the reasoning, not the version numbers.
