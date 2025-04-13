from tkinter import *
import requests


# TODO-5 - Create a function
def get_quote():
    # TODO-6 - Request response from api endpoint
    response = requests.get("https://api.kanye.rest")

    # TODO-7 - Raise exceptions
    response.raise_for_status()

    # TODO-8 - Parse the response to json
    data = response.json()

    # TODO-9 - Configure the quote to be written on canvas
    canvas.itemconfig(quote_text, text=data["quote"], font=("Ariel", 15, "bold"))


# TODO-1 - Create a window from Tkinter
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# TODO-3 - Create a Canvas, attach the background image and edit the default text
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

# TODO-4 - Add a button, attach image on it and call function when pressed
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


# TODO-2 - Initialize below statement to view the window
window.mainloop()