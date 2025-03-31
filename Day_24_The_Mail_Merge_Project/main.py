# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# TODO-1 - Create a variable placeholder and store [name] to replace it with actual name
placeholder = "[name]"

# TODO-2 - Read names from invited_names.txt
with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

# TODO-3 - Read the letter and replace [name] with names in invited_names.txt
with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_contents = letter_file.read()

# TODO-4 - Loop through the names and remove spaces and /n using strip method
# TODO-5 - Replace placeholder with names from invited_names
# TODO-6 - Create all letters in ReadyToSend Folder
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(placeholder, stripped_name)
        print(new_letter)

        with open(f"./Output/ReadyToSend/Letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)