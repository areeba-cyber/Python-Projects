import random 
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty(level_chosen):
    if level_chosen == 'easy':
     return EASY_LEVEL_ATTEMPTS
    else:
     return HARD_LEVEL_ATTEMPTS

def check_answer(guessed_number, answer, attempts):
  if guessed_number < answer:
    print("Your guess is LOW")
    return attempts-1
  elif guessed_number > answer:
    print("Your guess is HIGH")
    return attempts-1
  else:
    print(f"Your guess is right... The answer was {answer}")


def game():
 print("Let me think of a number between 1 to 50")
 answer = random.randint(1, 50)
 print(answer)

 Level = input("Choose the level of difficulty... Type 'easy' or 'hard'")
 attempts = set_difficulty (Level)
 guessed_number = 0
 while guessed_number != answer:

  print(f"You have {attempts} reamaining attempts to guess a number")
  guessed_number = int(input("Guess Number:"))
  attempts = check_answer(guessed_number, answer, attempts)
  if attempts == 0:
   print("You are out of guesses... YOY LOSE!")
   return
  else:
    print("Guess Number again . . . ")

game()