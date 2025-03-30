
from turtle import Turtle, Screen
import random

# TODO-1 - Initialize object screen from class Screen
screen = Screen()

# TODO-3 - Set up a screen with desired height and width
screen.setup(width=500, height=400)

is_race_on = False

# TODO-4 - Implement a pop up window to ask for user input and save it
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
print(user_bet)

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# TODO-5 - Initialize object tim from class Turtle, define its shape and its starting position
# TODO-6 - Create 6 turtle for the race

for t in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[t])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[t])
    all_turtles.append(new_turtle)

# TODO-7 - Check for user bet and turn on the race
if user_bet:
    is_race_on = True

while is_race_on:

    # TODO-8 - generate random distance for all turtles

    for turtle in all_turtles:
        # TODO-9 - if any turtle reaches end of the line then print whether user wins or looses
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# TODO-2 - Disable screen on click function
screen.exitonclick()