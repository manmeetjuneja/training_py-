import random

from Card import Card


class Deck(object):

    def __init__(self):
        self.cards = []

        ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        suits = ["Spades", "Diamonds", "Clubs", "Hearts"]

        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))

        random.shuffle(self.cards)

    def top_card(self):
        top = self.cards.pop()
        return top
