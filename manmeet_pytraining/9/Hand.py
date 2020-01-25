class Hand(object):

    def __init__(self, cards):
        self.cards = cards
        self.value = 0  # If multiple values are possible (i.e. hand contains an ace), value is the lower of the two

    def add(self, card):
        self.cards.append(card)

    def eval_hand(self):
        aces_count = 0
        self.value = 0
        for card in self.cards:
            self.value += card.val()
            if card.rank == "Ace":
                aces_count += 1

        if aces_count == 0:  # No aces - return normal value
            return [self.value]
        elif (aces_count == 1 and self.value > 21) or aces_count == 2:  # One ace with bust or two aces: count ace as 1
            self.value -= 10
            return [self.value]
        else:  # One ace and no bust
            self.value -= 10
            return [self.value + 10, self.value]
