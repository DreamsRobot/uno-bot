from telegram.ext import Application
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Register handlers here
    # app.add_handler(CommandHandler("start", start))

    # Old (❌): app.updater.start_polling()
    # New (✅):
    app.run_polling()

if __name__ == "__main__":
    main()
