
# Import Classes from Modules
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# TODO-1 - Create the screen
# TODO-2 - Create and move a paddle
# TODO-3 - Create another paddle
# TODO-4 - Create the ball and make it move
# TODO-5 - Detect collision with wall and bounce
# TODO-6 - Detect collision with paddle
# TODO-7 - Detect when paddle misses
# TODO-8 - Keep score

# Define Object Screen from Class Screen
Screen = Screen()

# Create the Pong Game Screen
Screen.setup(height=600, width=800)             # Define width and height of Turtle Screen
Screen.bgcolor("black")                         # Define Background colour of Turtle Screen
Screen.title("Pong")                            # Define Title of Turtle Screen
Screen.tracer(0)                                # Turn Screen Animation OFF

# Define Object r_paddle and l_paddle from Class Paddle()
r_paddle = Paddle((350, 0))                     # Pass x and y cor to Paddle class for right paddle
l_paddle = Paddle((-350, 0))                    # Pass x and y cor to Paddle class for left paddle

# Define Object ball from Class Ball()
ball = Ball()

# Define Object scoreboard from Class Scoreboard()
scoreboard = Scoreboard()

# Screen Keys
Screen.listen()                                 # Sets focus on Turtle Screen to check key events
Screen.onkey(r_paddle.go_up, "Up")              # Calls up function when "Up" key is pressed from snake.py file
Screen.onkey(r_paddle.go_down, "Down")          # Calls down function when "Down" key is pressed from snake.py file
Screen.onkey(l_paddle.go_up, "w")               # Calls up function when "w" key is pressed from snake.py file
Screen.onkey(l_paddle.go_down, "s")             # Calls down function when "s" key is pressed from snake.py file

game_is_on = True                               # Set it True
while game_is_on:                               # While condition is True
    time.sleep(ball.move_speed)                 # Delay
    Screen.update()                             # Update the Screen
    ball.move()                                 # Move the Ball, call function from ball.py

    # Detect collision with top and bottom of Screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()                         # Bounce the Ball in y direction, call function from ball.py

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()                         # Bounce the Ball in x direction, call function from ball.py

    # Detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()                   # Reset the ball position to center and move opposite of its x direction
        scoreboard.l_point()                    # Increase left paddle point

    # Detect when l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()                   # Reset the ball position to center and move opposite of its x direction
        scoreboard.r_point()                    # Increase right paddle point

Screen.exitonclick()                            # Function to exit Turtle Screen on click
