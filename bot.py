from telegram.ext import Application, CommandHandler
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Example command
async def start(update, context):
    await update.message.reply_text("Hello! UNO Bot is running 🚀")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))

    # Run polling loop
    app.run_polling()

if __name__ == "__main__":
    main()
