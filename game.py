# game.py
import random

# Basic UNO cards
COLORS = ["🔴", "🟢", "🔵", "🟡"]
NUMBERS = list(range(0, 10))
SPECIALS = ["Skip", "Reverse", "+2"]

def generate_deck():
    """Generate UNO deck with colors, numbers, and specials."""
    deck = []
    for color in COLORS:
        for num in NUMBERS:
            deck.append(f"{color} {num}")
        for special in SPECIALS:
            deck.append(f"{color} {special}")
    # Add Wild cards
    deck += ["❌ Wild", "❌ Wild +4"] * 4
    random.shuffle(deck)
    return deck
