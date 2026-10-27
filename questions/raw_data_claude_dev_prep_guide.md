Developer · Module 5

Accelerators and IP Contribution

01
Module Introduction
Orientation

02
Packaging for Reuse
Teaching
Watch Out
Checkpoint

03
Contributing Back
Teaching
Watch Out
Checkpoint

04
Requirements & Lifecycle
Teaching
Checkpoint
Teaching
Checkpoint

05
Deployment & Versioning
Teaching
Watch Out
Checkpoint

06
Comparing Platforms
Teaching
Watch Out
Checkpoint

07
Trust Boundaries
Teaching
Watch Out
Checkpoint

08
Cumulative Task
Diagnose
Assemble

09
Key Takeaways
Recap
Glossary
Module Complete
Progress
4%
Reset progress
Teaching
Packaging for Reuse
·
16 min
Packaging a working build so the next engagement starts from an asset
You finished the prior modules with a build that runs: an agent loop, a configured MCP server, an eval that proves that the prompt works. The most time-consuming and expensive thing on a team is the engineering time that gets spent rebuilding the same thing for the next customer.

What an accelerator does: keep the reusable parts and separate out the rest
An accelerator is a solution packaged so future engagements start from a working foundation rather than from a blank repository. In blueprint terms, this is packaging for reuse: separating engagement-specific code from the reusable core and parameterizing the rest. Take a working build, separate the parts that are customer-specific, and expose them as parameters with documented defaults. The asset then configures rather than gets entirely rewritten. Packaging for reuse while the build is fresh is cheaper than reconstructing the intent months later, when the person who knew why a value was hardcoded has moved on.

Most reusable work falls into different asset types, and each one packages differently
Most reusable work falls into one of three categories used throughout this module: a template, a configurable server, or a portable eval. Each type holds a different kind of work and needs to be packaged in its own way. Reaching for the wrong type can make an asset look reusable while still making it difficult to apply.

Asset type	What it bundles	What correct packaging requires
Agent Template	The system prompt, the tool schemas, and the loop structure from a working agent.	Pull the domain-specific values into configuration with documented defaults, so a new team sets the values rather than editing the loop.
MCP Server Package	The tools the server exposes, with their inputs and the scope the installing team controls.	Document each tool input and let the installing team set the scope, so the server installs into a new environment without code edits.
Eval Suite	The graded test set and the judge rubric that prove the asset works.	Ship the dataset and rubric together so a new team can run them in their own context and confirm the asset still works there. The same eval suite also acts as the gate at deployment. When you promote a new model version to production, run it against a pinned baseline score before the version goes live.
Shipping an agent as a set of loose scripts instead of a template is the most common version of the wrong approach. The scripts run, so they look reusable, but every customer-specific value is buried in a different file, and the next team copies and diverges them instead of configuring one asset.

Document both the code and the assumptions
Code describes behavior. Documentation covers what a future builder cannot reliably infer from reading the source: the assumptions the asset makes about its environment, the inputs it expects, the failure modes it already handles, and the eval that defines whether it still works. Without this, the next team treats the asset as a black box and rebuilds it.

Bundle the audit log as part of the package
A regulated customer's reviewer asks what data the asset touches, what identity it acts under, and what log it leaves. An accelerator without these passes a demo and stalls at the first security review. Treat the audit log as part of the package.

The packaging checklist
Keep this checklist next to the build while you package it. Each column is a decision you make once per asset.

Asset type	What to parameterize	What to document	What to bundle for audit
Agent template	Every value that changes per customer: prompts, paths, scopes, credentials by reference, and thresholds.	Environment assumptions, expected inputs, handled failure modes, and the eval that defines working.	The data touched, the identity acted under, and the log of what the asset did.
MCP Server	Scopes, credentials by reference, and per-customer paths.	Expected inputs per tool, scope boundaries, and handled failure modes.	The data touched, the identity acted under, and the log of what the asset did.
Eval Suite	Thresholds and dataset paths that change per customer or environment.	The rubric logic, what the scores mean, and the baseline the asset is pinned to.	The data touched, the identity acted under, and the log of what the asset did.
Handles well
Parameterizing while the build is fresh turns one delivery into an asset the next engagement configures in hours.

Adds cost or complexity
Separating generalizable from customer-specific parts and documenting assumptions adds real time to the first build.

Use a different approach
For a one-off a customer will never reuse, packaging overhead is not worth it: ship the build and move on.

← Previous
Screen 2 of 25
≡ CONTENTS
Next →Developer · Module 5

Accelerators and IP Contribution

01
Module Introduction
Orientation

02
Packaging for Reuse
Teaching
Watch Out
Checkpoint

03
Contributing Back
Teaching
Watch Out
Checkpoint

04
Requirements & Lifecycle
Teaching
Checkpoint
Teaching
Checkpoint

05
Deployment & Versioning
Teaching
Watch Out
Checkpoint

06
Comparing Platforms
Teaching
Watch Out
Checkpoint

07
Trust Boundaries
Teaching
Watch Out
Checkpoint

08
Cumulative Task
Diagnose
Assemble

09
Key Takeaways
Recap
Glossary
Module Complete
Progress
16%
Reset progress
Teaching
Contributing Back
·
12 min
Moving an asset from private reuse into shared infrastructure a maintainer accepts
You have already done most of the work that makes an asset shareable. When you packaged it for your own team to reuse, you pulled out the parameters, wrote down the assumptions, and bundled the eval. The parameters show the asset can be configured rather than rewritten. The documented assumptions tell the maintainer what environment the asset expects. The bundled eval gives them a way to confirm it still works. An asset packaged for internal reuse is already close to what a maintainer needs to accept it.

The contribution channel is designed to receive that packaged asset. It carries the version, the installation steps, and the components as a single unit, so a team that never spoke to you can install it and get the same working setup.

Match the contribution to the channel built for it
Contributing back means moving an asset from private reuse to shared infrastructure through a documented channel. Each channel is built for a specific kind of contribution. The Claude Cookbook is a GitHub repository of focused reference implementations. It is designed for self-contained single- or multi-pattern implementations demonstrated clearly and working end to end. Open-source MCP servers and tools each live in their own repository with their own contribution conventions. Sending a full multi-component application to the Cookbook is a mismatch. The repository is set up to review one focused pattern rather than an entire application, so a submission that large does not fit what reviewers are looking for and will stall. The first step is matching the contribution to the channel built for it. Putting a full application where a focused example belongs is one of the most common reasons a contribution never gets reviewed.

What makes verifying a contribution possible
A maintainer accepts a contribution they can verify. The bar is set by what they need to check, not by how clever the code is. Four things make that verification possible:

1The code does one thing. A sprawling contribution forces a reviewer to reconstruct your intent before evaluating it.
2An example shows it running. A reviewer should not have to build a harness to see the behavior.
3A test proves it works. A test lets a maintainer verify the result without reproducing the reasoning themselves.
4A short statement names the assumptions. Otherwise, the first failure becomes the maintainer's problem.
Rights and attribution come before technical review
Licensing and attribution decide whether a contribution can be accepted at all, which is why they come before the technical review. Code carried in from a customer engagement may have constraints on where it can go. Confirming you have the right to contribute it, and attributing anything you built on, is a gate the contribution must pass first. Skipping this is what turns a contribution into a problem the legal team must unwind later.

The example worked here is the customer service agent case. A reusable conversation-handling pattern, built during an engagement, gets stripped of customer specifics and prepared as a general example for the Cookbook. The contribution-back motion is shared across all three roles in this curriculum. Your job as the Developer is technical readiness: the focused code, the example, the test, the assumptions, and the rights check. The engagement context comes from the broader team.

The contribution-readiness reference
Channel	What a maintainer checks	Licensing and attribution	The example and test bar to clear
Cookbook for a focused example, or the tool or server's own repository for a tool or fix.	That the code does one thing and that they can read it in full.	Confirm that you have the right to contribute code from an engagement, with prior work attributed.	A runnable example plus a test that proves the behavior, not just a description of it.
Handles well
A packaged asset needs only the example, test, and rights check to become shared infrastructure others build on.

Adds cost or complexity
Clearing the maintainer bar and the licensing gate is real work on top of making the code run for you.

Use a different approach
When code carries an engagement licensing constraint you cannot clear, do not contribute it: escalate to the owner instead.

← Previous
Screen 5 of 25
≡ CONTENTS
Next →Developer · Module 5

Accelerators and IP Contribution

01
Module Introduction
Orientation

02
Packaging for Reuse
Teaching
Watch Out
Checkpoint

03
Contributing Back
Teaching
Watch Out
Checkpoint

04
Requirements & Lifecycle
Teaching
Checkpoint
Teaching
Checkpoint

05
Deployment & Versioning
Teaching
Watch Out
Checkpoint

06
Comparing Platforms
Teaching
Watch Out
Checkpoint

07
Trust Boundaries
Teaching
Watch Out
Checkpoint

08
Cumulative Task
Diagnose
Assemble

09
Key Takeaways
Recap
Glossary
Module Complete
Progress
36%
Reset progress
Teaching
Requirements & Lifecycle
·
8 min
Systems lifecycle for Claude applications
The requirements you just captured are the first phase of a longer arc. This screen names that arc as the systems lifecycle, so the deployment, versioning, and boundary work in the rest of this module sits in the right phase rather than arriving as unrelated tasks.

The lifecycle phases applied to a Claude application
A Claude application moves through the same lifecycle as any engineered system, with the model work mapped onto it:

1Requirements: capture functional and infrastructure needs
2Design: choose the platform, the model, and the trust boundaries
3Build: write the agent, tools, and prompts
4Test: evals, unit, integration, and end-to-end checks
5Deploy: pin the version, gate promotion on the eval
6Operate: instrument cost, latency, and errors; enforce guardrails
7Iterate: feed production findings back into requirements
The phases are the same ones the earlier modules taught one at a time. Identifying them as a lifecycle is what shows how they connect.

Gating between phases
A gate is a decision to move from one phase to the next, and it is where a regulated engagement keeps control. You do not move from design to build until the platform satisfies the residency requirement; you do not move from deploy toward full production until the new version clears the eval against the pinned baseline. Placing engineering work in the right phase, and refusing to skip a gate, is what keeps a Claude application reviewable.

Handles well
Placing each piece of engineering work in the lifecycle phase it belongs to, with a defined artifact and gate.

Adds cost or complexity
Gating between phases adds checkpoints a team under deadline is tempted to skip.

Use a different approach
A one-off experiment may collapse phases, but a regulated deployment cannot.

← Previous
Screen 10 of 25
≡ CONTENTS
Next →Checkpoint 4: place the work in the right phase
Try it now. Place each activity in the lifecycle phase it belongs to: requirements, design, test, deploy, operate.

(a) pinning the full model ID and keeping the prior version
requirements
design
test
deploy
operate
(b) gating promotion on the eval result before a version goes to production
requirements
design
test
deploy
operate
(c) deciding data must be processed in a specific region
requirements
design
test
deploy
operate
(d) instrumenting token cost and latency per call in production
requirements
design
test
deploy
operate
(e) choosing Amazon Bedrock because the customer holds its compliance posture there
requirements
design
test
deploy
operateDeveloper · Module 5

Accelerators and IP Contribution

01
Module Introduction
Orientation

02
Packaging for Reuse
Teaching
Watch Out
Checkpoint

03
Contributing Back
Teaching
Watch Out
Checkpoint

04
Requirements & Lifecycle
Teaching
Checkpoint
Teaching
Checkpoint

05
Deployment & Versioning
Teaching
Watch Out
Checkpoint

06
Comparing Platforms
Teaching
Watch Out
Checkpoint

07
Trust Boundaries
Teaching
Watch Out
Checkpoint

08
Cumulative Task
Diagnose
Assemble

09
Key Takeaways
Recap
Glossary
Module Complete
Progress
44%
Reset progress
Teaching
Deployment & Versioning
·
15 min
Choosing where a Claude workload runs and versioning what ships
A packaged asset and a contributed one are both merely code until something runs them. The asset now faces a different question: where it runs and how to lock its version, so an upstream change does not become an untracked change in production. That platform decision is rarely about technical merit alone. In practice, it is usually shaped by where the customer already has cloud infrastructure, identity management, and compliance agreements in place. The first question is usually about which platform the customer already trusts and operates on.

The customer's cloud usually determines the platform
The deployment platform is the environment where the Claude workload runs. The same model can run in several deployment environments, and the customer's existing cloud usually determines which one. The first-party Claude API is Anthropic's own environment and typically receives new features first. Claude Platform on AWS is accessed through the customer's AWS account using Anthropic's own model IDs and lifecycle; inference is Anthropic-operated, outside the AWS boundary. Amazon Bedrock offers two integrations: Claude in Amazon Bedrock uses the Messages API at /anthropic/v1/messages with broad feature parity; confirm any feature-specific requirements against the Bedrock documentation, as a features-not-supported list exists, while Claude on Amazon Bedrock (legacy) uses the InvokeModel/Converse APIs with ARN-versioned identifiers. Google Vertex AI does the same inside Google Cloud. Third-party platforms, such as Microsoft Foundry, embed Claude inside a product the customer already uses. Microsoft Foundry offers Claude in two hosting forms: Hosted on Azure (currently Claude Opus 4.8, Claude Sonnet 5, and Claude Haiku 4.5, with inference running end-to-end on Azure infrastructure, generally available) and Hosted on Anthropic (all other Foundry Claude models, with inference on Anthropic-operated infrastructure). Residency assumptions for regulated customers depend on the hosting form of the specific model. Confirm the hosting form and the current model split with Microsoft at build time.

Identity and data residency are important for security
Identity and data location are answered by the platform, not your code. Bedrock uses AWS identity and keeps data inside the customer's AWS boundary; Vertex uses Google Cloud identity and boundary. Both offer regional routing when residency is a constraint. Matching the platform to the customer's existing compliance agreement avoids a data-residency review from scratch.

Pin the version so an upstream model change is not a silent production change
Versioning is what keeps a model or prompt change from becoming a silent change in production. Every Claude model ID points to a specific model snapshot. Aliases such as Opus and Sonnet are convenient, but they evolve over time and may resolve to different versions across deployment platforms. A pinned full model ID resolves to a fixed snapshot. Pin the specific model version rather than the alias, so an upstream model update is a deliberate choice rather than a silent production change. Then version the prompt and the asset alongside the code. Finally, keep the prior version available so the regression can be rolled back. An unpinned deployment makes every upstream model update an untracked change to your output.

The first line follows a moving alias. The second pins the snapshot.

# Pre-4.6 example: a convenience alias can resolve to a new
# version without you knowing
model = "claude-haiku-4-5"

# Pre-4.6 pinned snapshot: the version is fixed until you change this line
model = "claude-haiku-4-5-20251001"
For Claude 4.6 and later, the model ID alone pins to a specific snapshot; for earlier models, the ID plus a date suffix is required. Verify the current convention at platform.claude.com at build time.

Promote a version through the eval
Gate promotion on the eval suite. Send a new version to a portion of traffic, compare against the pinned baseline, and promote or roll back on the result. This is where the eval stops being a one-time test and becomes the deployment gate.

The deployment-platform decision table
Platform	Identity and data model	When to choose it	How versioning is pinned
First-party Claude API	Anthropic identity and terms.	The customer has no binding cloud or residency constraint and wants the newest capabilities.	Pin the full model ID and keep the prior snapshot.
Claude Platform on AWS	Anthropic identity and terms, accessed through the customer's AWS account; inference is Anthropic-operated outside the AWS boundary. Model lifecycle follows Anthropic's deprecation schedule.	The customer is on AWS but wants Anthropic model IDs, lifecycle, and feature parity with the first-party API.	Pin using the same model ID format as the Claude API (for example, claude-opus-4-8). Lifecycle follows Anthropic's schedule. (Confirm at publish time.)
Claude in Amazon Bedrock	Messages API at /anthropic/v1/messages, broad feature parity with the first-party API; confirm feature-specific requirements against the Bedrock documentation. Data stays inside the customer's configured AWS boundary.	The customer is on AWS, wants broad feature parity with the first-party API (confirm feature-specific requirements), and holds a compliance posture there.	Pin the full model ID using the anthropic. prefix format. Partner retirement dates differ from Anthropic's schedule. Confirm at publish time.
Claude on Amazon Bedrock (legacy)	AWS identity and billing, InvokeModel/Converse APIs with ARN-versioned model identifiers.	The customer is on an existing Bedrock integration using InvokeModel or Converse and has not migrated to the Messages API.	Pin via ARN-versioned model identifiers per Bedrock's versioning controls.
Google Vertex AI	Google Cloud identity, Identity and Access Management (IAM), and billing, with regional or global endpoints for residency.	The customer is on Google Cloud and holds a compliance posture there.	Pin the full model ID before rollout using Vertex's model ID format. Partner retirement dates differ from Anthropic's schedule.
Third-party platform	The wrapping product's identity and billing model. Note: Claude in Microsoft Foundry offers two hosting forms: Hosted on Azure (currently Opus 4.8, Sonnet 5, and Haiku 4.5; inference end-to-end on Azure) and Hosted on Anthropic (all other Foundry Claude models). Confirm residency and compliance terms with Microsoft before selecting this path for a regulated customer.	The customer already runs the platform that embeds Claude.	Pin per the platform's versioning controls.
Handles well
Matching the platform to the customer cloud and pinning the version keeps a migration reviewable and a rollback possible.

Adds cost or complexity
Pinning, retaining prior versions, and gating promotion on the eval add release-process overhead to every deployment.

Use a different approach
For a throwaway prototype that never touches production, a moving alias is fine: pinning is for what ships.

← Previous
Screen 12 of 25
≡ CONTENTS
Next →The deployment that broke when the model alias moved
Setup
You shipped against the alias that pointed at the recommended version, because that was the convenient default and it gave you the latest model for free. It worked. Then the alias advanced, and what was free turned out to have a price.

This is a trace excerpt from a production log, the kind you would scroll back through after an incident. It shows the day the output shape changed and why there was nothing to roll back to.

The log

--:  deploy: model="opus"  status=ok
--:  alias advanced -> new opus version (no app change)
--:  parser: KeyError "summary" in response payload
--:  Error: output shape changed; downstream parse failed
--:  rollback attempted -> no pinned prior version retained
--:  incident: hotfix parser; root cause = unpinned deployment
Why it broke
The application never changed, but the alias did. No pinned prior version had been retained, so there was nothing to roll back to. The hotfix repaired the parser but left the unpinned deployment in place.

What to Watch Out for
An alias resolves to a moving target; a pinned full model ID is a fixed snapshot. Pin the full model ID so an upstream update is something you adopt on purpose. Keep the prior pinned version available so a regression is a rollback rather than a hotfix. Gate the new version through your eval before you promote it, so the output-shape change shows up in a test run instead of in production.Checkpoint 5: Match the deployment platform and version pin to each scenario
Try it now. A customer runs AWS with a data-residency requirement and needs to be able to roll back a model update. Select the one correct piece in each group below to assemble the minimal deployment configuration that satisfies both. Leave out what does not belong.

Platform Group
First-party API
Amazon Bedrock
Google Vertex AI
Identity Group
AWS identity reference
Anthropic API key
Model reference group
A pinned full model ID
A moving alias
Rollback Group
Retain the prior pinned version
No retention
Submit
Skip for now
Correct
Bedrock keeps identity and data inside the AWS boundary the customer already cleared, the pinned full Bedrock model ID (with the anthropic. prefix) makes an upstream change something you adopt deliberately, and retaining the prior version gives you a rollback target. That is the minimal set that satisfies both residency and rollback.Comparing platforms on latency, compliance, and cost so the choice survives review
In the last two screens you chose a platform and pinned its version. That choice was right for the customer's cloud, but "right for their cloud" is not yet an argument a procurement and security team will sign off on.

Measure latency from the customer's region
Latency depends on where the platform runs relative to the customer and on how access to new features is routed. A platform running in the customer's own cloud region can reduce round-trip time compared to a first-party endpoint located farther away. The trade-off is timing of access: the first-party API typically receives new capabilities before they reach other platforms. The number is only accurate when you measure it from the customer's actual region against their actual payload. A measurement from your laptop hides the round-trip penalty that appears once the workload runs where the customer is. Within Bedrock specifically, the choice between global and regional endpoints is also the primary residency control and can affect cost. You should measure from the customer's actual region against both options before committing.

Compliance often determines the platform
Compliance is often the dimension that ends the debate. A customer who already holds a certification on one cloud is unlikely to re-certify on another. Data residency is a rule that a customer's data must be processed in a specific country or region. Available compliance certifications and who can audit access differ by platform, and a regulated financial or healthcare customer treats these as pass-or-fail rather than as tradeoffs to balance. The first-party Claude API may not offer EU data residency; confirm current regional coverage at platform.claude.com, since EU-only residency typically requires Bedrock or Vertex AI; on third-party platforms such as Microsoft Foundry, hosting is per-model: Azure-hosted Foundry models run inference end-to-end on Azure infrastructure, while Anthropic-hosted Foundry models do not satisfy EU regional residency requirements. Residency must be confirmed per model and deployment with Microsoft. Raise the compliance constraint during scoping, or it surfaces at contract review after the work is done.

What drives total cost beyond the per-token rate
Per-token rates are broadly aligned across platforms; total cost moves on egress, platform fees, and integration effort. A lower token price can cost more in total once data transfer and integration are factored in. Instrument cost per call for each platform. Confirm the current pricing pages at scoping.

The cross-platform comparison reference
Dimension	How it differs by platform	How to measure it	Where each platform wins
Latency	A platform in the customer's region shortens the round trip, while the first-party API may reach new features first.	From the customer's actual region against their actual payload.	An in-region cloud platform wins on round-trip latency, while the first-party API is advantaged on earliest feature access.
Compliance	Data residency, certifications, and audit controls are determined by the deployment platform.	Against the customer's existing certification and residency requirements during scoping.	The cloud platform the customer has already certified wins, because it needs no re-certification.
Cost	Token price, data egress, platform fees, and integration effort all vary.	Total cost per call per platform, including egress and integration, rather than token price alone.	The platform with the lowest total cost for the actual workload wins, which is not always the cheapest token.
Coordinating several Claude deployments with the trust boundaries holding under review
The accelerators, deployments, and tradeoffs now come together in a single application. Connecting components multiplies the places where identity, secrets, and untrusted input can cross. The discipline is to identify every boundary before connecting anything.

Map which component does what before you connect them
A multi-component app coordinates more than one Claude capability into a single workflow. An API request might trigger a Claude Code task, which then reaches a customer system through an MCP server. Each component contributes a capability the others do not have. The challenge is that every connection between them creates a place where identity, secrets, and untrusted input can cross. Map which component does what before connecting anything.

The trust boundary is where data moves
The trust boundary is the point where data or instructions move from one deployment environment to another. It is exactly where the injection and access controls from the prior module apply. Content fetched by a Claude Code task is untrusted when it reaches the next component. The receiving component should treat it as data, rather than as instructions, following the same principle used throughout the security module. The core discipline here is to identify every seam as a boundary. Don't assume a component is trusted simply because it worked correctly on its own.

Least privilege applies to the whole application
Identity and least privilege, which means giving each component only the access its task needs and nothing more, apply to the application as a whole. Each component operates under an identity. The application is only as contained as its most privileged seam, which means a single component scoped too broadly becomes the weak point even when every other component is properly scoped. You scope each component to the least privilege its role in the workflow requires. This is what keeps a steered component from reaching beyond its intended task.

Scoping for a regulated review pulls the module together
A regulated review requires justifying audit logging, data-residency decisions, and permission controls across the full application. For regulated deployments, Bedrock and Vertex AI are typically the platforms that satisfy regional residency constraints. Confirm ZDR and HIPAA BAA eligibility for each component against the Anthropic Trust Center and platform.claude.com before scoping.

The multi-component integration map
Component	What it contributes	The trust boundary at its seam	The control that enforces it
First-party API	Orchestrates the workflow and holds the entry point.	The request entering the app from outside.	Input validation and the identity the call runs under.
Claude Code task	Runs the agentic work and may fetch external content.	Content it fetched, which is untrusted downstream.	Treat fetched content as data at the next seam.
MCP server	Reaches a customer system to read or act.	The system access it holds on the app's behalf.	Scope the server to least privilege and log the access.
Handles well
Naming every seam as a boundary and scoping each component to least privilege makes a multi-component app deployable under review.

Adds cost or complexity
Mapping seams, enforcing controls at each, and logging boundary crossings adds design and audit work to every integration.

Use a different approach
When a seam cannot be secured, do not ship around it: escalate to a human owner.Key takeaways
01
Package while the build is fresh.
An accelerator keeps the reusable logic, exposes the customer-specific parts as documented parameters, and bundles the eval and the audit log alongside the asset. Correct packaging produces an asset teams configure. The knowledge of what is customer-specific is most expensive to reconstruct after the people who held it have moved on.

02
A maintainer accepts what they can verify.
Moving an asset into shared infrastructure means matching it to the channel built for its shape, then clearing the review bar: focused code, a runnable example, a test, and a statement of assumptions, with licensing rights confirmed before the technical review. A contribution a reviewer cannot verify sits at the back of the queue. Readiness moves a private asset into shared infrastructure others build on.

03
Pin what ships.
Choose the deployment platform based on the customer's cloud and compliance posture, then pin the specific model version rather than the moving alias and keep the prior version available. An alias is like asking for the current edition of a book: convenient, but the text can change. Pinning cites a fixed edition, so an upstream model change is something you adopt deliberately rather than something that arrives overnight with no rollback path.

04
Measure the dimension that decides the placement.
A platform choice is defensible only when latency, compliance, and cost are measured: latency from the customer's region, compliance against their existing certification, and cost as the total per call rather than the token price alone. For regulated customers, compliance is usually pass-or-fail. Raising compliance as a constraint during scoping prevents it from rejecting the build later at contract review.

05
Mark every seam as a boundary.
A multi-component application is only as contained as its most privileged seam. Scope each component to the minimum access its role requires and treat every point where data crosses as a trust boundary. Fetched content is treated as data, not instructions. Trust at a component boundary must be explicitly established. It does not carry over from the component that sent the data. When a seam cannot be secured, it goes to a human owner rather than being shipped.

What comes next
You can now package a build into a reusable asset, contribute it back, place and version it on the right platform, defend that placement, and connect components together so the boundaries hold. That completes the build-to-deploy arc for this persona: from writing production code in the earlier modules to shipping assets a regulated customer can audit and a team can reuse.

Anthropic public references (time-sensitive)
ID	Source	Type	Used for
S1	platform.claude.com (Claude in Amazon Bedrock, Claude on Vertex AI)	Product documentation	Deployment platforms, identity and data models, residency routing, regional and global endpoints.
S2	platform.claude.com (Model IDs and versioning, Model deprecations)	Product documentation	Pinned model IDs, alias resolution, lifecycle and retirement, partner-set schedules.
S3	anthropic.com and the Anthropic GitHub organization (Cookbook)	Product and repository	Contribution channels, the Cookbook as a home for focused examples, contribution conventions.
S4	Building with the Claude API (Skilljar)	Course source	Eval datasets, graders, and the evaluation pipeline used as the deployment gate.
S5	Claude Code 101 In Action (Skilljar)	Course source	Claude Code agentic tasks and MCP server roles in a multi-component workflow.
System prompts, XML, few-shot, and output constraints
A prompt that works once in interactive use often breaks when it runs in production against untested inputs. The fix for this isn’t just adding more words, it is identifying which structural piece is missing from the prompt and adding that one piece. This section reviews how to read a failed output, then walks through the four techniques that produce the fixes.

Four techniques that give Claude a reliable output shape
When a first-pass response misses, the instinct is often to add more words to the prompt and run it again. However, that instinct can make the problem harder to isolate and rarely fixes it. Rewording changes how you say something but does not add to the structural piece of the prompt that’s missing. For example, if Claude is crossing the boundary between your instructions and your input data, clearer phrasing will not fix it, and if the output format keeps drifting, "please format this correctly" will not fix it either.

The failure mode tells you which of the four techniques is absent. Diagnose how your prompt is failing first, then add the specific technique that addresses that failure. The four techniques themselves are defined in full further down this screen.

What you observed	What the prompt is missing	Why this technique is the fix
The result comes back in the wrong shape: a sentence where you expected a label, prose where you expected JSON.	An output constraint. The prompt never specified the form, field names, or stopping point of the response.	An output constraint controls the form of the response independent of its content. Without one, Claude returns plausible text that the downstream parser was not built to accept.
The content is off: scope drifts, tone shifts, or Claude answers a wider question than you asked, and it gets worse deeper into the conversation.	A system prompt, or a more specific one. The behavioral contract was too vague to hold across turns.	The system prompt sets the rules that apply to every response regardless of the user turn. When it is underspecified, there is nothing holding role, scope, and format steady as the conversation runs on.
The task is right, but the structure is invented: Claude understood what to do and produced output in a shape you never asked for.	Few-shot examples. Claude cannot infer an exact structure from a description alone.	Few-shot examples show the pattern rather than describe it. One correct input-output pair gives Claude the exact shape to match, which a written instruction often fails to pin down.
Output is clean on the inputs you tested but breaks on a variant: an edge case, an unusual field, an input you did not anticipate.	A constraint covering the variant. The prompt handles the happy path and has no rule for the case the parser breaks on.	The prompt was validated against a narrow set of inputs. Naming the variant in the constraint, or adding an example that covers it, closes the gap the test inputs never exposed.
Diagnosing a classification prompt that returns the wrong output shape
The rule is simple: name the failure, add the one technique that matches it, and re-run it. If it still fails, diagnose again. When a prompt keeps getting longer with every pass, that’s the sign you’re skipping the diagnosis step and just adding words.

The pattern below is the first row of the table in action: a prompt that produces the right content in a shape the downstream code cannot accept. The classifier understands the task and returns the correct category, but the form of that answer varies from run to run, so the router that consumes it fails. The missing piece is an output constraint, and the fix pulls in two of the other techniques to lock the label set and show the format. The walkthrough moves from the bare prompt that causes the problem to the constrained version that resolves it.

Worked example: a classification prompt before and after
A developer needs Claude to classify support tickets into three categories: billing, technical, and escalation. The first prompt is a bare instruction with no constraint on the output:

System: "You are a support classifier. Classify the ticket."


User: <ticket>I was charged twice for the same month.</ticket>
Claude returns "Billing" on some runs, "billing" on others, and occasionally a full sentence like "This looks like a billing issue." The downstream router expects one of a fixed set of labels and breaks on the inconsistency.

Read this against the table above, this situation matches what is described in the first row: the output comes back in a shape the parser cannot accept, so the missing piece is an output constraint. Adding that constraint pulls in two more techniques, because locking the label set and showing the format are jobs those techniques do better than a written instruction can. Few-shot examples show Claude the exact label and casing to return, and XML tags keep those examples separate from the instruction so Claude does not read them as part of the task:

System: "You are a support classifier. Classify each ticket into exactly one of: BILLING, TECHNICAL, ESCALATION. Return only the label. No other text."

<sample_input>My account shows two charges for April.</sample_input>
<ideal_output>BILLING</ideal_output>

<sample_input>The API keeps returning a 429 error.</sample_input>
<ideal_output>TECHNICAL</ideal_output>

User: <ticket>I was charged twice for the same month.</ticket>
Three techniques are doing distinct work here. The system prompt sets the output contract: exactly one label from a fixed set, nothing else. The XML tags mark where each example ends and the next begins, so Claude does not read the examples as part of the instruction. The few-shot pairs show the exact casing and format rather than describing it. Together they produce a result consistent enough to route programmatically.

The table below shows how we can stack all the four techniques together, where the prompt should be simplified, and where we should diagnose before adding more before too many iterations.

Stack all four techniques	Stacking all four techniques against a clearly defined output contract. Tasks with well-specified formats and edge cases that can be covered by examples.
Simplify the prompt	Adding all four techniques to a simple task that only needs one. A "summarize this paragraph" prompt does not need few-shot examples and an output schema.
Diagnose before adding more	Prompts that are growing longer with each iteration rather than more precise. If you have re-prompted five times and the output is still wrong, diagnose the failure type before adding more text.
When to reach for each technique
Now, let’s understand more about each of these techniques and when each one applies:

System Prompts
XML Tags
Few-shot Examples
Output Constraints
System prompts carry the behavioral contract for the whole session. Write them once and treat them as your persistent instruction layer. They define Claude’s role, the output format, and any rules that must not change between conversations.

The iteration loop: Diagnosing before re-prompting
When a first-pass response misses the mark, the instinct is to add more words to the prompt and try again. That instinct almost always makes the problem harder to diagnose and rarely fixes it.

Instead, diagnose the problem first, and then re-prompt based on your findings. The failure type tells you which technique is missing:

Wrong format: This is caused due to a missing output constraint. The prompt never specified what shape the result should take.
Wrong content or scope drift: This is caused due to an underspecified system prompt; the behavioral contract was too vague to hold across conversations.
Correct task but hallucinated structure: This happens when few-shot examples are needed. Claude cannot infer the exact structure from a description alone.
Good output on simple inputs but breaks on edge cases: The prompt handles the happy path but has no constraint covering the variant the parser breaks on.
The fix is structural, not a matter of phrasing. For example, if Claude is ignoring a boundary between your instructions and your content, clearer wording will not fix it, and if the output format keeps drifting, saying "please format this correctly" will not fix it either. In each case, identify which of the four techniques is absent and add it.

Moving output control from the prompt into the API with structured outputs
Everything up to this point shapes the output by writing instructions into the prompt and hoping Claude follows them. That works most of the time, but the prompt is a request, so a model can still return a stray sentence, a wrong field name, or malformed JSON that breaks the parser downstream.

The Claude API has a separate mechanism that removes that gap for production code. It is called structured outputs, and instead of asking for a shape in words, you hand the API a JSON schema, and the model is constrained at generation time to produce output that matches it. This technique is constrained decoding: as Claude generates each token, the API only allows tokens that keep the output valid against your schema, so a response that violates the schema cannot be produced in the first place.

Structured outputs cover two situations that show up in real pipelines. Each one constrains a different part of what the model returns, and you can use them on their own or together in the same request.

JSON outputs constrain the final response. You set the output_config.format parameter with type json_schema and your schema, and Claude returns valid JSON in the response text that matches that schema every time. Reach for this when the model itself is producing the structured payload your code consumes, like extracting fields from a support ticket or formatting an API response, because it removes the parse-and-retry code you would otherwise write around every call.
Strict tool use constrains the inputs Claude passes to your tools. You set strict to true on a tool definition, and the arguments Claude sends to that tool are validated against the input schema before your code runs. Reach for this in agentic loops where a malformed tool argument would crash the function or trigger a wrong action; this helps guarantee the call your code receives already conforms to the contract you defined.
The reason this belongs in the production code and not just in the prompt is because of reliability under inputs you did not test. A prompt-level instruction to return only JSON holds on the cases you tried and then slips on an edge case you did not, which is the exact failure the earlier classification example walked through. A schema constraint does not slip, because the API enforces it on every token rather than trusting the model to remember the instruction. That moves output correctness from something you verify after the fact to something the API rules out before it happens.

Constraining generation has costs, and a developer choosing this in production needs to weigh them rather than enabling it everywhere by default. Below are some of those costs you must consider:

The first request on a new schema is slower. The API compiles your schema into a grammar before it can constrain output, and that compilation adds latency on the first call. Compiled grammars are cached for 24 hours from last use, so steady traffic on a stable schema pays the cost once, but a workload that changes schemas constantly pays it repeatedly.
Your input token count rises. When structured outputs are on, the API adds a system prompt describing the expected format, and that injected prompt is billed like any other input token. The increase is small per call, but it is worth knowing when you are estimating cost at volume.
A guaranteed schema is not a guaranteed success. Two cases still return output that does not match: a refusal, where the model declines for safety reasons and the response carries stop_reason refusal, and a truncation, where the response hits the max_tokens limit and stops mid-structure with stop_reason max_tokens. Your code still checks stop_reason rather than assuming every response parses.
It does not combine with message prefilling. JSON outputs and prefilling the assistant message are incompatible, so a pattern that starts the response for Claude and a pattern that constrains the whole response to a schema cannot run on the same request. Pick the one that fits the task.The prompt that grew longer instead of better
Setup
Even though a prompt looks ready for production, it can still produce quiet failures. Sometimes edge cases cause fields to go missing or constraints to be ignored; when this happens, it’s often because constraints weren’t specified precisely enough.

Six revision passes, each one longer than the last
The prompt that we used in the previous example is given below: a developer needs Claude to classify support tickets into three categories: Billing, technical, and escalation. The first prompt is a bare instruction:

System: "You are a support classifier. Classify the ticket."
User: <ticket>I was charged twice for the same month.</ticket>
The trace below shows a developer iterating on a classification prompt, and although each pass adds more words, the output keeps drifting. This pattern emerges when a developer adds to their prompt without regard to constraint specifications.

Pass	What was added	Output behavior
1	"Classify this ticket as billing, technical, or escalation."	Returns full sentences: "This appears to be a billing issue." Parser breaks.
2	Added "Be concise." and "Use only the category name."	Returns "Billing" capitalized sometimes, "billing" lowercase other times. Router breaks on case mismatch.
3	Added three paragraphs describing each category in detail.	Output correct on simple tickets. For ambiguous tickets, returns 'billing/technical' instead of a single label. Parser breaks on the slash.
4	Added "Never return two categories." and "If ambiguous, choose the most likely one."	Works on 80% of tickets. Fails on tickets that could reasonably fit two categories (e.g., 'I was charged but the feature also stopped working'). Here it returns a full explanation instead of a label.
5	Added two more paragraphs about edge cases and a reminder to be precise.	The verbose prompt is now producing verbose output, over 2,000 characters per call, as long, unfocused prompts tend to produce long, unfocused outputs. The model calibrates response length and style to match the input. Latency has increased significantly due to output length, but accuracy has not improved.
6	Replaced all instructions with a JSON schema and two few-shot examples showing exact input/output pairs	Returns {"category": "billing"} on every ticket. Parser works. Latency drops. Accuracy on ambiguous tickets matches Pass 4.
Two things went wrong across these six passes and they are worth identifying separately. Pass 4 is the diagnostic failure: the developer identified the wrong problem, added description instead of a constraint, and the output stayed broken. Pass 5 is the engineering failure: the prompt became verbose enough to induce a latency regression, and the model calibrates response length to match the input, generating over 2,000 characters per call, with no accuracy gain. The fix for both is the same structural move: an output constraint and two few-shot examples but recognizing that these are two different failures matters because the second one can appear even when the first one has been resolved. Here is the prompt with the output constraint and few-shot examples applied:

System: "You are a support classifier. Classify each ticket into exactly one of: BILLING, TECHNICAL, ESCALATION. Return only the label. No other text."

<sample_input>My account shows two charges for April.</sample_input>
<ideal_output>BILLING</ideal_output>

<sample_input>The API keeps returning a 429 error.</sample_input>
<ideal_output>TECHNICAL</ideal_output>

User: <ticket>I was charged twice for the same month.</ticket>
What to Watch Out for
Every pass made the prompt longer and none of them added the missing output constraint. The developer was describing the problem more precisely with each iteration, but Claude does not need a detailed description of what a billing ticket looks like, instead it needs to know that the only acceptable response is one word in all capital letters.

The fix is two lines: an output constraint specifying the exact format and a few-shot example covering the ambiguous case. The six-pass trace is a pattern to recognize early: if three re-prompts in a row have not worked, stop adding text and diagnose which technique is missing.