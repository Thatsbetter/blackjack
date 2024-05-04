from random import shuffle


class Card:
    """Represents a single playing card with a number and suit."""

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_card_value(self):
        if self.value in ['J', 'Q', 'K']:
            return 10
        if self.value == 'Ace':
            return 11
        return self.value

    def suit_to_emoji(self):
        """Maps suit names to emojis."""
        suit_emojis = {
            'Clubs': '♣️',
            'Hearts': '♥️',
            'Diamonds': '♦️',
            'Spades': '♠️'
        }
        return suit_emojis.get(self.suit, '')

    def __str__(self):
        return f" {self.suit_to_emoji()} {self.value} "


class Deck:
    def __init__(self):
        self.cards = []
        self.initialize_deck()

    def initialize_deck(self):
        suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
        values = list(range(2, 11)) + ["J", "Q", "K", "Ace"]
        self.cards = [Card(value, suit) for value in values for suit in suits]
        shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def draw_cards(self, count):
        return [self.draw_card() for _ in range(count)]


class Player:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def add_cards(self, cards):
        self.hand.extend(cards)

    def calculate_score(self):
        total = 0
        aces = 0
        for card in self.hand:
            value = card.get_card_value()
            if card.value == 'Ace':
                aces += 1
            total += value
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def show_hand(self, reveal_all):
        if reveal_all:
            return ', '.join(str(card) for card in self.hand)
        return f"{self.hand[0]}, [ -❓- ]"
#
