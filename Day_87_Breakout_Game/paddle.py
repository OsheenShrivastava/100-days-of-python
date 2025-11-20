
from turtle import Turtle, Screen

# Initialize class and super class
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        # Create Paddle
        self.shape('square')
        self.color('blue')
        self.shapesize(stretch_wid=1, stretch_len=12)
        self.penup()
        self.goto(position)

        # Paddle boundaries
        # 20(px) x 12 = 240 px
        # Half-width = 120 px
        # Right Limit = 500 - 120 = 380
        # Left Limit = -500 + 120 = -380

        self.left_limit = -380
        self.right_limit = 380

    def go_right(self):
        new_x = self.xcor() + 20

        if new_x < self.right_limit:
            self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20

        if new_x > self.left_limit:
            self.goto(new_x, self.ycor())