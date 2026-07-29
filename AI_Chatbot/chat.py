import os
from google import genai

client = genai.Client(api_key="AQ.Ab8RN6JCoouf618uO3ySVfmOy6I6r0toUx78bLJ2Qi30fivUxQ")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="""
System:
You are a fed up and sassy assistant who hates answering questions.

User:
What is the weather like today?
""",
    temperature = 0.7
)

reply = response.text
print(reply)
