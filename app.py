import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
import time

# Page configuration
st.set_page_config(
    page_title="Gemini Apex AI",
    page_icon="💠",
    layout="wide"
)

# Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Ultra-Premium CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #05070a;
        color: #e0e0e0;
    }

    .stApp {
        background: radial-gradient(circle at top right, #1a1c24 0%, #05070a 100%);
    }

    /* Glassmorphism Containers */
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }

    .bubble {
        padding: 25px;
        border-radius: 24px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        animation: fadeIn 0.5s ease-out;
    }

    .user-bubble {
        background: rgba(255, 255, 255, 0.03);
        margin-left: 50px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    .ai-bubble {
        background: rgba(0, 242, 254, 0.05);
        margin-right: 50px;
        border-left: 4px solid #00f2fe;
        box-shadow: 0 8px 32px 0 rgba(0, 242, 254, 0.1);
    }

    .bubble:hover {
        transform: translateY(-2px);
        border: 1px solid rgba(0, 242, 254, 0.3);
    }

    /* Header Styling */
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
        letter-spacing: -2px;
    }

    .subtitle {
        text-align: center;
        color: #888;
        font-size: 1.1rem;
        margin-bottom: 50px;
    }

    /* Input Field Styling - FORCED VISIBILITY */
    .stTextInput > div > div > input {
        background: #1a1c24 !important;
        color: #ffffff !important;
        border-radius: 18px !important;
        border: 2px solid rgba(0, 242, 254, 0.2) !important;
        padding: 15px 25px !important;
        font-size: 1.1rem !important;
        transition: 0.3s !important;
    }

    /* Placeholder text visibility */
    .stTextInput > div > div > input::placeholder {
        color: rgba(255, 255, 255, 0.4) !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #00f2fe !important;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.2) !important;
    }

    /* Button Styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%) !important;
        color: white !important;
        border-radius: 15px !important;
        border: none !important;
        height: 55px !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        box-shadow: 0 10px 20px rgba(0, 242, 254, 0.2) !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 15px 30px rgba(0, 242, 254, 0.4) !important;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Sidebar Fixes */
    [data-testid="stSidebar"] {
        background-color: #0a0c10 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    </style>
""", unsafe_allow_html=True)

# Layout: Main Title
st.markdown('<h1 class="main-title">GEMINI APEX</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Next-Generation Neural Interface</p>', unsafe_allow_html=True)

if not api_key:
    st.error("⚠️ SYSTEM ERROR: GEMINI_API_KEY NOT FOUND")
    st.info("Please ensure your .env file contains a valid API key.")
else:
    # Initialize Gemini
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-flash-latest')

    # Session State for History
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Chat Container
    chat_placeholder = st.container()

    with chat_placeholder:
        for message in st.session_state.messages:
            role = message["role"]
            content = message["content"]
            if role == "user":
                st.markdown(f'<div class="bubble user-bubble"><b>YOU</b><br><div style="margin-top:10px; color:#ccc;">{content}</div></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="bubble ai-bubble"><b>GEMINI CORE</b><br><div style="margin-top:10px; color:#fff;">{content}</div></div>', unsafe_allow_html=True)

    # Floating Input area at the bottom
    st.markdown("<br><br>", unsafe_allow_html=True)
    with st.form(key='chat_form', clear_on_submit=True):
        cols = st.columns([0.85, 0.15])
        with cols[0]:
            user_input = st.text_input("", placeholder="Initialize query sequence...", key="input", label_visibility="collapsed")
        with cols[1]:
            submit_button = st.form_submit_button(label='EXECUTE')

    if submit_button and user_input:
        # Save user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Immediate display
        with chat_placeholder:
            st.markdown(f'<div class="bubble user-bubble"><b>YOU</b><br><div style="margin-top:10px; color:#ccc;">{user_input}</div></div>', unsafe_allow_html=True)
        
        # AI Response logic
        with st.spinner("Decoding Neural Pathways..."):
            try:
                response = model.generate_content(user_input)
                ai_response = response.text
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
                st.rerun()
            except Exception as e:
                st.error(f"Neural Link Severed: {e}")

# Sidebar Styling
with st.sidebar:
    st.markdown("### 🛠 SYSTEM STATUS")
    st.success("🟢 CORE ONLINE")
    st.info(f"📍 MODEL: GEMINI FLASH")
    st.markdown("---")
    st.markdown("### 📡 CONNECTION")
    st.write("API Latency: < 200ms")
    st.write("Link Status: Encrypted")
    
    if st.button("CLEAR MEMORY"):
        st.session_state.messages = []
        st.rerun()
