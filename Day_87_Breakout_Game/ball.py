
from turtle import Turtle, Screen

# Initialize class and super class
class Ball(Turtle):
    def __init__(self, position):
        super().__init__()

        # Create Paddle
        self.shape('circle')
        self.color('grey')
        self.penup()
        self.goto(position)

        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

        self.hit_count = 0

    def move(self):
       new_x = self.xcor() + self.x_move
       new_y = self.ycor() + self.y_move
       self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, -290)
        self.move_speed = 0.1
        self.bounce_y()

    def register_hit(self):
        self.hit_count += 1

    def update_speed(self, brick_color=None):
        # Boost at milestones
        if self.hit_count == 4:
            self.move_speed = max(self.move_speed - 0.002, 0.018)

        if self.hit_count == 12:
            self.move_speed = max(self.move_speed - 0.003, 0.015)

        # Red/orange bricks give extra acceleration
        if brick_color in ("red", "orange"):
            self.move_speed = max(self.move_speed - 0.0015, 0.015)