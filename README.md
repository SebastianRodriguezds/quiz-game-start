This is a simple True/False Quiz Game built using Python. The game allows users to answer a series of trivia questions, 
track their score, and see how well they did at the end. The game is structured using object-oriented principles and is
divided into three main modules: main.py, quiz_brain.py, and question_model.py.

Main Features:

  Question Model: Each question is represented by a Question object that holds the question text and the correct answer. The Question class is defined in question_model.py.

  Quiz Brain: The QuizBrain class manages the game flow, including checking answers, calculating the score, and keeping track of the questions. It is responsible for controlling the quiz logic and providing feedback to the user. The class is defined in quiz_brain.py.

  Game Flow: Still Has Questions: The game checks whether there are still questions to ask using the still_has_questions() method.
  Answer Checking: The user's answer is compared to the correct answer (case-insensitive) using the check_answer() method.
  Score Tracking: The score is updated each time the user answers correctly, and feedback is provided after each question.

  Final Score: At the end of the quiz, the player’s final score is displayed using the final_score() method.