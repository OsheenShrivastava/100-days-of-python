
# Function with Inputs

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Osheen")

print("\n")

# Positional Arguments

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Osheen", "Mumbai")

print("\n")

# Keyword Arguments

def Greet_With(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with(name="Osheen", location="Goa")