import openai
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace with your OpenAI API key
OPENAI_API_KEY = "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"  # Add your OpenAI API key here

# Replace with your Telegram bot token
TELEGRAM_BOT_TOKEN = "7649317053:AAEuahOjsqpu2aqQGs5qlJCsKvL35qU-leo"  # Add your Telegram bot token here

# Function to handle /gpt command
async def gpt_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = " ".join(context.args)
    if not query:
        await update.message.reply_text("Please provide a query after the /gpt command.")
        return

    await update.message.reply_text("Processing your request...")

    # Call OpenAI API (ChatGPT)
    try:
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query},
            ],
        )
        answer = response["choices"][0]["message"]["content"]
        await update.message.reply_text(answer)
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")

def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("gpt", gpt_command))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
