import pandas
import turtle

# TODO-1 - Import turtle and print the screen
Screen = turtle.Screen()
Screen.title("U.S. States Game")
image = "blank_states_img.gif"
Screen.addshape(image)
turtle.shape(image)

# TODO-2 - Import pandas, read the file and convert them to a list
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# TODO-5 - Loop TODO-3 and TODO-4 until user has guessed all the states
while len(guessed_states) < 50:
    # TODO-3 - Ask for user input
    answer_state = Screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # TODO-6 - Exit the game when user types exit
    if answer_state == "Exit":
        # TODO-7 - Loop through all_states list and if that state is not in guessed_states
        #  then append them to a list called missing_states. Create a data frame and store
        #  it to a new csv

        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        # TODO-4 - Create a turtle. If user has guessed the state in 50_states then write
        #  that state on the map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
