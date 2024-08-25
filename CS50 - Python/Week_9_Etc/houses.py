students = [
    {"name": "Herminone", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]

# itterating the set and getting unique houses
"""
houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)
"""

# set = getting unique values

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)

# global variables => is set above the whole code, but the problem is there is a problem changing them