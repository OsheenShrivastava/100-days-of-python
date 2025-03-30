
# Import Classes from Modules
from turtle import Turtle

STARTING_POSITION = (0, -280)            # Define Starting Position for Turtle
MOVE_DISTANCE = 10                       # Define Distance to be moved by Turtle
FINISH_LINE_Y = 280                      # Define Distance for Finish Line


class Player(Turtle):                    # Create Player class and inherit Turtle functions making it super class
    def __init__(self):                  # Initializer for class
        super().__init__()               # Initializer for super class
        self.shape("turtle")             # Define shape as Turtle
        self.penup()                     # Lift pen up
        self.go_to_start()               # Call go_to_start() function
        self.setheading(90)              # Turn the Turtle facing towards Forward Direction

    def Up(self):
        self.forward(MOVE_DISTANCE)      # Move the Turtle by 10

    def go_to_start(self):
        self.goto(STARTING_POSITION)     # Go to bottom of Screen

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:  # Check if turtle has reached finish line
            return True                  # Return True if condition satisfies
        else:
            return False                 # else False



