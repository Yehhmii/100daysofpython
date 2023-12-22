from art import logo, vs
from game_data import data
import random
import os

def clear_console():
    os.system('cls')



def data_option(random_option):
    """Takes the accounts data and returns a printable format."""
    account_name = random_option["name"]
    account_descrip = random_option["description"]
    account_country = random_option["country"]
    return f"{account_name}, a {account_descrip}, from {account_country}"

# winner is determined by number of followers 
def winner():
    """checkes if the users choice is correct"""
    # 5 who has more followers? type a or b
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    f1 = random_option1['follower_count']
    f2 = random_option2['follower_count']
    print(f1, f2)

    if f1 > f2:
        return choice == "a"
    else:
        return choice == "b"
    # alternative shorter code .........................
    # if choice == 'a':
    #     if f1 > f2:
    #         score += 1
    #         print(f"You're right. Current score is: {score}")
    #     else:
    #         print(f"Sorry, that's wrong. Final score: {score}")
    #         return
    # elif choice == 'b':
    #     if f2 > f1:
    #         score += 1
    #         print(f"You're right. Current score is: {score}")
    #     else:
    #         print(f"Sorry, that's wrong. Final score: {score}")
    #         return
 
# 1 call the logo 
print(logo) 
score = 0
random_option2 = random.choice(data)


game_continue = True
while game_continue:   
    # compare 2 ppl at random

    # after comparing a with b, if right b becomes position of a and a is removed from the list and a new entry at position b 
    random_option1 = random_option2
    random_option2 = random.choice(data)
    if random_option1 == random_option2:
        random_option2 = random.choice(data)

    # 2 compare a: name, title and from without num of followers 
    option1 = f"Compare A: {data_option(random_option1)}."
    print(option1)
    # 3 vs logo 
    print(vs)
    # 4 against b: name, title and from without num of followers
    option2 = f"Against B: {data_option(random_option2)}."
    print(option2)
    
    is_correct = winner()

    clear_console()
    print(logo)
    
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")





#  if right print current score: and put incresing till fail at top





# 6 if wrong end game and print final score at buttom: