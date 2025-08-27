continue_bidding = True
while continue_bidding:
    bidder_name, bid_amount = get_bid_from_user()
    bidding_record[bidder_name] = bid_amount
    continue_bidding = ask_to_continue()
    if continue_bidding:
        clear_screen()

# Clear once before showing results so only the outcome is visible
clear_screen()
find_highest_bidder(bidding_record)
