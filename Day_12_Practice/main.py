
# Namespace - Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# Below string will give error
# print(potion_strength)
print("\n")

# Namespace - Global Scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
print("\n")

# Block Scope
# new_enemy will never be printed and this is called block scope.
game_level = 2

enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)
# print("\n")

# Modify Global Variable
enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
print("\n")

# Global Constants
PI = 3.14159
GOOGLE_URL = "https://www.google.com"

def my_func():
    print(PI)
    print(GOOGLE_URL)

my_func()