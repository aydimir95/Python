

with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")



# assign proper variables to each column

with open("students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        print(f"{name} is in {house}")



# sort the list - sloppy method

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)


# sort it by name rather than what we have

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student ["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")


# tighter code


students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")



# sort the tighter code

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")



# reverse the sort

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name, reverse = True):
    print(f"{student['name']} is in {student['house']}")


# sort by house

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_house(student):
    return student["house"]

for student in sorted(students, key=get_house):
    print(f"{student['name']} is in {student['house']}")


# lambda - is an anonymous function - lets you do it all in one breath.

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

# you can use lambda twice if you want - to pass a function to some other function that itself does not need a name


students = []

with open("students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name": name, "home": home}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

# ValueError - how do we split the csv files other than with ","
# we can use someone else's library = csv

# function "reader" reads the csv and figures out where are all the commas and spaces etc, to split properly

# docs.python.org/3/library/csv.html

import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file) 
    for name, home in reader:
        students.append({"name": name, "home": home})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")



# csv.DictReader - reads the first row in the csv file as column headers - but technically it reads the csv columns not as a list of columns but as a dictionary of columns - "reader" returns lists. "DictReader" returns dictionaries.

import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file) 
    for row in reader:
        students.append({"name": row["name"], "home": row["home"], "city": row["city"]})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']} and lives in the City of {student['city']}")



# you can also just call row - and it will do the same thing rather than specifing the row names

import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file) 
    for row in reader:
        students.append(row)


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']} and lives in the City of {student['city']}")


# csv.writer

import csv

name = input("what's your name? ")
home = input("where are you from? ")

with open("write-students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name,home])


# csv.DictWriter

import csv

name = input("what's your name? ")
home = input("where are you from? ")

with open("write-students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})