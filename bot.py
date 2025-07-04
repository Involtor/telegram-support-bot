import os
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler
from aiohttp import web

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("Бот запущен!")

async def handle(request):
    return web.Response(text="OK")

async def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

async def run_webserver():
    app = web.Application()
    app.add_routes([web.get('/', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.getenv("PORT", 8080)))
    await site.start()
    print("Webserver started")
    while True:
        await asyncio.sleep(3600)

async def main():
    await asyncio.gather(run_bot(), run_webserver())

if __name__ == "__main__":
    asyncio.run(main())
