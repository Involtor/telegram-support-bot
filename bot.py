from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7299153170:AAEsiTqpE9pl1UT6D2vVtNjrxPll0j97cgg"
ADMIN_CHAT_ID = 591672212

async def user_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    msg = update.message.text
    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f"📩 От @{user.username or user.first_name} (id: {user.id}):\n\n{msg}"
    )

async def admin_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id == ADMIN_CHAT_ID and update.message.reply_to_message:
        parts = update.message.reply_to_message.text.split("id:")
        if len(parts) > 1:
            user_id = int(parts[-1])
            await context.bot.send_message(chat_id=user_id, text=update.message.text)

def main():
    print("✅ Starting bot...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), user_message))
    app.add_handler(MessageHandler(filters.TEXT & filters.Chat(chat_id=ADMIN_CHAT_ID), admin_reply))
    app.run_polling()

if __name__ == "__main__":
    main()
