class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...

wirzard = Wizard("Albus")
student = Student("Harry", "Gryffidor")
professor = Professor("Serverus", "Defense Against the Dark Arts")
