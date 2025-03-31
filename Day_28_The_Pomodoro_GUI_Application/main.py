from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25         # To test change this to 1 minute
SHORT_BREAK_MIN = 5   # Change this to 1 minute
LONG_BREAK_MIN = 10   # Change this to 2 minutes
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
# TODO-14 - Create a function reset_timer and cancel the timer
def reset_timer():
    window.after_cancel(timer)

    # TODO-15 - Finally, print 00:00 when timer resets, change timer label to green and reset
    #  check marks
    canvas.itemconfig(Timer_text, text="00:00")
    Timer_label.config(text="Timer", fg=GREEN)
    Tick_label.config(text="")

    # TODO-16 - Reset reps variable so that the cycle runs again from start
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
# TODO-7 - Create a function to start the timer


def start_timer():
    # TODO-9 - Calculate work and breaks time in seconds
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # TODO-10 - Call count_down() function to run all timers and create if else loop to write
    #  a short break for 4 times after work. Long break has to be added only on the 8th
    #  cycle. Otherwise, it should run work cycle.

    if reps % 8 == 0:
        count_down(long_break_sec)
        Timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        Timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        Timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# TODO-5 - Create a function to count minutes and seconds
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # TODO-8 - Add a 0 if seconds are less than 10
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(Timer_text, text=f"{count_min}:{count_sec}")
    # TODO-6 - Use window.after() function to count the time every second and reduce the time
    if count > 0:
        # TODO-13 - Define timer at the starting and then make it global, so it could be used
        #  in reset_timer function
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # TODO-12 - Add a check mark after every 2 reps completed on the canvas
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        Tick_label.config(text=mark)

    # ---------------------------- UI SETUP ------------------------------- #

# TODO-1 - Import Tkinter and create A Window
window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=YELLOW)

# TODO-2 - Use Canvas Module and import the image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)

# TODO - 3 - Write the text on image using Canvas module functions
Timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

# TODO-4 - Use Foreground function to write the floating text on the canvas
Timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
Timer_label.grid(row=0, column=1)

Tick_label = Label(fg=GREEN, bg=YELLOW)
Tick_label.grid(row=3, column=1)

# TODO-11 - Call start_timer function
Start_button = Button(text="Start", bg="white", highlightthickness=0, command=start_timer)
Start_button.grid(row=2, column=0)

Reset_button = Button(text="Reset", bg="white", highlightthickness=0, command=reset_timer)
Reset_button.grid(row=2, column=2)

window.mainloop()
