
from art import logo, vs
from game_data import data
import random


def Choose_Random_Question():
    Question = random.choice(data)
    return Question


# TODO-1 - print logo
print(logo)

Score = 0
game_continue = True

# TODO-2 - Choose Random A and B from the list
Question_B = Choose_Random_Question()

# TODO-6 - Find out who has more followers


def Check_greater_follower_count(Q_A, Q_B):
    if Q_A['follower_count'] > Q_B['follower_count']:
        return 'a'
    else:
        return 'b'


while game_continue:

    Question_A = Question_B

    # TODO-3 - Store A and B from list and store it in Compare A and Against B variable
    Question_B = Choose_Random_Question()

    while Question_B == Question_A:
        Question_B = Choose_Random_Question()

    Final_Question_A = f"Compare A: {Question_A['name']}, a {Question_A['description']}, from {Question_A['country']}"
    Final_Question_B = f"Against B: {Question_B['name']}, a {Question_B['description']}, from {Question_B['country']}"

    print(Final_Question_A)

    # TODO-4 - Print A then VS Symbol then B
    print(vs)

    print(Final_Question_B)

    # TODO-5 - Ask the user "Who has more followers? Type 'A' or 'B': " and store the result
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    Actual_answer = Check_greater_follower_count(Q_A=Question_A, Q_B=Question_B)

    # TODO-9 - Clear screen between rounds
    print("\n" * 20)
    print(logo)

    # TODO-7 - If its correct then print "You're right! Current score: 2." i.e. Increment the
    #  score by 1. Store question with lower followers question in A and generate new question for B. Repeat from
    #  step TODO-3

    if user_input == Actual_answer:
        Score += 1
        print(f"You're right! Current score: {Score}")
    else:
        # TODO-8 - If the answer is wrong then clear screen except for log and print "Sorry, that's
        #  wrong. Final Score: 0"

        game_continue = False

        print(f"Sorry, that's wrong. Final score: {Score}")