import random

print("Welcome to D Brain Guessing Game!!!")

number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")
# print(number)
choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def running(turn):
    print(f"You have {turn} attempts remaining to guess the number")
    player_number = int(input("Make a guess: "))

    while player_number != number:
        turn -= 1
        print(f"You have {turn} attempts remaining to guess the number")

        if player_number > number:
            print("Too high")
        elif player_number < number:
            print("Too low")

        player_number = int(input("Make a guess: "))

        if turn == 1:
            print("You've run out of guesses, you lose.")
            return
    print(f"You win the answer is {number}")


if choice == "easy":
    turn = 10
    running(turn)
elif choice == "hard":
    turn = 5
    running(turn)
