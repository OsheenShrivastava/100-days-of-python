from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# TODO-1 - Create the Question Class
# TODO-2 - Create the List of Question Objects from the data.py by fetching data from API endpoint
# TODO-3 - Create QuizBrain Class and the next_question() Method
# TODO-4 - Continue showing new Questions
# TODO-5 - Import html module in quiz_brain.py and use html.unescape() to remove unwanted strings in questions fetched
#  from API
# TODO-6 - Import Tkinter in ui.py,create a class QuizInterface and initialize the window
# TODO-7 - Create Labels,Buttons and Canvas Window to complete the GUI
# TODO-8 - Return the next question from quiz_brain and pass it to ui.py
# TODO-9 - Pass QuizBrain class in QuizInterface
# TODO-10 - Initialize quiz_brain class passed as a parameter as a attribute of QuizInterface
# TODO-11 - Import QuizBrain class from quiz_brain.py. Define the datatype of quiz_brain as QuizBrain
# TODO-12 - Change the width of question_text in canvas window to wrap the question text
# TODO-13 - Create two new methods that needs to be added as commands to True and False Button. These methods need
#  to call check_answer() from the quiz_brain and pass over the string "True" or "False".
# TODO-14 - Return True or False from check_answer() method of QuizBrain class from quiz_brain.py.
# TODO-15 - Change the background colour to green if user guessed right and to red if guessed wrong
# TODO-16 - Change the window after 1000 secs,display next question and change the background colour to white
# TODO-17 - Check Answers and Keep Score
# TODO-18 - Check if quiz still has questions, once all questions are completed then tell the user and disable the
#  buttons


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
