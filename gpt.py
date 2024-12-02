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
