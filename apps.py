import streamlit as st
import time
from datetime import datetime
import uuid
from logic.french_logic import ask_french_question
from logic.math_logic import ask_math_question
from logic.english_logic import ask_english_question
from logic.biology_logic import ask_biology_question
from logic.history_logic import ask_history_question

# Page configuration - MUST be the first Streamlit command
st.set_page_config(
    page_title="Cameroon GCE Homework Helper",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for ChatGPT-style interface
def load_css():
    st.markdown("""
    <style>
    /* Main theme colors */
    :root {
        --primary-color: #1e3d59;
        --secondary-color: #f5c842;
        --accent-color: #ff6b35;
        --success-color: #2ecc71;
        --background-light: #f8f9fa;
        --text-dark: #2c3e50;
        --chat-user-bg: #007bff;
        --chat-bot-bg: #f1f3f4;
        --sidebar-bg: #ffffff;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container */
    .main .block-container {
        padding-top: 2rem;
        max-width: none;
    }
    
    /* Custom header */
    .main-header {
        background: linear-gradient(135deg, #1e3d59 0%, #f5c842 100%);
        padding: 1.5rem 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.2rem;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: var(--sidebar-bg);
        padding: 1rem;
    }
    
    .sidebar-header {
        background: linear-gradient(135deg, #1e3d59 0%, #f5c842 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    
    /* Subject buttons in sidebar */
    .subject-button {
        width: 100%;
        margin-bottom: 0.5rem;
        padding: 0.75rem 1rem;
        border: 2px solid transparent;
        border-radius: 8px;
        background: white;
        color: var(--text-dark);
        font-weight: 500;
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .subject-button:hover {
        border-color: var(--primary-color);
        background: var(--background-light);
        transform: translateY(-1px);
    }
    
    .subject-button.active {
        background: var(--primary-color);
        color: white;
        border-color: var(--primary-color);
    }

    .stats-card{
        color: var(--text-dark);
    }
    
    /* Chat container */
    .chat-container {
        height: 60vh;
        overflow-y: auto;
        padding: 1rem;
        background: white;
        border-radius: 15px;
        border: 1px solid #e1e5e9;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
    }
    
    .chat-container::-webkit-scrollbar {
        width: 6px;
    }
    
    .chat-container::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 3px;
    }
    
    .chat-container::-webkit-scrollbar-thumb {
        background: #c1c1c1;
        border-radius: 3px;
    }
    
    .chat-container::-webkit-scrollbar-thumb:hover {
        background: #a8a8a8;
    }
    
    /* Chat messages */
    .chat-message {
        display: flex;
        margin-bottom: 1rem;
        animation: fadeIn 0.3s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .chat-message.user {
        justify-content: flex-end;
    }
    
    .chat-message.bot {
        justify-content: flex-start;
    }
    
    .message-content {
        max-width: 70%;
        padding: 1rem 1.25rem;
        border-radius: 18px;
        position: relative;
        word-wrap: break-word;
    }
    
    .message-content.user {
        background: var(--chat-user-bg);
        color: white;
        border-bottom-right-radius: 4px;
        margin-left: 2rem;
    }
    
    .message-content.bot {
        background: var(--chat-bot-bg);
        color: var(--text-dark);
        border-bottom-left-radius: 4px;
        margin-right: 2rem;
        border: 1px solid #e1e5e9;
    }
    
    .message-avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        font-weight: bold;
        margin: 0 0.5rem;
    }
    
    .message-avatar.user {
        background: var(--chat-user-bg);
        color: white;
    }
    
    .message-avatar.bot {
        background: var(--primary-color);
        color: white;
    }
    
    .message-time {
        font-size: 0.75rem;
        color: black;
        margin-top: 0.25rem;
        opacity: 0.7;
    }
    
    /* Input area */
    
    
    .input-container:focus-within {
        border-color: var(--primary-color);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #1e3d59 0%, #f5c842 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(30, 61, 89, 0.3);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(30, 61, 89, 0.4);
    }
    
    .stButton > button:disabled {
        background: #6c757d;
        transform: none;
        box-shadow: none;
    }
    
    /* Welcome message */
    .welcome-message {
        text-align: center;
        color: #6c757d;
        font-style: italic;
        margin: 2rem 0;
        padding: 2rem;
        background: #f8f9fa;
        border-radius: 15px;
        border: 2px dashed #dee2e6;
    }
    
    .welcome-message h3 {
        color: var(--primary-color);
        margin-bottom: 1rem;
    }
    
    /* Loading indicator */
    .typing-indicator {
        display: flex;
        align-items: center;
        color: #666;
        font-style: italic;
        margin-left: 50px;
    }
    
    .typing-dots {
        display: inline-flex;
        margin-left: 0.5rem;
    }
    
    .typing-dots span {
        height: 8px;
        width: 8px;
        background: #666;
        border-radius: 50%;
        display: inline-block;
        margin: 0 1px;
        animation: typing 1.4s infinite ease-in-out;
    }
    
    .typing-dots span:nth-child(1) { animation-delay: -0.32s; }
    .typing-dots span:nth-child(2) { animation-delay: -0.16s; }
    
    @keyframes typing {
        0%, 80%, 100% { transform: scale(0.8); opacity: 0.5; }
        40% { transform: scale(1); opacity: 1; }
    }
    
    /* Stats cards */
    .stats-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid var(--primary-color);
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-header h1 { font-size: 1.8rem; }
        .message-content { max-width: 85%; }
        .chat-container { height: 50vh; }
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
def initialize_session_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'selected_subject' not in st.session_state:
        st.session_state.selected_subject = None
    if 'questions_count' not in st.session_state:
        st.session_state.questions_count = 0
    if 'subjects_used' not in st.session_state:
        st.session_state.subjects_used = set()
    if 'chat_session_id' not in st.session_state:
        st.session_state.chat_session_id = str(uuid.uuid4())

# Sidebar with subject selection
def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-header">
            <h2>📚 Subjects</h2>
            <p>Choose your subject area</p>
        </div>
        """, unsafe_allow_html=True)
        
        subjects = {
            "Mathematics": {"icon": "🧮", "description": "Algebra, Geometry, Calculus"},
            "English": {"icon": "📝", "description": "Grammar, Literature, Essays"},
            "French": {"icon": "🇫🇷", "description": "Grammar, Vocabulary, Literature"},
            "Biology": {"icon": "🧬", "description": "Cell Biology, Genetics, Ecology"},
            "History": {"icon": "🏛", "description": "World & Cameroon History"}
        }
        
        # Subject selection buttons
        for subject, info in subjects.items():
            if st.button(
                f"{info['icon']} {subject}",
                key=f"subject_{subject}",
                help=info['description'],
                use_container_width=True
            ):
                st.session_state.selected_subject = subject
                st.rerun()
        
        st.markdown("---")
        
        # Difficulty level selector
        st.markdown("### 📊 Difficulty Level")
        difficulty = st.selectbox(
            "",
            ["GCE O-Level (Forms 1-5)", "GCE A-Level (Lower & Upper Sixth)"],
            key="difficulty"
        )
        
        if st.session_state.selected_subject:
            st.markdown(f"""
            <div class="stats-card">
                <strong>Current Subject:</strong><br>
                {subjects[st.session_state.selected_subject]['icon']} {st.session_state.selected_subject}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Clear chat button
        if st.button("🗑 Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.session_state.questions_count = 0
            st.session_state.subjects_used = set()
            st.rerun()
        
        # Study resources
        with st.expander("📚 Study Resources"):
            st.markdown("""
            - *Past Papers*: GCE previous questions
            - *Syllabus*: Current curriculum guide
            - *Study Tips*: Effective learning strategies
            - *Practice Tests*: Self-assessment tools
            """)

# Header component
def render_header():
    if st.session_state.selected_subject:
        subjects = {
            "Mathematics": "🧮", "English": "📝", "French": "🇫🇷", 
            "Biology": "🧬", "History": "🏛"
        }
        subject_icon = subjects.get(st.session_state.selected_subject, "📚")
        st.markdown(f"""
        <div class="main-header">
            <h1>{subject_icon} {st.session_state.selected_subject} Homework Helper</h1>
            <p>Ask me anything about {st.session_state.selected_subject} - I'm here to help!</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="main-header">
            <h1>📚 Cameroon GCE Homework Helper</h1>
            <p>Your AI-powered tutor for all GCE subjects</p>
        </div>
        """, unsafe_allow_html=True)

# Chat message component
def render_message(message, is_user=True):
    message_class = "user" if is_user else "bot"
    avatar = "👤" if is_user else "🤖"
    
    timestamp = datetime.now().strftime("%H:%M")
    
    st.markdown(f"""
    <div class="chat-message {message_class}">
        <div class="message-avatar {message_class}">{avatar}</div>
        <div class="message-content {message_class}">
            {message}
            <div class="message-time">{timestamp}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Typing indicator
def show_typing_indicator():
    st.markdown("""
    <div class="typing-indicator">
        🤖 AI is thinking
        <div class="typing-dots">
            <span></span>
            <span></span>
            <span></span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Generate AI response (placeholder for Gemini API integration)
def generate_response(question, subject, difficulty):
    if subject == "French":
        return ask_french_question(question, difficulty)
    elif subject == "Mathematics":
        return ask_math_question(question, difficulty)
    elif subject == "English":
        return ask_english_question(question, difficulty)
    elif subject == "Biology":
        return ask_biology_question(question, difficulty)
    elif subject == "History":
        return ask_history_question(question, difficulty)
    else:
        return "I'd be happy to help with your question! Please provide more details so I can give you the best answer."
    
    # Simulate processing time
    time.sleep(2)
    
    
# Main chat interface
def render_chat_interface():
    if not st.session_state.selected_subject:
        st.markdown("""
        <div class="welcome-message">
            <h3>👋 Welcome to GCE Homework Helper!</h3>
            <p>Please select a subject from the sidebar to get started.</p>
            <p>I'm here to help you with Mathematics, English, French, Biology, and History!</p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Chat container
    with st.container():        
        
        for message in st.session_state.messages:
            render_message(message["content"], message["role"] == "user")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Input area
    with st.container():        
        user_input = st.chat_input("Type your question here...",)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Handle user input
    if (user_input) and user_input.strip():
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.questions_count += 1
        st.session_state.subjects_used.add(st.session_state.selected_subject)
        
        # Clear input
        st.session_state.user_input = ""
        
        # Show typing indicator
        with st.container():
            show_typing_indicator()
        
        # Generate and add AI response
        response = generate_response(
            user_input, 
            st.session_state.selected_subject,
            st.session_state.get('difficulty', 'GCE O-Level')
        )
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Rerun to update the chat
        st.rerun()

# Main application
def main():
    # Initialize session state
    initialize_session_state()
    
    # Load custom CSS
    load_css()
    
    # Render components
    render_sidebar()
    render_header()
    render_chat_interface()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6c757d; padding: 1rem;">
        🎓 <strong>Study Smart, Achieve More!</strong> | Made for Cameroon GCE Students
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()