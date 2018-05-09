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
x = input("What subject would you like to revise? ")
while x:
    if x == "maths":
        for q in maths:
            a = input(q).lower()
            if maths[q] in a:
                print("Correct!")
                score += 1
            else:
                print("Incorrect, the answer was", maths[q])
        print("Your final score was", score,"out of", len(maths), "or", str(score/len(maths)*100)+"%")
    elif x == "science":
        for q in science:
            a = input(q).lower()
            if science[q] in a:
                print("Correct!")
                score += 1
            else:
                print("Incorrect, the answer was", science[q])
        print("Your final score was", score,"out of", len(science), "or", str(score/len(science)*100)+"%")
    elif x == "history":
        for q in history:
            a = input(q).lower()
            if history[q] in a:
                print("Correct!")
                score += 1
            else:
                print("Incorrect, the answer was", history[q])
        print("Your final score was", score,"out of", len(history), "or", str(score/len(history)*100)+"%")
    elif x == "supersecretsubject":
        for q in secret:
            a = input(q).lower()
        if secret[q] in a:
            print("Correct!")
            score += 1
        else:
            print("Incorrect, the answer was", secret[q])
        print("Your final score was", score,"out of", len(secret), "or", str(score/len(secret)*100)+"%")
    else:
        print("Sorry, we don't have any questions for that subject. Please chose from: maths, science or history.")
    x = input("What subject would you like to revise? ")
