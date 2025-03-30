
# Import Classes from Modules
import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# TODO-1 - Move the turtle with keypress
# TODO-2 - Create and move the cars
# TODO-3 - Detect collision with car
# TODO-4 - Detect when turtle reaches the other side
# TODO-5 - Create a scoreboard

# Define Object Screen from Class Screen
screen = Screen()
screen.setup(width=600, height=600)       # Define width and height of Turtle Screen
screen.tracer(0)                          # Function to turn animation ON/OFF. It set to OFF.

# Define Object player from Class Player
player = Player()

# Define Object car_manager from Class CarManager
car_manager = CarManager()

# Define Object scoreboard from Class Scoreboard
scoreboard = Scoreboard()

# Create Control Keys
screen.listen()                           # Sets focus on Turtle Screen to check key events
screen.onkey(player.Up, "Up")             # Calls up function when "Up" key is pressed from player.py file

# Function to run when game is on
game_is_on = True
while game_is_on:
    time.sleep(0.1)                       # To update screen every 0.1 sec
    screen.update()                       # Performs Turtle Screen update. To be used when tracer is OFF.

    car_manager.create_car()              # Call create_car() function from car_manager.py file
    car_manager.move_cars()               # Call move_cars() function from car_manager.py file

    # Detect collision with cars
    for car in car_manager.all_cars:      # for loop to check through all the cars
        if car.distance(player) < 20:     # If distance between cars and player is less than 20 (as 20 is the width)
            game_is_on = False            # exit while game_is_on loop
            scoreboard.game_over()

    # Detect if reached finish line
    if player.is_at_finish_line():
        player.go_to_start()             # Call go_to_start function from player.py file
        car_manager.level_up()           # Call level_up function from car_manager.py file
        scoreboard.increase_level()


screen.exitonclick()