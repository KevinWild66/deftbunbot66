from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7362610114:AAHRCtTThfAs0Q-mZjAVqlSotwiLhxlRIzs"
CHANNEL_USERNAME = "@deftbuncrypto"
PRIVATE_CHAT_LINK = "https://t.me/+QHPRPFA4sPlmNjYy"

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

    # Запуск бота
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    await application.updater.stop()
    await application.stop()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
