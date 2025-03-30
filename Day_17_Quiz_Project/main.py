from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# TODO-1 - Create the Question Class
# TODO-2 - Creating the List of Question Objects from the Data
# TODO-3 - Create QuizBrain Class and the next_question() Method
# TODO-4 - Continue showing new Questions
# TODO-5 - Checking Answers and Keeping Score


question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")