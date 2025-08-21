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
        custom_config = genai.GenerationConfig(
            temperature=1.2,
            max_output_tokens=6000,
            top_p=0.8,
            top_k=30,
            stop_sequences=["END"]
        )

        model = genai.GenerativeModel(
            model_name='gemini-2.5-flash',
            generation_config=custom_config,
            system_instruction=prompt
        )
        response = model.generate_content(f"{prompt}\n\nQuestion: {question}")
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
