
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO-1 - Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(dict)

# TODO-2 - Create a list of the phonetic code words from a word that the user inputs.

# Method 1 using dataframe comprehension without exceptions

# word = input("Enter a word: ").upper()
# output_list = [dict[letter] for letter in word]
# print(output_list)

# Method 2 using dataframe comprehension using exceptions


def generate_phonetic():
    word = input("Enter a word: ").upper()
    # TODO-3 - Create a function called generate_phonetic()
    # TODO-4 - Use try: to create a list from the word user entered
    # TODO-5 - Unless add an exception using except: that word should only contain letters
    #  and call the function again
    # TODO-6 - else: print the output_list
    try:
        output_list = [dict[letter] for letter in word]
    except KeyError:
        print(f"Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
