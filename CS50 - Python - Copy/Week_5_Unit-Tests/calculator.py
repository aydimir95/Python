# writing "tests" to make sure our code solves the problem as we intend 

def main():
    x = int(input("what's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n 

# main() - removed to make sure we can call it from another file

if __name__ == "__main__":
    main()

# Having multiple functions in your program is the best practice - rather than placing all of your function in just "main" - it's a really good idea to break your idea up into smaller bite sized functions that themselves are testable.

# square is perfectly testable 

