regex - defines patterns to compare to data that we receive

The first script validate.py validates email addresses through a series of checks, starting with basic string operations and progressing to more advanced regular expressions.

1. Initial Checks: It first ensures the email contains both "@" and "." symbols, which are fundamental to any email format.

2. Splitting for Validation: The script then splits the email into `username` and `domain` parts, checking if both exist and if the domain contains a period or ends with specific extensions like ".edu".

3. Regular Expressions: Finally, the script introduces regular expressions (`re` library) for more robust validation, checking for the correct structure and specific domain endings (e.g., ".com").

Each step builds on the previous one, moving from simple validation to more precise pattern matching to ensure the email format is correct.




"""
Email Validation Function

This function prompts the user for an email address and validates it using a regular expression. 
The regex checks for the following criteria:
- The email must start with one or more alphanumeric characters.
- The "@" symbol must be present.
- The domain part may include zero or more subdomains, each followed by a dot.
- The domain must be followed by a valid top-level domain (TLD) such as .com, .edu, .org, .net, or .gov.
- The validation is case-insensitive.

If the email matches the pattern, the function prints "Valid". Otherwise, it prints "Invalid".

"""

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)*\w+\.(com|edu|org|net|gov)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

"""


Here is the best practice from the industry:


from email_validator import validate_email, EmailNotValidError

email = "my+address@example.org"

try:

  # Check that the email address is valid. Turn on check_deliverability
  # for first-time validations like on account creation pages (but not
  # login pages).
  emailinfo = validate_email(email, check_deliverability=False)

  # After this point, use only the normalized form of the email address,
  # especially before going to a database query.
  email = emailinfo.normalized

except EmailNotValidError as e:

  # The exception message is human-readable explanation of why it's
  # not a valid (or deliverable) email address.
  print(str(e))



Here is an acrual example:

from email_validator import validate_email, EmailNotValidError

email = input("What's your email? ").strip()

try:
    # Validate the email and return the normalized form.
    valid = validate_email(email)
    email = valid.email
    print("Valid")
except EmailNotValidError as e:
    # email is not valid, exception message is human-readable
    print("Invalid:", str(e))
