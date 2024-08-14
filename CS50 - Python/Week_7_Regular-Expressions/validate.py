"""

email = input("What's your email? ").strip()


if "@" in email:
    print("Valid")
else:
    print("Invalid")


# add "."

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")



# if username splits at the @

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")
else:
    print("Invalid")




username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")





# re - regular expressions library 

# re.search(pattern, string, flags = 0)


import re

email = input("What's your email? ").strip()

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")

"""

# we will define patters 

"""
. - any character except a newline
* - 0 or more repetitions
+ - 1 or more repetitions 
? - 0 or 1 repetition
{m} - m repetitions
{m,n} - m-n repetitions



import re

email = input("What's your email? ").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")




# I need to check for the domain ending - using \ - backslash

import re

email = input("What's your email? ").strip()

if re.search(r".+@.+\.com", email):
    print("Valid")
else:
    print("Invalid")

"""


# add ^ - carrot and $ - dollar sign for begining and end of the email

import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.com$", email):
    print("Valid")
else:
    print("Invalid")

