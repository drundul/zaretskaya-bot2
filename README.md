# Telegram ИИ-Бот в стиле Татьяны Зарецкой

## 📦 Запуск на Render

1. Создайте новый Web Service на https://render.com
2. Подключите этот репозиторий или загрузите архив
3. Установите переменные окружения:
   - `your-openai-api-key` — вставьте свой OpenAI API ключ
4. Build Command:
   ```
   pip install -r requirements.txt
   ```
5. Start Command:
   ```
   uvicorn main:app --host 0.0.0.0 --port 10000
   ```
6. Настрой webhook через Telegram:
   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://your-render-url/webhook
   ```

## 🧠 Что умеет бот

- Отвечает в стиле Татьяны Зарецкой
- Предлагает медитации, ритуалы, дыхательные практики
- Задаёт наводящие вопросы и учитывает ответ в диалоге

## 🔐 Важно

Никогда не публикуйте свой bot token и OpenAI API key в открытом доступе.
