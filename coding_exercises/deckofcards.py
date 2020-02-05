"""
OOP Exercise

Introduction

Goal of this exercise is to implement two classes, Card  and Deck .

Specifications:

Card

    Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
    Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
    Card 's __repr__  method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)

Deck

- Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
- Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
- Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards",
"Deck of 12 cards", etc.)
- Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the
deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left
, this method should return a ValueError  with the message "All cards have been dealt".
- Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards
missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".
- shuffle should return the shuffled deck.
- Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the
deck and return that single card.
- Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a
list of cards from the deck and return that list of cards.

"""
from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit} "


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        self.cards = [Card(value, suits) for suits in suits for value in values]
        print(self.cards)

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def _deal(self, num):
        count = self.count()
        actual_cards = min([count, num])
        if count == 0:
            print("No more cards left to dealt")
        cards = self.cards[-actual_cards:]
        self.cards = self.cards[:-actual_cards]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only complete deck can be shuffled")

        shuffle(self.cards)


a = Deck()
a.shuffle()
print(a.cards)
print(a.count())
print(a.deal_hand(49))
print(a.count())
print(a.deal_hand(3))
print(a.count())
print(a.deal_hand(5))
