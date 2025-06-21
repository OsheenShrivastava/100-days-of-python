# TODO-1 - Import Flask

from flask import Flask
import random

# TODO-2 - Create a Flask object and pass __name__ as an argument.

app = Flask(__name__)


# TODO-3 - Create a Home Route

@app.route("/")
def Higher_Lower():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


# TODO-4 - Import random module and generate a number 0 to 9

number = random.randint(0, 9)
print(number)


# TODO-5 - Create a route that can detect the number entered by the user e.g "URL/3" or "URL/9" and checks that number
#  against the generated random number. If the number is too low, tell the user it's too low, same with too high or
#  if they found the correct number. try to make the <h1> text a different colour for each page.

@app.route("/<int:user_choice>")
def User_Input(user_choice):
    if user_choice < number:
        return '<h1 style="color: red">Too low,try again!</h1> ' \
               '<img src= "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif user_choice > number:
        return '<h1 style="color: purple">Too high,try again!</h1> ' \
               '<img src= "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1 style="color: green">You found me!</h1> ' \
               '<img src= "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


# TODO-6 - Run the app

if __name__ == "__main__":
    app.run(debug=True)