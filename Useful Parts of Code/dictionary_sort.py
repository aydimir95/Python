students = [
    {"name": "Herminone", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]


for gryffindor in sorted(gryffindors):
    print(gryffindor)