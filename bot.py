from telegram.ext import ApplicationBuilder
from aiohttp import web

BOT_TOKEN = "ваш_токен"

async def handle(request):
    return web.Response(text="Bot is running")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    runner = web.AppRunner(web.Application())
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.environ.get('PORT', '8080')))
    await site.start()

    print("Bot started")
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    import os
    asyncio.run(main())
