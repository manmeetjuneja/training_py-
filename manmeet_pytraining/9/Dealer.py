from Deck import Deck
from Player import Player


class Dealer(Player):
    def __init__(self):
        Player.__init__(self, "Dealer")
        self.deck = Deck()

    def deal(self, user):
        deck = Deck()

        user.clear_hand()
        self.clear_hand()

        user.add_card(deck.top_card())
        self.add_card(deck.top_card())
        user.add_card(deck.top_card())
        self.add_card(deck.top_card())

        print("\nDealer's face card is:"+str(self.hand.cards[1]))

    def hit(self, user):
        user.add_card(self.deck.top_card())
