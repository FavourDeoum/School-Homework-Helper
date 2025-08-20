import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load env vars
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to ask Gemini with subject-specific prompt
def ask_gemini(prompt, question):
    """
    Calls Gemini API with subject-specific prompt + question
    """
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(f"{prompt}\n\nQuestion: {question}")
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
