'''
Prog: Caesar 2.0.py
Name: Katie Mackey
Date: 2018-03-14
Desc: An improved caesar cypher, this time with caps sensitivity.
'''
import string

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Please enter a number.")
            continue
        else:
            return int(userInput)
        break
#letter to number
a = dict()
#counting variable
i = 1
#making dictionary a
for x in string.ascii_lowercase:
    a[x] = i
    i += 1
i = -26
for x in string.ascii_uppercase:
    a[x] = i
    i += 1
i = 0
#number value to letter
b = {v: k for k, v in a.items()}
#define functions
def encode():
    import string
    i = 0
    txt = input("Plaintext: ").split()
    o = inputNumber("Offset: ")
    ctxt = []
    for x in txt:
        while i < len(x):
            if x[i] in string.ascii_letters:
                z = a[x[i]]+ o
                ctxt.append(b.get(z, b.get(z + 26, b.get(z - 26, z))))
            elif x[i] in string.digits:
                ctxt.append(str(int(x[i])+ o))
            else:
                ctxt.append(x[i])
            i += 1
        i = 0
        ctxt.append(" ")
    print(''.join(ctxt))

def decode():
    import string
    i = 0
    txt = input("Plaintext: ").split()
    o = inputNumber("Offset: ")
    ctxt = []
    for x in txt:
        while i < len(x):
            if x[i] in string.ascii_letters:
                z = a[x[i]]- o
                ctxt.append(b.get(z, b.get(z + 26, b.get(z - 26, z))))
            elif x[i] in string.digits:
                ctxt.append(str(int(x[i])- o))
            else:
                ctxt.append(x[i])
            i += 1
        i = 0
        ctxt.append(" ")
    print(''.join(ctxt))
'''
Here is where the fun began.
'''
mode = inputNumber("Encode - 1, Decode - 2 : ")
while mode:
    if mode == 1:
        encode()
        mode = inputNumber("Encode - 1, Decode - 2 : ")
    elif mode == 2:
        decode()
        mode = inputNumber("Encode - 1, Decode - 2 : ")
