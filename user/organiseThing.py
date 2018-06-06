'''
Prog:   organiseThing.py
Name:   Katie Mackey
Date:   2018-05-31
Desc:   organise skincare products. hopefully.

mode = input("""What would you like to do:\n1 - Add a product\n2 - Find a product\n3 - Edit a product\n4 - Delete a product\n""")
'''
import csv
#F U N C T I O N S
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

#find and display a product or multiple products in database by category
def findShow(category,query):
    #counter in case product cannot be found
    i = 0
    with open('database.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            #check if product in user given category for each row
            if str(query).lower() in row[str(category)].lower():
                display(row)
                #add to counter to day you found something
                i += 1
        if i == 0:
            print("Product not in database. Try again\n")

def find(category,query):
    #counter in case product cannot be found
    i = 0
    with open('database.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            #check if product in user given category for each row
            if str(query).lower() in row[str(category)].lower():
                #add to counter to day you found something
                i += 1
                return(True)
        if i == 0:
            return(False)

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
print("Welcome to organiseThing, supposedly used to store and review details on different skincare products.")
mode = input("""What would you like to do:\n1 - Add a product\n2 - Find a product\n3 - Edit a product\n4 - Delete a product\nEnter 'help' for help.\n""")
while mode:
    #add mode
    if mode == "1" or mode == 'add':
        product = input("What is the name of the product? ")
        #check if product already exists
        if find('name',str(product)) == True:
            print("That product already exists, please use the edit function")
        else:
            add(product)
        mode = input("""What would you like to do:\n1 - Add a product\n2 - Find a product\n3 - Edit a product\n4 - Delete a product\n""")
    elif mode == "2" or mode == 'find':
        a = input("What would you like to search by? ")
        while a:
            if a in "brand,name,price,type,concern,rating,status":
                print("Searching by", a)
                b = input("What would you like to search? ")
                if b == 'all':
                    with open('database.csv', 'r') as f:
                        reader = csv.DictReader(f)
                        for row in reader:
                            display(row)
                else:
                    findShow(a,str(b))
                a = input("What would you like to search by? ")
            else:
                print("That is not a valid category, please try again.")
                a = input("What would you like to search by? ")
        mode = input("""What would you like to do:\n1 - Add a product\n2 - Find a product\n3 - Edit a product\n4 - Delete a product\n""")
    elif mode == "3" or mode == 'edit':
        product = input("What product would you like to change? ")
        if find('name',str(product)) == False:
            print("Product does not exist.")
        else:
            category = input("What detail would you like to change? ")
            newData = input("What would you like to change it to? ")
            replace(product, category, newData)
        mode = input("""What would you like to do:\n1 - Add a product\n2 - Find a product\n3 - Edit a product\n4 - Delete a product\n""")
    elif mode == "4" or mode == 'delete':
        product = input("What product would you like to delete? ")
        if find('name',str(product)) == False:
            print('product does not exist')
        else:
            delete(product)
        mode = input("""What would you like to do:\n1 - Add a product\n2 - Find a product\n3 - Edit a product\n4 - Delete a product\n""")
    elif mode == "help":
        print("Welcome to organiseThing, supposedly used to store and review details on different skincare products.")
        print("Available categories to search by:")
        print(" - brand\n - name\n - price\n - type\n - concern\n - rating\n - status")
        print("deleting products is currently unavailable, because CSV files are a pain in the ass. Sorry.\nYou can go into the database file manually if you really want, just don't move any commas around.\n\n")
        mode = input("""What would you like to do:\n1 - Add a product\n2 - Find a product\n3 - Edit a product\n4 - Delete a product\n""")
    else:
        print("\aSorry! That's not an option, try again.")
        mode = input("""What would you like to do:\n1 - Add a product\n2 - Find a product\n3 - Edit a product\n4 - Delete a product\n""")
