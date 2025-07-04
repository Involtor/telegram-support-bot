import os
import asyncio
from aiohttp import web
from telegram.ext import ApplicationBuilder, CommandHandler

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Убедись, что переменная окружения есть!

# Пример простой команды /start
async def start(update, context):
    await update.message.reply_text("Привет! Бот работает.")

# HTTP хэндлер для проверки работоспособности
async def handle(request):
    return web.Response(text="Bot is running")

async def main():
    # Создаем приложение бота
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    # Запускаем веб-сервер
    web_app = web.Application()
    web_app.router.add_get('/', handle)

    runner = web.AppRunner(web_app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

    print(f"Web server running on port {port}")
    print("Telegram bot started")

    # Запускаем polling бота (асинхронно, не блокирует)
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
