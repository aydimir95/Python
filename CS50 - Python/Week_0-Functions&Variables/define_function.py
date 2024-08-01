# https://cs50.harvard.edu/python/2022/weeks/0/

# def hello(to="World"):
#    print("Hello,", to)

# hello()

# name = input("What's your name? ")
# hello(name)

def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="World"):
    print("Hello,", to)

main()

# scope = only exists in the context in which you define it.
# defined name can only be used in your main function - you can't use it outside of the main function

# return = returns the value you passed in to it.

