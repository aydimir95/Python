"""
students = [
    {"name": "Herminone", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]
"""

"""
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]


for gryffindor in sorted(gryffindors):
    print(gryffindor)
"""

# filter(function, iterate) => it's like map, with more functional approach

"""
def is_gryffindor(s):
    return s["house"] == "Gryffindor"


gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
"""

# even tighter code using another lambda
"""
gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
"""

# here is an example that can be used to construct a dictionary comprehension
"""
students = ["Hermione", "Harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})

print(gryffindors)
"""

# simplified dictionary
"""
students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

print(gryffindors)
"""

# dictionary comprehension
"""
students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)
"""

# here is an example that we can built up to use enumerate
"""
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])
"""

# enumerate - much tighter than before

students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)

# generators => sleep.py


