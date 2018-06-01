'''
Prog:   turtleTest.py
Name:   Katie Mackey
Date:   2018-05-25
Desc:   messing around with turtle graphics
'''
import turtle
window = turtle.Screen()
al = turtle.Turtle()
def a():
    al.left(90)
    al.right(30)
    al.forward(100)
    al.right(120)
    al.forward(100)
    al.penup()
    al.backward(50)
    al.pendown()
    al.right(120)
    al.forward(50)
x = input()
while x:
    if x == "a":
        a()
    else:
        print("wot")
    x = input()
window.exitonclick()
