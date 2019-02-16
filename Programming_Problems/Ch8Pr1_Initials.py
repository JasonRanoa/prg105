# Programming Practice 8.1 Initials
"""
Write a program that gets a string from the user containing a
person's first, middle, and last names and then displays their
first, middle, and last initials.  (Creating a new variable and
concatenating each letter plus a '.' is the easiest way to do this.)
"""

name = input("Please enter your full name: ")
print("Here are your initials:", end=" ")
for parts in name.split(" "):  # Assuming answers are formatted correctly
    print(parts[0].upper() + ".", end=" ")
