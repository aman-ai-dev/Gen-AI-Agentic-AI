from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)


prompt = """
You are a strict JSON API.

Task:
Analyze sentiment of the given text.

Rules:
- Respond ONLY in valid JSON
- Do NOT include explanation or extra text
- Use this exact schema:

{
  "sentiment": "positive | negative | neutral",
  "confidence": number between 0 and 1
}

Text:
"I really like this course, but the pace is slow."
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

# Parse JSON safely
result = json.loads(response.text)

print(result)
print("Sentiment:", result["sentiment"])
print("Confidence:", result["confidence"])
