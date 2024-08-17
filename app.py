from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackQueryHandler, Application

app = Flask(__name__)

TOKEN = "7362610114:AAHRCtTThfAs0Q-mZjAVqlSotwiLhxlRIzs"
bot = Bot(token=TOKEN)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    # Здесь добавьте обработку обновлений Telegram, например:
    # dispatcher.process_update(update)
    return 'OK'

if __name__ == "__main__":
    app.run(debug=True)
