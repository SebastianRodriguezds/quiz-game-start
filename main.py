import question_model
import data
import random

questions_list = []

def make_question(text, answer):
  question = question_model.Question(text, answer)
  questions_list.append(question)

for item in data.question_data:
  make_question(item["text"] , item["answer"])

def return_question():
  question = random.choice(questions_list)
  return question



def check_answer(guess, answer):
  if answer == guess:
    return True
  return False



game_is_playing = True


while game_is_playing:
  question = return_question()
  print(question.text)
  print(question.answer)
  user_answer = input("is either 'True' or 'False'")
  if check_answer(user_answer, question.answer):
    print("Repsuesta correcta")
  else:
    print("Incorrecta")
  
  game_is_playing = False




  
  
