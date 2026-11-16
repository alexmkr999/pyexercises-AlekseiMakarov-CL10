"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# The program uses three marketing permissions.

# 2. Process:
# It combines permissions, checks if one is present,
# adds a new permission, and removes another one.

# 3. Out:
# The program displays permissions in binary
# after each step.

# 4. My permissions:
# The permissions are for a marketing campaign.
# VIEW allows someone to see the campaign.
# EDIT allows someone to change the campaign.
# PUBLISH allows someone to publish the campaign.

# Define permissions using bits

# Your code below
VIEW = 0b001
EDIT = 0b010
PUBLISH = 0b100

# Combine two permissions
permissions = VIEW | EDIT
print("Initial permissions:", bin(permissions))

# Check if PUBLISH is present
print("Can publish:", bool(permissions & PUBLISH))

# Add PUBLISH permission
permissions = permissions | PUBLISH
print("After adding PUBLISH:", bin(permissions))

# Remove EDIT permission
permissions = permissions & ~EDIT
print("After removing EDIT:", bin(permissions))

# Final check
print("Can view:", bool(permissions & VIEW))
print("Can edit:", bool(permissions & EDIT))
print("Can publish:", bool(permissions & PUBLISH))
