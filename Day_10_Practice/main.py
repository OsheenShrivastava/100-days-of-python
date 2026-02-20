
# Function with Outputs Return Statements - 1 function

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("Angela", "Yu"))
print("\n")

# Function with Outputs Return Statements - 2 functions

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("angela"))
print(output)
print("\n")

# Multiple Return Values

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name?"), input("What is your last name?")))
print("\n")

# Docstrings

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the
    title case version of the name."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("Angela", "Yu"))
print("\n")