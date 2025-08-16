import random

COLORS = ["Red", "Yellow", "Green", "Blue"]
VALUES = ["0","1","2","3","4","5","6","7","8","9","Skip","Reverse","Draw Two"]
WILD_CARDS = ["Wild", "Wild Draw Four"]

class UNOGame:
    def __init__(self):
        self.players = []
        self.turn = 0
        self.direction = 1
        self.deck = self.generate_deck()
        self.discard = []
        self.hands = {}
        self.started = False

    def generate_deck(self):
        deck = []
        for color in COLORS:
            deck.append(f"{color} 0")
            for value in VALUES[1:]:
                deck.append(f"{color} {value}")
                deck.append(f"{color} {value}")
        for wc in WILD_CARDS:
            deck.extend([wc] * 4)
        random.shuffle(deck)
        return deck

    def draw_card(self, player, n=1):
        for _ in range(n):
            if not self.deck:
                self.reshuffle()
            self.hands[player].append(self.deck.pop())

    def reshuffle(self):
        self.deck = self.discard[:-1]
        self.discard = [self.discard[-1]]
        random.shuffle(self.deck)

    def add_player(self, player_id):
        if self.started:
            return False
        if player_id not in self.players:
            self.players.append(player_id)
            self.hands[player_id] = []
        return True

    def start_game(self):
        if len(self.players) < 2:
            return False
        self.started = True
        for p in self.players:
            self.draw_card(p, 7)
        first = self.deck.pop()
        while first.startswith("Wild"):
            self.deck.insert(0, first)
            first = self.deck.pop()
        self.discard.append(first)
        return True

    def get_current_player(self):
        return self.players[self.turn]

    def next_turn(self, skip=1):
        self.turn = (self.turn + skip * self.direction) % len(self.players)

    def play_card(self, player, card, chosen_color=None):
        top = self.discard[-1]
        if self.get_current_player() != player:
            return False, "Not your turn!"
        if card not in self.hands[player]:
            return False, "You don’t have this card."
        if not self.valid_play(card, top):
            return False, f"Invalid move. Top card: {top}"
        self.hands[player].remove(card)
        if card.startswith("Wild"):
            card = f"{card} ({chosen_color})" if chosen_color else card
        self.discard.append(card)
        self.apply_action(card, player)
        return True, f"{card} played!"

    def valid_play(self, card, top):
        if card.startswith("Wild"):
            return True
        if "(" in top:
            top = top.split("(")[0].strip()
        return (card.split()[0] == top.split()[0]) or (card.split()[1] == top.split()[1])

    def apply_action(self, card, player):
        if "Skip" in card:
            self.next_turn(2)
            return
        if "Reverse" in card:
            if len(self.players) == 2:
                self.next_turn(2)
            else:
                self.direction *= -1
                self.next_turn()
            return
        if "Draw Two" in card:
            self.next_turn()
            self.draw_card(self.get_current_player(), 2)
            self.next_turn()
            return
        if "Wild Draw Four" in card:
            self.next_turn()
            self.draw_card(self.get_current_player(), 4)
            self.next_turn()
            return
        self.next_turn()
