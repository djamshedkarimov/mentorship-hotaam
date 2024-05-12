from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
'''importing everything'''

question_bank = []
'''the question list!!!'''
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    '''for every question in question_data (data with all of the questions)
        make text and answer and append that to question_bank'''


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
'''quiz and quiz gui'''
