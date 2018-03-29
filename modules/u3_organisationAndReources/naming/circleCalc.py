'''
Prog: circleCalc.py
Name: Katie Mackey
Date: 2018-03-29
Desc: Calculates and returns the area and perimeter of a circle from the radius
'''
#welcome message
print('Welcome to the Circle Calculator!')

#get radius from user
r = input('Enter a radius: ')
#turn into integer
r = int(r)

#calculate and print area
area = 3.14 * r * r
print('The area is', area)
#calculate and print perimeter
perimeter = 3.14 * r * 2
print('The perimeter is', perimeter)
