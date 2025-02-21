"""
This module demonstrates the usage of Python's `re` module for regular expressions.
It includes examples of search, validation, split, and substitution.
"""

import re  # Import the 're' module for regular expressions

# Example 1: re.search()
my_search = re.search(r"([A-z]+)\s([A-z]+)", "Karim Tantawy")

"""
Search for a pattern with two groups:
- First group: One or more alphabetic characters ([A-z]+)
- Second group: A space (\s) followed by one or more alphabetic characters ([A-z]+)
"""
print(my_search.string)  # Prints the input string "Karim Tantawy"

print("*" * 50)  # Separator for clarity in output

# Example 2: Validating an email address
VALIDATE_EMAIL = r"^([A-z0-9._%+-]+)@([A-z0-9._%+-]+)\.([A-z]{2,})$"
"""
Regular expression breakdown for email validation:
- ^: Start of the string
- ([A-z0-9._%+-]+): Matches the local part (letters, digits, and some special characters)
- @: Matches the '@' symbol
- ([A-z0-9._%+-]+): Matches the domain name
- \.: Matches the '.' before the domain suffix
- ([A-z]{2,}): Matches the domain suffix (at least 2 alphabetic characters)
- $: End of the string
"""
email = input("Enter your email: ")  # Prompt the user to enter an email

is_email = re.search(VALIDATE_EMAIL, email)  # Validate the email against the regex

if is_email:
    print("Valid Email")  # Output if the email matches the pattern
else:
    raise ValueError(
        f"{email} is not a valid email!"
    )  # Raise an error if the email is invalid

print("*" * 50)  # Separator for clarity in output

# Example 3: Splitting a string
phrase = r"I Love-Python as a programmign language"
"""
Split the string 'phrase' using the regex pattern '-|\s':
- -: Matches hyphens
- \s: Matches spaces
"""
splitted_phrase = re.split(r"-|\s", phrase)  # Split the string into words
print(splitted_phrase)  # Output the list of words

for counter, word in enumerate(
    splitted_phrase, 1
):  # Enumerate over the split words, starting at 1
    print(f"{counter}) {word}")  # Print each word with its index

print("*" * 50)  # Separator for clarity in output

# Example 4: Substituting characters in a string
print(re.sub(r"\s", r"-", "I Love Python"))  # Replace all spaces with hyphens

"""
Regex pattern:
- \s: Matches any whitespace character
Replacement:
- "-": Replaces spaces with hyphens
Result:
- "I Love Python" -> "I-Love-Python"
"""
