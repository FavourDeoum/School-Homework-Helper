from services.gemini_api import ask_gemini
from config.prompts_biology import BIOLOGY_PROMPT

def ask_biology_question(question, difficulty):
    """
    Handles Biology questions by calling the Gemini API with a specific prompt.
    """
    prompt = BIOLOGY_PROMPT
    full_prompt = f"{prompt}\n\nDifficulty: {difficulty}"
    return ask_gemini(full_prompt, question)
