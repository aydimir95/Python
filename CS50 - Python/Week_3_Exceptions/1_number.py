# handling errors

x = int(input("What's x? "))
print(f"x is {x}") 



# try except - to handle ValueError

try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

try:
    x = int(input("What's x? "))

except ValueError:
    print("x is not an integer")


print(f"x is {x}")



# else - to handle NameError 

try:
    x = int(input("What's x? "))

except ValueError:
    print("x is not an integer")

else:
    print(f"x is {x}")



# break - stop the loop

while True:

    try:
        x = int(input("What's x? "))

    except ValueError:
        print("x is not an integer")

    else:
        break


print(f"x is {x}")



# break after try - different design of the same code

while True:

    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")


print(f"x is {x}")


# return - rather than print

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


main()



# return - breaks and returns 

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x 


main()



# return after try - tightening the code but it's not necessarily better

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? ")) 
        except ValueError:
            print("x is not an integer")


main()



# pass - silently ignore it

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? ")) 
        except ValueError:
            pass # if we don't have to specify why - just pass the error


main()



# prompt - to make the code reusable

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt)) 
        except ValueError:
            pass


main()