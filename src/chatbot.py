import os
import requests
from dotenv import load_dotenv
from src.web_search import search_web
from src.prompt import build_prompt
from src.history import ConversationHistory

load_dotenv()

class Chatbot:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.model = "nvidia/nemotron-3-super-120b-a12b:free"
        self.history = ConversationHistory()

    def get_ai_response(self, messages):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://ai-kelautan.local",
            "X-Title": "AI Kelautan"
        }
        payload = {
            "model": self.model,
            "messages": messages,
            "max_tokens": 1000,
            "temperature": 0.7
        }
        try:
            resp = requests.post(self.base_url, json=payload, headers=headers, timeout=60)
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error: {str(e)}"

    def run(self):
        print("=" * 50)
        print("AI KELAUTAN - Tanya apa saja tentang kelautan!")
        print("Ketik 'keluar' untuk berhenti, 'bersihkan' untuk reset chat")
        print("=" * 50)

        while True:
            user_input = input("\nKamu: ").strip()

            if user_input.lower() in ["keluar", "exit", "quit"]:
                print("AI: Selamat berlayar! Sampai jumpa.")
                break

            if user_input.lower() in ["bersihkan", "clear", "reset"]:
                self.history.clear()
                print("AI: Histori chat berhasil dibersihkan.")
                continue

            if not user_input:
                continue

            conversation_messages = self.history.get_messages()

            search_results = ""
            if len(user_input.split()) >= 3:
                print("AI: Mencari informasi terbaru di internet...")
                search_results = search_web(user_input)
                if search_results:
                    context_prompt = build_prompt(user_input, search_results)
                    conversation_messages.append({"role": "user", "content": context_prompt})
                else:
                    conversation_messages.append({"role": "user", "content": user_input})
            else:
                conversation_messages.append({"role": "user", "content": user_input})

            print("AI: Sedang menjawab...")
            response = self.get_ai_response(conversation_messages)

            if not search_results:
                self.history.add_user(user_input)
            self.history.add_assistant(response)

            print(f"\nAI: {response}")
