
from turtle import Turtle
import random

START_Y = 380
MOVE_DISTANCE = 3
MAX_RIGHT = 380
MAX_LEFT = -380


class Monster(Turtle):
    def __init__(self):
        super().__init__()

        # Hide turtle here otherwise it will be seen in the middle of the screen
        self.penup()
        self.hideturtle()  # ✅ VERY IMPORTANT
        self.speed(0)

        self.monsters = []
        self.direction = MOVE_DISTANCE

        y = START_Y

        for j in range(5):

            num_monsters = 8
            spacing = 80
            start_x = - (num_monsters - 1) * spacing / 2

            for i in range(num_monsters):
                x = start_x + i * spacing

                monster = Turtle()
                monster.shape("images/monster.gif")
                monster.penup()
                monster.goto(x, y)

                self.monsters.append(monster)

            y = y - 60


    def move_monsters(self):
        for monster in self.monsters:
            monster.setx(monster.xcor() + self.direction)

        for monster in self.monsters:

            if monster.xcor() > MAX_RIGHT:
                self.direction *= -1
                break

            elif monster.xcor() < MAX_LEFT:
                self.direction *= -1
                break


    def monster_position(self):
        if not self.monsters:
            return None, None
        monster = random.choice(self.monsters)
        return monster.xcor(), monster.ycor()