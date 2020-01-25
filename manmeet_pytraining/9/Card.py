class Card(object):

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def val(self):
        card_rank = self.rank
        value = 0

        if card_rank == "Ace":
            value = 11
        elif card_rank == "Two":
            value = 2
        elif card_rank == "Three":
            value = 3
        elif card_rank == "Four":
            value = 4
        elif card_rank == "Five":
            value = 5
        elif card_rank == "Six":
            value = 6
        elif card_rank == "Seven":
            value = 7
        elif card_rank == "Eight":
            value = 8
        elif card_rank == "Nine":
            value = 9
        elif card_rank == "Ten" \
                or card_rank == "Jack" \
                or card_rank == "Queen" \
                or card_rank == "King":
            value = 10

        return value

    def __str__(self):
        return(str((self.rank, self.suit)))
