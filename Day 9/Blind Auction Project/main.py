import art

WELCOME_MESSAGE = "Welcome to the secret auction program."
ASK_NAME_PROMPT = "What is your name?: "
ASK_BID_PROMPT = "What is your bid?: $"
ASK_CONTINUE_PROMPT = "Are there any other bidders? Type 'yes' or 'no': "


def get_bid_from_user():
    while True:
        bidder_name = input(ASK_NAME_PROMPT).strip()
        if bidder_name:
            break
        print("Name cannot be empty. Please try again.")
    while True:
        raw = input(ASK_BID_PROMPT).strip()
        try:
            bid_amount = int(raw)
            if bid_amount < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid non-negative integer amount.")
    return bidder_name, bid_amount


def ask_to_continue():
    while True:
        answer = input(ASK_CONTINUE_PROMPT).strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Please answer with 'yes' or 'no'.")


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder, bid_amount in bidding_record.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


print(art.logo)
print(WELCOME_MESSAGE)

# Dictionary storing names and bids as key-value pairs
bidding_record = {}

continue_bidding = True
while continue_bidding:
    bidder_name, bid_amount = get_bid_from_user()
    bidding_record[bidder_name] = bid_amount
    continue_bidding = ask_to_continue()

find_highest_bidder(bidding_record)
