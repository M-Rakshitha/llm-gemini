from google import genai
from dotenv import load_dotenv
load_dotenv()

client = genai.Client()
prompt = """
Classify feedback as Positive or Negative.

Examples:

Input: "I love this app"
Output: Positive

Input: "This is very slow"
Output: Negative

Input: "UI is confusing"
Output: Negative

Now classify:

Input: "The app is amazing"
Output:
"""

response = client.models.generate_content(
    model="gemini-3-flash-preview", 
    contents=prompt
)
print(response.text)
