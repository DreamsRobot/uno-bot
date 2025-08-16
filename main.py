# main.py
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import game, inline

# Initialize Pyrogram Client
app = Client(
    "uno-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Load game command handlers
game.register_handlers(app)

# Load inline handlers
inline.register_handlers(app)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text(
        "👋 Welcome to UNO Bot!\n\n"
        "🎮 Game Commands:\n"
        "/newgame - Start a new game\n"
        "/joingame - Join the current game\n"
        "/leavegame - Leave the game\n"
        "/skip - Skip your turn\n"
        "/kill - End the current game\n\n"
        "✨ Inline Mode:\n"
        "Type @YourBotUsername in any chat to view and play cards 🎴"
    )

if __name__ == "__main__":
    print("UNO Bot is running...")
    app.run()
