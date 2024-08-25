# map => apply a function to a list
"""
def main():
    yell(["This", "is", "CS50"])

def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased) # added unpacking as *

if __name__ == "__main__":
    main()
"""

# *args
"""
def main():
    yell("This", "is", "CS50") # removed the list

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased) # added unpacking as *

if __name__ == "__main__":
    main()
"""

# map(function, terable, ...)
"""
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()
"""

# list comprehension = creating lists elegantly

def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper() for word in words] # adding a loop
    print(*uppercased)

if __name__ == "__main__":
    main()
