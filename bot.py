# bot.py
import os
import logging
from telegram.ext import Application, CommandHandler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")


# Define commands
async def start(update, context):
    await update.message.reply_text("✅ Bot is alive and working!")


async def help_command(update, context):
    await update.message.reply_text("Here are the commands:\n/start - check bot\n/help - show this help")


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Start polling
    app.run_polling()


if __name__ == "__main__":
    main()
