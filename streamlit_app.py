import streamlit as st
from src.chatbot import Chatbot
from src.web_search import search_web
from src.prompt import build_prompt

st.set_page_config(page_title="AI Kelautan", page_icon="🌊")

if 'history' not in st.session_state:
    st.session_state.history = Chatbot().history

st.title("🌊 AI Kelautan")
st.caption("Tanya apa saja tentang kelautan")

for msg in st.session_state.history.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ketik pertanyaan..."):
    with st.chat_message("user"):
        st.write(prompt)
    
    messages = st.session_state.history.get_messages()
    if len(prompt.split()) >= 3:
        with st.spinner("Mencari informasi..."):
            search_results = search_web(prompt)
            if search_results:
                prompt = build_prompt(prompt, search_results)
            messages.append({"role": "user", "content": prompt})
    else:
        messages.append({"role": "user", "content": prompt})
    
    with st.spinner("Menjawab..."):
        chatbot = Chatbot()
        response = chatbot.get_ai_response(messages)
    
    st.session_state.history.add_user(prompt if len(prompt.split()) < 3 else prompt)
    st.session_state.history.add_assistant(response)
    
    with st.chat_message("assistant"):
        st.write(response)