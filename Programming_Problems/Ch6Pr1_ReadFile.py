# Programming Practice 6.1 Read File
"""
Read and Display the list of names from the file
Display the number of names that are read from the file
(You will need a variable to keep a count of the number of
items read from the file.)
"""

names = open("Ch6_Files/names.txt", "r")
count = 0

print("Here are the names in file: ")
for name in names:
    print("  ", name, end="")
    count = count + 1
print("{} name(s) are read and displayed".format(count))

names.close()
