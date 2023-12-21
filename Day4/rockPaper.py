import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print('Welcome to Rock Paper and Scissors')
choice = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n')
choice_int = int(choice)

if choice_int >= 3 or choice_int < 0:
    print('Wrong input, You lose!')
else:
    game = [rock, paper, scissors]

    you = print(game[choice_int])

    ran_num = random.randint(0,2)
    computer = game[ran_num]
    print(f"Computer chose: \n {computer}")


    if choice_int == 0 and ran_num == 2:
        print('You Win!')
    elif choice_int == 2 and ran_num == 0:
        print('You Lose!')
    elif ran_num > choice_int:
        print('You Lose!')
    elif choice_int > ran_num:
        print('You Win!')
    elif choice_int == ran_num:
        print('You Draw!')
