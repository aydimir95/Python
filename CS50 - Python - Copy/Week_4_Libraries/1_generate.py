# modules - removes duplicating functions again and again - make it reusable

# random - library

# import - allows to import the functions from library
# random.choice(seq) 

# coin toss to generate the random number


import random


coin = random.choice(["heads", "tails"])
print(coin)



# from - importing functions from module

from random import choice

coin = choice(["heads", "tails"])
print(coin)


# random.randint(a, b) - the probability between the 2 numbers 

import random

number = random.randint(1, 10)
print(number)




# random.shuffle(x)

import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)





# statistics - library that lets you import the functions related to statistics

import statistics

print(statistics.mean([100, 90]))


# command-line arguments -> you can prompt the input 

# sys.argv - system argument vector -> 

import sys

print("hello, my name is", sys.argv[1])




# IndexError 


import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")



# else

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])





# remove else

import sys

# Check for Errors
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("To many arguments")

# Print name tages
print("hello, my name is", sys.argv[1])




# Removed the else clause for better code readability and logic flow. However, this introduces a potential IndexError if there are too few arguments, as the script will attempt to access sys.argv[1] without checking if it exists. To prevent this, we check the number of arguments and exit the script if the count is not exactly 2 (the script name plus one additional argument).


# sys.exit

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])




# listing the names after argv

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("hello, my name is", arg)




# adding list length to argv

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)




# packages - pypi.org


# cowsay - for a cow to say something in your computer
# pip - allows you to install packages


import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])



# trex - for a trex to say somthing in your screen

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])