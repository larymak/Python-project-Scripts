from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

quiz_list = []
for question in question_data:
    q_object = Question(question["question"], question["correct_answer"])
    quiz_list.append(q_object)

quiz = QuizBrain(quiz_list)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_num}")