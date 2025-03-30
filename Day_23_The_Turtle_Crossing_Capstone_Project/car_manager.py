
# Import Classes from Modules
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]    # Define colours for cars
STARTING_MOVE_DISTANCE = 5                                         # Define Starting Distance to move
MOVE_INCREMENT = 10                                                # Define Increment Value for Distance


class CarManager:                                                  # Create CarManager class
    def __init__(self):                                            # Initializer for class
        self.all_cars = []                                         # List to append all cars created
        self.car_speed = STARTING_MOVE_DISTANCE                    # Create attribute car_speed and assign distance

    def create_car(self):
        random_chance = random.randint(1, 6)                       # To run create_car loop every 6th time
        if random_chance == 1:
            new_car = Turtle("square")                             # Define shape of car as square
            new_car.shapesize(stretch_wid=1, stretch_len=2)        # Define length and width of car
            new_car.penup()                                        # Lift pen up
            new_car.color(random.choice(COLORS))                   # Assign random colour to cars
            y = random.randint(-250, 250)                          # Define boundaries for cars to move
            new_car.goto(300, y)                                   # Define starting position for cars to move
            self.all_cars.append(new_car)                          # Append the new created car to all_cars[] list

    def move_cars(self):
        for car in self.all_cars:                                  # for loop to move all cars
            car.backward(self.car_speed)                           # Move cars with defined distance

    def level_up(self):
        self.car_speed += MOVE_INCREMENT                           # Increment Car Speed by adding Increment factor


