from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Replace with your Telegram bot token
TELEGRAM_BOT_TOKEN = "7649317053:AAEuahOjsqpu2aqQGs5qlJCsKvL35qU-leo"  # Replace with your bot's token

# List of trigger words
TRIGGER_WORDS = ['alo', 'ալօ', 'ալյո', 'ալո', 'ալյօ' 'ало' 'але' 'алё']  # Add more trigger words to this list

# Function to handle messages
async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text.lower()  # Convert message to lowercase to make the search case-insensitive

    # If any trigger word is found, respond
    if any(word in message for word in TRIGGER_WORDS):
        await update.message.reply_text("Hello! How can I assist you today?")

def main():
    # Create application with the bot token
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add message handler for responding to trigger words
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()
