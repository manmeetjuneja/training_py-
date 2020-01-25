import time

from Dealer import Dealer
from User import User

# Introduction
print("Welcome to Game:\n")
name =str(input("Enter your name: "))
print("cards are being shuffled..."+str(name))
print("Press enter to begin the game!!!!!!!!")


# Create players
user = User(name, 100)
dealer = Dealer()
i = 0

while user.bank > 0:
    i += 1
    input()
    print("\n--------Game %d---------- "+str(i))


    bet = int(input("%s (Rs:%d), place your bet: " % (user.name, user.bank)))
    user.place_bet(bet)

    dealer.deal(user)
    if dealer.has_blackjack():
        dealer.print_hand()
        print("Dealer wins with a blackjack.")
        continue

    if user.has_blackjack():
        user.print_hand()
        print("Blackjack!")
        user.payout(int(bet * 2.5))
        continue

    stand = False
    busted = False

    # Action round
    while not stand:
        print("\nYour hand:")
        user.print_hand()

        if user.bust():
            print("Busted!")
            busted = True
            break

        action =input("Pres Hit(H) or Stand(S): ").lower()
        if action == "h":
            dealer.hit(user)
        elif action == "s":
            stand = True

    if busted:
        continue

    # Dealer cards
    print("-----")
    print("Dealer cards:")
    dealer.print_hand()

    while dealer.hand.value < 17:
        time.sleep(2)
        print("\nDealer hits:")
        dealer.hit(dealer)
        dealer.print_hand()

    if dealer.bust():
        print("Dealer busted!")
        user.payout(bet * 2)
    else:
        if dealer.hand.value > user.hand.value:
            print("Dealer won!")
        elif dealer.hand.value < user.hand.value:
            print("You won!")
            user.payout(bet * 2)
        else:
            print("Tie")
            user.payout(bet)
