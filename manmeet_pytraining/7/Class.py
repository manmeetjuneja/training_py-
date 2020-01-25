import random as rd
class Coin:
    def __init__(self):
        self.sideup="Heads"
    def toss(self):
        if rd.randint(0,1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"

    def get_sideup(self):
        return self.sideup
        
def main():
    obj1 = Coin()
    print(obj1.toss())
    print(obj1.get_sideup())

main()
