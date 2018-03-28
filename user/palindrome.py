'''
Prog: palindrome.py
Name: Katie M
Date: 27.3.18
Desc: User inputs a word or phrase and the program will test if it is a palindrome
'''
#get word or phrase
w = input("Enter a word to check: ")
#removes spaces from a sentence, if it is only one word it stays the same
w2 = ''.join(w.split())
#creates reversed word
bw = w2[::-1]
#testing if they are the same (getting rid of capitalisation)
if w2.lower() == bw.lower():
    print(w,"is an anagram!")
else:
    print(w,"is not an anagram.")
