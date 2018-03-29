"""
Prog:   yesNoProgram.py
Name:   Katie Mackey
Date:   2018-03-29
Desc:   Answers yes or no to any question.
"""
#import random module
import random
# Ask the user for a question.
question = input('Ask me anything! ')

# Check for special input.
if  question == 'Quit':
    print('Goodbye.')
elif question == 'Hi' or question == 'Hello':
    print("What's up?")

# Answer yes or no randomly.
num = random.randint(1,2)
if num == "1":
    print("Yes!")
elif num == 2:
    print("No")
