from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=API_KEY)

BASE_PROMPT = """
You are a JSON-only generator.

CRITICAL RULES:
1. Output ONLY valid JSON
2. No extra text
3. No markdown
4. No comments

Schema:
{
  "topic": string,
  "steps": array of strings,
  "common_mistakes": array of strings
}

Task:
Explain API setup.
"""

def get_structured_output(max_retries=2):
    for attempt in range(max_retries):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=BASE_PROMPT
        )

        raw = response.text.strip()

        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            print(f"⚠️ JSON failed, retrying... ({attempt+1})")

    raise ValueError("Model failed to produce valid JSON")

data = get_structured_output()
print(data)
