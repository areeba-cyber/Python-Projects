from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("AQ.Ab8RN6L9-mVY2anp0EPBdVCB2w34na3kDMKBuFjO9m_ie15a_Q"))

for model in client.models.list():
    print(model.name)