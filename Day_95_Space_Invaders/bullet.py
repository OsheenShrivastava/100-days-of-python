
from turtle import Turtle

class Bullet(Turtle):
    def __init__(self, x, y, direction, speed, color):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_len=0.5, stretch_wid=1.0)
        self.penup()
        self.color(color)
        self.goto(x, y)

        self.direction = direction
        self.speed = speed


    def shoot(self):
        self.sety(self.ycor() + self.direction * self.speed)