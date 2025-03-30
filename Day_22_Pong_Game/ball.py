
# Import Classes from Modules
from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self):                     # Initialize class
        super().__init__()                  # Initialize super class

        # Create Ball
        self.shape("circle")                # Define Shape of Paddle as square
        self.color("white")                 # Define Colour of Paddle as white
        self.penup()                        # Lift pen up
        self.x_move = 10                    # Defining x position moves
        self.y_move = 10                    # Defining y position moves
        self.move_speed = 0.1               # Define ball speed

    def move(self):
        new_x = self.xcor() + self.x_move   # self.xcor() provides the current xcor to which we add 1
        new_y = self.ycor() + self.y_move   # self.ycor() provides the current ycor to which we add 1
        self.goto(new_x, new_y)             # Go to defined x,y position

    def bounce_y(self):
        self.y_move *= -1                   # Multiply self.y_move with -1 so that we can have -10 and 10 automatically

    def bounce_x(self):
        self.x_move *= -1                   # Multiply self.x_move with -1 so that we can have -10 and 10 automatically
        self.move_speed *= 0.9              # Increase the speed by multiplying it by 0.9

    def reset_position(self):
        self.goto(0, 0)                     # Go to center of the Screen
        self.move_speed = 0.1               # Reset the speed to 0.1
        self.bounce_x()                     # Change x direction