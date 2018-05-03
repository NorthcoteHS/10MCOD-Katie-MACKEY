'''
Prog:   countdown.py
Name:   Katie Mackey
Date:   2018-05-03
Desc:   Counts down from 10 then says BLASTOFF, with a second in between each one.
'''
import time

for i in range(0,10):
    print(10-i)
    time.sleep(1)
print("BLASTOFF!")
