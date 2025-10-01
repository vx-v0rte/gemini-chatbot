import streamlit as st
import google.generativeai as genai
import os

# ✅ Configure with API key (from environment or Streamlit secrets)
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("💬 Gemini Chatbot")

# Choose your model (fast vs smart)
MODEL_NAME = "models/gemini-2.5-flash"   # or "models/gemini-2.5-pro"

# Initialize chat session
if "chat" not in st.session_state:
    st.session_state.chat = genai.GenerativeModel(MODEL_NAME).start_chat(history=[])
    st.session_state.messages = []  # keep track of history for display

# Display past messages
for role, text in st.session_state.messages:
    if role == "user":
        st.markdown(f"🧑 **You:** {text}")
    else:
        st.markdown(f"🤖 **Gemini:** {text}")

# Input box
user_input = st.chat_input("Type your message...")

# Send and display response
if user_input:
    # Add user message to history
    st.session_state.messages.append(("user", user_input))
    
    # Get model response
    response = st.session_state.chat.send_message(user_input)
    bot_reply = response.text
    
    # Add bot message to history
    st.session_state.messages.append(("bot", bot_reply))
    
    # Refresh page to show new messages
    st.experimental_rerun()
