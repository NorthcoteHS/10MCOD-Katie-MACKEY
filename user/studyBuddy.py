'''
Prog:   studyBuddy.py
Name:   Katie Mackey
Date:   2018-05-08
Desc:   FLASHCARDS
To-do: add more questions
randomise question order

'''
score = 0
subjects = ["maths","science","history","secret"]
maths = {
    "A histogram is used to display what kind of data? ":"numerical",
    "What is another name for the average? ":"mean",
    "The x-intercepts of a graph can be found when y equals what? ":"0",
    "y=a(x-k)^2+h | what is this form called? ":"turning point"
}
science = {
    "The mitochondria is often referred to as the what of the cell? ":"powerhouse",
    "Distance over time is equal to what? ":"velocity",
    "Covalent bonding occurs between which kind of atoms? ":"non-metal",
    "Pb is the atomic symbol for which element? ":"lead"
}
history = {
    "x":"x",
}
secret = {
    "What is Suga's real name? ":"min yoongi",
    "How many members are in Seventeen? ":"13",
    "Who is the main dancer in NCT? ":"ten",
    "Who is the youngest member of NCT Dream? ":"jisung park"
}
def ask(subject,q):
    global score
    a = input(q).lower()
    a = a.strip()
    if eval(subject)[q] in a:
        print("Correct!")
        score += 1
    else:
        print("Incorrect, the answer was", eval(subject)[q])

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
            globals()[s] = dict()
            globals()[s][q] = a
            q = input("Please enter your question: ")

x = input("What subject would you like to revise? ")
while x:
    if x in subjects:
        for q in eval(x):
            ask(x,q)
        print("Your final score was", score,"out of", len(eval(x)), "or", str(score/len(eval(x))*100)+"%")
        score = 0
    else:
        print("Sorry, we don't have any questions for that subject.")
        p = input("Would you like to add a question? ")
        if p == "yes":
            create()
        else:
            x = input("What subject would you like to revise? ")
    x = input("What subject would you like to revise? ")
