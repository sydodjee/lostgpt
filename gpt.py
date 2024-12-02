import os
import asyncio
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import openai
from threading import Thread

# Your OpenAI API key
OPENAI_API_KEY = "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"

# Your Telegram bot token
TELEGRAM_BOT_TOKEN = "7649317053:AAEuahOjsqpu2aqQGs5qlJCsKvL35qU-leo"

# Flask app for the dummy web server
app = Flask(__name__)

@app.route("/")
def home():
    return "Telegram Bot is Running!"

# Function to handle /gpt command
async def gpt_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = " ".join(context.args)
    if not query:
        await update.message.reply_text("Please provide a query after the /gpt command.")
        return

    await update.message.reply_text("Processing your request...")

    try:
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Kara, a witty, flirty, sarcastic assistant."},
                {"role": "user", "content": query},
            ],
        )
        answer = response["choices"][0]["message"]["content"]
        await update.message.reply_text(answer)
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")

# Set up Telegram bot
async def start_telegram_bot():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("gpt", gpt_command))
    await application.run_polling()

# Main function to start both Flask and Telegram bot using asyncio
def run_flask():
    # Use the environment port or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

# Start Flask and Telegram bot in separate threads
def main():
    # Start Flask in a separate thread
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    # Run the Telegram bot with asyncio
    asyncio.run(start_telegram_bot())

if __name__ == "__main__":
    main()
