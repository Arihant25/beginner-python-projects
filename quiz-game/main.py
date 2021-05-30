from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in range(len(question_data)):
    question = Question(question_data[q]['question'], question_data[q]['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

print("Let's start the quiz, shall we?\n")
print("Get ready, here's the first question, coming up on your screen!\n")

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")