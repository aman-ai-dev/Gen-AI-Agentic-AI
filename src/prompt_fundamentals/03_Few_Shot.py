from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)

prompt = """
Classify sentiment as Positive or Negative.

Input: The camera quality is excellent
Output: Positive

Input: The app crashes every time
Output: Negative

Input: Customer support was helpful
Output:
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)
