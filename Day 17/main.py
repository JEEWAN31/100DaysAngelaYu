# from quiz_brain import QuizBrain
# from question_model import Question
# from data import question_data
#
# questions = []
#
# for question in question_data:
#     problem = question["question"]
#     solution = question["correct_answer"]
#     m = Question(problem, solution)
#     questions.append(m)
#
# quiz = QuizBrain(questions)
#
# while quiz.still_has_questions():
#     quiz.next_question()
#
# print(f"You have completes the quiz with score of {quiz.score} out of total question as {quiz.question_number}")
#
#
#
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

