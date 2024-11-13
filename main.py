import question_model
import data
import random
from quiz_brain import QuizBrain
def make_question():
  for item in data.question_data:
    question = question_model.Question(item["text"] , item["answer"])
    questions_list.append(question)

def return_question():
  question = random.choice(questions_list)
  return question

def check_answer(guess, answer):
  if answer == guess:
    return True
  return False


questions_list = []
make_question()
quiz = QuizBrain(questions_list)
quiz.next_question()




  
  
