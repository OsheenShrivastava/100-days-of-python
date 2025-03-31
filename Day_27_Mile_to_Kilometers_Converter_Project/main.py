# TODO-1 - Import all files of Tkinter
from tkinter import *


def miles_to_kilometre():
    Final_Km_value = round(float(input.get()) * 1.609)
    Km_converted_value_Label.config(text=f"{Final_Km_value}")


# TODO-2 - Create a Window and name it

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# TODO-3 - Create Labels,Entry and Buttons
# Entry

input = Entry(width=7)
input.grid(row=0, column=1)

# Label
Miles_Label = Label(text="Miles")
Miles_Label.grid(row=0, column=2)

is_equal_to_Label = Label(text="is equal to")
is_equal_to_Label.grid(row=1, column=0)

Km_converted_value_Label = Label(text="0", )
Km_converted_value_Label.grid(row=1, column=1)

Km_Label = Label(text="Km")
Km_Label.grid(row=1, column=2)

# Button

# TODO-4 - Create a function to convert miles to km and call it as a command
Calculate_Button = Button(text="Calculate", command=miles_to_kilometre)
Calculate_Button.grid(row=2, column=1)

window.mainloop()
