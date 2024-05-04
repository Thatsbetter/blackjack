from random import randint

from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        self.initialize_deck()

    def initialize_deck(self):
        suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
        values = list(range(2, 11)) + ["J", "Q", "K", "Ace"]
        self.cards = [Card((value), suit) for suit in suits for value in values]
        shuffle(self.cards)  # Shuffle deck on initialization

    def draw_card(self):
        if not self.cards:
            self.initialize_deck()  # Reinitialize deck if empty
        return self.cards.pop()
class Card:
    """Represents a single playing card with a number and suit."""
    def __init__(self, number=None, suit=None):
        self.number = number
        self.suit = suit

    def get_card_value(self):
        if self.number in ['J', 'Q', 'K']:
            return 10
        elif self.number == 'Ace':
            return 11  # Handling the value of Ace appropriately will be done in Player class
        else:
            return self.number

    def __str__(self):
        return f"{self.number} of {self.suit}"

    def __str__(self):
        return f"{self.number} of {self.suit}"

class Cards:
    """Collection of playing cards."""
    def __init__(self):
        self.list = []
        self.suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
        self.initialize_deck()

    def initialize_deck(self):
        """Populates a standard deck of cards."""
        for suit in self.suits:
            for i in range(2, 11):
                self.list.append(Card(i, suit))
            for j in ["J", "Q", "K", "Ace"]:
                self.list.append(Card(j, suit))

class Player:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def calculate_score(self):
        total = 0
        aces = 0
        for card in self.hand:
            if card.number == 'Ace':
                aces += 1
            total += card.get_card_value()
        while total > 21 and aces:
            total -= 10  # Counting Ace as 1 instead of 11
            aces -= 1
        return total

    def show_hand(self, reveal_all=False):
        if reveal_all:
            return ', '.join(str(card) for card in self.hand)
        return str(self.hand[0]) + ', [hidden]'