
# TODO-1 - Import time module to track inactivity duration.
# TODO-2 - Import Tk, widgets (Label, Button, Text, Frame, OptionMenu), and constants from tkinter.
# TODO-3 - Import filedialog to allow saving text to a file.
# TODO-4 - Define global font settings used across the application. Define color palette for dark-themed UI:
#  BG_COLOR -> background for text areas and labels, FRAME_BG_COLOR -> background for frames and window,
#  TEXT -> main text color, BUTTON_BG_COLOR -> button background color and BUTTON_FG_COLOR -> button hover/active color.
# TODO-5 - Initialize timer-related global variables: start_time -> stores the last time user typed set it to current
#  time, timer_running -> controls whether the timer is active set it to False and time_duration -> stores allowed idle
#  time based on difficulty set it to None.
# TODO-6 - Define instruction text displayed to the user explaining how the app works and store them to 'instructions'
#  set. Create a flag 'instructions_visible' to toggle instruction panel visibility. Set it to False.
# TODO-7 - Define on_key_release(event) function. It is triggered whenever a key is released in the text box. If timer
#  is not running then it stops the function immediately. It resets start_time if typing is active. It ignores
#  non-character keys (Shift, Ctrl, etc.).
# TODO-8 - Define start_writing() function. Add global variables timer_running, time_duration, start_time. Disable
#  Start, Difficulty and Instructions buttons and set timer_running to True.
# TODO-9 - Assign time_duration based on selected difficulty. 10 secs for Easy, 7 secs for Medium and 5 secs for Hard.
# TODO-10 - Set the text box to normal state, clear text box and focus cursor in text box.
# TODO-11 - Store current time to start_time. Bind KeyRelease event to track typing and call timer_function() to start
#  the countdown timer.
# TODO-12 - Define timer_function(). Add global variables timer_running, time_duration, start_time. If timer_running is
#  True then it calculates remaining_time using current time and start_time. Update timer label every second using
#  config and after function.
# TODO-13 - If remaining time is greator than 0, if true then change text and timer colors when time is low. Change the
#  desired colors at 3,2,1 and 0 else keep a single color.
# TODO-14 - If remaining time is less than or equal to 0 then saves user text before deletion, reset timer variables,
#  Enable start_button, difficulty_menu and instruction_button. Delete text and disable input when time expires. Call
#  save_file() function and pass text to it.
# TODO-15 - Define reset() function. Add global variables timer_running, time_duration, start_time. Stop the timer by
#  setting timer_running = False and time_duration = None.
# TODO-16 - Reset timer label. Clear and disable text box. Add default colors for text box. Re-enable Start, Difficulty
#  and Instructions controls. Reset timer label fg at the end.
# TODO-17 - Define save_file(text) function and pass text to it. It opens file save dialog, define file types, default
#  extension and title of the file. If a filename is chosen open it, set mode to write, encoding-'utf-8'. Save user text
#  into a .txt file using write function.
# TODO-18 - Define toggle_instructions() function. Add global variable instructions_visible. This shows or hides the
#  instruction Text widget.
# TODO-19 -If instruction button is pressed then it used grid() function to display them setting instructions_visible to
#  True. When button is toggles again it checks if instructions_visible is true then it removes the grid using
#  grid_remove() function setting instructions_visible to False.
# TODO-20 - Initialize the main Tkinter window using Tk(). Set window size, padding and apply background color. Set
#  window title and disable window resizing.
# TODO-21 - Create StringVar() to store difficulty selection and set the default to 'Easy'.
# TODO-22 - Create main layout frames. typing_frame for writing area and info_frame for controls and instructions. Add
#  FRAME_BG_COLOR as bg to both. Use grid to lay them.
# TODO-23 - Create title label named write_below using Label() and place inside typing_frame. Add text, bg, fg and font.
# TODO-24 - Create main Text widget (user_type) for typing. Apply bg, fg and font as defined at the start. Set size.
#  This is initially disabled until Start is pressed.
# TODO-25 - Create instruction Text widget and place it in info_frame. Add all the desired parameters to display the
#  button. Use insert() to add instructions created at the start. Make it read-only using state=DISABLED i.e., hidden
#  by default.
# TODO-26 - Create Instructions button and place it in typing_frame. Add the text as 'Instructions'. Add all the desired
#  parameters to display the button. Add command as toggle_instructions to display instructions when toggled.
# TODO-27 - Create control panel frames. timer_frame -> displays countdown, difficulty_frame -> difficulty selector and
#  start_frame -> displays Start and Reset buttons.
# TODO-28 - Create timer label and place it in timer_frame. It displays remaining time and changes color based on
#  urgency. Set default text as 'Timer: 00'.
# TODO-29 - Create difficulty label and OptionMenu. Use OptionMenu and add options for Difficulty_var. Place this in
#  difficulty_frame. Allows user to select Easy / Medium / Hard.
# TODO-30 - Config the difficulty_menu by adding bg, fg, font, width etc. Config difficulty_menu["menu"] menu inside the
#  button, dropdown menu colors are adjusted for visibility.
# TODO-31 - Create Start button and place it in start_frame. Set its text as 'Start'. Add bg, fg, font, width etc. Add
#  command=start_writing to call start_writing() function when pressed. It starts the writing session, activates timer
#  and enables typing.
# TODO-32 - Similarly, create Reset button and place it in start_frame. Set its text as 'Reset'. Add bg, fg, font, width
#  etc. Add command=reset to call reset() function when pressed. It stops timer, clears text and restores app to initial
#  state.
# TODO-33 - Start Tkinter main event loop using window.mainloop().It keeps application running and responsive.



import time
from tkinter import *
from tkinter import filedialog


FONT = ('arial', 12, 'bold')
BG_COLOR = "#0F172A"
FRAME_BG_COLOR = "#1E293B"
TEXT = "#E5E7EB"
BUTTON_BG_COLOR = "#38BDF8"
BUTTON_FG_COLOR = "#0284C7"

start_time = time.time()
timer_running = False
time_duration = None


instructions = (
                "Welcome to the Disappearing Text App!\n\n"
                "Start typing and keep going — if you stop, your text will disappear.\n\n"
                "Choose a difficulty level to set how long you can pause:\n"
                "Easy   – 10 seconds\n"
                "Medium – 7 seconds\n"
                "Hard   – 5 seconds\n\n"
                "Every keystroke resets the timer. Keep typing!"
               )

instructions_visible = False



def on_key_release(event):
    global start_time

    if not timer_running:
        return

    if event.char.strip():   # ignore Shift, Ctrl, etc.
        start_time = time.time()


def start_writing():
    global timer_running, time_duration, start_time

    start_button.config(state=DISABLED)
    difficulty_menu.config(state=DISABLED)
    instruction_button.config(state=DISABLED)

    timer_running = True
    if Difficulty_var.get() == 'Easy':
        time_duration = 10
    elif Difficulty_var.get() == 'Medium':
        time_duration = 7
    else:
        time_duration = 5

    user_type.config(state='normal', fg='black', bg='#CBD5E1')
    user_type.delete("1.0", END)
    user_type.focus_set()

    start_time = time.time()

    user_type.bind("<KeyRelease>", on_key_release)

    timer_function()

def timer_function():
    global timer_running, time_duration, start_time
    if timer_running:
        remaining_time = time_duration - (time.time() - start_time)

    if remaining_time <= 0:
        text = user_type.get("1.0", END)

        remaining_time = 0
        timer_running = False

        start_button.config(state=NORMAL)
        difficulty_menu.config(state=NORMAL)
        instruction_button.config(state=NORMAL)

        user_type.delete("1.0", END)
        user_type.insert("1.0", 'Text deleted due to inactivity.')
        user_type.config(bg='red', state=DISABLED)

        save_file(text)

    timer_label.config(text=f'Timer: {remaining_time:.0f} seconds')

    if f'{remaining_time:.0f}' == '3':
        user_type.config(fg='firebrick1')
        timer_label.config(fg='firebrick1')
    elif f'{remaining_time:.0f}' == '2':
        user_type.config(fg='red2')
        timer_label.config(fg='red2')
    elif f'{remaining_time:.0f}' == '1':
        user_type.config(fg='red4')
        timer_label.config(fg='red4')
    elif f'{remaining_time:.0f}' == '0':
        timer_label.config(fg='firebrick4')
    else:
        user_type.config(fg='black')
        timer_label.config(fg='gold')


    if remaining_time > 0:
        info_frame.after(1000, timer_function)


def reset():
    global timer_running, time_duration, start_time

    # Stop timer
    timer_running = False
    time_duration = None

    # Reset timer display
    timer_label.config(text="Timer: 00", fg=TEXT)

    # Clear and disable text box
    user_type.config(state='normal', fg=TEXT, bg=BG_COLOR)
    user_type.delete("1.0", END)
    user_type.config(state=DISABLED)

    # Reenable controls
    start_button.config(state=NORMAL)
    difficulty_menu.config(state=NORMAL)
    instruction_button.config(state=NORMAL)

    # Reset timer colors
    timer_label.config(fg=TEXT)

def save_file(text):

    filename = filedialog.asksaveasfilename(
        filetypes=( ("Text Files", "*.txt"),("All Files", "*.*") ),
        defaultextension=".txt",
        title="Save your text"
    )

    if filename:
        with open(filename, "w", encoding="utf-8") as text_file:
            text_file.write(text)


def toggle_instructions():
    global instructions_visible

    if instructions_visible:
        instruction_text.grid_remove()
        instructions_visible = False
    else:
        instruction_text.grid(
            row=5,
            column=0,
            padx=(0, 20),
            pady=(20, 0),
            sticky="w"
        )
        instructions_visible = True





window = Tk()
window.config(height=800, width=1000, padx=20, pady=20, bg=FRAME_BG_COLOR)
window.title("Disappearing Text Writing App")
window.resizable(False, False)

Difficulty_var = StringVar()
Difficulty_var.set('Easy')

typing_frame = Frame(window, bg=FRAME_BG_COLOR)
typing_frame.grid(column=0, row=0, padx=10, pady=10)

info_frame = Frame(window, bg=FRAME_BG_COLOR)
info_frame.grid(column=1, row=0, padx=10, pady=10, sticky='n')

write_below = Label(typing_frame, text='Disappearing Text Writing App', bg=BG_COLOR, fg=TEXT, font=FONT)
write_below.grid(column=0, row=0, padx=10, pady=10)

user_type = Text(typing_frame, bg=BG_COLOR, fg=TEXT, font=FONT, height=10, width=80)
user_type.grid(column=0, row=1, padx=10, pady=10)

instruction_text = Text(
                        info_frame,
                        bg=BG_COLOR,
                        fg=TEXT,
                        font=FONT,
                        wrap='word',
                        width=30,
                        height=15,
                        relief="solid",
                        bd=1,
                        padx=10,
                        pady=10
                       )

instruction_text.insert('1.0', instructions)
instruction_text.config(state=DISABLED)

instruction_button = Button(
                            typing_frame,
                            text='Instructions',
                            bg=BUTTON_BG_COLOR,
                            fg='white',
                            font=FONT,
                            activeforeground='white',
                            activebackground=BUTTON_FG_COLOR,
                            width=10,
                            command=toggle_instructions
                            )

instruction_button.grid(column=0, row=2, padx=10, pady=10)

timer_frame = Frame(info_frame, bg=FRAME_BG_COLOR)
timer_frame.grid(column=0, row=0, padx=(0, 20))

difficulty_frame = Frame(info_frame, bg=FRAME_BG_COLOR)
difficulty_frame.grid(column=0, row=1, padx=(0, 20))

start_frame = Frame(info_frame, bg=FRAME_BG_COLOR)
start_frame.grid(column=0, row=2, padx=(0, 20))

timer_label = Label(timer_frame, text='Timer: 00', bg=BG_COLOR, fg=TEXT, font=FONT)
timer_label.grid(pady=10)

difficulty_label = Label(difficulty_frame, text='Difficulty', bg=BG_COLOR, fg=TEXT, font=FONT)
difficulty_label.grid(column=0, row=0, pady=(0, 20))

difficulty_menu = OptionMenu(difficulty_frame, Difficulty_var, *['Easy', 'Medium', 'Hard'])
difficulty_menu.config(
                        bg=BUTTON_BG_COLOR,
                        fg='white',
                        font=FONT,
                        activeforeground='#0F172A',
                        activebackground=BUTTON_FG_COLOR,
                        width=12
                      )

difficulty_menu["menu"].config(
                                bg=FRAME_BG_COLOR,
                                fg=TEXT,
                                font=FONT,
                                activebackground=BUTTON_BG_COLOR,
                                activeforeground="#0F172A"
                              )

difficulty_menu.grid(column=0, row=3, padx=10, pady=(0, 20))

start_button = Button(
                        start_frame,
                        text='Start',
                        bg=BUTTON_BG_COLOR,
                        fg='white',
                        font=FONT,
                        activeforeground='white',
                        activebackground=BUTTON_FG_COLOR,
                        width=14,
                        command=start_writing
                      )
start_button.grid(column=0, row=4, padx=10, pady=(0, 10))

reset_button = Button(
                        start_frame,
                        text='Reset',
                        bg=BUTTON_BG_COLOR,
                        fg='white',
                        font=FONT,
                        activeforeground='white',
                        activebackground=BUTTON_FG_COLOR,
                        width=14,
                        command=reset
                      )
reset_button.grid(column=0, row=5, padx=10, pady=(0, 10))

window.mainloop()