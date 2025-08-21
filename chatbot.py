from openai import OpenAI
import os
from dotenv import load_dotenv
from prompts import AI_TEACHER

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
base_url="https://generativelanguage.googleapis.com/v1beta/openai"

client = OpenAI(base_url=base_url, api_key=api_key)

def ai_chatbot(message, history):
    messages = [{"role": "system", "content": AI_TEACHER}]
    messages.extend(history)
    messages.append({"role": "user", "content": message})
    response = client.chat.completions.create(model="gemini-2.5-flash", messages=messages)
    ai_response = response.choices[0].message.content
    return ai_response