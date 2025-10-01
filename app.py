import os
import streamlit as st
import google.generativeai as genai   # ✅ fallback works on Streamlit

# Load API key
api_key = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("⚠️ No API key found! Please set GOOGLE_API_KEY in Streamlit Secrets.")
else:
    genai.configure(api_key=api_key)

    st.title("💬 Google Gemini Chatbot")

    if "chat" not in st.session_state:
        st.session_state.chat = genai.GenerativeModel("gemini-1.5-flash").start_chat()

    user_input = st.text_input("You:", "")

    if st.button("Send") and user_input:
        response = st.session_state.chat.send_message(user_input)
        st.write("**Bot:**", response.text)
