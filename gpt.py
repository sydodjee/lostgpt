from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Replace with your Telegram bot token
TELEGRAM_BOT_TOKEN = "7649317053:AAEuahOjsqpu2aqQGs5qlJCsKvL35qU-leo"  # Replace with your bot's token

# Function to handle messages
async def respond_alo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if "alo" in update.message.text.lower():
        await update.message.reply_text("ալօ, ջուլի, պատմի?")

def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Handler for responding to "alo" in messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond_alo))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
