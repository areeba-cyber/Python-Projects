import random 

def set_difficulty(level_chosen):
    if level_chosen == 'easy':
     attempts = 10
    else:
     attempts = 5


print("Let me think of a number between 1 to 50")
answer = random.randint(1, 50)
print(answer)

Level = input("Choose the level of difficulty... Type 'easy' or 'hard'")
set_difficulty (Level)
