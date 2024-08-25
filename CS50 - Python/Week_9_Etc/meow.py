"""
import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meow.py")
"""
"""
as well as we just let the user to pass arguments from the command line by declaring sys.argv for the 3rd part of the command line, to specify something suing "-n", we also have to program all the possible use cases for programmers to pass arguments through command line, and that's possible using library "argparse" - letting users to pass in configuration oprions from the command line. 

"""

# argparse = very useful for a real world programs

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")

