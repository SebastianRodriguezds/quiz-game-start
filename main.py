import question_model
import data
from quiz_brain import QuizBrain

def make_question():
  for item in data.question_data:
    question = question_model.Question(item["text"] , item["answer"])
    questions_list.append(question)

questions_list = []
make_question()
quiz = QuizBrain(questions_list)

while quiz.still_has_questions():
  quiz.next_question()
quiz.final_score()





  
  
