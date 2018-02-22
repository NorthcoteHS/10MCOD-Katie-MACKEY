'''
Name: Katie Mackey
Desc: Caesar cypher encoder and decoder, where the user sets the offset. Ignores punctuation and spaces (and numbers).
'''
#integer checker I may or may not have stolen from the internet
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an option! Try again.")
       continue
    else:
       return int(userInput) 
       break
#chose if encoding or decoding
mode = inputNumber("Select: 1-encode 2-decode ")
if mode == 1:
    #original message
    code = input("Enter message: ")
    #how much it's shifted by
    offset = int(input("Enter offset: "))
    #because I'm having enough difficulty with only capitals...
    code = code.upper()
    #original code turned into list as ascii numbers
    code2 = []
    #shifted code
    shift = []
    #shifted code turned back into letters
    shift2 = []
    for c in code:
        #change into numbers in a list
        code2.append(ord(c))

    for i in code2:
        #ignoring punctuation (and numbers)
        if i <= 64:
            shift.append(i)
        else:
            shift.append(i + offset) #adding offset
    for s in shift:
        #making it wrap back around
        if s > 90:
            s = s - 26
        shift2.append(chr(s))
    #joining together into string
    final = "".join(shift2)
    print(final)
else:
  #same as when encoding
    code = input("Enter message: ")
    offset = int(input("Enter offset: "))
    code = code.upper()
    code2 = []
    shift = []
    shift2 = []
    for c in code:
        code2.append(ord(c))
    for i in code2:
        if i <= 64:
            shift.append(i)
        else:
          #a slightly different method to make it wrap around because punctuation
          if i - offset <=64:
            shift.append(i - offset + 26)
          else:
            shift.append(i - offset)
    for s in shift:
        shift2.append(chr(s))
    final = "".join(shift2)
    print(final)
