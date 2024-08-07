students = ["Hermione", "Harry", "Ron", "Draco"]

# print(students[0])
# print(students[1])
# print(students[2])


# for a variable of one student in a list of students itterate over and print each of those names

"""

for student in students: 
    print(student)

for i in range(students): # Can't do - since range is taking the range of integers

"""

# For loop names

for i in range(len(students)):
    print(students[i])

# Better way to for loop names

for i in range(len(students)):
    print(i, students[i])

# Best way to for loop names

for i in range(len(students)):
    print(i + 1, students[i])



# dict is a dictionary = keys & values (2 dimensional association)
# list is a set of multiple values

houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

