from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from config import BOT_TOKEN
import handlers

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", handlers.start))
    app.add_handler(CommandHandler("help", handlers.help_cmd))
    app.add_handler(CommandHandler("new", handlers.new_game))
    app.add_handler(CommandHandler("join", handlers.join))
    app.add_handler(CommandHandler("leave", handlers.leave))
    app.add_handler(CommandHandler("kill", handlers.kill))
    app.add_handler(CommandHandler("begin", handlers.start_game))

    # Inline buttons
    app.add_handler(CallbackQueryHandler(handlers.button))

    print("✅ UNO Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
