rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game_images = [rock, paper, scissors]

# TODO-1 - Checking for user input
user_input = int(input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# TODO-2 - Print user's choice
if user_input >= 0 and user_input <= 2:
    print(game_images[user_input])

# TODO-3 - Generate random elements
Computer_Choice = random.randint(0, 2)

print("Computer chose: ")
print(game_images[Computer_Choice])

# TODO-4 - Print the Final Result after comparing both user and computer's input
if user_input >= 3 or user_input < 0:
    print("You typed an invalid number. You Lose!")
elif user_input == 0 and Computer_Choice == 2:
    print("You Win!")
elif Computer_Choice == 0 and user_input == 2:
    print("You Lose!")
elif Computer_Choice > user_input:
    print("You Lose!")
elif user_input > Computer_Choice:
    print("You win!")
elif Computer_Choice == user_input:
    print("It's a draw!")
