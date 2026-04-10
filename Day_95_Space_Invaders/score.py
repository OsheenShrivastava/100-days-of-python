
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(400, -340)

        self.update_display()

    def update_display(self):
        self.clear()
        self.write("Score: {}".format(self.score), align="left", font=("Arial", 20, "bold"))

    def increase_score(self):
        self.score += 20
        self.update_display()