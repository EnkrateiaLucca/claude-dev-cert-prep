# /// script
# requires-python = ">=3.12"
# dependencies = ["anthropic"]
# ///

import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude",
        }
    ],
)
for block in message.content:
    if block.type == "text":
        print(block.text)