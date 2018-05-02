'''
Prog:   lists.py
Name:   Katie Mackey
Date:   2018-05-02
Desc:   List exercise from GitHub.
'''
import random

roll = ['Jessica', 'Emily', 'Jordan', 'Kayley', 'Bruce', 'Michael', 'Everett', 'Lisa', 'Sam', 'Noah']
print(roll[2])
enrolment = len(roll)
roll.append("James")
del roll[2]
roll[4] = 'Mike'
#I keep getting error messages when trying to sort and reverse lists??
#sRoll = roll.sort()
#print(sRoll)
#rRoll = sRoll.reverse()
#print(rRoll)
print(roll[random.randint(0,9)])
roll1 = roll[:4]
roll2 = roll[-5:]
