class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    # define attributes of a student
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()



# Object = instance of a class

class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    # define attributes of a student
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()


# Classes are mutable but you can make them inmutable

class Student:
# Classes come with METHODS = that lets you define functions
# __init__ method = lets you add variables to objects, creates a template
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # create a function to pass arguments to the class = constructs a Student Object for you = we have a Student object with a templated function inside (name & house), that lets you pass those variable into
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()



# raise

class Student:
    def __init__(self, name, house):
        if not name:
            # print("Missing Value") <= not enough
            # sys.exit("Missing Value") <= That's too harsh
            # return None <= That's not applicable since it's saying that there is no object, however there is an object. We just need to signal an error = we have to "raise" an exception
            raise ValueError("Missing Name")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house) # tighter
    except Value:
        ...

if __name__ == "__main__":
    main()



# we can control what goes into class

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House") # capability that dictionary can't do = we can control what goes into class
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house) # tighter

if __name__ == "__main__":
    main()



# to make house OPTIONAL

class Student:
    def __init__(self, name, house=None): # to make house OPTIONAL
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()


# change print pass

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(student) # describes where this is stored

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()


# __str__ = when you want to print the string value of the class

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} is from {self.house}"


def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()


# pass patronus

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} is from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()



# removed all patronuses

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} is from {self.house}"

def main():
    student = get_student()
    student.house = "Number Four, Privet Drive" # you can change the stored data this way, "properties" lets you defend from that
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house,)

if __name__ == "__main__":
    main()



# property / @property / decorate / Getter / Setter

class Student:
    def __init__(self, name, house):

        # no longer need this error check
        """
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        """

        self.name = name
        self.house = house 
        # There is a bug here = you need to decide whether you want a variable to be called "house" or the property / function to be called "house"

    def __str__(self):
        return f"{self.name} is from {self.house}"

    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house # can't have a variable "house" & a property "house"

    # Setter
    @house.setter 
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house # can't have a variable "house" & a property "house"

def main():
    student = get_student()
    # need to remove to stop receiving the error that we raised to check
    
    # student.house = "Number Four, Privet Drive" 
    
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house,)

if __name__ == "__main__":
    main()



# This is a way to break the code = you can still change the value if you wanted to, but convention is not to touch the setter with underscore "_" here is how:

class Student:
    def __init__(self, name, house):

        self.name = name
        self.house = house 

    def __str__(self):
        return f"{self.name} is from {self.house}"


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


    @property
    def house(self):
        return self._house

    @house.setter 
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house 

def main():
    student = get_student()
    student._house = "Number Four, Privet Drive" # Here is how it's done
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house,)

if __name__ == "__main__":
    main()

# integers = int = class int(x, base=10) 
# strings = str = class str(object='')
# str.lower() = method - class "lower"
# str.strip([chars]) = method
# list = class list([iterable])
# list.append(x) = method to append
# dict = class dictionary 

# see type.py

