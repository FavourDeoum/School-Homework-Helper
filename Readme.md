# Cameroon GCE Homework Helper

An AI-powered homework assistant for Cameroon GCE students. This app helps users with Mathematics, English, French, Biology, and History questions, providing clear explanations, study tips, and exam strategies.

## Features
- Chat-based interface for asking homework questions
- Subject-specific AI prompts for accurate, helpful answers
- Supports GCE O-Level and A-Level difficulty
- Customizable study resources and tips
- Beautiful, modern UI with Streamlit

## How It Works
- Select your subject and difficulty level from the sidebar
- Type your question in the chat
- Get instant, AI-generated answers tailored to your needs

## Technologies Used
- Python 3
- Streamlit
- Google Gemini API (Generative AI)

## Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/FavourDeoum/School-Homework-Helper.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your Gemini API key to a `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## File Structure
```
app.py                # Main Streamlit app
config/prompts.py     # French prompt
config/prompts_math.py, prompts_english.py, prompts_biology.py, prompts_history.py # Other subject prompts
logic/                # Subject logic files
services/gemini_api.py # Gemini API integration
```

## Contributing
Pull requests and suggestions are welcome!

## License
MIT

---
Made for Cameroon GCE students. Study smart, achieve more!
