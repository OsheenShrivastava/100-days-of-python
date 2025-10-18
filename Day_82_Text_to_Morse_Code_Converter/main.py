
# TODO-1 - Take text input from user and convert it to Uppercase.
# TODO-2 - Use FOR loop to decode code for each alphabet in the string from predefined morse codes dictionary.
# TODO-3 - Create the final string with Morse codes extracted from the given input.


Morse_Codes = {
    # Letters
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",   "E": ".",
    "F": "..-.",  "G": "--.",   "H": "....",  "I": "..",    "J": ".---",
    "K": "-.-",   "L": ".-..",  "M": "--",    "N": "-.",    "O": "---",
    "P": ".--.",  "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",  "Y": "-.--",
    "Z": "--..",

    # Numbers
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
}


User_Input = input("Enter the code ").upper()
print(User_Input)

Output = ''

for letter in User_Input:
    if letter in Morse_Codes:
        Output += Morse_Codes[letter]
        Output += ' '
print(Output)