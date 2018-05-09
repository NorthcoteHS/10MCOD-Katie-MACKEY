'''
Prog:   subjectMaker.py
Name:   Katie Mackey
Date:   2018-05-09
Desc:   add a subject with questions to studyBuddy.py
'''
subjects = ["maths","science","history","secret"]
p = input("would like to add a subject? ")
if p == "yes":
    s = input("Please enter the name of the subject: ")
    if s in subjects:
        print("to finish entering questions hit enter when entered")
    q = input("Please enter your question: ")
    while q:
        a = input("Please enter the answer: ")
        s[q] = a
        q = input("Please enter your question: ")
    else:
        s = {}
        subjects.append(s)
        print("to finish entering questions hit enter when entered")
        q = input("Please enter your question: ")
        while q:
            a = input("Please enter the answer: ")
            s[q] = a
            q = input("Please enter your question: ")
else:
    break
