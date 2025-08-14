# game.py
import random

COLORS = ["Red", "Green", "Blue", "Yellow"]
VALUES = list(map(str, range(0, 10))) + ["Skip", "Reverse", "Draw Two"]
SPECIALS = ["Wild", "Wild Draw Four"]

class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return f"{self.color or ''} {self.value}".strip()

    def matches(self, other):
        return (
            self.color == other.color or
            self.value == other.value or
            self.color is None
        )

class Deck:
    def __init__(self):
        self.cards = []
        for color in COLORS:
            for value in VALUES:
                self.cards.append(Card(color, value))
                self.cards.append(Card(color, value))
        for special in SPECIALS:
            for _ in range(4):
                self.cards.append(Card(None, special))
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            raise ValueError("No more cards in deck")
        return self.cards.pop()

class Player:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.hand = []

    def draw_card(self, deck, num=1):
        for _ in range(num):
            self.hand.append(deck.draw())

    def remove_card(self, card):
        self.hand.remove(card)

class Game:
    def __init__(self):
        self.players = []
        self.deck = Deck()
        self.discard_pile = []
        self.current_player_index = 0
        self.direction = 1
        self.started = False

    def add_player(self, user_id, name):
        if self.started:
            return False
        if any(p.user_id == user_id for p in self.players):
            return False
        self.players.append(Player(user_id, name))
        return True

    def start(self):
        if len(self.players) < 2:
            return False
        self.started = True
        for player in self.players:
            player.draw_card(self.deck, 7)
        self.discard_pile.append(self.deck.draw())
        return True

    def current_player(self):
        return self.players[self.current_player_index]

    def play_card(self, player, card):
        if not card.matches(self.discard_pile[-1]):
            return False
        player.remove_card(card)
        self.discard_pile.append(card)
        if card.value == "Reverse":
            self.direction *= -1
        elif card.value == "Skip":
            self.next_turn(skip=True)
            return True
        elif card.value == "Draw Two":
            self.next_turn()
            self.current_player().draw_card(self.deck, 2)
            return True
        elif card.value == "Wild Draw Four":
            self.next_turn()
            self.current_player().draw_card(self.deck, 4)
            return True
        self.next_turn()
        return True

    def next_turn(self, skip=False):
        step = 2 if skip else 1
        self.current_player_index = (self.current_player_index + step * self.direction) % len(self.players)

class GameManager:
    def __init__(self):
        self.games = {}  # chat_id -> Game

    def get_game(self, chat_id):
        if chat_id not in self.games:
            self.games[chat_id] = Game()
        return self.games[chat_id]
