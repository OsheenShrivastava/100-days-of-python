from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# TODO-10 - Generate a random password
def Generate_Password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)

    # TODO-11 - Convert password list to a string and insert it in Password_Entry box.
    password = "".join(password_list)

    # TODO-13 - Insert the newly created password in the Password_Entry at the starting position i.e., 0
    Password_Entry.insert(0, password)

    # TODO-14 - Copy the new password from Password_Entry to pyperclip clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # TODO-6 - Obtain data from Website,Email and Password entry box
    Website = Website_Entry.get()
    Email = Email_Username_Entry.get()
    Password = Password_Entry.get()

    # TODO-9 - Check length of Website and Password and generate a pop up / message box
    if len(Website) == 0 or len(Password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't leave any fields empty!")
    else:
        # TODO-7 - Ask the user to click ok to save the details
        is_ok = messagebox.askokcancel(title=Website, message=f"These are the details entered: \nEmail: {Email} "
                                                              f"\nPassword: {Password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{Website} | {Email} | {Password}\n")
                # TODO-8 - Delete Website and Email entry once button is pressed
                Website_Entry.delete(0, END)
                Password_Entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# TODO-1 - Create a window and insert the image

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=0, column=1)

# TODO-2 - Create all Labels,Entry and Button
Website_Label = Label(text="Website:")
Website_Label.grid(row=1, column=0)

# TODO-3 - Call entry.focus() to place cursor in the entry field
Website_Entry = Entry(width=21)
Website_Entry.grid(row=1, column=1)
Website_Entry.focus()

Email_Username_Label = Label(text="Email/Username:")
Email_Username_Label.grid(row=2, column=0)

# TODO-4 - Use entry.insert() to define the starting position i.e. 0 and then type the email
#  "abcd123@gmail.com"

Email_Username_Entry = Entry(width=35)
Email_Username_Entry.grid(row=2, column=1, columnspan=2)
Email_Username_Entry.insert(0, "abcd123@gmail.com")

Password_Label = Label(text="Password:")
Password_Label.grid(row=3, column=0)

Password_Entry = Entry(width=21)
Password_Entry.grid(row=3, column=1)

# TODO-12 - Call Generate Password function when Generate_Password_Button is clicked
Generate_Password_Button = Button(text="Gen Password", command=Generate_Password)
Generate_Password_Button.grid(row=3, column=2)

# TODO-5 - Call save() function when Add_Button is clicked
Add_Button = Button(text="Add", width=30, command=save)
Add_Button.grid(row=4, column=1, columnspan=2)

window.mainloop()