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




# add ^ - carrot and $ - dollar sign for begining and end of the email

import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.com$", email):
    print("Valid")
else:
    print("Invalid")



# [] - set of characters that are not supposed to be there
# [^] - complementing the set
# {1} - to specify the number of characters that are supposed be there

import re

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.com$", email):
    print("Valid")
else:
    print("Invalid")



# narrow the definitions

import re

email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
    print("Valid")
else:
    print("Invalid")





# \w - any word 

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.com$", email):
    print("Valid")
else:
    print("Invalid")

"""
"""
\d - decimal digit
\D - not a decimal digit
\s - whitespace characters
\S - not a whitespace character
\w - word character ... as well as numbers and the underscore
\W - not a word character
"""
"""

# to accomodate more domains you can use brackets and pipes
# (com|org|etc) - | means "or"



import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.(com|edu|org|net|gov)$", email):
    print("Valid")
else:
    print("Invalid")


"""
"""
A|B - A or B
(...) - a group
(?:...) - non-capturing version
"""
"""
"""

# lower the input or flag it.

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.(com|edu|org|net|gov)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

