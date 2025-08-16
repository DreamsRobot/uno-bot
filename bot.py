# bot.py
from telegram.ext import Application
from handlers import register_handlers
from config import BOT_TOKEN

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Register all handlers
    register_handlers(app)

    # Start polling (async, modern way)
    app.run_polling()

if __name__ == "__main__":
    main()
