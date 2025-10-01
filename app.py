import os
import streamlit as st
import google.genai as genai

# ✅ Get API key from environment variable (set in system or Streamlit secrets)
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ No API key found. Please set GOOGLE_API_KEY as an environment variable.")
    st.stop()

# ✅ Initialize client with your API key
client = genai.Client(api_key=api_key)

# Streamlit app
st.set_page_config(page_title="Chat with Google GenAI", page_icon="🤖")
st.title("🤖 Chat with Google GenAI")

# Keep chat history in session
if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(model="gemini-1.5-flash")

# Display conversation
for msg in st.session_state.chat.history:
    st.chat_message(msg.role).write(msg.content[0].text)

# Input box for user
if prompt := st.chat_input("Type your message..."):
    st.chat_message("user").write(prompt)
    response = st.session_state.chat.send_message(prompt)
    st.chat_message("model").write(response.text)



