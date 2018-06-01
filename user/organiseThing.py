'''
Prog:   organiseThing.py
Name:   Katie Mackey
Date:   2018-05-31
Desc:   organise skincare products. hopefully.
To-do:
delete products

mode = input("What would you like to do:\n1 - Add a product\n2 - Find a product\n3 - Edit a product\n")
'''
import csv
import fileinput
#F U N C T I O N S
def display(row):
    print("Name:",row['name'])
    print("Price: $"+row['price'])
    print("Type:",row['type'])
    print("Concern:",row['concern'])
    print('\n')

def find(category,query):
    with open('database.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if str(query).lower() in row[str(category)].lower():
                display(row)

def add(product):
    with open('database.csv', 'a') as f:
        brand = input("Brand: ")
        price = input("Price: ")
        type = input("Type of product: ")
        concern = input("Concern: ")
        rating = input("Rating: ")
        status = input("Status: ")
        f.write(brand+","+product+","+price+","+type+","+concern+","+rating+","+status+"\n")
    print("Product added")

def replace(product, category, newData):
    with open('database.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if str(product).lower() in row['name'].lower():
                i = row[str(category)]
    with open('database.csv','r') as f:
        data = f.read()
        data = data.replace(i, newData)
    with open("database.csv", "w") as outputfile:
        outputfile.write(data)

#START BITCH
mode = input("What would you like to do:\n1 - Add a product\n2 - Find a product\n3 - Edit a product\n")
while mode:
    if mode == "1":
        add(input("What is the name of the product? "))
        mode = input("What would you like to do:\n1 - Add a product\n2 - Find a product\n3 - Edit a product\n")
    elif mode == "2":
        a = input("What would you like to search by? ")
        while a:
            if a in "brand,name,price,type,concern,rating,status":
                print("Searching by", a)
                b = input("What would you like to search? ")
                find(a,str(b))
                a = input("What would you like to search by? ")
            else:
                print("That is not a valid category, please try again.")
                a = input("What would you like to search by? ")
        mode = input("What would you like to do:\n1 - Add a product\n2 - Find a product\n3 - Edit a product\n")
    elif mode == "3":
        product = input("What product would you like to change? ")
        category = input("What detail would you like to change? ")
        newData = input("What would you like to change it to? ")
        replace(product, category, newData)
        print("Product changed")
        mode = input("What would you like to do:\n1 - Add a product\n2 - Find a product\n3 - Edit a product\n")
    elif mode == "help":
        print("Welcome to organiseThing, supposedly used to store and review details on different skincare products.")
        print("Available categories to search by:")
        print(" brand\n name\n price\n type\n concern\n rating\n status")
        print("editing and deleting products is currently unavailable, because CSV files are a pain in the ass. Sorry.\nYou can go into the database file manually if you really want, just don't move any commas around.\n\n")
        mode = input("What would you like to do:\n1 - Add a product\n2 - Find a product\n3 - Edit a product\n")
    else:
        print("\aSorry! That's not an option, try again.")
        mode = input("What would you like to do:\n1 - Add a product\n2 - Find a product\n3 - Edit a product\n")
