# Claude Certified Developer – Foundations (CCDV-F): Exam Guide Research

Research date: 2026-10-26.

## Context

This file records what Anthropic officially publishes about the Claude Certified Developer – Foundations exam: logistics, audience, blueprint, sample items, and the official prep path. The course content, practice questions, and cheatsheet in this repo should align to the official blueprint below.

**Headline:** The official exam guide is public. It is a 14-page PDF, "Version 1.0 · Effective July 2026 · Exam code: CCDV-F", linked from the Partner Academy certifications page. [source: https://anthropic-partners.skilljar.com/page/partner-certifications] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]

Label conventions: `[source: url]` marks a fetched and read source. `[inferred]` marks my own analysis built on sourced facts. `[unverified]` marks a claim I could not confirm with a fetched page. "Unofficial" marks third-party material.

## Sources

| ID | Source | Type | Fetched |
|----|--------|------|---------|
| S1 | [CCDV-F Exam Guide PDF v1.0 (English)](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf) | Official, primary | Yes. Downloaded with curl, extracted with `pdftotext -layout`. 14 pages, PDF created 2026-07-08 |
| S2 | [CCDV-F Exam Guide PDF (Japanese)](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F34hhd92iyp94a0gtbr15cy5jk%2Fpublic%2F1792453728%2FClaude+Certified+Developer+-+Foundations+Exam+Guide+%28Japanese%29.pdf) | Official | Yes. Same method. PDF created 2026-10-20 |
| S3 | [Partner Academy: Earn your Claude certification](https://anthropic-partners.skilljar.com/page/partner-certifications) | Official | Yes (WebFetch and curl) |
| S4 | [Partner Academy: Certification FAQ](https://anthropic-partners.skilljar.com/page/faq-certifications) | Official | Yes (curl, HTML parsed for verbatim text) |
| S5 | [Partner Academy: Certification policies](https://anthropic-partners.skilljar.com/page/policies-certifications) | Official | Yes (curl) |
| S6 | [Partner Academy: Who can take an exam](https://anthropic-partners.skilljar.com/page/certification-eligibility) | Official | Yes (curl) |
| S7 | [Partner Academy: CCDV-F exam purchase page](https://anthropic-partners.skilljar.com/claude-certified-developer-foundations-certification) | Official | Yes (WebFetch and curl) |
| S8 | [Partner Academy: CCDV-F Prep Course (path)](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations) | Official | Yes (curl) |
| S9 | [Lesson 1: MSO Foundations](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/mso-foundations) | Official | Yes (curl) |
| S10 | [Lesson 2: Production-Grade Prompting, Agents & Tool Use](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/production-grade-prompting-agents-tool-use) | Official | Yes (curl) |
| S11 | [Lesson 3: Claude Code, MCP & Integration](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/claude-code-mcp-integration) | Official | Yes (curl) |
| S12 | [Lesson 4: Production Engineering, Evals & Security](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/production-engineering-evals-security) | Official | Yes (curl) |
| S13 | [Lesson 5: Accelerators & IP Contribution](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/accelerators-ip-contribution) | Official | Yes (curl) |
| S14 | [Partner Academy: Exam prep courses](https://anthropic-partners.skilljar.com/page/claude-certification-exam-prep-courses) | Official | Yes (curl) |
| S15 | [Partner Academy: Claude Developer learning path](https://anthropic-partners.skilljar.com/path/claude-developer) | Official | Yes (curl) |
| S16 | [Exam Registration Guide PDF](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542947%2FClaude+Certification+Program+-+Exam+Registration+Guide.pdf) | Official | Yes (curl + `pdftotext`) |
| S17 | [Credly: CCDV-F badge](https://www.credly.com/org/anthropic/badge/claude-certified-developer-foundations) | Official (Anthropic org on Credly) | Yes (WebFetch) |
| S18 | [claude.com: Four role-based certifications (2026-07-23)](https://claude.com/resources/articles/four-role-based-claude-certifications) | Official | Yes (WebFetch) |
| F1 | [Tutorials Dojo CCDV-F study guide](https://tutorialsdojo.com/ccdv-f-claude-certified-developer-foundations-study-guide/) | Unofficial, commercial | **Failed**: WebFetch returned a truncated page with no body text |

## Verification of the draft domain weights

| Draft claim | Official value | Status | Source |
|-------------|----------------|--------|--------|
| 8 weighted domains | 8 domains | Confirmed | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] |
| Applications and Integration 33.1% | Domain 2, "Applications and Integration", 33.1% | Confirmed | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] |
| Model Selection and Optimization 16.8% | Domain 5, "Model Selection and Optimization", 16.8% | Confirmed | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] |
| Agents 14.7% | Domain 1, official name "Agents and Workflows", 14.7% | Confirmed, name corrected | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] |
| Claude Code 3.1% | Domain 3, "Claude Code", 3.1% | Confirmed | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] |
| Evals 2.6% | Domain 4, official name "Eval, Testing, and Debugging", 2.6% | Confirmed, name corrected | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] |
| (missing) | Domain 6 "Prompt and Context Engineering" 11.0%; Domain 7 "Security and Safety" 8.1%; Domain 8 "Tools and MCPs" 10.6% | Added | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] |

The Japanese guide (created 2026-10-20) carries the same version number, item count, and all eight weights. [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F34hhd92iyp94a0gtbr15cy5jk%2Fpublic%2F1792453728%2FClaude+Certified+Developer+-+Foundations+Exam+Guide+%28Japanese%29.pdf]

## Logistics

Values come from the CCDV-F guide, Section 5 "Exam Details at a Glance", unless noted. [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]

| Item | Value | Source |
|------|-------|--------|
| Credential | Claude Certified Developer – Foundations | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] |
| Exam code | CCDV-F | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] |
| Guide version | "Version 1.0 · Effective July 2026"; Document Control: "1.0 Initial publication July 2026" | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] |
| Number of items | 53 | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] |
| Item format | "Multiple-choice and multiple-response items; each item states how many responses to select". FAQ: "All Claude certification exams use multiple choice and scenario-based multiple response questions." | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Exam structure | No scenario bank and no "Exam structure" row in the CCDV-F guide | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] |
| Time limit | 120 minutes. FAQ: "Plan for about 135 minutes of total seat time, which includes check-in, instructions, and a brief post-exam survey." | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Pace | About 2.3 minutes per item (120 / 53) | [inferred] |
| Delivery | "Proctored: online proctored and/or test center, per program policy". Section 10: "The exam is delivered by Pearson VUE." Online option is OnVUE. | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Open/closed book | "No. Exams are closed book. Browser translation tools are not permitted under the Pearson proctoring platform." | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Languages | "The exam and prep content are available in English and Japanese." A Japanese CCDV-F guide exists. | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F34hhd92iyp94a0gtbr15cy5jk%2Fpublic%2F1792453728%2FClaude+Certified+Developer+-+Foundations+Exam+Guide+%28Japanese%29.pdf] |
| Passing score | "Scaled score of 720 on a scale of 100–1,000". FAQ: "The minimum passing score is 720 for all four certifications." | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Scoring model | "a criterion-referenced assessment: each candidate is measured against a fixed performance standard, not against other candidates." Cut score set by "a formal standard-setting study in which trained subject matter experts judged the level of performance expected of a minimally qualified candidate." | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] |
| Scaled scoring rationale | "Scaled scoring equates scores across exam forms that may have slightly different difficulty." | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Result reporting | "Pass/fail with scaled score (100–1,000), plus percent-correct by domain on the score report". Section-level percentages "are not used to determine your pass or fail result, which is based on your total scaled score." Score shown on screen at the end of the exam. | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Fee | $125 USD. Section 10: "The fee shown at checkout reflects any discount that applies to your partner tier." | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/partner-certifications] [source: https://anthropic-partners.skilljar.com/claude-certified-developer-foundations-certification] |
| Discounts | "Registered-tier partners pay full price. Select, Preferred, and Global Premier partners receive 50% off, applied automatically at checkout. Through December 31, 2026, Global Premier partners receive a 100% discount on all certification exams". Payment is by credit card through Partner Academy. | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Validity | "12 months from the date the credential is awarded" | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] |
| Renewal | Guide: "To renew on time, you review what has changed since you certified and complete a free, non-proctored assessment on the Anthropic Partner Academy. There is no fee for on-time renewal. If your credential lapses, you must retake the full exam at the full fee to regain certified status." Policies: "an open-book online assessment ... which extends your certification for another 12 months from your current expiration date. You can retake that assessment as many times as you need." | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/policies-certifications] |
| Content-change rule | "If exam content changes significantly, Anthropic may require holders to retake the full exam to recertify rather than complete the renewal assessment." | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] |
| Prerequisites | "There are no mandatory prerequisites or courses required to sit this exam. The experience above is recommended, not required. The credential is awarded based on exam performance alone." | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] |
| Eligibility | "Claude certification exams are open to people who work at organizations in the Claude Partner Network." Registration requires "a company email on a domain listed in your organization's partner record". Candidates "need to be 18 or older and have a government-issued ID." FAQ: "Certification is currently available only to organizations in the Claude Partner Network." | [source: https://anthropic-partners.skilljar.com/page/certification-eligibility] [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Partner network credit | CCDV-F counts toward Claude Partner Network eligibility. Associate does not. | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Registration steps | Guide Section 10: open the exam page on Partner Academy; download the guide and review the Terms and Conditions and Exam Policy; register and check out; create a Pearson VUE account; choose online proctoring or a Pearson test center. The Registration Guide PDF adds a 12-step walkthrough (two Pearson emails, candidate agreement, password, security questions). | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542947%2FClaude+Certification+Program+-+Exam+Registration+Guide.pdf] |
| Registration window | "Once you register for an exam, your registration is valid for 5 years." | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Retakes | "14 days after the first, 30 days after the second, and 90 days after the third. You may take an exam up to four times within a rolling twelve-month period. Limits apply per exam ... The exam fee applies to each attempt." Policies: "If you pass, you can't retake the exam to improve your score." Wait and attempt count "reset when the exam moves to a new version." | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/policies-certifications] |
| Cancel/reschedule | **Conflict.** Guide Section 10: "You may cancel or reschedule up to 24 hours before your appointment." FAQ and Policies: "at least 48 hours before your appointment". The Japanese guide also says 24 hours. See Open questions. | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/faq-certifications] [source: https://anthropic-partners.skilljar.com/page/policies-certifications] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F34hhd92iyp94a0gtbr15cy5jk%2Fpublic%2F1792453728%2FClaude+Certified+Developer+-+Foundations+Exam+Guide+%28Japanese%29.pdf] |
| Practice exam | "The practice exam available on the previous platform was retired in the move to Pearson. The exam guide includes sample questions that show the format and style of what's on the exam." | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Badge | Credly badge on pass. Credly skills: Agent development, Application Security, Claude API integration, Context engineering, Eval & debugging, MCP Server Development, Model Optimization, Prompt Engineering. Earning criteria: "Successfully passed the proctored Claude Certified Developer – Foundations exam." | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] [source: https://www.credly.com/org/anthropic/badge/claude-certified-developer-foundations] |
| NDA | Candidates accept a confidentiality agreement covering "all exam content, including questions, answer options, and scenarios". Refusal ends the session with no refund. | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] |
| Launch timing | Guide "Effective July 2026"; PDF created 2026-07-08. A 2026-07-23 article announces three new role-based certifications and says the Developer credential "is for engineers building applications with Claude, and includes training on the Claude API, tool use, and agent development." | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://claude.com/resources/articles/four-role-based-claude-certifications] |

## Audience and minimally qualified candidate

### Purpose (Sections 1–2, verbatim)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]

> The Claude Certified Developer – Foundations certification validates that an individual can build, integrate, and ship production-grade applications, agents, and workflows using Anthropic's Claude platform at a foundational level. It is intended for technical professionals who bridge Claude's capabilities and production-ready applications, translating technical requirements into working systems through API integration, agent and tool construction, prompt and context engineering, evaluation, security, and model selection.

> The primary purpose of the Claude Certified Developer – Foundations certification is to provide an independent assessment of the knowledge, skills, and abilities required to build Claude-based applications competently at a foundational level. Earning the credential signals to employers, clients, and teams that the holder can independently own or significantly contribute to building, integrating, and shipping Claude-powered systems.

Candidates who earn the credential can demonstrate that they are able to effectively apply knowledge in the following areas (verbatim):

- Building agents and workflows using the Claude Agent SDK, agentic frameworks, and custom agent loops
- Integrating Claude into application code through the API, client SDKs, and third-party integrations, including streaming, error handling, and multi-format input
- Operating Claude Code across interfaces, authoring Claude Skills, and configuring CLAUDE.md, settings.json, and plugins
- Writing effective prompts and applying context engineering techniques to control model behavior and prevent context drift
- Designing and running evals, debugging failure modes through trace analysis, validating structured output, and monitoring production quality
- Selecting Claude model tiers and managing tokens, caching, and batch processing to optimize cost and latency
- Applying secure-by-design principles and implementing guardrails through hooks to defend against prompt injection and destructive actions
- Building custom tools, function schemas, and MCP servers, while weighing tradeoffs across built-in tools, custom tools, Skills, and MCPs

### Intended audience (Section 3, verbatim)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]

> The certification is intended for technical professionals who build, integrate, and ship production-grade AI solutions using large language models (LLMs), particularly Anthropic's Claude platform. This audience primarily includes AI and machine learning engineers, technical leads, and senior software engineers operating at the intersection of business requirements and technical implementation.

> These professionals typically have one to five years of experience in software engineering, along with at least six months of hands-on experience with Claude or comparable LLM-based systems. They possess strong foundational knowledge and applied skills in software development, with the ability to build agents and workflows using the Claude Agent SDK and agentic frameworks, integrate Claude through the Application Programming Interface (API) and client Software Development Kits (SDKs), operate Claude Code for codebase modernization, write effective prompts and apply context engineering, design and run evals, and build custom tools and Model Context Protocol (MCP) servers. They understand tradeoffs in model selection and tool type and can apply appropriate patterns to meet technical requirements. They are proficient in Python and/or TypeScript, fluent with REST APIs and Command Line Interface (CLI) tools, and have a working understanding of LLM fundamentals, agents, context management, and MCP.

> This certification is not intended for non-technical or casual users of Claude-based applications, or individuals without hands-on software development experience. It also excludes roles limited to prompt writing or other isolated tasks without broader application development responsibility.

### Minimally qualified candidate (Section 4, verbatim)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]

> The exam is targeted at the minimally qualified candidate (MQC): a hands-on technical individual who builds, integrates, and ships Claude-powered applications, agents, and workflows. They bridge Claude's capabilities and production-ready applications, translating technical requirements into working applications.

> The MQC possesses strong foundational knowledge and applied skills in software development, including the ability to build agents and workflows using the Claude Agent SDK and agentic frameworks, integrate Claude through the API and client SDKs, operate Claude Code for codebase modernization, write effective prompts and apply context engineering, design and run evals, and build custom tools and MCP servers. They understand tradeoffs in model selection (cost, latency, capability) and tool type (built-in, custom, Skills, MCPs) and can apply appropriate patterns to meet technical requirements.

Recommended experience (verbatim):

- One to five years of experience in software engineering
- At least six months of hands-on experience with Claude or comparable LLM-based systems
- Proficiency in Python and/or TypeScript
- Fluency with REST APIs and CLI tools
- Working understanding of LLM fundamentals, agents, context management, and MCP

### Other official descriptions (verbatim)

- Certifications page, Developer role card: "For engineers who build with the Claude API, Claude Code, and Model Context Protocol — from first integration to production agents." [source: https://anthropic-partners.skilljar.com/page/partner-certifications]
- Credly: "The Claude Certified Developer – Foundations credential is designed for developers." [source: https://www.credly.com/org/anthropic/badge/claude-certified-developer-foundations]

## Domains and objectives

Section 6 verbatim. "The percentages indicate the approximate proportion of scored items drawn from each domain." "Each domain below lists the skills against which exam items are written. Skill descriptions summarize the knowledge and competencies measured. Skill weights show each skill's share of the overall exam." Weights "reflect the relative importance of each domain to competent performance as determined through the job task analysis and content validation surveys." [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]

| # | Content Domain | Weight | Skills | Approx. items of 53 [inferred] |
|---|----------------|--------|--------|------------------|
| 1 | Agents and Workflows | 14.7% | 3 | ~8 |
| 2 | Applications and Integration | 33.1% | 6 | ~18 |
| 3 | Claude Code | 3.1% | 1 | ~2 |
| 4 | Eval, Testing, and Debugging | 2.6% | 1 | ~1 |
| 5 | Model Selection and Optimization | 16.8% | 4 | ~9 |
| 6 | Prompt and Context Engineering | 11.0% | 3 | ~6 |
| 7 | Security and Safety | 8.1% | 4 | ~4 |
| 8 | Tools and MCPs | 10.6% | 3 | ~6 |
| | **Total** | **100%** | **25** | 53 |

Weights and skill text: [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]. Item counts are my arithmetic (weight × 53, rounded). The guide does not say whether any of the 53 items are unscored. Skill weights within each domain sum exactly to the domain weight. [inferred]

The CCDV-F blueprint uses named, weighted **skills** with a one-paragraph description each. It has no numbered "Task Statement X.Y" items and no "Knowledge of / Skills in" lists. The numbering below (1.1, 1.2, ...) is mine for cross-referencing. [inferred]

### Domain 1: Agents and Workflows (14.7%)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]

- **1.1 Agent Architecture (4.5%)**: Principles, patterns, and tradeoffs of agent and workflow architecture, including the decision criteria for using a workflow versus an agent, the structure of manager/supervisor hierarchies, and the role of subagents in improving task execution.
- **1.2 Agent Construction with Claude (5.3%)**: Methods, tools, and platforms for constructing Claude agents, including the Claude Agent SDK, custom agent loops and harnesses, managed agent deployment models (self-hosted vs. Anthropic-hosted), and hooks for deterministic actions.
- **1.3 Agent Patterns and Frameworks (4.9%)**: Common agent design patterns (tool-use loops, sub-agents, memory, context-window management) and agentic abstraction frameworks (e.g., Strands, LangGraph, PydanticAI) for building agents and workflows for multi-step tasks.

### Domain 2: Applications and Integration (33.1%)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]

- **2.1 Understanding Requirements (3.4%)**: Functional and infrastructure requirements based on business requirements and solution architecture.
- **2.2 Systems Life Cycle (2.8%)**: Systems life cycle management concepts and frameworks used to develop, implement, operate, and maintain IT systems.
- **2.3 Claude API Mechanics (6.8%)**: Claude API behavior and mechanics, including messages, tools, streaming, vision, thinking, caching, invoking Claude through third-party vendors, Messages API data access patterns, batch API use, and tradeoffs between realtime and batch API selection.
- **2.4 Software Engineering Foundations (7.4%)**: Core software engineering principles and practices, including REST APIs, JSON, asynchronous programming, version control, SDLC integration, code review, and small- and large-scale refactoring.
- **2.5 Claude Application Design (8.6%)**: Design considerations for building Claude applications, including how Claude interprets instructions across interfaces (Claude Code, Desktop, claude.ai, API, SDKs), content boundaries, schema design, session hygiene, and plugin management.
- **2.6 Configuration Management (4.1%)**: Configuration management for Claude system components, including CLAUDE.md files, settings.json, model version pinning, prompt versioning, and plugin dependencies.

### Domain 3: Claude Code (3.1%)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]

- **3.1 Claude Code Operation (3.1%)**: Claude Code core components (Rules, Skills, Commands, Agents, Agent Memory), features (session management, built-in and custom slash commands, headless mode, streaming mode, auto-mode), the CLAUDE.md hierarchy, repository initialization, and settings.json configuration.

### Domain 4: Eval, Testing, and Debugging (2.6%)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]

- **4.1 Debugging and Error Handling (2.6%)**: Debugging and error handling techniques for Claude applications, including error type identification, recovery strategy selection, trace analysis to identify failure modes, and problem origin isolation between the integration layer and model output.

### Domain 5: Model Selection and Optimization (16.8%)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]

- **5.1 LLM Fundamentals (5.2%)**: Basic understanding of LLMs (tokens, context windows, sampling, non-determinism, next-token generation), model options (fast mode, extended thinking, adaptive thinking, effort levels), and fundamental prompting techniques (zero-shot, single-shot, multi-shot).
- **5.2 Technical Fundamentals (6.1%)**: Foundational technical concepts supporting AI application development, including basic engineering practices (integrating with SDKs that wrap REST APIs, websockets).
- **5.3 Model Selection and Tradeoffs (2.7%)**: Claude model capabilities (Opus vs. Sonnet vs. Haiku use cases, adaptive thinking support), tradeoffs across quality/latency/cost parameters, and breaking behavior changes across model releases when selecting models for tasks.
- **5.4 Cost and Token Management (2.8%)**: Token budgeting and cost management techniques for Claude applications, including token usage tracking, cost modeling, and caching techniques (prompt caching, cache check-pointing) for cost optimization.

### Domain 6: Prompt and Context Engineering (11.0%)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]

- **6.1 Context Engineering (3.8%)**: Context and memory management techniques for Claude applications, including context window management, prevention of context drift and bloat (tool output pruning, compaction), and context isolation through subagents or multi-step agentic workflows.
- **6.2 Prompt Engineering (4.6%)**: Prompt engineering principles and methods (instruction clarity, few-shot examples, system versus user placement, output constraints, prompt and instruction placement across components, iterative refinement, prompt adjustment, input sanitization) when writing and iterating on prompts for Claude.
- **6.3 Output Handling (2.6%)**: Established patterns and techniques for producing, validating, and consuming Claude output, including structured output patterns, response validation, defensive parsing, and skepticism toward confident output.

### Domain 7: Security and Safety (8.1%)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]

- **7.1 AI Application Security (3.2%)**: Data privacy and security best practices, including prompt injection awareness and mitigation, jailbreak defense, untrusted input handling, data leakage prevention, PII handling, and ensuring authentication, authorization, confidentiality, privacy, and integrity.
- **7.2 Guardrails and Safe Deployment (2.3%)**: Safe and responsible deployment practices (content policy, guardrail layering) and secure-by-design principles (privacy, identity and access management, least privilege).
- **7.3 Claude Hooks (1.0%)**: Leveraging hooks for guardrails and safety controls to prevent destructive actions within Claude applications.
- **7.4 Identity, Secrets, and Key Management (1.6%)**: Managing secrets, credentials, and API keys across Claude development and production environments, including identity validation and authentication, access approval and level verification, and authorized access monitoring.

### Domain 8: Tools and MCPs (10.6%)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]

- **8.1 Tool Implementation (4.4%)**: Tool implementation practices for Claude applications, including tool use and function calling, configuration for external system interaction, tool description writing, error handling, tool usage patterns (agentic harness dispatch, client-side vs. server-side tools, approval patterns), and tool set construction best practices.
- **8.2 MCP Server Development (2.1%)**: MCP server development practices, including server authoring, deployment, integration with Claude applications, MCP resources, tools, and prompts, and communication patterns (stdio, sockets, client vs. server).
- **8.3 Agentic Customization (4.1%)**: Tradeoffs among built-in Tools, custom Tools, Skills, and MCPs for selecting and applying the appropriate approach for a given use case.

### Skills ranked by weight [inferred]

Ranking computed from the official skill weights above.

| Rank | Skill | Weight | ~Items |
|------|-------|--------|--------|
| 1 | 2.5 Claude Application Design | 8.6% | 4.6 |
| 2 | 2.4 Software Engineering Foundations | 7.4% | 3.9 |
| 3 | 2.3 Claude API Mechanics | 6.8% | 3.6 |
| 4 | 5.2 Technical Fundamentals | 6.1% | 3.2 |
| 5 | 1.2 Agent Construction with Claude | 5.3% | 2.8 |
| 6 | 5.1 LLM Fundamentals | 5.2% | 2.8 |
| 7 | 1.3 Agent Patterns and Frameworks | 4.9% | 2.6 |
| 8 | 6.2 Prompt Engineering | 4.6% | 2.4 |
| 9 | 1.1 Agent Architecture | 4.5% | 2.4 |
| 10 | 8.1 Tool Implementation | 4.4% | 2.3 |
| 11 | 2.6 Configuration Management / 8.3 Agentic Customization | 4.1% each | 2.2 each |
| — | Smallest: 7.3 Claude Hooks | 1.0% | 0.5 |

### Blueprint observations [inferred]

- **Generic engineering carries real weight.** Skills 2.1 Understanding Requirements, 2.2 Systems Life Cycle, 2.4 Software Engineering Foundations, and 5.2 Technical Fundamentals name no Claude feature. Together they are 19.7% of the exam (about 10 items).
- **Claude Code reaches beyond Domain 3.** Domain 3 is 3.1%, but CLAUDE.md, settings.json, and plugins also appear in 2.5 and 2.6; hooks appear in 1.2 and 7.3; Skills appear in 8.3. Claude Code content spans roughly 5 skills.
- **Eval design is not a named blueprint skill.** The Section 2 list says "Designing and running evals", and the audience text says "design and run evals". Domain 4 contains only "Debugging and Error Handling". Eval-adjacent content also sits in 6.3 Output Handling (response validation). Expect eval items to be rare.
- **Domain 5 mixes fundamentals and selection.** Pure model-tier selection (5.3) is only 2.7%. LLM fundamentals (5.1) and SDK/REST/websocket plumbing (5.2) make up most of the 16.8%.
- **Fractional skills.** Six skills weigh under 2.5% (under ~1.3 items). A given form may test some of them with zero or one item.
- **Named third-party frameworks.** 1.3 names Strands, LangGraph, and PydanticAI as examples. These are the only non-Anthropic products named in the blueprint.

## In-scope / out-of-scope technologies

- The CCDV-F guide has **no** "In-Scope Topics", "Out-of-Scope Topics", or technology appendix. Its 16 sections end at Document Control. [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]
- The FAQ states the exam guide "lists the domains and task statements the exam covers and is the authoritative source for exam scope." [source: https://anthropic-partners.skilljar.com/page/faq-certifications]
- Technologies and features named in the Section 6 skill text: Claude Agent SDK; custom agent loops and harnesses; managed agent deployment (self-hosted vs. Anthropic-hosted); hooks; Strands, LangGraph, PydanticAI; Messages API (messages, tools, streaming, vision, thinking, caching); third-party vendors; batch API; Claude Code, Desktop, claude.ai, API, SDKs; plugins; CLAUDE.md; settings.json; model version pinning; prompt versioning; Claude Code Rules, Skills, Commands, Agents, Agent Memory; slash commands; headless mode; streaming mode; auto-mode; fast mode; extended thinking; adaptive thinking; effort levels; Opus, Sonnet, Haiku; prompt caching; cache check-pointing; websockets; compaction; tool output pruning; subagents; MCP resources, tools, and prompts; stdio and sockets; built-in vs. custom Tools; client-side vs. server-side tools. [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]
- Prep lessons add Files API, XML tags, LLM-as-judge, permission modes, Amazon Bedrock, and Google Vertex AI. [source: https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/production-grade-prompting-agents-tool-use] [source: https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/production-engineering-evals-security] [source: https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/claude-code-mcp-integration] [source: https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/accelerators-ip-contribution]

## Item style and scenario format

- Guide: "Multiple-choice and multiple-response items; each item states how many responses to select". [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]
- FAQ: "All Claude certification exams use multiple choice and scenario-based multiple response questions." [source: https://anthropic-partners.skilljar.com/page/faq-certifications]
- The NDA covers "questions, answer options, and scenarios", so the live exam contains scenario material of some kind. [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]
- The guide publishes no scenario bank. The samples "show the style and cognitive level of the exam" and are standalone items. [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]
- Each sample opens with a 2–3 sentence mini-scenario (a constraint plus a goal) and asks "Which approach best fits" or "Which mitigation is most effective". All three samples are single-answer. [inferred]

## Sample questions

Section 8, verbatim. "These illustrative items show the style and cognitive level of the exam. They are not drawn from the live item bank. Correct answers and rationale appear after the questions." [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]

**Sample 1 · Domain 2 — Applications and Integration**

A developer must process 10,000 documents overnight to produce a non-urgent analytics report. Cost is the primary concern, and results are not needed until the following morning. Which approach best fits the requirement?

- A. Send every request synchronously through the Messages API in parallel to finish as quickly as possible.
- B. Use the Message Batches API, which processes large asynchronous workloads within a 24-hour window at reduced cost.
- C. Lower max_tokens on synchronous calls to minimize cost.
- D. Switch to the smallest available model regardless of output quality.

**Answer: B.** "The Message Batches API is designed for latency-tolerant, high-volume workloads at lower cost, which matches an overnight, non-urgent job. Sending requests synchronously in parallel (A) does not reduce per-token cost; lowering max_tokens (C) or blindly downsizing the model (D) does not address the batch-versus-realtime tradeoff."

**Sample 2 · Domain 7 — Security and Safety**

A Claude-powered agent summarizes web pages submitted by end users. One page contains hidden text instructing the model to ignore previous instructions and reveal its system prompt. Which mitigation is most effective?

- A. Raise the model's temperature so its behavior is harder to predict.
- B. Treat retrieved page content as untrusted input, keep it separate from trusted instructions, and use guardrails or hooks so injected instructions cannot trigger sensitive actions.
- C. Add a line to the system prompt asking users not to include malicious instructions.
- D. Switch to a larger model that follows instructions more reliably.

**Answer: B.** "Prompt injection is addressed by isolating untrusted content from trusted instructions and enforcing least-privilege guardrails so injected text cannot invoke sensitive tools. Temperature (A) is irrelevant to injection; a polite request (C) is not an enforceable control; a more instruction-following model (D) can be more susceptible, not less."

**Sample 3 · Domain 8 — Tools and MCPs**

A team needs Claude to call an internal inventory service exposed as a REST API. They want the capability to be reusable across several Claude applications and maintained independently of any one app. Which approach best fits?

- A. Hard-code the inventory logic into each application's system prompt.
- B. Build an MCP server that exposes the inventory operations as tools so multiple Claude applications can connect to it.
- C. Paste the current inventory data into the context window on every request.
- D. Rely on a built-in tool, since built-in tools can reach any internal REST API.

**Answer: B.** "An MCP server exposes reusable tools that multiple Claude applications can share and that can be maintained independently. Hard-coding logic into prompts (A) is neither reusable nor maintainable; pasting data (C) gives no live access and wastes context; built-in tools (D) do not automatically reach arbitrary internal APIs."

Observations [inferred]:

- The guide publishes exactly 3 samples, covering Domains 2, 7, and 8. No sample covers Domains 1, 3, 4, 5, or 6.
- All three correct answers are B. Students should not read a pattern into this.
- Each correct answer names the purpose-built platform mechanism: Message Batches API, untrusted-input isolation plus guardrails or hooks, an MCP server.
- Distractors repeat three patterns: change the model (S1 D, S2 D), add a prompt-only instruction (S2 C, S3 A), and a lever that misses the stated constraint (S1 A/C, S2 A, S3 C/D).
- Each stem states the deciding constraint plainly: "Cost is the primary concern", "hidden text", "reusable across several Claude applications". Teaching students to underline that constraint is a direct strategy.

## How to prepare (Section 7, verbatim)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf]

> There is no single required course. Anthropic does not guarantee that any particular resource ensures a passing result. Candidates are encouraged to combine hands-on experience with the resources below:

- Study the exam blueprint in Section 6 and self-assess against each objective
- Review official Anthropic documentation for the Claude API, models, prompt engineering, Claude Code, Skills, and MCP
- Build and operate at least one Claude application that exercises the API, integrates one or more tools, applies basic prompt and context engineering, and includes simple security and evaluation practices
- Practice the developer competencies: writing prompts and system instructions, building agents and workflows, configuring Claude Code, managing tokens and cost, implementing guardrails, and creating custom tools or MCP servers
- Complete the sample questions in Section 8 to familiarize yourself with item style

## Prep path

### Path overview

[source: https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations]

Title: "Claude Certified Developer - Foundations Prep Course". Price: "Register | FREE". The exam-prep index lists it as "5 Courses". [source: https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations] [source: https://anthropic-partners.skilljar.com/page/claude-certification-exam-prep-courses]

Tagline (verbatim):

> Learn to build production-grade applications, agents, and workflows on Claude, and to make engineering decisions that determine whether code holds up when real users are depending on it.

Description (verbatim):

> Most developers start by using Claude in a chat window or sending a few API calls; that works until the code must survive production. A prompt that looked solid can fail on an untested input, a tool call can break halfway, a stream can get interrupted, an agent can run past its budget. The decisions of how you structure prompts, define tools, manage context, and wire agents, determine whether a working prototype can become a system you can defend in a heightened leadership review.

> This course teaches the hands-on builder to operate Claude as a production system by building the engineering judgment that turns a prototype into something reliable, affordable, and controllable once deployed.

Path learning objectives (verbatim, "By the end of this course, you'll be able to:"):

- Explain how Claude works at the level that affects engineering decisions: tokens, the context window as a fixed budget, sampling and non-determinism, model tiers, and SDK versus REST access patterns
- Write production-ready prompts using system prompts, XML, few-shot, and constraints, and diagnose why a prompt underperforms when first-pass results miss the mark
- Define and implement tool schemas, construct the tool-use loop, and manage extended thinking across multi-turn work
- Build a production agent with the right orchestration, memory scope, and human-in-the-loop checkpoints for irreversible actions
- Run Claude Code under a permission model, give it durable project context, package workflows as Skills and plugins, and connect Claude to enterprise systems through MCP without leaking credentials
- Build eval suites that define "done," create test and tracing layers that catch regressions, and keep a system inside its cost, latency, and reliability budget
- Secure an integration against prompt injection, untrusted input, and exposed secrets so a deployment survives a security or compliance review
- Package a working build into a reusable accelerator, choose where a workload runs across platforms, and contribute assets back into shared infrastructure

Prerequisites (verbatim): "Before starting this course, we recommend you complete: Claude 101, Claude Code 101, Claude Platform 101, Claude Code in Action, AI Fluency: Framework & Foundations, Building with the Claude API, Introduction to Model Context Protocol, Model Context Protocol: Advanced Topics, and AI Capabilities and Limitations."

Who this is for (verbatim): "The Claude Certified Developer Foundations course is for the hands-on builder who writes production code, builds agents, runs evals, and decides whether a customer's code makes it to production."

### Lessons

| # | Lesson | Minutes | Card description (verbatim) | Likely domains [inferred] |
|---|--------|---------|------------------------------|---------------------------|
| 1 | MSO Foundations | 57 | "Learn the model fundamentals and technical foundations the rest of the Developer Foundations course builds on." | D5 ("MSO" matches Model Selection and Optimization) |
| 2 | Production-Grade Prompting, Agents & Tool Use | 209 | "Build your first production integration on Claude, with reliable prompts, tools, context management, and agent loops." | D6, D1, D8 (8.1), D2 (2.3 API mechanics) |
| 3 | Claude Code, MCP & Integration | 142 | "Learn to make a working Claude integration configurable, shareable, and safe to connect to real systems." | D3, D2 (2.6), D8 (8.2, 8.3), D7 (7.3, 7.4) |
| 4 | Production Engineering, Evals & Security | 211 | "Learn to take an agent that works in development and prove it holds up under real production traffic." | D4, D7, D5 (5.4), D6 (6.3) |
| 5 | Accelerators & IP Contribution | 155 | "Package a build that works into one that survives reuse, review, and deployment beyond the engagement that created it." | D2 (2.2, 2.3, 2.6) |

Titles, minutes, descriptions: [source: https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations]. Total 774 minutes (about 12.9 hours). [inferred]

Lesson pages show "About this course" and learning objectives publicly. Module lists sit behind Skilljar sign-in. Lesson 4 shows an empty "About this course" block. [source: https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/production-engineering-evals-security]

#### Lesson 1: MSO Foundations (57 min)

[source: https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/mso-foundations]

> Before writing a line of code that calls Claude, it helps to know what the right vocabulary is and why they matter for production. This module covers how the context window behaves under load, why non-determinism changes how you test, and how model choice and reasoning mode compound into cost and quality decisions that are hard to reverse later. It closes with the technical access layer: SDKs, REST, streaming, and async patterns.

- Explain what a token is, how the context window works as a fixed budget, why sampling makes outputs vary, and what non-determinism means for testing and evals
- Describe the Claude model family and its capability tiers, and distinguish choosing a model from enabling a reasoning mode such as extended thinking
- Choose between zero-shot, one-shot, and multi-shot prompting, and weigh the cost and quality trade-off of adding examples
- Describe how a developer accesses Claude: SDK versus raw REST, synchronous versus streaming responses, and asynchronous patterns for high-volume work

#### Lesson 2: Production-Grade Prompting, Agents & Tool Use (209 min)

[source: https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/production-grade-prompting-agents-tool-use]

> Writing code that uses Claude is different from using Claude to write code. Each topic in this module addresses a specific failure mode: a prompt that looked solid but breaks on real input, a stream that fails partway through, an agent that runs past its budget, and an action that turns out to be irreversible. Learning to identify and avoid these failure modes early is what makes a Claude integration reliable and affordable in production.

- Write production-ready prompts using system prompts, XML tags, few-shot examples, and output constraints, and diagnose why a prompt underperforms when first-pass results miss the mark
- Decide when to enable extended thinking, set a thinking budget, and handle thinking blocks correctly across tool-use turns
- Define and implement a tool schema that Claude selects correctly, construct the tool-use loop, handle multi-turn message blocks, and distinguish when to use a single tool call versus multiple parallel calls
- Consume a streamed response, assemble streamed events into complete content blocks, and recover cleanly when a stream is interrupted partway through
- Apply context engineering techniques including managing the context window, compacting, clearing history between, and subagent handoffs, to keep multi-turn agent sessions within budget without losing task continuity
- Build a production agent by choosing between workflow and agent patterns, wiring tools and context into a working loop, selecting a wiring path that fits your deployment constraints, and adding human-in-the-loop (HITL) checkpoints where actions are irreversible
- Manage agent memory across sessions using persistent storage patterns and choosing the right memory scope so that agent state survives across turns without inflating context cost
- Understand sending images and PDFs to Claude using the correct message block structure, apply the Files API for reusable assets, and submit high-volume workloads using the Message Batches API so they complete asynchronously

#### Lesson 3: Claude Code, MCP & Integration (142 min)

[source: https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/claude-code-mcp-integration]

> Claude Code is your terminal-native development partner. Building on the prior API foundations, this module covers adding a permission layer, a configuration system, and team-oriented sharing features, it then covers using the MCP protocol to connect Claude securely to external and enterprise systems. Each topic teaches a configuration decision that may feel safe on your own machine but could become a failure when someone else runs it.

- Run Claude Code through the explore, plan, and code loop, and select a permission mode that matches the risk level of the work, so the agent stays productive without being granted more authority than the task requires
- Read AI-generated code, review output with calibrated trust, and place a human review gate where the cost of a wrong call is high
- Give Claude Code durable project context using CLAUDE.md, rules instruction files, hooks, and subagents
- Package a workflow as Skills, custom commands, and a plugin, authoring a Skill once that runs the same way across Claude Code, the Messages API, and the Agent SDK
- Build an MCP server that makes tools, resources, and prompts available to Claude, select the transport that matches how the client and server communicate, and set the configuration scope that controls who loads it
- Connect Claude to enterprise systems, authenticate those connections using patterns a regulated customer will accept, and scope a code modernization engagement so the work holds up under a security review

#### Lesson 4: Production Engineering, Evals & Security (211 min)

[source: https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/production-engineering-evals-security]

- Write an eval suite that defines what "done" means for a Claude feature before you deploy it, pick the grading method that fits the task, and calibrate an LLM-as-judge scoring against human-labeled cases so the result is one you can defend
- Build a test and tracing layer that catches regressions at the unit, functional, integration, and end-to-end levels
- Create an application resilient to production failures by distinguishing retriable errors from terminal ones
- Keep a system inside its cost, latency, and reliability budget, including when work is spread across several coordinating agents, by instrumenting each call and reaching for parallel agents only when the task needs them
- Defend an integration against prompt injection, jailbreaks, untrusted input, scoped identity, exposed secrets, and data boundaries so the deployment survives a security or compliance review

#### Lesson 5: Accelerators & IP Contribution (155 min)

[source: https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/accelerators-ip-contribution]

Tagged "Topic: Partner practice". [source: https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations]

> A build that works once is often rebuilt from scratch on the next engagement. This module covers packaging finished code into something reusable, deployable, and defensible to people who did not write it. You will learn to turn a working solution into a reusable accelerator, contribute assets back into shared infrastructure, and choose where a workload runs so it holds up under review.

- Package a working solution as a reusable accelerator, whether that is a parameterized agent template, a configurable MCP server, or a portable eval suite, so the next engagement configures an asset rather than fully rebuilding it
- Contribute a tool, pattern, or fix back through the documented channels and prepare it so a maintainer can accept it, turning a private asset into shared infrastructure
- Choose where a Claude workload runs across the first-party API, Amazon Bedrock, Google Vertex AI, and third-party platforms, and version what ships so a model or prompt change does not silently break production
- Compare those platforms on latency, compliance, and cost so the choice is one a procurement and security team can sign off on
- Build an application that coordinates several Claude deployments into one workflow and scope it so the data and identity boundaries are held under a security or compliance review

### Prep time vs exam weight [inferred]

| Lesson | Share of 774 min | Mapped exam weight |
|--------|------------------|--------------------|
| 1 MSO Foundations | 7% | D5 = 16.8% |
| 2 Prompting, Agents & Tool Use | 27% | D1 + D6 + part of D8 + part of D2 ≈ 35% |
| 3 Claude Code, MCP & Integration | 18% | D3 + part of D8 + part of D2/D7 ≈ 14% |
| 4 Production Engineering, Evals & Security | 27% | D4 + D7 ≈ 11% |
| 5 Accelerators & IP Contribution | 20% | part of D2 ≈ 7% |

The official path under-weights Domain 5 (16.8% of the exam, 7% of prep time) and the generic engineering skills in Domain 2. It over-weights evals and Claude Code relative to their 2.6% and 3.1% blueprint weights. Lesson 5 is largely partner-practice content with thin blueprint coverage. A 2-hour course should over-index on D2 and D5 relative to the official path.

### Related official path

The Partner Academy "Claude Developer" learning path describes itself as: "Build, evaluate, and ship agents on Claude. 10 courses about 8 hours". Its "Before you start" text says: "If you already hold Claude Certified Developer - Foundations, skip this path, because it prepares you for that exam." Courses listed include AI Capabilities and Limitations, AI Fluency for Builders, Claude Platform & Model Foundations, Claude Platform 101, Claude Code 101, Claude Code in Action, Introduction to Model Context Protocol, Introduction to agent skills, and Introduction to subagents. [source: https://anthropic-partners.skilljar.com/path/claude-developer]

## Community material

- A web search on 2026-10-26 for CCDV-F returned only commercial practice banks and study guides (Udemy, Tutorials Dojo, SkillCertPro, open-exam-prep.com, claudecertifiedarchitects.com). None was fetched except Tutorials Dojo, which failed (F1). No first-hand pass reports surfaced. [unverified]
- Search snippets from third-party sites repeat the official figures (53 items, 120 minutes, 720, $125) and describe the items as scenario-based. Some snippets round weights differently (Applications and Integration "32%"). Treat the official guide as the only authority. [unverified]

## Open questions

- **Eligibility vs. course audience.** Only Claude Partner Network employees with a partner-domain email can register. Many O'Reilly learners will not be eligible to sit CCDV-F. The course framing should say this up front. [source: https://anthropic-partners.skilljar.com/page/certification-eligibility]
- **Cancellation window conflict.** Guide Section 10 (English and Japanese) says 24 hours. FAQ and Policies say 48 hours. The Policies page says the Terms and Conditions and Exam Policy override it. Teach 48 hours as the safe rule and flag the conflict? [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/faq-certifications] [source: https://anthropic-partners.skilljar.com/page/policies-certifications]
- **Scenario format.** The FAQ says "scenario-based multiple response questions". The guide lists no scenario bank, and all three samples are standalone single-answer items. The share of multiple-response items on a live form is unknown.
- **Unscored items.** Weights apply to "scored items". The guide does not say whether any of the 53 items are unscored pretest items.
- **Eval coverage.** Eval design appears in Sections 2–4 of the guide and in prep Lesson 4, but no blueprint skill names it. Decide how much course time evals deserve against a 2.6% domain.
- **Fast-moving terms.** Skills name fast mode, adaptive thinking, effort levels, auto-mode, cache check-pointing, Agent Memory, and managed (Anthropic-hosted) agents. Each needs a current-docs check in a separate research file before slides cite specifics.
- **Prep module detail.** Sub-lesson lists require a partner Skilljar account. An enrolled account would allow an exact lesson-to-skill map.
