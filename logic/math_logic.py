from services.gemini_api import ask_gemini
from config.prompts_math import MATH_PROMPT

def ask_math_question(question, difficulty):
    """
    Handles Mathematics questions by calling the Gemini API with a specific prompt.
    """
    prompt = MATH_PROMPT
    full_prompt = f"{prompt}\n\nDifficulty: {difficulty}"
    return ask_gemini(full_prompt, question)
