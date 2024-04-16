from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
#importing all the classes

question_bank = []
# question_bank used for storing the questions
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    #adding the questions from data.py to question_bank

quiz = QuizBrain(question_bank)
#used to tap into the attributes in the quizbrain class

while quiz.still_has_questions():
    quiz.next_question()
    #while quiz is not done

print("\nyou have completed the quiz")
print(f"your final score was {quiz.score}/{quiz.question_number}")
#shows results