
from turtle import Turtle

class Life(Turtle):
    def __init__(self):
        super().__init__()

        self.lives = 3

        self.hideturtle()
        self.penup()
        self.color("red")
        self.goto(-400, -340)

        self.update_display()

    def update_display(self):
        self.clear()
        self.write("❤️" * self.lives, align="left", font=("Arial", 20, "bold"))

    def lose_life(self):
        self.lives -= 1
        self.update_display()