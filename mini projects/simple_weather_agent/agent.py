from google import genai
from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)


def get_weather(city: str):
    url="https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather of {city} is {response.text}"
    
    return "Something went wrong"

available_tools = {
    "get_weather": get_weather
}

def main():
    user_querry = input("> ")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_querry
    )
    print(f"🤖: {response.text}")

main()