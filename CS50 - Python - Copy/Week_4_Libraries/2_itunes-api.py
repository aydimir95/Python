# requests - pypi.org/project/requests

# JSON - JavaScrip Object Notation - language agnostic format - to access data and integrate into your own program

import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(response.json())



# JSON package - allows you to manipulate the data and even 3D print it

# docs.python.org/3/library/json.html

import requests
import sys
import json # imported json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]) # changed the limit to 50

print(json.dumps(response.json(), indent=2)) # bring in json dumps

# itterate to get 50 songs
o = response.json()
for result in o["results"]:
    print(result["trackName"])


# you can also make your own packages

