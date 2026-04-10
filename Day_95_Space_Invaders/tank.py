
from turtle import Turtle

START_POSITION = (0, -280)
MOVE_DISTANCE = 25
MAX_LEFT = -360
MAX_RIGHT = 360


class Tank(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("images/tank.gif")
        self.color("green")
        self.penup()
        self.goto(START_POSITION)
        self.setheading(90)


    def move_left(self):
        if self.xcor() > MAX_LEFT:
            self.setx(self.xcor() - MOVE_DISTANCE)


    def move_right(self):
        if self.xcor() < MAX_RIGHT:
            self.setx(self.xcor() + MOVE_DISTANCE)


    def start_position(self):
        self.penup()
        self.goto(START_POSITION)
        self.setheading(90)