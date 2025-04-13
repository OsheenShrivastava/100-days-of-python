from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR)
        self.window.config(padx=20, pady=20)

        # Score Label
        self.Score_Label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.Score_Label.grid(row=0, column=1)

        # Canvas window for Question
        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(125, 120, width=250, text="Some Question Text",
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # NOTE: Since we won't be using True and False button image, so we did not create them as a part of class
        # True Button
        True_png = PhotoImage(file="images/true.png")
        self.True_Button = Button(image=True_png, highlightthickness=0, command=self.True_Loop)
        self.True_Button.grid(row=2, column=0)

        # False Button
        False_png = PhotoImage(file="images/false.png")
        self.False_Button = Button(image=False_png, highlightthickness=0, command=self.False_Loop)
        self.False_Button.grid(row=2, column=1)

        self.get_next_question()

        # Command to display the screen
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.Score_Label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.True_Button.config(state="disabled")
            self.False_Button.config(state="disabled")

    def True_Loop(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def False_Loop(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, func=self.get_next_question)


