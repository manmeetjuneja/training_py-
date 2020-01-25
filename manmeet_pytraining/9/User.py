from Player import Player


class User(Player):
    def __init__(self, name, bank):
        Player.__init__(self, name)
        self.bank = bank

    def place_bet(self, bet):
        self.bank -= bet

    def payout(self, payout):
        self.bank += payout
        print("\nYou won £%d!"+str(payout))
