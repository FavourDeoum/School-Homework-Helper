from services.gemini_api import ask_gemini
from config.prompts import FRENCH_PROMPT

def ask_french_question(question, difficulty):
    """
    Handles French questions by calling the Gemini API with a specific prompt.
    """
    prompt = FRENCH_PROMPT
    # Append difficulty to the prompt.
    full_prompt = f"{prompt}\n\nDifficulty: {difficulty}"
    return ask_gemini(full_prompt, question)

