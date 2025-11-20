# main.py
# TODO-1 - Import class Screen from module turtle.
# TODO-2 - Create an object screen from class Screen().
# TODO-3 - Set up the screen with height=700, width=1000, bgcolor=black, title=Breakout Game.
# TODO-4 - Turn OFF screen tracer to avoid showing animation of bricks.
# TODO-5 - Add exitonclick() function to exit screen when clicked. Test and run the code written uptil now.
# TODO-6 - Create start_x = -453 and start_y = 270. Import Bricks from bricks and create brick_wall object from class
#  Bricks().
# TODO-7 - Using brick_wall call make_bricks() function and pass start_x and start_x variables into this function.
# TODO-8 - Import Paddle from paddle, create paddle object from class Paddle() and pass default position as (0, -330).
# TODO-9 - Initialise screen.listen() function. Use screen.onkey() functions for "left" and "right" keys of keyboard.
# TODO-10 - Add paddle.go_right function and define its key as "Right". Add paddle.go_left function and define its key
#  as "Left".
# TODO-11 - Import Ball from ball, create ball object from class Ball((0, -290)) and pass these co-ordinates.
# TODO-12 - Add variable game_is_on and set it to True. Check while game_is_on: condition which will be true in order
#  to run this loop continuously.
# TODO-13 - Import time. Inside while loop add time.sleep(ball.move_speed) to provide a delay between ball movement.
# TODO-14 - Update the screen using screen.update() and move the ball by calling ball.move() function.
# TODO-15 - Detect Collison with left and right side of the wall by checking if ball.xcor() (x co-ordinate of ball) is
#  greator than 480 or less than -480. If true then call ball.bounce_x() function to bounce ball in x direction.
# TODO-16 - Detect Collison with top of the wall by checking if ball.ycor() (y co-ordinate of ball) is greator than 330.
#  If true then call ball.bounce_y() function to bounce ball in y direction.
# TODO-17 - Detect collision with paddle by checking if distance between ball and paddle is less than 140 and if
#  ball.ycor() (y co-ordinate of ball) is less than -300. If true then ball.bounce_y() function to bounce ball in y
#  direction. stretch_len = 12 → width = 12 × 20 = 240 px so Half-width = 120 px, therefore 140.
# TODO-18 - To avoid ball overlapping the paddle, push the ball slightly above the paddle. Send the ball using goto
#  function to current x co-ordinate of ball and current y co-ordinate of paddle + 20.
# TODO-19 - Detect collision with bricks. Run a FOR loop over bricks_list in briccks.py. Check if distance between ball
#  and brick is less than 50. If yes then force the ball to move downward by assigning ball.y_move equal to
#  -abs(ball.y_move).
# TODO-20 - abs(ball.y_move) - Takes the absolute value and Makes sure the number is positive e.g., If y_move = -5 →
#  abs(-5) = 5. Now -abs(ball.y_move) - Makes it negative, always so the ball always goes downward.
#  TODO-21 - To remove bricks that are hit by the ball send bricks to a location invisible to user like
#   brick.goto(2000, 2000) and remove that brick from bricks_list using brick_wall.bricks_list.remove(brick).
# TODO-22 - Now we need to keep an account of number of hits. Inside code of Detect collision with paddle after bouncing
#  the ball call ball.register_hit() function from ball.py to count number of hits.
# TODO-23 - We also need to update the speed if hits are greator than 4 or greator then 12 or if the ball hits red or
#  orange brick. So call ball.update_speed() function from ball.py and don't pass any variable keeping it "None". Add
#  this in Detect collision with paddle after calling ball.register_hit().
# TODO-24 - These 2 conditions have to be followed when detecting collision with bricks. So add ball.register_hit() and
#  ball.update_speed(brick_color) before removing the bricks. Here brick_color is passing since we are checking if ball
#  has hit red or orange brick. Points are incremented accordingly if true.
# TODO-25 - To realise score according to color create score_map = {"yellow": 1,"green": 3,"orange": 5,"red": 7,} after
#  initialising all the objects from classes in main.py file.
# TODO-26 - Inside Detect collision with bricks we will add scoring part according to brick color after ball hits a
#  brick and moves downward. Get current brick_color by calling brick.color()[0]. brick.color() returns a tuple of two
#  items:(fill_color, outline_color). brick_color = brick.color()[0] selects the fill color as [0] means “take the first
#  item in the tuple”.
# TODO-27 - Now store the points by finding the points count from score_map created for all 4 colors. Calculate points
#  by doing this --> score_map[brick_color]. Send current brick_color to score_map which will search the color and
#  assign the points accordingly.
# TODO-28 - Now we will need a scoreboard to display those points. So call add_score function and pass points to it like
#  this --> scoreboard.add_score(points).
# TODO-29 - Import Scoreboard from scoreboard, create scoreboard object from class Scoreboard().
# TODO-30 - Add these variables in main.py after initialisation of all classes lives = 3, game_over = False and
#  win = False.
# TODO-31 - Now we will detect if ball misses the paddle. So under Detect Ball Miss check if ball.ycor() < -360 i.e.,
#  ball missed the paddle. If true, then decrease lives by 1 and call show_lives() function from scoreboard.py and pass
#  in lives variable to display remaining lives.
# TODO-32 - Check if lives > 0, if true then add a delay of 1 sec using time.sleep(1) and call ball.reset_position() to
#  reset ball's position to its default position.
# TODO-33 - if all lives are over then, set game_over = True and game_is_on = False. Hide the ball and paddle using
#  ball.hideturtle() and paddle.hideturtle(). To hide bricks run a FOR loop through bricks_list and hide it.
#  for brick in brick_wall.bricks_list:
#    brick.hideturtle()
# TODO-34 - Update screen using screen.update() and call game_over() function from scoreboard.py to display game over
#  on the screen.
# TODO-35 - Now we need to check if all bricks are broken i.e., player won for that run FOR loop over brick_list and
#  check if it iss length is equal to 0 --> if len(brick_wall.bricks_list) == 0:. If true then game_is_on = False,
#  game_over = True and win = True. Again follow above steps to hide ball, paddle, bricks and screen.update() to display
#  winning message on screen.
# TODO-36 - Now to display winning message or restart the game we need to import Turtle from turtle. Check if game_over:
#  if true then create object msg from Turtle() class, hide turtle --> msg.hideturtle(), set its color to white, penup()
#  and goto position (0, 20).
# TODO-37 - Check if win:. if true then write the message --> msg.write("🎉 YOU WON! 🎉", align="center",
#  font=("Courier", 28, "bold")).
# TODO-38 - Now to restart create another object restart_turtle from Turtle() class, hide it, set its color to white,
#  penup() and goto (0 -50). Then write --> "CLICK TO RESTART", align="center", font=("Courier", 20, "bold").
# TODO-39 - Remove exitonclick() function and Add screen.onclick(lambda x, y: restart()) to display the screen with
#  wall,ball and paddle when restart is clicked.
# TODO-40 - Create a function restart() function. Add screen.bye() which closes the Turtle graphics window immediately.
#  It shuts down the game window and stops the current turtle event loop. Import subprocess and use
#  subprocess.call(["python", "main.py"]) to start a new process, run your game again by executing main.py. It’s like
#  restarting the program from scratch.

# bricks.py
# TODO-41 - Create bricks.py file. Inside the file import Turtle and Screen from turtle module.
# TODO-42 - Create class Bricks. Insert Turtle class so Bricks class becomes a Turtle objext and inherits all properties
#  from Turtle.
# TODO-43 - Initialise the class. Also initialise super class for Turtle.
# TODO-44 - Create class variables --- self.bricks_list = [], self.color_list = ['red', 'orange', 'green', 'yellow'] and
#  self.color_num = 0.
# TODO-45 - Create a function of this class named make_bricks() and receive starting x and y positions for the brick.
# TODO-46 - Define brick_width = 80, gap between bricks as gap = 10 and calculate final_width = brick_width + gap.
# TODO-47 - Use 3 nested FOR loops --- 1st one runs 4 times to create 8 rows, 2nd one runs 2 times to create 2 rows of
#  each color and 3rd runs for 11 times to create bricks along the row. In total this creates 8 rows with 2 rows of
#  each color laying 11 bricks in each row.
# TODO-48 - Inside 3rd FOR loop calculate x position by adding current brick no and multiplying it with final width.
# TODO-49 - Create bricks by creating object brick from Turtle() class. Define its shape to square, color using
#  self.color_list and inserting self.color_num so that 2 rows of each color can be created.
# TODO-50 - Stretch its shape by stretch_wid=2 and stretch_len=4 using shapesize function.
# TODO-51 - Use penup() function and goto(x, start_y) position to create 1st brick. Append each brick to bricks_list.
# TODO-52 - Once all 11 bricks are created calculate start_y position by subtracting 40 and gap between bricks.
# TODO-53 - Once 2 rows of 1st color are created increment color_num to move on to next color. Repeat the same process
#  for all 8 rows.

# paddle.py
# TODO-54 - Create paddle.py file. Inside the file import Turtle and Screen from turtle module.
# TODO-55 - Create class Paddle. Insert Turtle class so Paddle class becomes a Turtle objext and inherits all properties
#  from Turtle.
# TODO-56 - Initialise the class. Also initialise super class for Turtle. Receive starting x_position for the paddle.
# TODO-57 - Create the paddle inside the class. Define its shape to square, color to blue, Stretch its shape by
#  stretch_wid=1 and stretch_len=12 using shapesize function.
# TODO-58 - Use penup() function and goto(position) to display default position of the paddle.
# TODO-59 - Add left and right paddle boundaries. self.left_limit = -380 and self.right_limit = 380.
# TODO-60 - Create 2 functions go_right() and go_left. go_right() will calculate new_x by adding 20 to current x
#  position and go_left() will calculate new_x by subtracting 20 from current x position.
# TODO-61 - Next we will check if paddle is not crossing boundaries at both left and right. For right we will check if
#  new_x < self.right_limit, if yes paddle goes to (new_x,self.ycor()). For left if new_x > self.left_limit, if yes
#  paddle goes to (new_x,self.ycor()).

# ball.py
# TODO-62 - Create ball.py file. Inside the file import Turtle and Screen from turtle module.
# TODO-63 - Create class Ball. Insert Turtle class so Ball class becomes a Turtle objext and inherits all properties
#  from Turtle.
# TODO-64 - Initialise the class. Also initialise super class for Turtle. Receive starting position (position) i.e.,
#  (0, -290) for the ball.
# TODO-65 - Create the ball inside the class. Define its shape to circle, color to grey. Use penup() function and goto
#  position (0, -290).
# TODO-66 - Add variables self.x_move = 10 and self.y_move = 10 to define the steps with which the ball moves along with
#  its speed self.move_speed = 0.1. Also add self.hit_count = 0 to count the number of hits when ball hits the bricks.
# TODO-67 - Create move() function which calculates new_x and new_y by adding self_x.move and self.y_move variables to
#  self.xcor() and self.ycor() respectively.
# TODO-68 - Move the ball to its new calculated position using goto(new_x, new_y).
# TODO-69 - Create bounce_x() function to move the ball in x direction. This is done by multiplying self.x_move with -1
#  so that we can have -10 and 10 automatically.
# TODO-70 - Similarly create bounce_y() to move the ball in y direction. This is done by multiplying self.y_move with
#  -1.
# TODO-71 - Create reset_position() function by defining its default position,speed and bounce direction. Add
#  self.goto(0, -290), self.move_speed = 0.1 and self.bounce_y() in it.
# TODO-72 - Create register_hit() function to count number of hits by the ball. Increment self.hit_count by 1 whenever a
#  brick is hit.
# TODO-73 - Create update_speed() function to increase ball speed when certain number of hits are done or when ball hits
#  red or orange color bricks. Add brick_color=None to increase speed when ball hits paddle for more than 4 or 12.
# TODO-74 - When the count is equal to 4, then we reduce the speed by 0.002 by subtracting it from self.move_speed. The
#  max() function ensures it never goes below 0.018 so that ball never becomes too fast and game stays fair.
# TODO-75 - Similarly, when hits are equal to 12 then self.move_speed = max(self.move_speed - 0.003, 0.015). If red or
#  orange brick is hit then check if brick_color in ("red", "orange"). If true then, increase speed
#  self.move_speed = max(self.move_speed - 0.0015, 0.015).

# scoreboard.py
# TODO-76 - Create scoreboard.py file. Inside the file import Turtle and Screen from turtle module.
# TODO-77 - Create class Scoreboard. Insert Turtle class so Scoreboard class becomes a Turtle objext and inherits all
#  properties from Turtle.
# TODO-78 - Initialise the class. Also initialise super class for Turtle.
# TODO-79 - Create the scoreboard inside the class. Define self.score=0 and color to white. Use penup() function and
#  hideturtle to hide the turtle. Use self.goto(0, 310) and goto the default position. Add a method self.update_score().
# TODO-80 - Create update_score() function to display score. Clear it using self.clear() and write the current score
#  like this --> self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "bold")).
# TODO-81 - Create add_score() function and pass points in it. This is done to add points to self.score. Once added call
#  self.update_score() to display the current socre.
# TODO-82 - Create show_lives() function to display number of lives remaining. Clear it using self.clear() and display
#  current number of lives like this --> self.write(f"Score: {self.score}   Lives: {lives}", align="center",
#  font=("Courier", 22, "bold")).
# TODO-83 - Create game_over() function to display GAMEOVER on the screen. Go to (0,0) position using self.goto(0, 0)
#  and display --> self.write("GAME OVER", align="center", font=("Courier", 36, "bold")).



from turtle import Screen
from bricks import Bricks
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from turtle import Turtle

# Initialize Screen
screen = Screen()

root = screen.getcanvas().winfo_toplevel()
root.resizable(False, False)

# Setup Screen
screen.setup(height=700, width=1000)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

start_x = -453
start_y = 270

brick_wall = Bricks()
paddle = Paddle((0, -330))
ball = Ball((0, -290))
scoreboard = Scoreboard()

score_map = {
    "yellow": 1,
    "green": 3,
    "orange": 5,
    "red": 7,
}

brick_wall.make_bricks(start_x, start_y)

# Screen keys
screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

lives = 3
game_over = False
win = False

# Game starts
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collison with left and right side of the wall
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()

    # Detect Collison with top of the wall
    if ball.ycor() > 330:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 140 and ball.ycor() < -300:
        ball.bounce_y()
        ball.goto(ball.xcor(), paddle.ycor() + 20)
        ball.register_hit()  # count paddle hit
        ball.update_speed(None)

    # Detect collision with bricks
    for brick in brick_wall.bricks_list:
        if ball.distance(brick) < 50:
            # FORCE ball downward like real Breakout
            ball.y_move = -abs(ball.y_move)

            # Score according to brick color
            brick_color = brick.color()[0]
            points = score_map[brick_color]
            scoreboard.add_score(points)

            # Register the hit
            ball.register_hit()

            # Update speed using hit rules + orange/red rule
            ball.update_speed(brick_color)

            brick.goto(2000, 2000)
            brick_wall.bricks_list.remove(brick)

    # Detect Ball Miss (ball goes below paddle)
    if ball.ycor() < -360:
        lives -= 1
        scoreboard.show_lives(lives)

        if lives > 0:
            # Pause, reset ball, continue game
            time.sleep(1)
            ball.reset_position()
        else:
            game_over = True
            game_is_on = False

            ball.hideturtle()
            paddle.hideturtle()
            for brick in brick_wall.bricks_list:
                brick.hideturtle()
            screen.update()
            scoreboard.game_over()

    # Check if all bricks are broken
    if len(brick_wall.bricks_list) == 0:
        game_is_on = False
        game_over = True
        win = True

        ball.hideturtle()
        paddle.hideturtle()
        for brick in brick_wall.bricks_list:
            brick.hideturtle()

        screen.update()

# Restart section
def restart():
    screen.bye()
    import subprocess
    subprocess.call(["python", "main.py"])

if game_over:
    msg = Turtle()
    msg.hideturtle()
    msg.color("white")
    msg.penup()
    msg.goto(0, 20)

    if win:
        msg.write("🎉 YOU WON! 🎉", align="center", font=("Courier", 28, "bold"))

    restart_turtle = Turtle()
    restart_turtle.hideturtle()
    restart_turtle.color("white")
    restart_turtle.penup()
    restart_turtle.goto(0, -50)
    restart_turtle.write("CLICK TO RESTART", align="center", font=("Courier", 20, "bold"))

    screen.onclick(lambda x, y: restart())

screen.mainloop()