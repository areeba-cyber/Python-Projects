import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("AQ.Ab8RN6L9-mVY2anp0EPBdVCB2w34na3kDMKBuFjO9m_ie15a_Q"))

print("🤖 Gemini Terminal Chatbot")
print("Type 'exit' to quit.\n")

chat = client.chats.create(
    model="YOUR_TEXT_MODEL_HERE"
)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    try:
        response = chat.send_message(user_input)
        print(f"\nGemini: {response.text}\n")
    except Exception as e:
        print(f"\nError: {e}\n")