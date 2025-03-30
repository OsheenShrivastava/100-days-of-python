
# Import Classes from Modules
from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

# TODO-1 - Create a snake body
# TODO-2 - Move the snake
# TODO-3 - Create snake food
# TODO-4 - Detect collision with food
# TODO-5 - Create a scoreboard
# TODO-6 - Detect collision with wall
# TODO-7 - Detect collision with tail

# Define Object Screen from Class Screen
screen = Screen()

# To create a snake
screen.setup(width=600, height=600)         # Define width and height of Turtle Screen
screen.bgcolor("black")                     # Define Background colour of Turtle Screen
screen.title("My Snake Game")               # Define Title of Turtle Screen
screen.tracer(0)                            # Function to turn animation ON/OFF. It set to OFF.

snake = Snake()                             # Define object Snake for Class Snake() to call snake.py file.
food = Food()                               # Define object food for Class Food() to call food.py file
scoreboard = Scoreboard()                   # Define object scoreboard for Class Scoreboard() to call scoreboard.py file

# To create control keys for snake
screen.listen()                             # Sets focus on Turtle Screen to check key events
screen.onkey(snake.up, "Up")                # Calls up function when "Up" key is pressed from snake.py file
screen.onkey(snake.down, "Down")            # Calls down function when "Down" key is pressed from snake.py file
screen.onkey(snake.left, "Left")            # Calls left function when "Left" key is pressed from snake.py file
screen.onkey(snake.right, "Right")          # Calls right function when "Right" key is pressed from snake.py file

# Function to run when game is on
game_is_on = True
while game_is_on:
    screen.update()                         # Performs Turtle Screen update. To be used when tracer is OFF.
    time.sleep(0.1)                         # To update screen every 0.1 sec

    # To move snake forward
    snake.move()                            # Calls move function from snake.py file

    # Detect collision with food
    if snake.head.distance(food) < 15:      # if Snake head distance from food is less than 15
        food.refresh()                      # Calls refresh function from food.py to create new food
        snake.extend()                      # Calls extend function from snake.py to increase length of snake
        scoreboard.increase_score()         # Calls increase_score() function from scoreboard.py to update scoreboard

    # Detect collision with wall
    # Check if head of snake is not colliding with x and y extreme co-ordinates
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()                  # Call reset function from scoreboard.py file to reset scoreboard
        snake.reset()                       # Call reset function from snake.py file to create snake again

    # Detect collision with tail
    # For loop to check throughout length of snake (Slicing is used here [1:])
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:  # To check if distance between snake head and any other segment is < 10
            scoreboard.reset()              # Call reset function from scoreboard.py to reset scoreboard
            snake.reset()                   # Call reset function from snake.py file to create snake again

screen.exitonclick()                        # Function to exit Turtle Screen on click