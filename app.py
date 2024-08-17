from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import CommandHandler, Application

app = Flask(__name__)

TOKEN = "7362610114:AAHRCtTThfAs0Q-mZjAVqlSotwiLhxlRIzs"
bot = Bot(token=TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    # Здесь можно добавить код для обработки обновления
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
