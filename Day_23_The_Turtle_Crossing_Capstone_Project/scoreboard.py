
# Import Classes from Modules
from turtle import Turtle

FONT = ("Courier", 24, "normal")          # Define Font for Scoreboard


class Scoreboard(Turtle):                 # Create Scoreboard class and inherit Turtle functions making it super class
    def __init__(self):                   # Initializer for class
        super().__init__()                # Initializer for super class
        self.level = 1                    # Initialize level with 1
        self.penup()                      # Lift pen up
        self.goto(-280, 250)              # Go to top left of Screen
        self.hideturtle()                 # Hide turtle
        self.update_scoreboard()          # Call Update Scoreboard

    def update_scoreboard(self):
        self.clear()                      # Clear Screen
        self.write(f"Level: {self.level}", align='left', font=FONT)   # Update Score

    def game_over(self):
        self.goto(0, 0)                   # Go to 0,0 position
        self.write(f"GAME OVER", align="center", font=FONT)  # Display GAME OVER

    def increase_level(self):
        self.level += 1                     # Increment Level
        self.update_scoreboard()            # Update Scoreboard