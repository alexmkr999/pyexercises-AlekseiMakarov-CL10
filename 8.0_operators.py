"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# The program uses two strings.

# 2. Process:
# It compares the values using comparison operators.
# It also checks logical combinations with and, or, not.

# 3. Out:
# The program displays a table with True or False results.

# 4. My values:
# I chose "apple" and "Apple".
# I was surprised that "apple" > "Apple" is True.
# Python compares uppercase and lowercase letters differently.

# Your code below
a = "apple"
b = "Apple"

print("Value 1:", a)
print("Value 2:", b)
print("---------------------------")
print("Comparison       Result")
print("---------------------------")

print("a == b          ", a == b)
print("a != b          ", a != b)
print("a > b           ", a > b)
print("a < b           ", a < b)
print("a >= b          ", a >= b)
print("a <= b          ", a <= b)

print("---------------------------")
print("Logical operators")
print("---------------------------")

print("a != b and a > b:", a != b and a > b)
print("a == b or a > b: ", a == b or a > b)
print("not(a == b):     ", not(a == b))

# My predictions:
# == False, != True, > True, < False
# >= True, <= False
# and True, or True, not True
# I predicted 9 out of 9 correctly.
