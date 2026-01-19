from google import genai
from dotenv import load_dotenv
import os
import json
import requests

# ------------------ ENV SETUP ------------------
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)

# ------------------ SYSTEM PROMPT ------------------
SYSTEM_PROMPT = """
SYSTEM INSTRUCTIONS (HIGH PRIORITY):

You are an AI assistant that works in steps.
You must follow this flow strictly:
START → PLAN (can repeat) → TOOL (if needed) → OUTPUT

Rules:
- ALWAYS return valid JSON only
- NO markdown
- NO explanations outside JSON
- One step at a time only
- Never reveal internal reasoning

JSON FORMAT:
{
  "step": "START" | "PLAN" | "TOOL" | "OUTPUT",
  "content": "string",
  "tool": "string",
  "input": "string"
}

Available tool:
- get_weather(city: str)

When tool output is provided, continue planning and then produce OUTPUT.
"""

# ------------------ TOOL ------------------
def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    r = requests.get(url)
    if r.status_code == 200:
        return f"The weather of {city} is {r.text}"
    return "Weather service error"

TOOLS = {
    "get_weather": get_weather
}

# ------------------ CONVERSATION STATE ------------------
user_query = input("👉 ")

history = f"""
{SYSTEM_PROMPT}

USER:
{user_query}
"""

# ------------------ AGENT LOOP ------------------
while True:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=history
    )

    raw_output = response.text.strip()
    print("🤖 RAW:", raw_output)

    # ---- JSON SAFETY ----
    try:
        data = json.loads(raw_output)
    except json.JSONDecodeError:
        print("❌ ERROR: Model returned invalid JSON")
        break

    step = data.get("step")

    # ---- PLAN ----
    if step == "PLAN":
        print("🧠", data.get("content"))
        history += "\nASSISTANT:\n" + raw_output
        continue

    # ---- TOOL CALL ----
    if step == "TOOL":
        tool_name = data.get("tool")
        tool_input = data.get("input")

        print(f"🛠️ Calling tool: {tool_name}({tool_input})")

        if tool_name not in TOOLS:
            print("❌ Unknown tool")
            break

        tool_result = TOOLS[tool_name](tool_input)

        observe = json.dumps({
            "step": "OBSERVE",
            "tool": tool_name,
            "input": tool_input,
            "output": tool_result
        })

        history += "\nASSISTANT:\n" + raw_output
        history += "\nOBSERVE:\n" + observe
        continue

    # ---- OUTPUT ----
    if step == "OUTPUT":
        print("✅ FINAL:", data.get("content"))
        break

    # ---- START or UNKNOWN ----
    history += "\nASSISTANT:\n" + raw_output
