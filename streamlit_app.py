import streamlit as st
from src.chatbot import Chatbot
from src.web_search import search_web
from src.prompt import build_prompt

st.set_page_config(page_title="AI Kelautan", page_icon="🌊")

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #f5f7fa 0%, #e4edf5 100%); }
    .stChatMessage { border-radius: 12px !important; }
    .stChatMessage.user { background: #e3f2fd !important; }
    .stChatMessage.assistant { background: #ffffff !important; border: 1px solid #e0e0e0; }
    .stButton button { background: #2196f3; color: white; border-radius: 8px; }
    .stChatInput { border-radius: 20px; }
    .thinking { color: #64b5f6; font-style: italic; }
</style>
""", unsafe_allow_html=True)

if 'history' not in st.session_state:
    st.session_state.history = Chatbot().history

st.title("🌊 AI Kelautan")
st.caption("Asisten virtual tentang kelautan & perikanan")

chat_container = st.container()

with chat_container:
    for msg in st.session_state.history.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

if prompt := st.chat_input("Tanya tentang kelautan..."):
    with st.chat_message("user"):
        st.write(prompt)
    
    messages = st.session_state.history.get_messages()
    
    if len(prompt.split()) >= 3:
        with st.status("Sedang mencari informasi terbaru..."):
            search_results = search_web(prompt)
            if search_results:
                prompt = build_prompt(prompt, search_results)
            messages.append({"role": "user", "content": prompt})
    else:
        messages.append({"role": "user", "content": prompt})
    
    with st.spinner("💭 AI sedang merakit jawaban..."):
        chatbot = Chatbot()
        response = chatbot.get_ai_response(messages)
    
    st.session_state.history.add_user(prompt if len(prompt.split()) < 3 else prompt)
    st.session_state.history.add_assistant(response)
    
    with st.chat_message("assistant"):
        st.write(response)