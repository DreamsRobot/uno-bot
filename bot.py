from telegram.ext import Application
from handlers import register_handlers
from config import BOT_TOKEN

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # register all commands & callbacks
    register_handlers(app)

    print("🚀 UNO Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
