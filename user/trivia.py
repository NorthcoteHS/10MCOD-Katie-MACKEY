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
    "y=a(x-k)^2+h | what is this form called? ":"turning point form"
}
def quiz(subject):
    for q in subject:
        a = input(q).lower()
        if a == subject[q]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect, the answer was", subject[q])
    print("Your final score was", score,"out of", len(subject), "or", str(score/len(subject)*100)+"%")
x = input("What subject would you like to revise? ")
quiz(x)
