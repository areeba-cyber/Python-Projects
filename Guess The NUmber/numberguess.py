import random 
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty(level_chosen):
    if level_chosen == 'easy':
     return EASY_LEVEL_ATTEMPTS
    else:
     return HARD_LEVEL_ATTEMPTS


print("Let me think of a number between 1 to 50")
answer = random.randint(1, 50)
print(answer)

Level = input("Choose the level of difficulty... Type 'easy' or 'hard'")
attempts = set_difficulty (Level)

print(f"You have {attempts} reamaining attempts to guess a number")
guessed_number = input(int("Guess Number:"))
