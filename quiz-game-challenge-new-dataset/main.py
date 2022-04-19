from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_text = i["question"]                           # changing the variable is more than enough to complete this challenge
    question_answer = i["correct_answer"]                   # changing the variable is more than enough to complete this challenge
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)

# for i in question_bank:
#     print(i.text)
#     print(i.answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("you have completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")


