from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data_dictionary = {}
current_card = {}

# TODO-27 - Create exception handling so that the very first when
#  words_to_learn.csv does not exist, it takes all data from french_words.csv
#  and copies to words_to_learn.csv.
#  But the next time when all data has been copied to words_to_learn.csv then
#  it will generate random words from it

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # TODO-8 - Import Pandas and read the data from the french_words.csv file and it creates a dataframe.
    data_frame = pandas.read_csv("data/french_words.csv")
    print(data_frame)

    # TODO-9 - Convert all the data of data_frame to a dictionary.
    #  The orient = "records" so that index number is removed from
    #  data frame and we obtain a standard dictionary
    data_dictionary = data_frame.to_dict(orient="records")
else:
    data_dictionary = data.to_dict(orient="records")


# TODO-10 - Import random module and Create a function to generate random word from data_dictionary
def generate_random_word():
    global current_card, timer
    # TODO-21 - Cancel the previous timer
    window.after_cancel(timer)

    current_card = random.choice(data_dictionary)

    # TODO-12 - Display the random word and its title on canvas
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    # TODO-20 - Change the image again to card_front_png when any button is clicked
    canvas.itemconfig(current_canvas_image, image=card_front_png)

    # TODO-22 - Initialize the timer again
    timer = window.after(3000, Flip_Card)


# TODO-18 - Create function to display the English Card
def Flip_Card():
    # TODO-19 - Change the image to card_back_png and display English word on canvas and cancel the timer
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(current_canvas_image, image=card_back_png)


# TODO-24 - Create function to save data to a new file
def is_known():
    # TODO-25 - Remove the word from data_dictionary which is known to user
    data_dictionary.remove(current_card)
    print(len(data_dictionary))

    # TODO-26 - Save the word in a new dataframe and convert it to csv. Call generate_random_word() again
    #  to continue the process
    data = pandas.DataFrame(data_dictionary)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_random_word()


# TODO-1 - Import Tkinter and create a window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# TODO-17 - Import math module and use window.after function to show next window
timer = window.after(3000, Flip_Card)


# TODO-3 - Use Canvas Module and import card_front image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_png = PhotoImage(file="images/card_front.png")
# TODO-15 - Store the current canvas image to a variable
current_canvas_image = canvas.create_image(400, 263, image=card_front_png)


# TODO-16 - Import card_back image
card_back_png = PhotoImage(file="images/card_back.png")


# TODO-14 - Remove the words "Title" and "Word" from text and replace them with ""
# TODO-4 - Write the text "Title" and "WORD" using canvas and store them in variables
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
# TODO-7 - Add columnspan and increase columns to 2 to
#  arrange buttons symmetrically
canvas.grid(row=0, column=0, columnspan=2)


# TODO-11 - Add command function to Wrong_button button to generate random word when clicked
# TODO-5 - Create "x" button and import the wrong.png image
wrong_png = PhotoImage(file="images/wrong.png")
Wrong_button = Button(image=wrong_png, highlightthickness=0, command=generate_random_word)
Wrong_button.grid(row=1, column=0)

# TODO-23 - Add command function to Right_button to save data to a new file
# TODO-6 - Create "✓" button and import the right.png image
right_png = PhotoImage(file="images/right.png")
Right_button = Button(image=right_png, highlightthickness=0, command=is_known)
Right_button.grid(row=1, column=1)


# TODO-13 - Call generate_random_word() so that a french word is displayed the first time its run
generate_random_word()


# TODO-2 - Include window.mainloop() to see the window
window.mainloop()
