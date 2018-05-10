'''
Prog:   studyBuddy.py
Name:   Katie Mackey
Date:   2018-05-08
Desc:   FLASHCARDS
To-do:
randomise question order
'''
import random
#score counter
score = 0
#list of subjects
subjects = ["maths","science","history","secret"]
#questions
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
    "Did dinosaurs exist? ":"yes",
    "What was the famous wooden animal used to infiltrate Troy? ":"horse",
    "In what year was Jesus born?":"0bc",
    "When did WW1 end? ":"11 november 1980"
}
secret = {
    "What is Suga's real name? ":"min yoongi",
    "How many members are in Seventeen? ":"13",
    "Who is the main dancer in NCT? ":"ten",
    "Who is the youngest member of NCT Dream? ":"jisung park"
}
#function to ask the user the question, input for subject and q from for loop
def ask(subject,q):
    #allow access to global variable
    global score
    #get lOW
    a = input(q).lower()
    #Get rid of whitespace before and after answer
    a = a.strip()
    #is is correct?
    if eval(subject)[q] in a:
        print("Correct!")
        score += 1
    else:
        print("Incorrect, the answer was", eval(subject)[q])
#function to create questions, adding to subjects if it already exists or creating a new subject.
def create():
    #access global
    global subjects
    #get name of subject
    s = input("Please enter the name of the subject: ").lower()
    #check if subject already exists
    if s in subjects:
        #instructions to finish
        print("To finish entering questions hit enter when prompted for your question.")
        #get question and add space for aesthetic purposes
        q = input("Please enter your question: ")+" "
        #loop to add multiple questions
        while q:
            a = input("Please enter the answer: ")
            #add to dictionary
            s[q]=a
            q = input("Please enter your question: ")
    else:
        #add to list of subjects
        subjects.append(s)
        #create global dictionary
        globals()[s] = dict()
        print("To finish entering questions hit enter when prompted for your question.")
        q = input("Please enter your question: ")+" "
        #loopity loop
        while q:
            a = input("Please enter the answer: ").lower()
            #add question to dictionary
            globals()[s][q] = a
            q = input("Please enter your question: ")
#ask what subject
x = input("What subject would you like to revise? ")
#loop loop motherfuckers
while x:
    #check if subject exists
    if x in subjects:
        #cycle through questions
        for q in eval(x):
            ask(x,q)
        #print score out of total and percentage
        print("Your final score was", score,"out of", len(eval(x)), "or", str(score/len(eval(x))*100)+"%")
        #reset score
        score = 0
    else:
        #my deepest apologies sire.
        print("Sorry, we don't have any questions for that subject.")
        #would you like to fix it sire?
        p = input("Would you like to add a question? ")
        if p == "yes" or p == "y":
            create()
        else:
            #keep tha loop going (or let it stop at some point)
            x = input("What subject would you like to revise? ")
    #pls don't loop to infinity my bro
    x = input("What subject would you like to revise? ")
