
from turtle import Turtle, Screen

# Initialize class and super class
class Bricks(Turtle):
    def __init__(self):
        super().__init__()

        self.bricks_list = []
        self.color_list = ['red', 'orange', 'green', 'yellow']
        self.color_num = 0

    def make_bricks(self, start_x, start_y):
        brick_width = 80
        gap = 10
        final_width = brick_width + gap

        for x in range(4):
            for loop in range(2):
                # Create bricks
                for i in range(11):
                    x = start_x + i * final_width

                    # Create bricks
                    brick = Turtle()
                    brick.shape("square")
                    brick.color(self.color_list[self.color_num])
                    brick.shapesize(stretch_wid=2, stretch_len=4)
                    brick.penup()
                    brick.goto(x, start_y)

                    self.bricks_list.append(brick)

                start_y = start_y - 40 - gap
            self.color_num += 1


