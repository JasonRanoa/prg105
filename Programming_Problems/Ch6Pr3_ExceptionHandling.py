# Programming Practice 6.3 Exception Handling
"""
Copy your file from the previous exercise (Average numbers)
and modify it so that it handles the following exceptions:
-   It should handle any IOError exceptions that are raised when
    the file is opened and data is read from it.
-   It should handle any ValueError exceptions that are raised when
    the items that are read from the file are converted to a number.
"""

filename = "Ch6_Files/numbers2.txt"
num_file = ""  # we haven't done global vars yet.
total = 0
count = 0

try:
    num_file = open(filename, "r")  # IOError can stem from here
    for num in num_file:   # ValueError can stem from here
        total = total + int(num)
        count = count + 1
    num_file.close()

except IOError:  # Throws exception if file does not exist
    print("File not found.")

except ValueError:  # Throws exception when int(value) fails
    print(
        "There were non-integer data in the file.\n"
        "Reading of file stopped. Displaying read data...\n"
    )
    # File is open when this exception gets thrown.
    # Assumed to be a file at this point -- not the best way to handle it
    # but meh.
    num_file.close()

# This is done later. Might still occur is ValueError comes later.
if count > 0:
    average = total / count
    print(
        "Numbers Read: {}\n"
        "Total: {:,.0f}\n"
        "Average: {:,.2f}"
        .format(count, total, average)
    )
