# main.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from config import BOT_TOKEN
from game import GameManager

gm = GameManager()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to UNO Bot! Use /join to join the game.")

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    game = gm.get_game(chat_id)
    player_added = game.add_player(update.effective_user.id, update.effective_user.first_name)
    if player_added:
        await update.message.reply_text(f"{update.effective_user.first_name} joined the game!")
    else:
        await update.message.reply_text("You can't join right now.")

async def startgame(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    game = gm.get_game(chat_id)
    if game.start():
        await update.message.reply_text("Game started!")
        await send_turn(chat_id, context)
    else:
        await update.message.reply_text("Need at least 2 players to start.")

async def send_turn(chat_id, context):
    game = gm.get_game(chat_id)
    player = game.current_player()
    keyboard = [[InlineKeyboardButton(str(card), callback_data=str(i))] for i, card in enumerate(player.hand)]
    await context.bot.send_message(
        chat_id=player.user_id,
        text=f"Your turn! Top card: {game.discard_pile[-1]}\nYour hand:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def handle_card(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = update.effective_chat.id
    game = gm.get_game(chat_id)
    player = game.current_player()
    card_index = int(query.data)
    card = player.hand[card_index]
    if game.play_card(player, card):
        await query.edit_message_text(f"You played {card}")
        if not player.hand:
            await context.bot.send_message(chat_id=chat_id, text=f"{player.name} wins!")
            del gm.games[chat_id]
            return
        await send_turn(chat_id, context)
    else:
        await query.edit_message_text("Invalid move!")

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("join", join))
    app.add_handler(CommandHandler("startgame", startgame))
    app.add_handler(CallbackQueryHandler(handle_card))
    app.run_polling()
