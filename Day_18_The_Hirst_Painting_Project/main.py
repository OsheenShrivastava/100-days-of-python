from turtle import Turtle, Screen
import random

color_list = [(240, 242, 245), (223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159),
              (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84),
              (229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90),
              (110, 99, 87), (193, 187, 46), (240, 204, 2), (1, 102, 119), (19, 22, 21), (50, 150, 109),
              (172, 212, 172), (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210)]

# TODO-1 - Create an object from Turtle Class
Tim = Turtle()

# TODO-2 - Change the shape and colour of Turtle
Tim.shape("turtle")

# TODO-3 - Create an object from Screen Class
My_Screen = Screen()

# TODO-4 - Specify the color values in the range of 0 to 255
My_Screen.colormode(255)

# TODO-5 - Assign speed as fastest, penup and hide the turtle to draw only dots
Tim.speed("fastest")
Tim.penup()
Tim.hideturtle()

# TODO-6 - setheading() function is used to change the direction the turtle is facing. Move
# forward and restore the original position
Tim.setheading(225)
Tim.forward(300)
Tim.setheading(0)
number_of_dots = 100

# TODO-7 - Move the turtle for 10 columns and then change its position to starting and repeat 
# the process

for dot_count in range(1, number_of_dots + 1):
    Tim.dot(20, random.choice(color_list))
    Tim.forward(50)

    if dot_count % 10 == 0:
        Tim.setheading(90)
        Tim.forward(50)
        Tim.setheading(180)
        Tim.forward(500)
        Tim.setheading(0)


My_Screen.exitonclick()