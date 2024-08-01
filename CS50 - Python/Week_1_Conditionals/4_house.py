name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Drako":
    print("Slytherin")
else:
    print("Who?")


# Make it better

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")

elif name == "Drako":
    print("Slytherin")

else:
    print("Who?")


# Match - is like "switch" function in JavaScript

match name:
    case "Harry": 
        print("Gryffidor")
    case "Hermione":
        print("Gryffidor")
    case "Ron":
        print("Gryffidor")
    case "Drako":
        print("Slytherin")
    case _:
        print("Who?")



# Even better:

match name:
    case "Harry" | "Hermione" | "Ron": 
        print("Gryffidor")
    case "Drako":
        print("Slytherin")
    case _:
        print("Who?")