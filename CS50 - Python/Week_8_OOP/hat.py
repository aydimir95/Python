import random



class Hat: 
    # class is a template that can create a bunch of hats but there is only one hat
    def __init__(self):
        self.house = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.house))


hat = Hat() # instantiate the variable only sorting capability
hat.sort("Harry")



# to create one instance of a class

class Hat:

    house = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name): #cls = because conflicts with class
        print(name, "is in", random.choice(cls.house))

Hat.sort("Harry")


# you can always just define a variable and let it sort the values, but in order for the code to be reusable elsewhere, we use classes

