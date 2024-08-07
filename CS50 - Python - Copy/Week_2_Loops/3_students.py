students = ["Hermione", "Harry", "Ron", "Draco"]
houses   = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

students = {"Hermione": "Gryffindor", 
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin",
}

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

for student in students:
    print(student, students[student], sep=", from ")

