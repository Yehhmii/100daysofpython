import random
import os
# =================== Basic rules for the game ====================
# The deck is unlimited in size
# There are no jokers
# The Jack/Queen/King all counts as 10
# The Ace can count as 1 or 11 .
# The cards in the list have equal probability of being drawn 
# Card are not removed from the deck as they are drawn.

def clear_console():
    os.system('cls')

# to pick a card at random 
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take an input and calculate the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a Draw"
    elif computer_score == 0:
        return "Lose, opponent has a Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over you lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else: 
        return "You lose"

def play_game():
    print("Welcome to Blackjack")
    # to pick the first two cards of the players
    user_cards = []
    computer_cards = []
    is_game_over = False

    for c in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score =  calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            play_again = input("Type 'y' to get another card, type 'n' to pass: ")
            if play_again == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
            
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, finial score: {user_score}")
    print(f" Computer final hand: {computer_cards}, finial score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear_console()
    play_game()
