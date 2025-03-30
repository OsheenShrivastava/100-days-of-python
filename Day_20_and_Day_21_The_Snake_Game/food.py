
# Import Classes from Modules
from turtle import Turtle
import random


class Food(Turtle):                           # Create Food class and inherit Turtle functions making it super class

    def __init__(self):                       # initializer for class
        super().__init__()                    # initializer for super class
        self.shape("circle")                  # Define shape of food as circle
        self.penup()                          # Lift pen up
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Define length and width of circle
        self.color("blue")                    # Define colour of food as blue
        self.speed("fastest")                 # Define speed of forming as fastest
        self.refresh()                        # Call refresh function to place food at a random place

    def refresh(self):
        random_x = random.randint(-280, 280)  # Create random x position variable
        random_y = random.randint(-280, 280)  # Create random y position variable
        self.goto(random_x, random_y)         # Go to that position

