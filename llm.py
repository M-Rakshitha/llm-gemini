import json
from google import genai
from dotenv import load_dotenv
load_dotenv()

client = genai.Client()
resume = """
Software Engineer with experience in Python, AWS, and backend development.
Built APIs and worked on data pipelines.
"""
prompt = f"""
You are a strict resume reviewer.

Rules:
- Be critical
- No generic answers
- Give specific suggestions

Return output in JSON:
{{
  "strengths": [],
  "weaknesses": [],
  "suggestions": []
}}

Resume:
{resume}
"""

response = client.models.generate_content(
    model="gemini-3-flash-preview", 
    contents=prompt
)
clean_text = response.text.strip()

if "```" in clean_text:
    clean_text = clean_text.split("```")[1]
    clean_text = clean_text.replace("json", "").strip()

try:
    data = json.loads(clean_text)
    for s in data["strengths"]:
      print("-", s)
except json.JSONDecodeError:
    print("Failed to parse JSON:")
    print(clean_text)
