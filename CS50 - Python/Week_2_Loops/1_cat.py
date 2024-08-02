# print("meow")
# print("meow")
# print("meow")



"""

while loop 
allows you to ask a question again and again - to which an answer is true or false



i = 3 # i is always equals to 3 and the while is always true
while i !=0:
    print("meow")



while i is not equal zero - python goes back and forth line 1 - 2 - 3 then back to 2 - 3 back to 2 - 3 if you are never changing the value of i - it will will go forever



i = 3
while i !=0:
    i = i - 1
    print("meow")



i = 0
while i < 3:
    i += 1
    print("meow")




List of Data Types that Python Supports

str   or strings
int   or integers
float or floating point value
bool  or boolean expressions
list  or list of things in python - containing multiple values all in the same place




for i in [0, 1, 2]:
    print("bark")



for _ in range(3): # if you don't want to define a variable - you can specify an underscore (_) instead
    print("bark")



or just use the following 



print("meow\n" * 3, end="")



while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break


while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

"""

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")

main()
