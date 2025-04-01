from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# TODO-14 - Generate a random password
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

    # TODO-15 - Convert password list to a string and insert it in Password_Entry box.
    password = "".join(password_list)

    # TODO-16 - Insert the newly created password in the Password_Entry at the starting position i.e., 0
    Password_Entry.insert(0, password)

    # TODO-17 - Copy the new password from Password_Entry to pyperclip clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # TODO-6 - Obtain data from Website,Email and Password entry box
    Website = Website_Entry.get()
    Email = Email_Username_Entry.get()
    Password = Password_Entry.get()

    # TODO-7 - Create the data in json format
    new_data = {
        Website: {
            "Email": Email,
            "Password": Password,
        }
    }

    # TODO-8 - Check length of Website and Password and generate a pop up / message box
    if len(Website) == 0 or len(Password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't leave any fields empty!")
    else:
        try:
            # TODO-9 - Read the data from json file and include this in try: section
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)

        except FileNotFoundError:
            # TODO-10 - Include FileNotFoundError exception and if it occurs then create a file and write in it
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            # TODO-11 - if no error then update the data and write it to the file
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)

        finally:
            # TODO-12 - Delete Website and Email entry once button is pressed
            Website_Entry.delete(0, 'end')
            Password_Entry.delete(0, 'end')


# ---------------------------- FIND PASSWORD------------------------------- #
# TODO-19 - Create a function called find_password(), get hold of website data and load json file
def find_password():
    Website = Website_Entry.get()
    try:
        with open("data.json") as file:
            # Reading old data
            data = json.load(file)
    # TODO-22 - Catch an exception that might occur trying to access data.json
    #  showing a messagebox with the text "No Data File Found"
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        # TODO-20 - Check if the user's text entry matches an item in data.json
        if Website in data:
            # TODO-21 - If yes then show a messagebox with website's name and password
            Email = data[Website]["Email"]
            Password = data[Website]["Password"]
            messagebox.showinfo(title=Website, message=f"Email: {Email}\nPassword: {Password}")
        else:
            # TODO-23 - If the user's website does not exist inside the data.json
            #  then show a messagebox that reads "No details for the website exists."
            messagebox.showinfo(title="Error", message=f"No details for {Website} exists.")


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
#  "osheenshrivastava01@gmail.com"

Email_Username_Entry = Entry(width=35)
Email_Username_Entry.grid(row=2, column=1, columnspan=2)
Email_Username_Entry.insert(0, "abcd123@gmail.com")

Password_Label = Label(text="Password:")
Password_Label.grid(row=3, column=0)

Password_Entry = Entry(width=21)
Password_Entry.grid(row=3, column=1)

# TODO-13 - Call Generate Password function when Generate_Password_Button is clicked
Generate_Password_Button = Button(text="Gen Password", command=Generate_Password)
Generate_Password_Button.grid(row=3, column=2)

# TODO-5 - Call save() function when Add_Button is clicked
Add_Button = Button(text="Add", width=30, command=save)
Add_Button.grid(row=4, column=1, columnspan=2)

# TODO-18 - Add Search button and trigger find_password() function when clicked
Search_Button = Button(text="Search", width=10, command=find_password)
Search_Button.grid(row=1, column=2)

window.mainloop()
