from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    CommandHandler, CallbackQueryHandler, ContextTypes, Application
)
from game import UNOGame
from config import BOT_TOKEN

games = {}

def get_hand_buttons(hand):
    buttons = []
    for card in hand:
        buttons.append([InlineKeyboardButton(card, callback_data=f"play|{card}")])
    buttons.append([InlineKeyboardButton("Draw", callback_data="draw")])
    return InlineKeyboardMarkup(buttons)

# ─── Commands ───────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎴 UNO Bot Ready!\n/start - Welcome\n/new - New game\n/join - Join\n"
        "/begin - Start\n/leave - Leave\n/help - Help"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📘 UNO Help:\n/new → Create game\n/join → Join game\n/begin → Start\n"
        "/leave → Leave\n/kick @user → Kick\n/kill → End game"
    )

async def new_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    games[chat_id] = UNOGame()
    await update.message.reply_text("🆕 New UNO game created! Players use /join to enter.")

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    player = update.effective_user.id
    if chat_id not in games:
        await update.message.reply_text("No active game. Use /new first.")
        return
    if games[chat_id].add_player(player):
        await update.message.reply_text(f"{update.effective_user.first_name} joined UNO! 🎮")
    else:
        await update.message.reply_text("You cannot join now.")

async def leave(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    player = update.effective_user.id
    if chat_id in games and player in games[chat_id].players:
        games[chat_id].players.remove(player)
        del games[chat_id].hands[player]
        await update.message.reply_text(f"{update.effective_user.first_name} left the game.")
    else:
        await update.message.reply_text("You’re not in the game.")

async def kill(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id in games:
        games.pop(chat_id)
        await update.message.reply_text("💀 Game ended.")

async def start_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    game = games.get(chat_id)
    if not game:
        await update.message.reply_text("No game found.")
        return
    if not game.start_game():
        await update.message.reply_text("Need at least 2 players to start!")
        return
    await update.message.reply_text(f"Game started! First card: {game.discard[-1]}")
    await send_hand(context, chat_id, game.get_current_player())

async def send_hand(context, chat_id, player):
    game = games[chat_id]
    hand = game.hands[player]
    await context.bot.send_message(
        chat_id=player,
        text=f"Your turn! Top card: {game.discard[-1]}",
        reply_markup=get_hand_buttons(hand)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = update.effective_chat.id
    player = query.from_user.id
    game = games.get(chat_id)
    if not game:
        return

    action = query.data
    if action.startswith("play"):
        _, card = action.split("|", 1)
        ok, msg = game.play_card(player, card)
        await query.edit_message_text(msg)
        if ok:
            if not game.hands[player]:
                await context.bot.send_message(chat_id, f"🎉 {query.from_user.first_name} wins the round!")
                games.pop(chat_id)
                return
            await context.bot.send_message(chat_id, f"{query.from_user.first_name} played {card}. Next: {game.get_current_player()}")
            await send_hand(context, chat_id, game.get_current_player())
    elif action == "draw":
        game.draw_card(player)
        await query.edit_message_text("You drew a card.")
        await send_hand(context, chat_id, game.get_current_player())

# ─── Register Handlers ──────────────────────────────────────
def register_handlers(app: Application):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("new", new_game))
    app.add_handler(CommandHandler("join", join))
    app.add_handler(CommandHandler("leave", leave))
    app.add_handler(CommandHandler("kill", kill))
    app.add_handler(CommandHandler("begin", start_game))
    app.add_handler(CallbackQueryHandler(button))
