regex - defines patterns to compare to data that we receive

The first script validate.py validates email addresses through a series of checks, starting with basic string operations and progressing to more advanced regular expressions.

1. Initial Checks: It first ensures the email contains both "@" and "." symbols, which are fundamental to any email format.

2. Splitting for Validation: The script then splits the email into `username` and `domain` parts, checking if both exist and if the domain contains a period or ends with specific extensions like ".edu".

3. Regular Expressions: Finally, the script introduces regular expressions (`re` library) for more robust validation, checking for the correct structure and specific domain endings (e.g., ".com").

Each step builds on the previous one, moving from simple validation to more precise pattern matching to ensure the email format is correct.