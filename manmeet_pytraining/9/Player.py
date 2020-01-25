from Hand import Hand


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = Hand([])

    def add_card(self, card):
        self.hand.add(card)

    def print_hand(self):
        cards = self.hand.cards
        for card in cards:
            print(" "+str(card))

        value = self.hand.eval_hand()
        if len(value) == 1:
            print("Value of hand:"+str(value[0]))
        else:
            print("Value of hand:"+str((value[0])+"  "+str(value[1])))

    def has_blackjack(self):
        aces = [card.rank == "Ace" for card in self.hand.cards]
        tens = [card.val() == 10 for card in self.hand.cards]
        return any(aces) and any(tens)

    def bust(self):
        return self.hand.value > 21

    def clear_hand(self):
        self.hand = Hand([])
