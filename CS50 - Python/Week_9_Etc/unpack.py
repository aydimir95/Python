"""
first, _ = input("What's your name? ").split(" ")

print(f"hello, {first}")
"""

# converting Harry Potter money
"""
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


print(total(100, 50, 25), "Knuts")
"""

# a bit of a better code
"""
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100,50,25]


print(total(coins[0], coins[1], coins[2]), "Knuts")
"""

# much better code - using a star * to pass each coin rather than typing it out
"""
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100,50,25]


print(total(*coins), "Knuts") # "*" star coins = passes each coin individually, respectively
"""

# changing the order of those coins will break the logic
# so lets give each coin a name and preserve the position of the coin by name
"""
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
"""

# double asterix "**" for passing more positional arguments for dictionaries
"""
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts") 
"""

# *args => variable number of arguments
# **kwargs
"""
def f(*args, **kwargs):
    print("Positional:", args)

f(100, 50, 25, 5)
"""

"""
def f(*args, **kwargs):
    print("Named:", kwargs)

f(galleons=100, sickles=50, knuts=25)
"""
"""

Lets look at "print" function more closely

print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

this indicates that "print" takes a variable number of arguments. 

"""

# here is how "print" is constructed by python developers
"""
def print(*objects, sep=' ', end='\n', ...):
    for object in objects:
        ...
"""

def f(*args, **kwargs):
    print("Positional:", args)

f(100, 50, 25, 5)

