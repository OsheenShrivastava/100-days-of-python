
# Dictionary

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
print(programming_dictionary["Bug"])
print("\n")

# Adding an item to dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)
print("\n")

# Edit an item in dictionary

programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)
print("\n")

# Loop through a disctionary

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary)
    print("\n")

# Empty dictionary

programming_dictionary = {}
print(programming_dictionary)
print("\n")

# Nesting List in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}
print(travel_log["France"])
print("\n")

# Nested List

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2])
print(nested_list[2][1])
print("\n")

# Nested Dictionaries

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}
print(travel_log["Germany"]["cities_visited"][2])
print("\n")