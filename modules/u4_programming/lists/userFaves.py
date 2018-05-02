'''
Prog:   userFaves.py
Name:   Katie Mackey
Date:   2018-05-02
Desc:   List exercise from GitHub
'''
favourites = []
i = input("What's one of your favourite movies? ")
while i != "quit":
    r = input("Rate it out of 10: ")
    favourites.append([i,r])
    i = input("What's one of your favourite movies? ")
print("Thank you for using Favourites, you stored", len(favourites), "movies.")
