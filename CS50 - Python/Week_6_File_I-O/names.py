names = []
"""
for _ in range(3):
    name = input("What's your name? ")
    names.append(name)


# better design - but we could break it down to have a name variable if the question is longer

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}")

# but the names are lost after you print it out - we would like to save this information using "File I/O"

name = input("What's your name? ")

# open - to open the file - to read & write program into the file


for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}")


name = input("what's you name? ")

file = open("names.txt", "w")
file.write(name)
file.close()

# You need to append names


name = input("what's you name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()


# you can close "with"

name = input("what's you name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")



# read the written names and remove spaces

with open ("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())



# tightening the code

with open ("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())



# sorting the names - very common technique

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")



# compact code

with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())



# reverse the sort

with open("names.txt") as file:
    for line in sorted(file, reverse=True):
        print("hello,", line.rstrip())

"""


