# prompt for user url for twitter - you can just take their username and create a url for the username provided
"""
url = input("URL: ").strip()
print(url)

"""
"""
# find and replace

url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")

"""


"""
# remove prefix

url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")

"""
"""
# re.sub(pattern, repl, string, count=0, flags=0)

import re 

url = input("URL: ").strip()

username = re.sub(r"https://twitter.com/", "", url)
print(f"Username: {username}")
"""

"""
# chipping away at fixing the bugs

import re 

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter.com/", "", url)
print(f"Username: {username}")
"""


"""
# re.search - to solve the domain bug

import re 

url = input("URL: ").strip()

matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(2)) # it's the second set of parantheses
"""



# walrus operator / whether to use www or not / and finally the proper username input

import re 

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1)) # now it's the first one, because of the (?:...) regex
