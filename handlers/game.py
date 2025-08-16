# handlers/game.py
from pyrogram import filters
import game

# Store lobbies {chat_id: {...}}
lobbies = {}

def register_handlers(app):

    @app.on_message(filters.command("newgame"))
    async def new_game(client, message):
        chat_id = message.chat.id
        if chat_id in lobbies:
            return await message.reply("⚠️ A game is already running.")
        lobbies[chat_id] = {
            "deck": game.generate_deck(),
            "players": [message.from_user.id],
            "turn": 0
        }
        await message.reply("🎮 New UNO game created! Use /joingame to join.")

    @app.on_message(filters.command("joingame"))
    async def join_game(client, message):
        chat_id = message.chat.id
        if chat_id not in lobbies:
            return await message.reply("❌ No game running.")
        if message.from_user.id in lobbies[chat_id]["players"]:
            return await message.reply("⚠️ You already joined.")
        lobbies[chat_id]["players"].append(message.from_user.id)
        await message.reply(f"✅ {message.from_user.mention} joined the game!")

    @app.on_message(filters.command("leavegame"))
    async def leave_game(client, message):
        chat_id = message.chat.id
        if chat_id not in lobbies:
            return await message.reply("❌ No game running.")
        if message.from_user.id not in lobbies[chat_id]["players"]:
            return await message.reply("⚠️ You are not in the game.")
        lobbies[chat_id]["players"].remove(message.from_user.id)
        await message.reply(f"👋 {message.from_user.mention} left the game.")

    @app.on_message(filters.command("skip"))
    async def skip_turn(client, message):
        chat_id = message.chat.id
        if chat_id not in lobbies:
            return await message.reply("❌ No game running.")
        lobbies[chat_id]["turn"] = (lobbies[chat_id]["turn"] + 1) % len(lobbies[chat_id]["players"])
        await message.reply("⏭ Turn skipped!")

    @app.on_message(filters.command("kill"))
    async def kill_game(client, message):
        chat_id = message.chat.id
        if chat_id in lobbies:
            del lobbies[chat_id]
            await message.reply("💀 Game ended.")
        else:
            await message.reply("❌ No game running.")
