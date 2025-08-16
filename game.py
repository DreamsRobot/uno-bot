import random

# Active games per chat
games = {}

# UNO deck
colors = ["R", "G", "B", "Y"]
values = [str(i) for i in range(0, 10)] + ["+2", "SKIP", "REVERSE"]
deck = [f"{c}{v}" for c in colors for v in values] + ["WILD", "WILD+4"] * 4

def draw_cards(n=7):
    return random.sample(deck, n)

def start_new_game(chat_id):
    games[chat_id] = {"players": {}, "turn": 0, "order": []}
    return "🎮 New UNO game started! Use /join to enter."

def join_game(chat_id, player):
    game = games.get(chat_id)
    if not game:
        return "❌ No active game. Use /newgame first."
    if player in game["players"]:
        return f"{player}, you already joined."
    hand = draw_cards()
    game["players"][player] = hand
    game["order"].append(player)
    return f"✅ {player} joined! Hand dealt."

def show_hand(chat_id, player):
    game = games.get(chat_id)
    if not game or player not in game["players"]:
        return "❌ You're not in a game."
    return f"🃏 Your hand: {', '.join(game['players'][player])}"

def play_card(chat_id, player, card):
    game = games.get(chat_id)
    if not game or player not in game["players"]:
        return "❌ You're not in a game."
    hand = game["players"][player]
    if card not in hand:
        return f"❌ You don’t have {card}."
    hand.remove(card)
    if not hand:
        return f"🎉 UNO! {player} wins!"
    return f"✅ {player} played {card}. Remaining: {', '.join(hand)}"
