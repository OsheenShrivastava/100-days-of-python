
# main.py
# TODO-1 - Import Turtle and Screen from turtle module.
# TODO-2 - Import Tank from tank.
# TODO-3 - Import Bullet from bullet.
# TODO-4 - Import Monster from monsters.
# TODO-5 - Import Life from life.
# TODO-6 - Import Score from score.
# TODO-7 - Import Time.
# TODO-8 - Import pygame.
# TODO-9 - Initialize the turtle Screen and configure size, title, tracer, and background image. Set height and width as
#  "1.0" to maximize the screen. Set title as "Space invaders". Set background as background.gif.
# TODO-10 - Register shapes for tank.gif and monster.gif for game objects. In Python Turtle graphics, we need to
#  register a shape when using an image because Turtle doesn’t automatically recognize external image files as valid
#  shapes.
# TODO-11 - Update the screen using screen.update(). Create objects for all classes - Tank, Monster, Life and Score.
# TODO-12 - Initialize lists for tank bullets and monster bullets. Initialize variables last_shot_time = 0,
#  SHOOT_DELAY = 0.5, last_enemy_shot = 0 and ENEMY_DELAY = 0.8. Set game_is_on to True.
# TODO-13 - Initialize pygame mixer for sound handling. Create a file named "wav_files" and store all .wav files in it.
# TODO-14 - Load sound using pygame.mixer.Sound() function. Pass in the respective wav file in it. Set appropriate
#  volume levels using set_volume() function.
# TODO-15 - Load and set volume levels for - tank bullet, enemy bullet, enemy explosion, tank hit, game win and game
#  loose.
# TODO-16 - Create a function named "fire_bullet" to shoot from tank. Declare 'last_shot_time' as global so we can
#  update it inside the function. Get the current time using time.time() to track when the player is firing.
# TODO-17 - Check if enough time has passed since the last shot using SHOOT_DELAY to prevent continuous/rapid firing
#  (cooldown logic). If cooldown is satisfied, create a new Bullet object using the tank's current position
#  (tank.xcor(), tank.ycor()). Pass direction, speed and color along with position.
# TODO-18 - Append the newly created Bullet object to the 'bullets' list so it can be updated and rendered in the game
#  loop.
# TODO-19 - Play the laser sound effect using laser_sound.play() with a short duration (maxtime=100 ms).
# TODO-20 - Update 'last_shot_time' to the current time so the cooldown resets.
# TODO-21 - Uncomment height and width to read actual parameters of screen.
# TODO-22 - Create function init_game(). Inside it initialize all global game variables - tank, monster, bullets,
#  mons_bullets, life, score, game_is_on, last_shot_time, last_enemy_shot.
# TODO-23 - Clear screen, set title as "Space Invaders", make sure screen.tracer(0) to turn off animation avoiding the
#  user to see how the monsters align one by one. Set background.
# TODO-24 - Add background music using pygame.mixer.music.load() function. Set volume and edit play as "-1" to play it
#  continuously.
# TODO-25 - Re-register tank and monster shapes. Recreate all object from their respective classes. Update the screen.
# TODO-26 - Initialize bullets and mons_bullets. Reset last_shot_time and last_enemy_shot.
# TODO-27 - Bind keyboard controls using onkey() function. Add screen.listen() function to read the keys pressed. Then
#  using onkey() function make "Left", "Right", "Space" and "r" keys functional by calling tank.move_left,
#  tank.move_right, fire_bullet and restart on respective keys. Set game_is_on to True to start the game.
# TODO-28 - Create restart() function to safely reset the game without crashing the turtle screen. Add global variable
#  game_is_on. Set it to False. Add delay of 0.1 second. Stop the music using pygame.mixer.music.stop() function and
#  call init_game() function.
# TODO-29 - Create show_win() function to display win message and play win sound. Call tank.start_position() to move
#  tank to its default position before showing win. Update the screen. Stop the music, add a delay and play game_win
#  sound.
# TODO-30 - Now to display Win and option to restart the game we will create a Turtle object named game_won. Hide the
#  turtle, go to (0, 0) i.e., center of screen, set color as "white" and write "🏆 YOU WIN 🏆\nPress r to Restart" with
#  desired font and center alignment.
# TODO-31 - Create main function named game_loop() where everything happens. Add global variables game_is_on and
#  last_enemy_shot.
# TODO-32 - Wrap the entire game loop logic inside a try block to prevent crashes and handle unexpected errors
#  gracefully. Check if the game is currently running using 'game_is_on'.
# TODO-33 - If true then update the screen using screen.update() to render all movements. Move all monsters using
#  monster.move_monsters().
# TODO-34 - Get current time using time.time() to control enemy shooting cooldown. Check if enough time has passed since
#  last enemy shot (ENEMY_DELAY). Ensure there are monsters alive before attempting to shoot.
# TODO-35 - If true then get a valid monster shooting position using monster.monster_position(). If valid position
#  exists, create a new enemy bullet and append it to mons_bullets list. Pass (x, y) co-ordinate along with direction,
#  speed and color.
# TODO-36 - Play enemy shooting sound effect. Update last_enemy_shot time to enforce cooldown.
# TODO-37 - Loop through a copy of bullets list (bullets[:]) to avoid modification issues. Move each bullet using
#  bullet.shoot().
# TODO-38 - Initialize a flag 'removed' to track if bullet is deleted after collision. Loop through all monsters
#  (copy list) to check collision with bullet.
# TODO-39 - If bullet hits a monster i.e., distance < 30, then hide turtle, remove monster from list, play enemy
#  explosion sound and call increase_score() to increase the score.
# TODO-40 - Hide the turtle and check if bullet exixts. If yes then remove bullet from bullets list safely.
# TODO-41 - Set removed flag = True and break out of monster loop.
# TODO-42 - If no monsters remain then update the screen, stop the game by setting game_is_on to False and call
#  show_win() function.
# TODO-43 - Skip further processing for this bullet if it was removed.
# TODO-44 - Check y co-ordinate of bullet is greator than 380 i.e., goes off-screen then hide the turtle. Check again if
#  bullet exists, if yes then remove the bullet from bullets list.
# TODO-45 - Loop through a copy of bullets list (mons_bullets[:]) to avoid modification issues. Move each mons_bullet
#  using mons_bullet.shoot().
# TODO-46 - Check y co-ordinate of bullet is less than -280, if yes then hide the turtle. Check again if mons_bullet
#  exists in mons_bullets list, if yes then remove the mons_bullet from mons_bullets list.
# TODO-47 - Check collision between enemy bullet and player tank i.e., distance between mons_bullet and tank is less
#  than 40. If true then hide that mons_bullet.
# TODO-48 - Check again if that mons_bullet exists in mons_bullet list, if yes then remove that mons_bullet from
#  mons_bullets list. Play player hit sound, call lose_life() function to reduce the life and finally call
#  start_position() to move the tank to center i.e., at its default position.
# TODO-49 - Check if player lives reached zero. If yes then update the screen, set game_is_on to False, stop background
#  music, add a small delay and play game over sound.
# TODO-50 - Now to display Game Over and option to restart the game we will create a Turtle object named game_over. Hide
#  the turtle, go to (0, 0) i.e., center of screen, set color as "white" and write "GAME OVER\nPress r to Restart" with
#  desired font and center alignment.Display "GAME OVER" message using Turtle.
# TODO-51 - Catch any exception using except block. Print error message for debugging. Stop the game if unexpected error
#  occurs.
# TODO-52 - Use screen.ontimer(game_loop, 20) to repeatedly call game loop every 20 milliseconds (game refresh cycle).
# TODO-53 - Start the game by calling init_game() and game_loop().
# TODO-54 - Run screen.mainloop() to keep window open.The window stays open. It keeps listening for events (keyboard,
#  mouse clicks, etc.). It prevents the program from closing immediately.

# bullet.py
# TODO-55 - Create a file named bullet.py. Import Turtle class from turtle module.
# TODO-56 - Create Bullet class inheriting from Turtle.
# TODO-57 - Initialize Bullet with position (x, y), direction, speed, and color. Initialize super() class to inherit
#  Turtle class functionalities.
# TODO-58 - Select the shape as square, add shapesize, penup, assign the color which is passed in function and finally
#  go to the x,y co-ordinates passed.
# TODO-59 - Create 2 function variables self.direction and self.speed to store speed and direction passed in the
#  function.
# TODO-60 - Create a function named shoot(). Set y co-ordinate to move bullet in the direction and speed passed in the
#  function.
# TODO-61 - Handle upward movement for player bullets and downward for enemy bullets.

# life.py
# TODO-62 - Create a file named life.py. Import Turtle class from turtle module.
# TODO-63 - Create Life class inheriting from Turtle.
# TODO-64 - Initialize super() class to inherit Turtle class functionalities. Initialize a variable named self.lives
#  with 3 to store default number of lives.
# TODO-65 - Hide the turtle, penup, set the color as red and go to (-400, -340). Call function update_display() during
#  initialisation.
# TODO-66 - Create the function update_display(). Call clear function and then display lives on screen using write()
#  function.
# TODO-67 - Create another function named lose_life(). Inside this decrement lives when player is hit. Update display
#  after life loss by calling update_display() function.

# monster.py
# TODO-68 - Create a file named monsters.py. Import Turtle class from turtle module. Import random.
# TODO-69 - Define constants such as - START_Y = 380, MOVE_DISTANCE = 3, MAX_RIGHT = 380 and MAX_LEFT = -380.
# TODO-70 - Create Monster class inheriting from Turtle.
# TODO-71 - Initialize super() class to inherit Turtle class functionalities. Penup, hide the turtle and set speed as 0.
#  hideturtle() is added before setup to avoid flicker at (0,0).
# TODO-72 - Create a list named monsters. Create variable direction and set its value equal to MOVE_DISTANCE.
# TODO-73 - Create a variable y and set it value as START_Y. Add a FOR loop in range of 5 to create 5 rows of monsters.
# TODO-74 - Set number of monsters in a row as 8, set spacing between monsters as 80 and calculate start_x co-ordinate
#  using formula - [- (num_monsters - 1) * spacing / 2].
# TODO-75 - Add another FOR loop inside this loop and set its iteration = num_monsters. Calculate x co-ordinate using
#  formula - [start_x + i * spacing]
# TODO-76 - Create Turtle object, shape it as monster gif, penup and go to position (x,y) [already calculated].
# TODO-77 - Append individual monster to monsters list. Finally reduce y by 60 to implement next row. This way 5 rows
#  are created with 8 number of monsters in each row.
# TODO-78 - Create move_monsters() function to move monsters horizontally. Iterate a FOR loop through the list monsters.
#  Set x co-ordinate for every monster = monster.xcor() + self.direction. This way x co-ordinate changes resulting in
#  shifting each monster by x. Combined effect is seen as monsters moving.
# TODO-79 - Now to move them left to right and vice versa we will change the direction once monster.xcor() reaches
#  either MAX_RIGHT or MAX_LEFT. Add another FOR loop to iterate over the list monsters. Inside it add condition
#  if monster.xcor() > MAX_RIGHT: change direction to -1 and if monster.xcor() < MAX_LEFT: again change direction to -1.
#  This is done so that both positive and negative values can be read.
# TODO-80 - Create another function monster_position() to return random monster coordinates for shooting. Check if
#  monster exists if not then return None for both x and y.
# TODO-81 - Otherwise, Use random.choice() function to select a random monster from monsters list. Store it in variable
#  monster. Return monster.xcor(), monster.ycor() of the selected monster.

# score.py
# TODO-82 - Create a file named score.py. Import Turtle class from turtle module.
# TODO-83 - Create Score class inheriting from Turtle.
# TODO-84 - Initialize super() class to inherit Turtle class functionalities. Initialize score variable with 0.
# TODO-85 - Hide the turtle, penup, set the color as white and go to (400, -340). Call function update_display() during
#  initialisation.
# TODO-86 - Create the function update_display(). Call clear function and then display score on screen using string
#  formatting. Set it alignment to left and font.
# TODO-87 - Create another function named increase_score. Increment the score by 20 when a monster is hit and update it
#  on the screen by calling update_display() function.

# tank.py
# TODO-88 - Create a file named tank.py. Import Turtle class from turtle module.
# TODO-89 - Define constants such as - START_POSITION = (0, -280), MOVE_DISTANCE = 25, MAX_RIGHT = 360 and
#  MAX_LEFT = -360.
# TODO-90 - Create Tank class inheriting from Turtle.
# TODO-91 - Initialize super() class to inherit Turtle class functionalities. Set the shape of tank as "tank.gif", set
#  the color as green, penup, go to START_POSITION and set heading to 90.
# TODO-92 - Create a function named move_left(). Inside it check if x co-ordinate of tank is greater than MAX_LEFT, if
#  true then subsract MOVE_DISTANCE from x co-ordinate and set that as final x co-ordinate. This shifts tank to left.
# TODO-93 - Similarly, create a function named move_right(). Inside it check if x co-ordinate of tank is less than
#  MAX_RIGHT, if true then add MOVE_DISTANCE to x co-ordinate and set that as final x co-ordinate. This shifts tank to
#  right.
# TODO-94 - Create another function named start_position() to reset tank position after hit. Inside it add penup, go to
#  START_POSITION and set heading to 90.




from turtle import Turtle, Screen
from tank import Tank
from bullet import Bullet
from monsters import Monster
from life import Life
from score import Score
import time
import pygame


screen = Screen()


# Set the screen
screen.setup(1.0, 1.0)
screen.title("Space Invaders")
screen.tracer(0)
screen.bgpic("images/background.gif")

screen.register_shape("images/tank.gif")
screen.register_shape("images/monster.gif")

screen.update()


tank = Tank()
monster = Monster()
life = Life()
score = Score()
bullets = []
mons_bullets = []

last_shot_time = 0
SHOOT_DELAY = 0.5

last_enemy_shot = 0
ENEMY_DELAY = 0.8

game_is_on = True

pygame.mixer.init()

laser_sound = pygame.mixer.Sound("wav_files/tank_laser.wav")
laser_sound.set_volume(0.3)

enemy_sound = pygame.mixer.Sound("wav_files/enemy_laser.wav")
enemy_sound.set_volume(0.3)

enemy_explosion_sound = pygame.mixer.Sound("wav_files/enemy_explosion.wav")
enemy_explosion_sound.set_volume(0.4)

player_hit_sound = pygame.mixer.Sound("wav_files/tank_hit.wav")
player_hit_sound.set_volume(0.4)

game_win_sound = pygame.mixer.Sound("wav_files/game_win.wav")
game_win_sound.set_volume(0.5)

game_over_sound = pygame.mixer.Sound("wav_files/game_over.wav")
game_over_sound.set_volume(0.5)


def fire_bullet():
    global last_shot_time

    current_time = time.time()

    if current_time - last_shot_time > SHOOT_DELAY:
        bullets.append(Bullet(tank.xcor(), tank.ycor(), 1, 10, "white"))

        laser_sound.play(maxtime=100)

        last_shot_time = current_time



# Check screen width and height
# height = screen.window_height()
# width = screen.window_width()
# print(height, width)



def init_game():
    global tank, monster, bullets, mons_bullets, life, score, game_is_on, last_shot_time, last_enemy_shot

    # clear screen
    screen.clear()
    screen.title("Space Invaders")
    screen.tracer(0)
    screen.bgpic("images/background.gif")

    # 🎵 ADD THIS
    pygame.mixer.music.load("wav_files/bg_music.mp3")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)

    # re-register shapes
    screen.register_shape("images/tank.gif")
    screen.register_shape("images/monster.gif")

    # recreate objects
    tank = Tank()
    monster = Monster()
    life = Life()
    score = Score()

    screen.update()

    bullets = []
    mons_bullets = []

    # RESET TIMERS
    last_shot_time = 0
    last_enemy_shot = 0

    # 🔑 IMPORTANT: rebind keys again
    screen.listen()
    screen.onkey(tank.move_left, "Left")
    screen.onkey(tank.move_right, "Right")
    screen.onkey(fire_bullet, "space")
    screen.onkey(restart, "r")

    game_is_on = True



# Restart section
def restart():
    global game_is_on

    game_is_on = False  # ⛔ stop current loop
    time.sleep(0.1)  # small delay (important)

    # stop music
    pygame.mixer.music.stop()

    init_game()



def show_win():
    tank.start_position()
    screen.update()

    pygame.mixer.music.stop()
    pygame.time.delay(300)
    game_win_sound.play()

    game_won = Turtle()
    game_won.hideturtle()
    game_won.goto(0, 0)
    game_won.color("white")
    game_won.write("🏆 YOU WIN 🏆\nPress r to Restart", align="center", font=("Arial", 20, "bold"))



# Game Loop
def game_loop():
    global game_is_on, last_enemy_shot
    try:
        if game_is_on:
            screen.update()

            monster.move_monsters()

            current_time = time.time()

            if current_time - last_enemy_shot > ENEMY_DELAY:
                if monster.monsters:  # safety check
                    pos = monster.monster_position()
                    if pos != (None, None):
                        x, y = pos
                        mons_bullets.append(Bullet(x, y, -1, 5, "#00FF00"))

                        enemy_sound.play(maxtime=100)

                    last_enemy_shot = current_time

            for bullet in bullets[:]:
                bullet.shoot()

                removed = False

                for m in monster.monsters[:]:
                    if bullet.distance(m) < 30:
                        m.hideturtle()
                        monster.monsters.remove(m)

                        enemy_explosion_sound.play(maxtime=100)

                        score.increase_score()

                        bullet.hideturtle()
                        if bullet in bullets:
                            bullets.remove(bullet)

                        removed = True

                        # Game Won
                        if not monster.monsters:
                            screen.update()
                            game_is_on = False
                            show_win()
                        break

                if removed:
                    continue

                if bullet.ycor() > 380:
                    bullet.hideturtle()
                    if bullet in bullets:
                        bullets.remove(bullet)


            for mons_bullet in mons_bullets[:]:
                mons_bullet.shoot()

                if mons_bullet.ycor() < -280:
                    mons_bullet.hideturtle()
                    if mons_bullet in mons_bullets:
                        mons_bullets.remove(mons_bullet)
                    continue

                if mons_bullet.distance(tank) < 40:
                    mons_bullet.hideturtle()
                    if mons_bullet in mons_bullets:
                        mons_bullets.remove(mons_bullet)

                    player_hit_sound.play(maxtime=100)

                    life.lose_life()
                    tank.start_position()

            if life.lives == 0:
                screen.update()
                game_is_on = False

                pygame.mixer.music.stop()
                pygame.time.delay(300)
                game_over_sound.play()

                game_over = Turtle()
                game_over.hideturtle()
                game_over.goto(0, 0)
                game_over.color("white")
                game_over.write("GAME OVER\nPress r to Restart", align="center", font=("Arial", 20, "bold"))

    except Exception as e:
        print("Error:", e)
        game_is_on = False

    screen.ontimer(game_loop, 20)



init_game()
game_loop()
screen.mainloop()