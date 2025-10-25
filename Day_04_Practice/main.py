
# Random Module
import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.my_favourite_number)

# Generate number between 0 and 1
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

random_number_1_to_10 = random.random() * 10
print(random_number_1_to_10)

# Uniform - The range includes both 1 and 10 as well
random_float = random.uniform(1, 10)
print(random_float)

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

# Lists
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "California"]
print(states_of_america[0])
print(states_of_america[4])
print(states_of_america[-2])

states_of_america[1] = "New York"
print(states_of_america)

states_of_america.append("Pittsburgh")
print(states_of_america)

states_of_america.extend(["Osheenland", "Jack Bauer Land"])
print(states_of_america)

friends = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred"]
print(random.choice(friends))

# Index Errors
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "California"]
# print(states_of_america[10])

# Nested Lists
fruits = ["apple", "banana", "cherry", "orange"]
vegetables = ["spinach", "kale", "celery", "potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)