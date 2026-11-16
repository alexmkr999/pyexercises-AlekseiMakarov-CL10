"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# The user enters a campaign name, email, and campaign code.

# 2. Process:
# The program checks all three values using regular expressions.
# If all values are valid, it saves them to a CSV file.

# 3. Out:
# The program displays a success or error message.
# Valid data is saved in campaigns.csv.

# 4. My three fields and rules:
# Campaign name: letters and spaces only, at least 2 characters.
# Email: text before and after @, followed by a dot and letters.
# Campaign code: CR- followed by exactly four digits.

# Your code below
import re
import csv
import os

# Define the patterns
# ^ and $ mark the start and end of the text.
# [A-Za-z ] allows letters and spaces.
# {2,} means at least two characters.
name_pattern = r"[A-Za-z ]{2,}"

# [A-Za-z0-9._+-]+ allows common email characters.
# @ is required, and \. represents a real dot.
# [A-Za-z]{2,} requires at least two letters at the end.
email_pattern = r"[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

# CR- is fixed text and \d{4} means exactly four digits.
code_pattern = r"CR-\d{4}"

# Ask for information
name = input("Campaign name: ")
email = input("Email: ")
code = input("Campaign code: ")

# Check the three values
valid_name = re.fullmatch(name_pattern, name)
valid_email = re.fullmatch(email_pattern, email)
valid_code = re.fullmatch(code_pattern, code)

if valid_name and valid_email and valid_code:
    filename = "campaigns.csv"
    file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Campaign Name", "Email", "Campaign Code"])

        writer.writerow([name, email, code])

    print("Data saved successfully!")
else:
    print("Invalid data. Nothing was saved.")

# My tests:
# Campaign name: Lesha passed, L and Lesha2004 failed.
# Email: alex@example.com passed, alexexample.com and alex@ failed.
# Campaign code: CR-2004 passed, 6574830 and CR-20 failed.
# All nine results matched my expectations.
