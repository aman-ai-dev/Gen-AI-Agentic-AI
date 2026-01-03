from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

# Create client
client = genai.Client(api_key=API_KEY)

# Fetch available models
models = client.models.list()

print("\nAvailable Models:\n")

for model in models:
    print(f"- {model.name}")
