"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - There are two empty lines.
# - Some lines have extra spaces at the beginning.
# - Some first names are lowercase, while GUIDO is uppercase.
# - Last names have inconsistent capital letters.
# - 'van rossum' is a two-word last name, so the last word alone is not enough.


# 1. In:
# The program reads names.txt, which contains first names and last names.

# 2. Process, problem by problem:
# Skip empty lines.
# Remove extra spaces with strip() and split().
# Fix capitalization of first names and last names.
# Keep 'van Rossum' as one surname.
# Sort the names alphabetically by surname.

# 3. Out:
# The program writes eight cleaned, sorted names to cleaned_names.txt.
# The original names.txt stays unchanged.

# 4. How I decide which word is the last name:
# The first word is the first name; all remaining words form the surname.
# For example, 'Guido van Rossum' has the surname 'van Rossum'.

# Read and clean the original file.

# Your code below
people = []
with open("names.txt", "r", encoding="utf-8") as file:
    for line in file:
        words = line.split()
        if not words:
            continue
        first_name = words[0].capitalize()
        surname = " ".join(word.capitalize() for word in words[1:])
        if surname.lower() == "van rossum":
            surname = "van Rossum"
        people.append((surname, first_name))

# Sort by surname without being affected by capital letters.
people.sort(key=lambda person: person[0].lower())

# Save the clean names into a different file.
with open("cleaned_names.txt", "w", encoding="utf-8") as file:
    for surname, first_name in people:
        file.write(first_name + " " + surname + "\n")

# Display the results and line counts.
print("Saved", len(people), "names to cleaned_names.txt")
print("First:", people[0][1], people[0][0])
print("Last:", people[-1][1], people[-1][0])
