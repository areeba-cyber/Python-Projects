import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(model="gemini-2.5-flash")

print("Gemini Chatbot")
print("Type 'exit' to quit.")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    response = chat.send_message(user)

    print("Gemini:", response.text)