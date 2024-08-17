from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7362610114:AAHRCtTThfAs0Q-mZjAVqlSotwiLhxlRIzs"
CHANNEL_USERNAME = "@deftbuncrypto"
PRIVATE_CHAT_LINK = "https://t.me/+QHPRPFA4sPlmNjYy"

app = Flask(__name__)
bot = Bot(token=TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    bot = context.bot
    member_status = await bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user.id)

    if member_status.status in ['member', 'administrator', 'creator']:
        await update.message.reply_text(f"Спасибо за подписку! Вот ссылка на чат: {PRIVATE_CHAT_LINK}")
    else:
        await update.message.reply_text("Пожалуйста, подпишитесь на канал, чтобы получить доступ к чату.")

async def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    await application.initialize()
    await application.start()
    await application.updater.start_polling()

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    application = Application.builder().token(TOKEN).build()
    application.process_update(update)
    return 'OK'

if __name__ == '__main__':
    app.run()
