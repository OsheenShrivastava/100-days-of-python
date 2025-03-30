from art import logo


# TODO-6 - Create a function to calculate highest bid and bidder

def Calculate_Highest_Bid():
    Highest_bid = 0
    Highest_bid_user = ""

    for key in Auction_Dict:
        if int(Auction_Dict[key]) >= Highest_bid:
            Highest_bid = Auction_Dict[key]
            Highest_bid_user = key

    print(f"The winner is {Highest_bid_user} with a bid of ${Highest_bid}")


# TODO-1 - Print Logo
print(logo)
Auction_Dict = {}
Continue_bidding = True

while Continue_bidding:
    # TODO-2 - Ask for user name and their bid
    name_input = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    # TODO-3 - Store all user names and their bids in a dictionary
    Auction_Dict[name_input] = bid

    # TODO-4 - Ask if there are any other bidders
    Other_users = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    print(Other_users)

    # TODO-5 - If there are more users then continue asking for inputs else calculate Highest Bid and Highest Bid User

    if Other_users == 'yes':
        print('\n' * 100)
    else:
        Calculate_Highest_Bid()
        Continue_bidding = False