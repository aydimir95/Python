# property / @property / decorate / Getter / Setter

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
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house,)

if __name__ == "__main__":
    main()
