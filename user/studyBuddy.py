'''
Prog:   studyBuddy.py
Name:   Katie Mackey
Date:   2018-05-08
Desc:   FLASHCARDS
To-do: add more questions
randomise question order
add override for typos?
chose subject (again, more questions)

'''
score = 0
subjects = ["maths","science","history","secret"]
maths = {
    "A histogram is used to display what kind of data? ":"numerical",
    "What is another name for the average? ":"mean",
    "The x-intercepts of a graph can be found when y equals what? ":"0",
    "eggs? ":"eggs.",
    "y=a(x-k)^2+h | what is this form called? ":"turning point"
}
science = {
    "The mitochondria is often referred to as the what of the cell?":"powerhouse",
}
history = {
    "x":"x",
}
secret = {
    "x":"x",
}
def ask(subject,q):
    global score
    a = input(q).lower()
    a = a.strip()
    if subject[q] in a:
        print("Correct!")
        score += 1
    else:
        print("Incorrect, the answer was", subject[q])

def create():
    global subjects
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
        subjects.append(s)
        print("To finish entering questions hit enter when prompted for your question.")
        q = input("Please enter your question: ")+" "
        while q:
            a = input("Please enter the answer: ").lower()
            s = dict()
            s[q] = a
            q = input("Please enter your question: ")

x = input("What subject would you like to revise? ")
while x:
    if x == "maths":
        for q in maths:
            ask(maths,q)
        print("Your final score was", score,"out of", len(maths), "or", str(score/len(maths)*100)+"%")
        score = 0
    elif x == "science":
        for q in science:
            ask(science,q)
        print("Your final score was", score,"out of", len(science), "or", str(score/len(science)*100)+"%")
        score = 0
    elif x == "history":
        for q in history:
            ask(history,q)
        print("Your final score was", score,"out of", len(history), "or", str(score/len(history)*100)+"%")
        score = 0
    elif x == "supersecretsubject":
        for q in secret:
            ask(secret,q)
        print("Your final score was", score,"out of", len(secret), "or", str(score/len(secret)*100)+"%")
        score = 0
    else:
        print("Sorry, we don't have any questions for that subject.")
        p = input("Would you like to add a question? ")
        if p == "yes":
            create()
        else:
            x = input("What subject would you like to revise? ")
    x = input("What subject would you like to revise? ")
