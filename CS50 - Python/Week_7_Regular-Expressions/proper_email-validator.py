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