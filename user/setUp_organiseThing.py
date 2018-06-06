'''
Prog:   setUp_organiseThing.py
Name:   Katie Mackey
Date:   2018-06-06
Desc:   set up for first time use of organiseThing
'''
import csv
with open('database.csv', 'w') as csvfile:
    fieldnames = ["brand","name","price","type","concern","rating","status"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("Set-up successful")
