'''
Prog:   subjectMaker.py
Name:   Katie Mackey
Date:   2018-05-09
Desc:   add a subject with questions to studyBuddy.py
'''
subjects = ["maths","science","history","history"]
def create():
    s = input("Please enter the name of the subject: ").lower()
    #check if subject already exists
    if s in subjects:
        print("To finish entering questions hit enter when entered")
        q = input("Please enter your question: ")
        while q:
            a = input("Please enter the answer: ")
            s[q]=a
            q = input("Please enter your question: ")
    else:
        print("To finish entering questions hit enter when prompted for your question.")
        q = input("Please enter your question: ")
        while q:
            a = input("Please enter the answer: ")
            s = dict()
            s[q] = a
            q = input("Please enter your question: ")
#BEGIN
p = input("Would you like to add a question? ")
if p == "yes":
    create()
else:
    print("ok then.be that way.")
