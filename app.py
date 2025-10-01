import streamlit as st
import google.generativeai as genai
import os

# ✅ Configure with API key (must be set in Streamlit secrets or environment variable)
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("💬 Gemini Chatbot")

# Choose your model (fast vs smart)
MODEL_NAME = "models/gemini-2.5-flash"   # or "models/gemini-2.5-pro"

# Create a chat session if not already in state
if "chat" not in st.session_state:
    st.session_state.chat = genai.GenerativeModel(MODEL_NAME).start_chat(history=[])

# Input box
user_input = st.text_input("You:", "")

# Send button
if st.button("Send") and user_input:
    response = st.session_state.chat.send_message(user_input)
    st.write(f"**Bot:** {response.text}")
