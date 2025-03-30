## Hangman

import random

# TODO-10 - Update the word list to use the 'word_list' from hangman_words.py

from hangman_words import word_list
from hangman_art import stages, logo

# TODO-7 Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
lives = 6

# TODO-11 - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

chosen_word = random.choice(word_list)

# TODO-3 - Create a "placeholder with the same number of blanks as the chosen word

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += '_'

print(F"Word to guess: {placeholder}")

# TODO-5 Use a while loop to let user guess again

game_over = False
correct_letters = []

while not game_over:

    # TODO-12 - Update the code below to tell user how many lives they have left.

    print(f"****************************{lives}/6 LIVES LEFT**********************************")

    # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

    guess = input("Guess a letter: ").lower()

    # TODO-10 - If the user has entered a letter they've already guessed, print the letter and let them know.

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    # TODO-4 - Create a "display" that puts the guess letter in the right positions and _ in the rest of the string

    display = ""

    # TODO-6 - Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'

    print("Word to guess: " + display)

    # TODO-8 - If guess is not a letter in the chosen_word, then reduce lives by 1.
    #  If lives foes down to 0 then the game should end, and it should print "You lose".

    if guess not in chosen_word:
        lives -= 1

        # TODO-11 - If the letter is not in the chosen_word, print out the letter and let them know it's not the word.
        #  e.g. You guessed d, that's not in the word. You lose a life.

        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            # TODO-13 - Update the print statement below to give user the correct word they were trying to guess.
            print(f"**********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print(f"**********************YOU WIN**********************")

    # TODO-9 - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has
    #  remaining.

    print(stages[lives])