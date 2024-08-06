
"""
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

"""

# assign proper variables to each column
"""
with open("students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        print(f"{name} is in {house}")
"""


# sort the list - sloppy method
"""
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
"""

# sort it by name rather than what we have
"""
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
"""

# tighter code

"""
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
"""


# sort the tighter code
"""
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
"""

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


# reverse by house

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
