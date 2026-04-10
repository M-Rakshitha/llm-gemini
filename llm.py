import json
from google import genai
from dotenv import load_dotenv
from docx import Document
load_dotenv()

client = genai.Client()

def load_docx(file_path):
    doc = Document(file_path)
    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text
        
data = load_docx("data.docx")

question = input("Ask a question: ")

prompt = f"""
Answer the question based ONLY on the context below.

Context:
{data}

Question:
{question}

If the answer is not in the context, say "I don't know".
"""

response = client.models.generate_content(
    model="gemini-3-flash-preview", 
    contents=prompt
)
print(response.text)
