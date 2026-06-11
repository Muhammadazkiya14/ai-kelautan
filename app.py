from flask import Flask, render_template, request, jsonify
from src.chatbot import Chatbot
from src.web_search import search_web
from src.prompt import build_prompt

app = Flask(__name__)
chatbot = Chatbot()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"response": "Tidak ada pesan"})
    
    conversation_messages = chatbot.history.get_messages()
    
    search_results = ""
    if len(user_input.split()) >= 3:
        search_results = search_web(user_input)
        if search_results:
            context_prompt = build_prompt(user_input, search_results)
            conversation_messages.append({"role": "user", "content": context_prompt})
        else:
            conversation_messages.append({"role": "user", "content": user_input})
    else:
        conversation_messages.append({"role": "user", "content": user_input})
    
    response = chatbot.get_ai_response(conversation_messages)
    
    if not search_results:
        chatbot.history.add_user(user_input)
    chatbot.history.add_assistant(response)
    
    return jsonify({"response": response})

@app.route("/clear", methods=["POST"])
def clear():
    chatbot.history.clear()
    return jsonify({"status": "Histori chat dibersihkan"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)