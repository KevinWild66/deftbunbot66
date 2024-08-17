from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes

app = Flask(__name__)

TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_USERNAME = "@YOUR_CHANNEL_USERNAME"
PRIVATE_CHAT_LINK = "https://t.me/your_chat_link"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    context = ContextTypes.DEFAULT_TYPE()
    # Обработка обновлений здесь
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)
