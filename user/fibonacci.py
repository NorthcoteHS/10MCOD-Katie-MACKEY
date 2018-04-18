'''
prog: fibonacci.py
Name: Katie
Date: 2018-04-18
Desc: generates and prints fibonacci sequence to the Nth number.
'''

def fib(n):
    num = [0,1]
    i = 0
    for i < n:
        num.append(num[-2]+num[-1])
        i += 1
    print(num[0:n-1].join(","))

fib(5)
