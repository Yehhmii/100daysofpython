import os
from art_icon import air

print(air)

def clear_console():
    os.system('cls')

bids = {}
def highest_bidder(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bid_finished = False
while not bid_finished:
    name = input("What is your name?: ")
    bid = int(input("How much would you like to bid?: $"))
    bids[name] = bid
    again = input("Are there other people who want to bid? Type 'yes' or 'no'. \n ").lower()
    if again == "no":
        bid_finished = True
        highest_bidder(bids)
    elif again == "yes":
        clear_console()


