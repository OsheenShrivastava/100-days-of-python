
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 310)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "bold"))

    def add_score(self, points):
        self.score += points
        self.update_score()

    def show_lives(self, lives):
        self.clear()
        self.write(f"Score: {self.score}   Lives: {lives}", align="center", font=("Courier", 22, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "bold"))