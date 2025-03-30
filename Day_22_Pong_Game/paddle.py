
# Import Classes from Modules
from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, position):             # Initialize class
        super().__init__()                    # Initialize super class

        # Create paddle
        self.shape("square")                  # Define Shape of Paddle as square
        self.color("white")                   # Define Colour of Paddle as white
        self.shapesize(stretch_wid=5, stretch_len=1)  # Define Width and Length of Paddle
        self.penup()                          # Lift pen up
        self.goto(position)                   # Go to defined x,y position

    def go_up(self):
        new_y = self.ycor() + 20              # self.ycor() provides the current ycor to which we add 20
        self.goto(self.xcor(), new_y)         # There is no change in xcor so, we use self.xcor() and we shift y by 20

    def go_down(self):
        new_y = self.ycor() - 20              # self.ycor() provides the current ycor to which we subtract 20
        self.goto(self.xcor(), new_y)         # There is no change in xcor so, we use self.xcor() and we shift y by 20







