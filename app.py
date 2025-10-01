import streamlit as st
import google.generativeai as genai
import os

# Configure API key (make sure you set GOOGLE_API_KEY in Streamlit Secrets)
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Use the correct model
MODEL_NAME = "gemini-1.5-flash-latest"

if "chat" not in st.session_state:
    st.session_state.chat = genai.GenerativeModel(MODEL_NAME).start_chat()

st.title("Gemini Chatbot 🤖")

user_input = st.text_input("You:", "")

if user_input:
    response = st.session_state.chat.send_message(user_input)
    st.write("**Bot:**", response.text)
