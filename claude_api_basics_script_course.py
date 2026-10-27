"""
claude_api_basics.py — a guided tour of the Claude Messages API
=================================================================

Sources (fetched 2026-10-27):
  - https://platform.claude.com/docs/en/intro
  - https://platform.claude.com/docs/en/build-with-claude/working-with-messages
  - https://platform.claude.com/docs/en/build-with-claude/effort
  - https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - https://platform.claude.com/docs/en/build-with-claude/thinking
  - https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons
  - https://platform.claude.com/docs/en/build-with-claude/prompt-caching

Setup:
    pip install anthropic
    export ANTHROPIC_API_KEY="sk-ant-..."
    python claude_api_basics.py            # runs every lesson
    python claude_api_basics.py 4          # runs only lesson 4

THE MENTAL MODEL (read this first)
----------------------------------
There is ONE endpoint:  POST https://api.anthropic.com/v1/messages

    REQUEST  (what you send)                RESPONSE (what comes back)
    ------------------------                --------------------------
    model, max_tokens                       content      -> list of blocks:
    system       (behavioral contract)                      text / tool_use / thinking
    messages     (user/assistant turns)     stop_reason  -> WHY generation stopped
    tools, tool_choice                      usage        -> token accounting
    output_config (effort, format)                          (incl. cache fields)
    thinking, cache_control

The API is STATELESS: it remembers nothing between calls. Every request
carries the whole conversation. "Memory" is just a Python list you keep
appending to and resending.

Every lesson below is a function. Each one changes ONE thing in the request
and shows you what changes in the response.
"""

import json
import sys

import anthropic

# The SDK reads ANTHROPIC_API_KEY from the environment. Under the hood every
# client.messages.create(...) call is a POST to /v1/messages with your
# x-api-key and an anthropic-version header; the SDK just builds the JSON.
client = anthropic.Anthropic()

# The intro page recommends starting with Claude Opus 5.5 for most workloads.
# Swap this string to try other models (e.g. "claude-sonnet-5-5",
# "claude-haiku-5-5"). NOTE: several behaviors in this script (thinking
# defaults, effort defaults, forced tool_choice) are model-specific; the
# comments describe what the docs say for Opus 5.5.
MODEL = "claude-opus-5-5"

# NOTE ON SAMPLING PARAMETERS: you will NOT see temperature / top_p / top_k
# here. Per the "Using the Messages API" page, non-default values return a
# 400 error on Claude 4.7+ models, and from API version 2026-10-21 any value
# does. Steer behavior with the prompt (and effort) instead.


# ---------------------------------------------------------------------------
# Helper: pretty-print the three parts of every response you care about.
# ---------------------------------------------------------------------------
def show(response, title=""):
    """Print content blocks, stop_reason, and usage for a response."""
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")

    # 1) CONTENT is a LIST of typed blocks, not a single string.
    #    Always iterate and branch on block.type.
    for i, block in enumerate(response.content):
        if block.type == "text":
            print(f"[{i}] text: {block.text}")
        elif block.type == "tool_use":
            # Claude is ASKING you to run a function. It does not run it.
            print(f"[{i}] tool_use: id={block.id} name={block.name} input={block.input}")
        elif block.type == "thinking":
            # The text is a SUMMARY of the reasoning (never raw chain of
            # thought) and is empty unless you opt in with display="summarized".
            # The `signature` carries the encrypted full reasoning.
            preview = block.thinking[:200] or "(empty — display is 'omitted')"
            print(f"[{i}] thinking: {preview}")
        elif block.type == "redacted_thinking":
            print(f"[{i}] redacted_thinking: (encrypted, pass back unchanged)")
        else:
            print(f"[{i}] {block.type}: {block}")

    # 2) STOP_REASON tells you what to do next (see lesson 8).
    print(f"\nstop_reason: {response.stop_reason}")

    # 3) USAGE is your bill. Cache fields may be absent/None when unused.
    u = response.usage
    print(
        "usage: "
        f"input={u.input_tokens}  output={u.output_tokens}  "
        f"cache_creation={getattr(u, 'cache_creation_input_tokens', None)}  "
        f"cache_read={getattr(u, 'cache_read_input_tokens', None)}"
    )


# ===========================================================================
# LESSON 1 — The minimal request: model + max_tokens + messages
# ===========================================================================
def lesson_1_minimal():
    """
    Three fields are required:
      - model:      which Claude to use
      - max_tokens: a HARD ceiling on output tokens. On thinking models the
                    thinking tokens count against this too, so don't set it
                    too low.
      - messages:   the conversation so far. The simplest one is a single
                    user turn whose `content` is a plain string.
    """
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": "In one sentence: what is an API?"}],
    )
    show(response, "LESSON 1 — minimal request")

    # The raw object is also useful to look at once:
    #   response.id, response.model, response.role == "assistant",
    #   response.type == "message"


# ===========================================================================
# LESSON 2 — `system`: the behavioral contract
# ===========================================================================
def lesson_2_system():
    """
    `system` is a TOP-LEVEL field, not a message. It sets the rules of the
    game for the whole conversation: role, tone, constraints, format.

    The `messages` list only holds user/assistant turns. (Newer models also
    accept role="system" messages mid-conversation for instructions that
    become relevant later — out of scope here.)
    """
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=(
            "You are a terse Portuguese tutor. Always answer in European "
            "Portuguese first, then give the English translation in brackets."
        ),
        messages=[{"role": "user", "content": "How do I say 'good morning'?"}],
    )
    show(response, "LESSON 2 — system prompt")


# ===========================================================================
# LESSON 3 — `messages` + statelessness
# ===========================================================================
def lesson_3_stateless_conversation():
    """
    Rules for `messages`:
      - Turns alternate: user, assistant, user, assistant, ...
      - `content` can be a string (shorthand) OR a list of content blocks:
            [{"type": "text", "text": "..."},
             {"type": "image", "source": {...}},
             {"type": "tool_result", ...}]
      - The API stores NOTHING. To continue a conversation you append
        Claude's reply to your list and resend the WHOLE list.
    """
    history = []  # <- this list IS the conversation's memory

    # Turn 1
    history.append({"role": "user", "content": "My name is Lucas. Remember it."})
    r1 = client.messages.create(model=MODEL, max_tokens=1024, messages=history)
    show(r1, "LESSON 3a — turn 1")

    # Append Claude's reply EXACTLY as received (the full content list,
    # including any thinking blocks). Don't rebuild or edit it: the thinking
    # docs say modified thinking blocks can be rejected, and append-only
    # histories also keep prompt caching effective.
    history.append({"role": "assistant", "content": r1.content})

    # Turn 2 — we resend turn 1 + Claude's answer + the new question
    history.append({"role": "user", "content": "What is my name?"})
    r2 = client.messages.create(model=MODEL, max_tokens=1024, messages=history)
    show(r2, "LESSON 3b — turn 2 (whole history resent)")

    # Proof of statelessness: send ONLY the last question, no history.
    r3 = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": "What is my name?"}],
    )
    show(r3, "LESSON 3c — same question WITHOUT history")
    # Compare r2.usage.input_tokens with r3.usage.input_tokens: you pay for
    # the whole history as input on every call. That cost is why lesson 7
    # (caching) exists.


# ===========================================================================
# LESSON 4 — `tools` + `tool_choice`: the agent loop
# ===========================================================================
WEATHER_TOOL = {
    "name": "get_weather",
    "description": "Get the current weather for a city.",
    # input_schema is JSON Schema describing the arguments Claude must supply.
    "input_schema": {
        "type": "object",
        "properties": {"city": {"type": "string", "description": "City name"}},
        "required": ["city"],
    },
}


def run_tool(name, tool_input):
    """YOUR code runs tools. Claude only requests them. This one is fake."""
    if name == "get_weather":
        return f"{tool_input['city']}: 21°C, sunny (fake data)"
    return f"Unknown tool {name}"


def lesson_4_tools():
    """
    The loop:
      1. Send tools + user message.
      2. If stop_reason == "tool_use", the response contains tool_use blocks.
      3. Run each tool yourself.
      4. Append the assistant turn (unchanged) AND a user turn containing ONLY
         tool_result blocks (one per tool_use, matched by tool_use_id).
         The stop-reasons page warns: adding text after tool_result blocks
         ends the assistant turn and can cause empty responses.
      5. Resend. Repeat until stop_reason != "tool_use".

    tool_choice options:
      {"type": "auto"}  -> Claude decides (default)
      {"type": "none"}  -> Claude may not call tools
      {"type": "any"} / {"type": "tool", "name": ...} -> force a call.
      Per the thinking docs, Opus 5.5, Sonnet 5.5, Fable 5.1 and Mythos 5.1
      REJECT forced tool use with a 400 error, so this lesson uses "auto".
    """
    messages = [{"role": "user", "content": "Should I bring a jacket in Lisbon today?"}]

    for step in range(5):  # safety cap on loop iterations
        response = client.messages.create(
            model=MODEL,
            max_tokens=2048,
            tools=[WEATHER_TOOL],
            tool_choice={"type": "auto"},
            messages=messages,
        )
        show(response, f"LESSON 4 — tool loop step {step}")

        if response.stop_reason != "tool_use":
            break  # Claude produced its final answer

        # Step 4a: keep the assistant turn exactly as returned
        messages.append({"role": "assistant", "content": response.content})

        # Step 4b: answer every tool_use with a tool_result
        tool_results = [
            {
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": run_tool(block.name, block.input),
            }
            for block in response.content
            if block.type == "tool_use"
        ]
        messages.append({"role": "user", "content": tool_results})

    # Contrast: same request with tool_choice "none" -> no tool_use blocks.
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        tools=[WEATHER_TOOL],
        tool_choice={"type": "none"},
        messages=[{"role": "user", "content": "Should I bring a jacket in Lisbon today?"}],
    )
    show(response, "LESSON 4 — tool_choice='none'")


# ===========================================================================
# LESSON 5 — `output_config`: effort and format
# ===========================================================================
def lesson_5a_effort():
    """
    output_config.effort controls how many tokens Claude spends on the WHOLE
    response (text, tool calls, and thinking). Levels from the effort page:
        low < medium < high < xhigh < max
    Defaults: "medium" on Opus 5.5 and Haiku 5.5, "high" on other models.
    It is a behavioral signal, NOT a hard budget — max_tokens is the hard cap.

    Watch: output_tokens should generally drop at "low". This is a tendency
    the docs describe, not a guarantee for any single prompt.
    """
    prompt = "Explain why the sky is blue."
    for level in ["low", "high"]:
        response = client.messages.create(
            model=MODEL,
            max_tokens=8000,
            output_config={"effort": level},
            messages=[{"role": "user", "content": prompt}],
        )
        show(response, f"LESSON 5a — effort={level}")


def lesson_5b_format():
    """
    output_config.format = structured outputs. You give a JSON Schema; the
    API uses constrained decoding so the text block is valid JSON matching it.

    Schema rules worth knowing (structured-outputs page): objects need
    "additionalProperties": False; numeric/string-length constraints such as
    minimum/maxLength are NOT supported (400 error).

    Edge cases where output may NOT match the schema:
      stop_reason == "refusal" or "max_tokens".
    So: check stop_reason before json.loads().
    """
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "email": {"type": "string"},
            "wants_demo": {"type": "boolean"},
        },
        "required": ["name", "email", "wants_demo"],
        "additionalProperties": False,
    }
    response = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        output_config={"format": {"type": "json_schema", "schema": schema}},
        messages=[
            {
                "role": "user",
                "content": "Extract: 'Hi, I'm Ana (ana@ex.pt), can we book a demo?'",
            }
        ],
    )
    show(response, "LESSON 5b — structured output")

    if response.stop_reason == "end_turn":
        text = next(b.text for b in response.content if b.type == "text")
        data = json.loads(text)  # a real Python dict now
        print("parsed:", data)

    # SDK shortcut (same docs page): client.messages.parse(...,
    # output_format=SomePydanticModel) returns response.parsed_output.


# ===========================================================================
# LESSON 6 — `thinking`
# ===========================================================================
def lesson_6_thinking():
    """
    Thinking = Claude reasons in `thinking` blocks BEFORE the text answer.

    Per the thinking docs, for Opus 5.5:
      - Adaptive thinking is ALWAYS on (Claude decides when/how much).
      - thinking={"type": "disabled"} returns a 400 error.
      - display defaults to "omitted" -> thinking blocks come back with an
        EMPTY `thinking` field (you're still billed for them).
      - To SEE a summary, set display="summarized".
    Effort (lesson 5a) is the main dial for HOW MUCH it thinks.

    Thinking tokens are billed as output and count toward max_tokens, so
    give it room. When you continue a conversation (especially tool loops),
    pass thinking blocks back unchanged — which lesson 3's
    `history.append({"role": "assistant", "content": r.content})` does.
    """
    response = client.messages.create(
        model=MODEL,
        max_tokens=16000,
        thinking={"type": "adaptive", "display": "summarized"},
        messages=[
            {"role": "user", "content": "What is the greatest common divisor of 1071 and 462?"}
        ],
    )
    show(response, "LESSON 6 — adaptive thinking, summarized")
    # If no thinking block appears: under adaptive mode Claude may skip
    # thinking on requests it judges simple. That is documented behavior.


# ===========================================================================
# LESSON 7 — `cache_control`: prompt caching
# ===========================================================================
def lesson_7_caching():
    """
    Because the API is stateless, you resend the same prefix (tools, system,
    early messages) every call. Prompt caching lets the server reuse that
    prefix instead of reprocessing it.

    Cache order is: tools -> system -> messages, up to the breakpoint.

    Two styles (prompt-caching page):
      - Automatic: top-level cache_control={"type": "ephemeral"}; the
        breakpoint is placed on the last cacheable block and moves forward
        as the conversation grows.  <- used below
      - Explicit: put {"cache_control": {"type": "ephemeral"}} on specific
        content blocks (max 4 breakpoints).
    Default TTL is 5 minutes; {"type": "ephemeral", "ttl": "1h"} for 1 hour.

    Pricing multipliers (docs): 5-min cache write = 1.25x base input,
    1-hour write = 2x, cache read = 0.1x.

    WHAT TO WATCH in usage:
      call 1 -> cache_creation_input_tokens > 0  (written to cache)
      call 2 -> cache_read_input_tokens     > 0  (read from cache)

    Caching only activates above a per-model minimum prompt length; below it
    the request runs uncached with NO error. I could not verify the exact
    minimum for Opus 5.5 — check the "Minimum cacheable prompt length" table
    on the prompt-caching page. The long system prompt below is padded to
    try to clear it; if both calls show 0 cache tokens, make it longer.

    Also from the docs: changing thinking config or top-level effort between
    calls invalidates the cache — keep those constant within a cached session.
    """
    long_reference = "Reference handbook paragraph about road-safety statistics. " * 600

    for call in (1, 2):
        response = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            cache_control={"type": "ephemeral"},  # automatic caching
            system=f"You answer questions using this handbook:\n{long_reference}",
            messages=[{"role": "user", "content": "Summarize the handbook in 10 words."}],
        )
        show(response, f"LESSON 7 — caching, call {call}")


# ===========================================================================
# LESSON 8 — `stop_reason`: always branch on it
# ===========================================================================
def lesson_8_stop_reasons():
    """
    stop_reason values (handling-stop-reasons page):
      end_turn                      -> finished naturally; use it
      max_tokens                    -> truncated; raise limit or continue
      stop_sequence                 -> hit one of your stop_sequences
      tool_use                      -> run tools, send tool_result (lesson 4)
      pause_turn                    -> server-tool loop paused; resend as-is
      refusal                       -> declined; see response.stop_details
      model_context_window_exceeded -> filled the context window; truncated

    stop_reason is NOT an error. Errors are HTTP 4xx/5xx and raise
    exceptions (anthropic.APIStatusError) — handle those separately.

    Below we force "max_tokens" with a tiny limit. With always-on thinking,
    the limit may be consumed before any text is produced — itself a nice
    illustration of why max_tokens must leave room for thinking.
    """
    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=20,
            messages=[{"role": "user", "content": "Write a 500-word essay on bridges."}],
        )
        show(response, "LESSON 8 — forcing max_tokens")

        match response.stop_reason:
            case "end_turn":
                print("-> complete answer")
            case "max_tokens" | "model_context_window_exceeded":
                print("-> TRUNCATED: don't treat this as a full answer")
            case "tool_use":
                print("-> go run the tools")
            case "refusal":
                print("-> refused; details:", getattr(response, "stop_details", None))
            case other:
                print("-> other stop reason:", other)

    except anthropic.APIStatusError as e:
        # e.g. 400 for an invalid parameter combination, 429 for rate limits
        print(f"HTTP error {e.status_code}: {e.message}")


# ---------------------------------------------------------------------------
LESSONS = {
    "1": lesson_1_minimal,
    "2": lesson_2_system,
    "3": lesson_3_stateless_conversation,
    "4": lesson_4_tools,
    "5a": lesson_5a_effort,
    "5b": lesson_5b_format,
    "6": lesson_6_thinking,
    "7": lesson_7_caching,
    "8": lesson_8_stop_reasons,
}

if __name__ == "__main__":
    selected = sys.argv[1:] or list(LESSONS)
    # "5" runs both 5a and 5b
    expanded = []
    for key in selected:
        expanded += [k for k in LESSONS if k == key or k.startswith(key)]
    for key in expanded:
        LESSONS[key]()