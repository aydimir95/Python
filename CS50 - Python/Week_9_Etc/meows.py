"""
MEOWS = 3 # constant = just a visual cappitalized variable that lets user know that it's a constant

for i in range(MEOWS):
    print("meow")
"""

# using constant with a class to create a cat
"""
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")
        

cat = Cat()
cat.meow()
"""
# type hints => there a tool that lets you know what variable to use in a code

# "mypy" = pip install mypy
"""
def meow(n: int): # to hint that this variable on the left should be an int
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meow(number)
"""
# install mypy and run "mypy meows.py"

"""
def meow(n: int) -> None:
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)

"""

"""
def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)
"""


# docstring = peps.python.org/pep-0257

# to document this notation, meaning using """ """ - there are tools you can use to extract docstrings from within the comments and generate documentation


def meow(n: int) -> str:

    """
    Meow n times.
    
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """

    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)


