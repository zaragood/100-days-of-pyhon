import os

#function that clears the terminal for the next bidder
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

from art1 import logo
print(logo)

#delare an empty dictionary
bidders = {}

#function that adds to our dictionary the key and value
def add_new_bider(name, bid):
    bidders[name] = bid

#function that checkes for the highest bidder
def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for key in bidding_record:
        bid_amount = bidding_record[key]
        bid_amount_int = int(bid_amount)
        if bid_amount_int > highest_bid:
            highest_bid = bid_amount_int
            winner = key
    print(f"The winner is {winner} with the highest bid of {highest_bid}")

#condition to keep the loop running depending on the user input
choice = False
while choice:
    name_key = input("what is your name? ")
    bid_value = input("what's your bid? $") 
    
    #adding to our dictionary by calling our function
    add_new_bider(name_key, bid_value)
    
    #ask the user if there is another bidder
    user_choice = input("Is there another bidder? 'Yes' / 'No? ").lower()
    if user_choice == "yes":
        choice = False
        
        #call the clear function to clear the terminal
        clear_terminal()
    elif user_choice == "no":
        highest_bidder(bidders)
        choice = True
    else:
        print("invalide respond! try again")
        choice = False
        
        

