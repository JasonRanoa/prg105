# Programming Practice 8.3 Most Frequent Character
"""
Write a program that lets the user enter a string and displays
the letter that appears most frequently in the string.
Ignore spaces, punctuation, and uppercase vs lowercase
"""

# Unicode: A = 65, Z = 90
# Parallel arrays for record keeping
letters = [chr(x) for x in range(65, 91)]
l_counts = [0] * len(letters)

print("This program counts the most frequently used letter in a string.")
string = input("Enter a string: ")
print()

# Updates l_counts. Iterates over the entire string
for x in string:
    if x.isalpha():
        idx = letters.index(x.upper())
        l_counts[idx] += 1

# Gets all letters with l_counts. Checks everything just to be sure
# Not the most efficient but it works.
max_count = max(l_counts)
freq_letters = [letters[i] for i in range(len(letters)) if l_counts[i] == max_count]

# Print Results
print("The following letter(s) are the most common.")
# The * access the contents, rather through the list
print(*freq_letters, sep=", ", end=" ")
print("is/are used {} time(s)".format(max_count))
