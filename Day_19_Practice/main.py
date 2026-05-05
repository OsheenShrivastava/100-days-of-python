
# Event Listeners, Object, Class and State

from turtle import Turtle, Screen

# Here tim is the Object and Turtle() is the Class.
tim = Turtle()

# Here tim.color = green is the state in which the turtle is currently.
tim.color('green')
screen = Screen()

def move_forward():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)


screen.exitonclick()

# Functions as Inputs

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(n1, n2, func):
    return func(n1, n2)

result_1 = calculator(3, 2, add)
result_2 = calculator(3, 2, subtract)
result_3 = calculator(3, 2, multiply)
result_4 = calculator(3, 2, divide)
print(result_1)
print(result_2)
print(result_3)
print(result_4)