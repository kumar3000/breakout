from google import genai
import os
from dotenv import load_dotenv

ingredients = 'ingredients.txt'
bad_ings = [] # bad_ingredients

# Load env vars
load_dotenv("KEYS.env")

# Create a list of banned ingredients
with open(ingredients, 'r') as file:
    for line in file:
        bad_ings.append(line.strip())

api_key = os.getenv("GEMINI_API_KEY") # Get API key

# Failed to get API key or API key is invalid
if not api_key or api_key.strip().lower() in {"your_key_here", "changeme", "replace_me"}:
    raise RuntimeError(
        "Missing GEMINI_API_KEY. Set it in your shell or create a .env file with:\n"
        "GEMINI_API_KEY=your_key_here"
    )

# Query Gemini
client = genai.Client(api_key=api_key)
product = input("Product Name: ")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        ingredients,
        product,
        bad_ings,
        "Scan through the product ingredients and list any ingredients that are in the bad_ings list."
    ]
)

print(response.text)