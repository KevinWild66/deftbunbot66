from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from flask import Flask, request

TOKEN = "7362610114:AAHRCtTThfAs0Q-mZjAVqlSotwiLhxlRIzs"
CHANNEL_USERNAME = "@deftbuncrypto"
PRIVATE_CHAT_LINK = "https://t.me/+QHPRPFA4sPlmNjYy"

app = Flask(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Подтвердить подписку", callback_data='check_subscription')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Пожалуйста, подпишитесь на канал и нажмите кнопку ниже, чтобы получить доступ к чату.", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = query.from_user
    bot = context.bot
    member_status = await bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user.id)

    if member_status.status in ['member', 'administrator', 'creator']:
        await query.edit_message_text(text=f"Спасибо за подписку! Вот ссылка на чат: {PRIVATE_CHAT_LINK}")
    else:
        await query.edit_message_text(text="Пожалуйста, подпишитесь на канал, чтобы получить доступ к чату.")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Запускаем бота в фоне
    application.run_webhook(listen="0.0.0.0",
                            port=8443,
                            url_path=TOKEN,
                            webhook_url=f"https://your_pythonanywhere_username.pythonanywhere.com/{TOKEN}")

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.process_update(update)
    return "ok"

if __name__ == "__main__":
    main()
    app.run(host="0.0.0.0", port=8443)
