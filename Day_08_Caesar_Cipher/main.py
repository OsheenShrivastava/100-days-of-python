## Caesar Cipher

# TODO-2 - Import and print the logo from art.py when the program starts.

from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# TODO-1 - Combine the encrypt() and decrypt() functions into a single function called caeser().
#  Use the value of the user chosen direction variable to determine which functionality to use.
#  Call the caesar function instead of encrypt/decrypt and pass in all three variables direction/text/shift.


def caesar(text_input, shift_input, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_input *= -1

    for letter in text_input:

        # TODO-3 - What happens if the user enters a number/symbol/space?

        if letter not in alphabet:
            output_text += letter
        else:
            cipher_text_index = alphabet.index(letter) + shift_input

            cipher_text_index %= len(alphabet)

            output_text += alphabet[cipher_text_index]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-4 - Can you figure out a way to restart the cipher program?

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text_input=text, shift_input=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")