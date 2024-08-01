# Step 1: Ask user for their name.
name = input("What's your name? ")


# variables = returns values
# comments  = intent or to-do list or  pseudocode 

"""
Many lines of comments
Many lines of comments
Many lines of comments

"""

# Step 2: Say hello to the user.
print("hello, " + name)
print("hello,", name)

print("hello, ")
print(name)



# function =  print
# argument = "hello, world" 
# bugs     =  mistakes

# you can't use MS Word to code


# Python Documentation 
# https://docs.python.org/3/library/functions.html#print

# print(*objects, sep=' ', end='\n', file=None, flush=False)

print("Hello,", end="???")
print(name)

print("hello,", name, sep="???")

# parameters = positional parameters => sequncial
# named parameters = optional + pass at the end + use by name


# single and double quotes for quotations
print("Hello, 'friend'")

# escaping character
print("hello, \"friend\"")  


# built in to strings is a datatype = that can remove spaces from the input
# remove whitespace from str
# name = name.strip()

# capitalize user's name
# name = name.capitalize()

# capitalize every word
# name = name.title()


# now remove the whitespace & capitalize together:
# name = name.strip().title()


# taking it further => we can write the whole thing on one line
naem = input("What's your name? ").strip().title()

# split user's name into first name and last name
first, last = naem.split()


# say hello to the user by function
#print(f"hello, {name}")
print(f"hello, {first}") 
print(f"hello, {last}")



# str = strings 


# int = integer  
# operators: + - *  %

# interactive mode 


