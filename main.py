import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import openai
import prompt_config

openai.api_key = "your-openai-api-key"
TELEGRAM_TOKEN = "7339394405:AAEh-rWDxd_JVKENCel-S0QujIKy16pBHN0"

logging.basicConfig(level=logging.INFO)

# Команды
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

# Основной блок
def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))

    application.run_polling()  # ← вот он, Polling

if __name__ == "__main__":
    main()
