'''
prog: fibonacci.py
Name: Katie
Date: 2018-04-18
Desc: generates and prints fibonacci sequence to the Nth number.
'''
def fib(n):
    if n == 0:
        print("That's not how numbers work my friend...")
    elif n == 1:
        print("0, yes 0, the fibonacci sequence starts at 0 not at 1")
    else:
        num = ["0","1"]
        i = 2
        while i < n:
            num.append(str(int(num[-2])+int(num[-1])))
            i = i + 1
        print(", ".join(num))
