import streamlit as st
from chatbot import ai_chatbot

st.set_page_config(page_title="Caramel AI Chatbot", page_icon="https://raw.githubusercontent.com/hereandnowai/images/refs/heads/main/logos/favicon-logo-with-name.png")
st.title("Caramel AI Chatbot")
st.image("https://raw.githubusercontent.com/hereandnowai/images/refs/heads/main/logos/logo-of-here-and-now-ai.png", width=500)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    avatar_url = "https://raw.githubusercontent.com/hereandnowai/images/refs/heads/main/logos/caramel-face.jpeg" if msg["role"] == "assistant" else None
    st.chat_message(msg["role"], avatar=avatar_url).write(msg["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.spinner("Thinking..."):
        ai_response = ai_chatbot(prompt, st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        st.chat_message("assistant", avatar="https://raw.githubusercontent.com/hereandnowai/images/refs/heads/main/logos/caramel-face.jpeg").write(ai_response)
