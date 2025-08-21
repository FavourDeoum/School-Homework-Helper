from services.gemini_api import ask_gemini
from config.prompts_english import ENGLISH_PROMPT

def ask_english_question(question, difficulty):
    """
    Handles English questions by calling the Gemini API with a specific prompt.
    """
    prompt = ENGLISH_PROMPT
    full_prompt = f"{prompt}\n\nDifficulty: {difficulty}"
    return ask_gemini(full_prompt, question)
