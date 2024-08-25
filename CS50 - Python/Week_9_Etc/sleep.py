"""
def main():

    n = int(input("What's n? "))
    for i in range(n):
        print(sheep(i))

def sheep(n):
    return "🐑" * n


if __name__ == "__main__":
    main()
"""

# here is a better way
"""
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock


if __name__ == "__main__":
    main()
"""

# for a million sheep it's not possible to do it with the previous code
# that's when we use "generator"

# "yield" is what you use

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()

# iterator 