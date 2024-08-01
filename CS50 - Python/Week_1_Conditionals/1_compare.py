# Ask questions to get implement this kind of code, that kind of code or the other:


""""
> - more than
>= - more or equal
< - less than
<= - less or equal
== - comparing left and right
!= - not equal to

if - ask questions "if the answer to this questions is true then go ahead and execute the following code for me"

"""

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else: # don't need to ask the questions - it's assumed x == y
    print("x is equal to y")




"""

Conditional Statements 


"""

if x < y or x > y:
    print('x is not equal to y')
else:
    print("x is equal to y")

# Could my code be better

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# or 

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")

