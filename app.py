import streamlit as st
import time
from datetime import datetime
import base64

# Page configuration - MUST be the first Streamlit command
st.set_page_config(
    page_title="Cameroon GCE Homework Helper",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
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
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom header */
    .main-header {
        background: linear-gradient(135deg, #1e3d59 0%, #f5c842 100%);
        padding: 2rem 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    /* Subject cards */
    .subject-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid var(--primary-color);
        margin: 1rem 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .subject-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 20px rgba(0,0,0,0.15);
    }
    
    /* Question input area */
    .question-container {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px dashed #dee2e6;
        margin: 1rem 0;
    }
    
    /* Response area */
    .response-container {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        border-left: 5px solid var(--success-color);
        margin: 1rem 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
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
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(30, 61, 89, 0.4);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #f8f9fa;
    }
    
    /* Success/Error messages */
    .success-msg {
        background: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 8px;
        border-left: 5px solid #28a745;
        margin: 1rem 0;
    }
    
    .error-msg {
        background: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 8px;
        border-left: 5px solid #dc3545;
        margin: 1rem 0;
    }
    
    /* Loading animation */
    .loading-container {
        text-align: center;
        padding: 2rem;
    }
    
    .loading-text {
        color: var(--primary-color);
        font-size: 1.1rem;
        margin-top: 1rem;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2rem;
        }
        .main-header p {
            font-size: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Professional header component
def render_header():
    st.markdown("""
    <div class="main-header">
        <h1>📚 Cameroon GCE Homework Helper</h1>
        <p>Your AI-powered tutor for Mathematics, English, French, Biology & History</p>
    </div>
    """, unsafe_allow_html=True)

# Subject selection with icons and descriptions
def render_subject_selector():
    st.markdown("### 📖 Choose Your Subject")
    
    subjects = {
        "Mathematics": {
            "icon": "🧮",
            "description": "Algebra, Geometry, Calculus, Statistics",
            "color": "#e74c3c"
        },
        "English": {
            "icon": "📝",
            "description": "Grammar, Literature, Essay Writing, Comprehension",
        },
        "French": {
            "icon": "🇫🇷",
            "description": "Grammar, Vocabulary, Conversation, Literature",
            "color": "#9b59b6"
        },
        "Biology": {
            "icon": "🧬",
            "description": "Cell Biology, Genetics, Ecology, Human Biology",
            "color": "#2ecc71"
        },
        "History": {
            "icon": "🏛️",
            "description": "World History, Cameroon History, Ancient Civilizations",
            "color": "#f39c12"
        }
    }
    
    # Create columns for subject cards
    cols = st.columns(3)
    selected_subject = None
    
    for i, (subject, info) in enumerate(subjects.items()):
        with cols[i % 3]:
            if st.button(f"{info['icon']} {subject}", key=f"subject_{subject}", use_container_width=True):
                selected_subject = subject
                st.session_state.selected_subject = subject
    
    # Display selected subject info
    if 'selected_subject' in st.session_state:
        subject_info = subjects[st.session_state.selected_subject]
        st.markdown(f"""
        <div class="subject-card">
            <h3>{subject_info['icon']} {st.session_state.selected_subject}</h3>
            <p><strong>Topics covered:</strong> {subject_info['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    return st.session_state.get('selected_subject', None)

# Professional question input area
def render_question_input(subject):
    st.markdown("### ❓ Ask Your Question")
    
    # Difficulty level selector
    col1, col2 = st.columns([1, 1])
    with col1:
        difficulty = st.selectbox(
            "📊 Select Difficulty Level",
            ["GCE O-Level (Forms 1-5)", "GCE A-Level (Lower & Upper Sixth)"],
            key="difficulty"
        )
    
    with col2:
        question_type = st.selectbox(
            "📋 Question Type",
            ["Homework Help", "Concept Explanation", "Practice Problems", "Exam Preparation"],
            key="question_type"
        )
    
    # Question input with placeholder
    placeholders = {
        "Mathematics": "Example: Solve for x in the equation 2x + 5 = 15, and explain each step...",
        "English": "Example: Explain the main themes in 'Things Fall Apart' by Chinua Achebe...",
        "French": "Example: Conjugate the verb 'avoir' in present tense and give examples...",
        "Biology": "Example: Explain the process of photosynthesis and its importance...",
        "History": "Example: Describe the major causes of World War I and its impact on Africa..."
    }
    
    st.markdown("""
    <div class="question-container">
        <p><strong>💡 Tip:</strong> Be specific about what you need help with. The more details you provide, the better I can assist you!</p>
    </div>
    """, unsafe_allow_html=True)
    
    question = st.text_area(
        "Type your question here:",
        placeholder=placeholders.get(subject, "Type your question here..."),
        height=120,
        key="question_input"
    )
    
    # Additional context
    with st.expander("🔧 Additional Context (Optional)"):
        context = st.text_area(
            "Provide any additional information, specific topics, or context:",
            placeholder="Example: This is for my upcoming exam, focus on step-by-step solutions...",
            height=80,
            key="additional_context"
        )
    
    return question, difficulty, question_type, st.session_state.get('additional_context', '')

# Loading animation component
def show_loading():
    with st.container():
        st.markdown("""
        <div class="loading-container">
            <div style="font-size: 3rem;">🤖</div>
            <div class="loading-text">Processing your question...</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Progress bar animation
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            progress_bar.progress(i + 1)

# Professional response display
def render_response(response, subject):
    st.markdown("### 💡 Your Answer")
    
    # Response container with subject-specific styling
    st.markdown(f"""
    <div class="response-container">
        <h4>📚 {subject} Solution</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Display the response
    st.markdown(response)
    
    # Action buttons
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("👍 Helpful", key="helpful"):
            st.success("Thank you for your feedback!")
    
    with col2:
        if st.button("👎 Not Helpful", key="not_helpful"):
            st.info("We'll improve our responses. Thank you!")
    
    with col3:
        if st.button("🔄 Ask Follow-up", key="follow_up"):
            st.session_state.show_follow_up = True
    
    with col4:
        if st.button("📤 Share", key="share"):
            st.info("Response copied to clipboard!")

# Sidebar with additional features
def render_sidebar():
    with st.sidebar:
        st.markdown("## 🎯 Quick Tools")
        
        # Study tips
        with st.expander("📖 Study Tips"):
            st.markdown("""
            - Break down complex problems into smaller steps
            - Practice regularly with different question types
            - Ask for explanations, not just answers
            - Review your mistakes to learn from them
            """)
        
        # GCE Resources
        with st.expander("📚 GCE Resources"):
            st.markdown("""
            - **Past Papers**: Practice with previous GCE questions
            - **Syllabus Guide**: Check current curriculum requirements
            - **Study Schedule**: Plan your revision effectively
            """)
        
        # Contact/Help
        with st.expander("❓ Need Help?"):
            st.markdown("""
            **Having issues?**
            - Check your internet connection
            - Refresh the page if needed
            - Contact your teacher for additional support
            """)
        
        # Session stats
        st.markdown("---")
        st.markdown("### 📊 Session Stats")
        questions_asked = st.session_state.get('questions_count', 0)
        st.metric("Questions Asked", questions_asked)
        st.metric("Subjects Covered", len(set(st.session_state.get('subjects_used', []))))

# Error handling component
def show_error(error_message):
    st.markdown(f"""
    <div class="error-msg">
        <strong>⚠️ Oops!</strong> {error_message}
    </div>
    """, unsafe_allow_html=True)

# Success message component
def show_success(success_message):
    st.markdown(f"""
    <div class="success-msg">
        <strong>✅ Success!</strong> {success_message}
    </div>
    """, unsafe_allow_html=True)

# Main application flow
def main():
    # Initialize session state
    if 'questions_count' not in st.session_state:
        st.session_state.questions_count = 0
    if 'subjects_used' not in st.session_state:
        st.session_state.subjects_used = []
    
    # Load custom CSS
    load_css()
    
    # Render components
    render_header()
    render_sidebar()
    
    # Main content area
    selected_subject = render_subject_selector()
    
    if selected_subject:
        question, difficulty, question_type, context = render_question_input(selected_subject)
        
        if question and st.button("🚀 Get Help", key="submit_question", use_container_width=True):
            # Update session stats
            st.session_state.questions_count += 1
            if selected_subject not in st.session_state.subjects_used:
                st.session_state.subjects_used.append(selected_subject)
            
            # Show loading animation
            show_loading()
            
            # Here you would integrate with your Gemini API
            # For demo purposes, showing a sample response
            sample_response = f"""
            **Subject**: {selected_subject}
            **Level**: {difficulty}
            **Type**: {question_type}
            
            ## Step-by-Step Solution:
            
            1. **Understanding the Question**: {question[:100]}...
            
            2. **Approach**: Based on the Cameroon GCE {difficulty} curriculum...
            
            3. **Solution**: [This is where your Gemini API response would appear]
            
            ## Key Points to Remember:
            - This concept is important for your GCE exams
            - Practice similar problems to reinforce learning
            - Review related topics in your textbook
            
            ## Additional Practice:
            Try solving similar problems and ask for help if needed!
            """
            
            render_response(sample_response, selected_subject)
            show_success("Your question has been processed successfully!")
    
    else:
        st.info("👆 Please select a subject to get started!")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6c757d; padding: 1rem;">
        Made with ❤️ for Cameroon GCE Students | 
        <strong>Study Smart, Achieve More!</strong>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()