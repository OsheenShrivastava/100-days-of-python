print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
__________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# TODO-1 - Add ASCII art enclosed in r""" """. Print Welcome message and mission.
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# TODO-2 - Ask the user his choice of direction "left" or "right". Add lower() function at the end to convert input to
#  lower case to avoid errors.
choice1 = input("You're at a crossroad, where do you want to go?"
                " Type 'left' or 'right'. ").lower()

# TODO-3 - If user chooses "left: then ask for "swim" or "wait". If "right" is choosen then print Game Over.
if choice1 == "left":
    choice2 = input("You've come to a lake."
                    "There is an island in the middle of the lake."
                    "Type 'wait' to wait for a boat."
                    "Type 'swim' to swim accross.").lower()

    # TODO-4 - If user chooses "wait" then ask for door selection - "red" or "yellow" oe "blue". If "swim" is choosen
    #  then print Game Over.
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed."
                        "There is house with 3 doors. One red,"
                        "one yellow and one blue. "
                        "Which colour do you choose?").lower()

        # TODO-5 - If user chooses "red" then print Game Over, if "yellow" then print You Win! and if "blue" then print
        #  Game Over.
        # TODO-6 - If anything else apart from the options is given by the user then print Game Over.
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts/ Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an agry trout. Game Over.")
else:
    print("You fell in to a hole. Game Over.")