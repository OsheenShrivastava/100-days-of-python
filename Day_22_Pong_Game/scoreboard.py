
# Import Classes from Modules
from turtle import Turtle, Screen


class Scoreboard(Turtle):
    def __init__(self):                          # Initialize class
        super().__init__()                       # Initialize super class
        self.color("white")                      # Define Colour of Scoreboard as white
        self.penup()                             # Lift pen up
        self.hideturtle()                        # Hide Turtle
        self.l_score = 0                         # Define l_score
        self.r_score = 0                         # Define r_score

    def update_scoreboard(self):
        self.clear()                             # Clear previous data
        self.goto(-100, 200)                     # Go to defined x,y position
        self.write(self.l_score, align="center", font=("Courier", 80, "normal")) # Write l_score to scoreboard screen
        self.goto(100, 200)                      # Go to defined x,y position
        self.write(self.r_score, align="center", font=("Courier", 80, "normal")) # Write r_score to scoreboard screen

    def l_point(self):
        self.l_score += 1                        # Increment l_score by 1
        self.update_scoreboard()                 # Call update_scoreboard()

    def r_point(self):
        self.r_score += 1                        # Increment r_score by 1
        self.update_scoreboard()                 # Call update_scoreboard()