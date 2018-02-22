'''
Name: Katie Mackey
Desc: simulates a magic 8Ball using random integers
'''
options = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Do not count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
q = input("What do you wish to ask the Magic 8-Ball? ")
import random
import sys
while q != "quit":
    r = random.randint(0,19)
    print(options[r])
    q = input("What do you wish to ask the Magic 8-Ball? ")
#in combination with the while statement, when the user says quit, the program shuts down
sys.exit()
