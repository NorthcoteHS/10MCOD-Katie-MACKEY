'''
Prog:   squareNumbers.py
Name:   Katie Mackey
Date:   2018-05-03
Desc:   squres numbers 1-10 and prints them in a list
'''
squares = []
for i in range(1,11):
    squares.append(str(i**2))
print(",".join(squares))
