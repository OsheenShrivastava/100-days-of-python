
# TODO-1 - Import randint from random. Create another file named art.py. Add the logo in it enclosed within 'r' which
#  tells python don't treat backslashes as escape characters. Import logo from art.py file.
# TODO-2 - Define constants for difficulty levels: EASY_LEVEL_TURNS → 10 and HARD_LEVEL_TURNS → 5.
# TODO-3 - Create a function named 'check_answer'. Pass user_guess, actual_answer and turns to it. Compare user guess
#  with actual answer, if guess > answer then print "Too high", reduce the turns by 1 and return it.
# TODO-4 - If guess < answer then print "Too low", reduce the turns by 1 and return it. Else if the answer is correct
#  then print success message with actual answer.
# TODO-5 - Create a function 'set_difficulty'. Ask user to choose 'easy' or 'hard'. If easy is choosen then return
#  EASY_LEVEL_TURNS else return HARD_LEVEL_TURNS.
# TODO-6 - Create another function 'game'. Display logo. Print welcome message and generate a number between 1 and 100.
#  Set difficulty by call set_difficulty() function and assigning the return of this function to variable turns.
# TODO-7 - Initialize guess variable with 0.
# TODO-8 - Add a while loop and check while guess != answer: to continue the loop running. Print remaining turns, take
#  the user's guess as input and store it to a variable guess.
# TODO-9 - Call check_answer() function by passing guess, answer and turns. Store the returned result in turns.
# TODO-10 - Check if player has run out of turns, If turns == 0 → print losing message and exit game. Else check if
#  guess != answer, if true then prompt user to try again.
# TODO-11 - Call the game function to start execution.



from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")



def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS



def game():
    print(logo)

    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")



game()