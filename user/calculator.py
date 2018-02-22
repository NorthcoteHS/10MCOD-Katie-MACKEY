'''
Name: Katie Mackey
Desc: Calculator that has the option have show division with a remainder or as a decimal
'''
#making sure the user puts in an integer
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return int(userInput) 
       break
#getting all the inputs
r = input("remainder or decimal (r/d): ")
nA = inputNumber("First number: ")
o = input("Operation: ")
#checking operation against supported operations
op = ['divide', 'multiply', 'plus', 'minus']
if o in op != True:
    print("Sorry! that operation is not supported. Please check your input and try again.")
    o = input("Operation: ")
nB = inputNumber("Second number: ")

#checking operation against supported operations
op = ['divide', 'multiply', 'plus', 'minus']
if o in op:
    print("Sorry! that operation is not supported. Please check your input and try again.")
    o = input("Operation: ")
#now for division, trying to support having a remainder or just a decimal
if r == "r" and o == "divide":
    print("The answer is",int(nA/nB),nA%nB) 
elif r == "d" and o == "divide":
    print("The answer is",float(nA/nB)) 
elif o == 'plus':
          print("The answer is",nA + nB) 
elif o == 'minus':
          print("The answer is",nA - nB) 
elif o == 'multiply':
          print("The answer is",nA*nB) 
else:
          print("Something went wrong. Sorry.")



''' I DONT UNDERSTAND WHY WE'RE MAKING A CALCULATOR
          WHEN PYTHON CAN ALREADY DO IT'''

