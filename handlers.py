from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from game import start_new_game, join_game, play_card, show_hand

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎲 Welcome to UNO Bot! Use /newgame to start.")

# /newgame
async def newgame(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = start_new_game(update.effective_chat.id)
    await update.message.reply_text(msg)

# /join
async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = join_game(update.effective_chat.id, update.effective_user.first_name)
    await update.message.reply_text(msg)

# /hand
async def hand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = show_hand(update.effective_chat.id, update.effective_user.first_name)
    await update.message.reply_text(msg)

# /play <card>
async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Usage: /play <card>")
        return
    card = context.args[0].upper()
    msg = play_card(update.effective_chat.id, update.effective_user.first_name, card)
    await update.message.reply_text(msg)

def register_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("newgame", newgame))
    app.add_handler(CommandHandler("join", join))
    app.add_handler(CommandHandler("hand", hand))
    app.add_handler(CommandHandler("play", play))
