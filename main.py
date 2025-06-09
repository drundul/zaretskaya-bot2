import logging
from fastapi import FastAPI, Request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import openai
import prompt_config

openai.api_key = "your-openai-api-key"

TELEGRAM_TOKEN = "7339394405:AAEh-rWDxd_JVKENCel-S0QujIKy16pBHN0"

app = FastAPI()
bot = Bot(token=TELEGRAM_TOKEN)
application = Application.builder().token(TELEGRAM_TOKEN).build()

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✨ Привет, я Татьянин помощник. Готова поддержать тебя, дать практику или вдохновение. Спроси меня о чём-то важном 💫")

async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    messages = [
        {"role": "system", "content": prompt_config.SYSTEM_PROMPT},
        {"role": "user", "content": user_message}
    ]
    response = openai.ChatCompletion.create(model="gpt-4o", messages=messages)
    reply_text = response.choices[0].message["content"]
    await update.message.reply_text(reply_text)

application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))

@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    update = Update.de_json(data, bot)
    await application.process_update(update)
    return "ok"
# ✅ Запуск Telegram-хендлеров при старте FastAPI
import asyncio
asyncio.create_task(application.initialize())
