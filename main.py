# main.py
from pyrogram import Client, filters
from config import BOT_TOKEN
from handlers import game, inline

app = Client("uno-bot", bot_token=BOT_TOKEN)

# Load game command handlers
game.register_handlers(app)

# Load inline handlers
inline.register_handlers(app)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text(
        "👋 Welcome to UNO Bot!\n\n"
        "Commands:\n"
        "/newgame - Start new game\n"
        "/joingame - Join game\n"
        "/leavegame - Leave game\n"
        "/skip - Skip turn\n"
        "/kill - End game\n\n"
        "Try inline mode: type @YourBotName in any chat 🎴"
    )

print("UNO Bot is running...")
app.run()
