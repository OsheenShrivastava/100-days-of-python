
## The Calculator Project

from art import logo

# TODO-1 - Write add,subtract,multiply and divide functions


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

# TODO-2 - Add these 4 functions inta a dictionary as the values. Keys = "+", "-", "*", "/"


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def Calculator():

    # TODO-10 - Add the logo from art.py
    print(logo)

    Continue = True

    # TODO-3 - Ask the user to type the first number
    First_Number = float(input("What's the first number?: "))

    while Continue:

        # TODO-4 - Ask the user to type a mathematical operator (a choice of "+", "-", "*", or "/")
        Operation = input("+\n-\n*\n/\nPick an operation: ")

        # TODO-5 Ask the user to type the second number
        Second_Number = float(input("What's the next number?: "))

        # TODO-6 - Work out the result based on the chosen mathematical operator.
        Output = operations[Operation](n1=First_Number, n2=Second_Number)
        print(f"{First_Number} {Operation} {Second_Number} = {Output}")

        # TODO-7 - Ask if the user wants to continue working with the previous result
        User_Choice = input(f"Type 'y' to continue calculating with {Output}, or type 'n' to start a new "
                            f"calculation: ").lower()

        if User_Choice == 'y':
            # TODO-8 - if yes, program loops to use the previous result as the first number and then
            #  repeats the calculation process
            First_Number = Output
        else:
            # TODO-9 - If no, program asks the user for the first number again and wipes all memory
            #  of previous calculations
            Continue = False
            print("\n" * 30)

            # Calling a function in itself is called "Recursion".
            Calculator()


# Call Function
Calculator()
