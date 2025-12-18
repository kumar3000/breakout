from google import genai
import os
from dotenv import load_dotenv

file_path = 'ingredients.txt'
bad_ings = [] # bad_ingredients

# Load env vars from local files (Windows-friendly).
# - `.env` is the common default
# - `GEMINI_API_KEY.env` kept for backward compatibility with this repo
load_dotenv()
load_dotenv("GEMINI_API_KEY.env")

# Create a list of banned ingredients
with open(file_path, 'r') as file:
    for line in file:
        bad_ings.append(line.strip())

# Gemini Query
api_key = os.getenv("GEMINI_API_KEY")
if not api_key or api_key.strip().lower() in {"your_key_here", "changeme", "replace_me"}:
    raise RuntimeError(
        "Missing GEMINI_API_KEY. Set it in your shell or create a .env file with:\n"
        "GEMINI_API_KEY=your_key_here"
    )

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is the capital of France?"
)

print(response.text)