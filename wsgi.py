from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, CallbackContext

app = Flask(__name__)

TOKEN = '7362610114:AAHRCtTThfAs0Q-mZjAVqlSotwiLhxlRIzs'
bot = Bot(token=TOKEN)

@app.route('/' + TOKEN, methods=['POST'])
def respond():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

dispatcher = Dispatcher(bot, None, use_context=True)

# Команды и обработчики
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет! Подпишитесь на канал и получите доступ к чату.')

dispatcher.add_handler(CommandHandler('start', start))

if __name__ == "__main__":
    app.run(debug=True)
