import os
from openai import OpenAI

client = OpenAI(
    api_key="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"
)

response = client.chat.completions.create(
    model = "gpt-4.1-nano-2025-04-14",
     messages=[
         {"role": "system", "content":"You are a fed up and sassy assistant who hates answering questions"},
         {"role": "user", "content":"What is the weather like today?"}
     ]
)

print(response)