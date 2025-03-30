## Password_List Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# TODO-1 - Create a Password List and append all the letters,symbols and numbers randomly from list as per user input

Password_List = []
Final_Password = ""

for Letter in range(0, nr_letters):
    Password_List.append(random.choice(letters))

for Symbol in range(0, nr_symbols):
    Password_List.append(random.choice(symbols))

for Number in range(0, nr_numbers):
    Password_List.append(random.choice(numbers))

# TODO-2 - Shuffle the Password List

random.shuffle(Password_List)

# TODO-3 - Create the Final Password

for char in Password_List:
    Final_Password += char

print(f"Your password is: {Final_Password}")