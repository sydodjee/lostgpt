import os
import openai
import asyncio
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import threading

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

    await update.message.reply_text("
