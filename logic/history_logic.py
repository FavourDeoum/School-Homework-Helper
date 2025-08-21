from services.gemini_api import ask_gemini
from config.prompts_history import HISTORY_PROMPT

def ask_history_question(question, difficulty):
    """
    Handles History questions by calling the Gemini API with a specific prompt.
    """
    prompt = HISTORY_PROMPT
    full_prompt = f"{prompt}\n\nDifficulty: {difficulty}"
    return ask_gemini(full_prompt, question)
