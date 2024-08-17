from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = 7362610114:AAHRCtTThfAs0Q-mZjAVqlSotwiLhxlRIzs
CHANNEL_USERNAME = @deftbuncrypto
PRIVATE_CHAT_LINK = https://t.me/+QHPRPFA4sPlmNjYy

def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    bot = Bot(TOKEN)

    member_status = bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user.id).status

    if member_status in ['member', 'administrator', 'creator']:
        update.message.reply_text(f"Спасибо за подписку! Вот ссылка на чат: {PRIVATE_CHAT_LINK}")
    else:
        update.message.reply_text("Пожалуйста, подпишитесь на канал, чтобы получить доступ к чату.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if name == 'main':
    main()