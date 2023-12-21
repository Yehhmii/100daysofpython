import random
from hangMan_word import word_list
from hangMan_art import stages, logo

print(logo)
chosen_word = random.choice(word_list)
# print(chosen_word)

lives = 6

display = []
for _ in chosen_word:
    display += "_"

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: \n").lower()
    # clear() trying to clear the console

    if guess in display:
        print(f"You've already guessed: {guess}")

# checking the guessed letter 
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word you lose a life.")
        lives -= 1
    if lives == 0:
        end_of_game = True
        print("You lose")

    print(f"{' '.join(display)}")

# check if user has gotten all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])

