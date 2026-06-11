from dotenv import load_dotenv
from src.chatbot import Chatbot

if __name__ == "__main__":
    load_dotenv()
    bot = Chatbot()
    bot.run()
