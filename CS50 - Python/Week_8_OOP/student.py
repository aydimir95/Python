

name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")


def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")


# This function can be better to be reusable:

def get_name():
    name = input("Name: ")
    return name


# here is a reusable frunction

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()


# tuple = collection of inmutable values

def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house =  input("House: ")
    return (name, house) # this tells python to return tuple - it's one value with 2 items

if __name__ == "__main__":
    main()


# return tuple

def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house =  input("House: ")
    return (name, house) # this tells python to return tuple - it's one value with 2 items


if __name__ == "__main__":
    main()


# tuple can't be changed = returns error


def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ranvenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house =  input("House: ")
    return (name, house) # this tells python to return tuple - it's one value with 2 items


if __name__ == "__main__":
    main()



# list can be changed

def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ranvenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house =  input("House: ")
    return [name, house] # this tells python to return tuple - it's one value with 2 items


if __name__ == "__main__":
    main()


# to store constant values

def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main()


# better code

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return{"name": name, "house": house}

if __name__ == "__main__":
    main()



# Better way to collect data of the variable = create a data type

# class = to invent your own objects => see class_student.py




# Cleaning up the code - since we have a class and a separate variables, we want to have everything in the class

class Student:
    def __init__(self, name, house):

        self.name = name
        self.house = house 

    def __str__(self):
        return f"{self.name} is from {self.house}"

# removed properties & defined variable "get_student"

    @classmethod 
    # @classmethod means I can call this method without instantiating the Student Object first, this removes the chicken egg problem, lets just get a student via a class method that doesn't require you to create a student object first.
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house) # create an object of the current class

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()


# cleaner version - no comments

class Student:
    def __init__(self, name, house):

        self.name = name
        self.house = house 

    def __str__(self):
        return f"{self.name} is from {self.house}"

    @classmethod 
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house) 

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()


# in general you would move the classes definitions to it's own file and then import it.

# there is also @staticmethods

# but the most compelling features of OOP is this notion of "Ingeritance"
# inheritance = borrowing attributes to the class from other classes