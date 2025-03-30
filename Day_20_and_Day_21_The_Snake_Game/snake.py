
# Import Classes from Modules
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]      # Define x,y co-ordinates for squares to create snake
MOVE_DISTANCE = 20                                     # Define distance to be moved by snake
UP = 90                                                # Define UP Direction in Degrees (Constant is defined in CAPS)
DOWN = 270                                             # Define DOWN Direction in Degrees
LEFT = 180                                             # Define UP Direction in Degrees
RIGHT = 0                                              # Define UP Direction in Degrees


class Snake:                                           # Create Snake class

    def __init__(self):                                # Initializer for  Snake class
        self.segments = []                             # List to append all 3 squares
        self.create_snake()                            # Call Function to create snake
        self.head = self.segments[0]                   # Defining last square as head to move snake from box 3 to 2 to 1

    def create_snake(self):
        for position in STARTING_POSITIONS:            # For loop to move through all 3 positions to create snake
            self.add_segment(position)                 # Call add_segment Function by passing position variable

    def add_segment(self, position):
        new_segment = Turtle(shape="square")         # Assign a square to new_segment by defining Turtle shape as square
        new_segment.color("white")                     # Define colour as white
        new_segment.penup()                            # Lift Pen up
        new_segment.goto(position)                     # Go to position of first square to place it
        self.segments.append(new_segment)              # Append the square segments list. All 3 squares are appended

    def reset(self):
        for seg in self.segments:                      # for loop to go through all the segments
            seg.goto(1000, 1000)                       # Shift all the segments to a position out of the grid
        self.segments.clear()                          # Clearing all the segments
        self.create_snake()                            # Call Function to create snake
        self.head = self.segments[0]                   # Defining last square as head to move snake from box 3 to 2 to 1

    def extend(self):
        self.add_segment(self.segments[-1].position())

        # First we add add_segment & then we pass square to be added
        # Second we get caught hold of last segment by passing -1 to it
        # as -1 in list indicates last segment
        # Third we add .position to command to get the position of that
        # segment
        # to create a snake

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # FOR loop to move all 3 squares to move snake
            new_x = self.segments[seg_num - 1].xcor()  # Move x-cor of last square to 2nd last square
            new_y = self.segments[seg_num - 1].ycor()  # Move y-cor of last square to 2nd last square
            self.segments[seg_num].goto(new_x, new_y)  # Move that square to new x and y positions
        self.head.forward(MOVE_DISTANCE)               # Move snake forward by distance 20

    def up(self):
        if self.head.heading() != DOWN:                # Check if snake is not moving down
            self.head.setheading(UP)                   # Move it up by setting angle as 90

    def down(self):
        if self.head.heading() != UP:                  # Check if snake is not moving up
            self.head.setheading(DOWN)                 # Move it down by setting angle as 270

    def left(self):
        if self.head.heading() != RIGHT:               # Check if snake is not moving right
            self.head.setheading(LEFT)                 # Move it left by setting angle as 180

    def right(self):
        if self.head.heading() != LEFT:                # Check if snake is not moving left
            self.head.setheading(RIGHT)                # Move it right by setting angle as 0
