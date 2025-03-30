
# Import Classes from Modules
from turtle import Turtle

ALIGNMENT = 'center'                               # Define Constant Alignment
FONT = ('Arial', 24, 'normal')                     # Define Constant Font


class Scoreboard(Turtle):                  # Create Scoreboard class and inherit Turtle functions making it super class

    def __init__(self):                            # initializer for class
        super().__init__()                         # initializer for super class
        self.score = 0                             # initialize score with 0
        with open("data.txt", mode="r") as file:   # Open the data.txt file to read
            self.high_score = int(file.read())     # Assign the read value from data.txt to high_score
        self.color("white")                        # Define colour as white
        self.penup()                               # Lift pen up
        self.goto(0, 270)                          # Go to top of Screen
        self.hideturtle()                          # Hide turtle
        self.update_scoreboard()                   # Call Update Scoreboard

    def update_scoreboard(self):
        self.clear()                               # Clear Screen
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)   # Update Score

    def reset(self):
        if self.score > self.high_score:           # Check if score is greater than high_score
            self.high_score = self.score           # If true then assign score value to high_score

            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")

        self.score = 0                             # Reset score value
        self.update_scoreboard()                   # Call Update Scoreboard

    def increase_score(self):
        self.score += 1                            # Increment Score
        self.update_scoreboard()                   # Update Scoreboard