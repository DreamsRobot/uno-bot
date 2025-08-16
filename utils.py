from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_hand_buttons(hand):
    """Build inline buttons for a player’s hand."""
    buttons = []
    for card in hand:
        buttons.append([InlineKeyboardButton(card, callback_data=f"play|{card}")])
    buttons.append([InlineKeyboardButton("Draw", callback_data="draw")])
    return InlineKeyboardMarkup(buttons)
