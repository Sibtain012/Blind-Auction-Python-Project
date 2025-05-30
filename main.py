from art import logo
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

print(logo)
bid_list = {}
def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for i in bids:
        bid_price = bids[i]
        if bid_price > highest_bid:
            highest_bid = bid_price
            winner = i
    print(f"The winner is {winner} with a bid of ${highest_bid}")


isFalse = False
while not isFalse:
    name = str(input("What is your name?: "))
    price = int(input("What is your bid?: $"))
    bid_list = {name: price}
    more = str(input("Are there any other bidders? Type 'yes' or 'no'.\n")).lower()
    if more == "no":
        isFalse = True
        find_highest_bidder(bid_list)
    elif more == "yes":
        print("\n" * 20)
