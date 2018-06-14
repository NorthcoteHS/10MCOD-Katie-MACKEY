'''
Prog:   organiseThing.py
Name:   Katie Mackey
Date:   2018-05-31
Desc:   organise skincare products. hopefully.
'''
import csv
#F U N C T I O N S
#modified input to make sure the user enters something to prevent B U G S
def ask(text):
    x = input(str(text))
    while x == "":
        print("*This field is required*")
        x = input(str(text))
    return x
#function to display data for a product in a nice way
def display(row):
    print("Brand:",row['brand'])
    print("Name:",row['name'])
    print("Price: $"+row['price'])
    print("Type:",row['type'])
    print("Concern:",row['concern'])
    print("Rating:",row['rating'])
    print("Status:",row['status'])
    print('\n')

#find and display (if you want) a product or multiple products in database by category
def find(category,query,show):
    #counter in case product cannot be found
    i = 0
    with open('database.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            #check if product in user given category for each row
            if str(query).lower() in row[str(category)].lower():
                #add to counter to day you found something
                i += 1
                if show == 'no':
                    return(True)
                else:
                    display(row)
        if show == 'no':
            if i == 0:
                return(False)
        else:
            if i == 0:
                print("Product not in database. Try again\n")

def rating(query):
#counter in case product cannot be found
    i = 0
    with open('database.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            #check if product in user given category for each row
            if str(query).lower() == row['rating'].lower():
                #add to counter to day you found something
                i += 1
                display(row)
        if i == 0:
            print("Product not in database. Try again\n")

def add(product):
    with open('database.csv', 'a') as f:
        #get data from user
        brand = ask("Brand: ")
        #all these if statements are so the user can bail at any time.
        if brand == "cancel":
            pass
        price = ask("Price: ")
        if price == "cancel":
            pass
        type = ask("Type of product: ")
        if type == "cancel":
            pass
        concern = ask("Concern: ")
        if concern == "cancel":
            pass
        rating = ask("Rating: ")
        if rating == "cancel":
            pass
        status = ask("Status: ")
        if status == "cancel":
            pass
        #add to database file.
        f.write(brand+","+product+","+price+","+type+","+concern+","+rating+","+status+"\n")
    #feedback for user (note: doesn't actually confirm if it worked. entirely superficial.)
    print("Product added")

def replace(product, category, newData):
    with open('database.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            #finding exact product name in database and seeing if product is in that row
            if str(product).lower() in row['name'].lower():
                #data to be replaced
                i = row[str(category)]
                name = row['name']
    #replace existing entry with new data given
    with open('database.csv','r') as f:
        data = f.read()
        data = data.replace(i, newData)
    #overwrite file with new data
    with open("database.csv", "w") as outputfile:
        outputfile.write(data)
    print(name,'has been changed.')

def delete(product):
    #list to store data in
    data = []
    with open('database.csv','r') as f:
        for row in f:
            #if the product name is in the row it does not add the data from the row to list
            if product in row:
                continue
            else:
                data.append(row)
    #overwrite with changed data
    with open("database.csv", "w") as outputfile:
        outputfile.write("".join(data))
    print("Product Deleted.")

#~ S T A R T ~
#welcome
print("Welcome to organiseThing, supposedly used to store and review details on different skincare products.")
intro = "What would you like to do:\n1 - Add a product\n2 - Find a product\n3 - Edit a product\n4 - Delete a product\n"
mode = input(intro+"Enter 'help' for help. <-- DO THIS IT'S USEFUL\n")
while mode:
    #add mode
    if mode == "1" or mode == 'add':
        product = ask("What is the name of the product? ")
        if product == "cancel":
            pass
        else:
            #check if product already exists
            if find('name',str(product),'no') == True:
                print("That product already exists, please use the edit function")
            else:
                add(product)
        mode = input(intro)
    elif mode == "2" or mode == 'find':
        a = input("What would you like to search by? ")
        while a:
            if a in "brand,name,price,type,concern,rating,status":
                print("Searching by", a)
                b = ask("What would you like to search? ")
                if b == 'all':
                    with open('database.csv', 'r') as f:
                        reader = csv.DictReader(f)
                        for row in reader:
                            display(row)
                elif a == 'rating':
                    rating(b)
                else:
                    find(a,str(b),'yes')
                a = input("What would you like to search by? ")
            else:
                print("That is not a valid category, please try again.")
                a = input("What would you like to search by? ")
        mode = input(intro)
    elif mode == "3" or mode == 'edit':
        product = ask("What product would you like to change? ")
        if product == "cancel":
                pass
        elif find('name',str(product),'no') == False:
            print("Product does not exist.")
        else:
            category = ask("What detail would you like to change? ")
            if category == "cancel":
                pass
            else:
                newData = ask("What would you like to change it to? ")
                if newData == "cancel":
                    pass
                else:
                    replace(product, category, newData)
        mode = input(intro)
    elif mode == "4" or mode == 'delete':
        product = ask("What product would you like to delete? ")
        if product == "cancel":
                pass
        elif find('name',str(product),'no') == False:
            print('product does not exist')
        else:
            delete(product)
        mode = input(intro)
    elif mode == "help":
        print("~Welcome to organiseThing, supposedly used to store and review details on different skincare products.~")
        print("Available categories to search by:")
        print(" - brand\n - name\n - price\n - type (eg. cleanser, toner, moisturiser)\n - concern (What it is supposed to help with eg. acne, redness)\n - rating\n - status (eg. own, running low, sample)\n")
        print("When adding, deleting or editing a product, type cancel if you change your mind. Otherwise entering nothing will exit the part of the program you're in, with entering nothing on the main menu closing the program.\n")
        mode = input(intro)
    else:
        print("Sorry! That's not an option, try again.")
        mode = input(intro)
