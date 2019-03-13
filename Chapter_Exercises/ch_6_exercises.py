"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 6.1 Introduction to File Input and Output
print("=" * 10, "Section 6.1 file input and output", "=" * 10)
# 1) Assign the variable file_variable to open states.txt in read mode
file_variable = open("states.txt", "r")

# 2) Close the file
file_variable.close()

# 3) Assign the variable state_capitals to open capitals.txt in write mode.
#    Please note, the file does not currently exist, and by opening it in
#    write mode you will create it
state_capitals = open("capitals.txt", "w")

# 4) Write three state capitals to the file
#    There is a list of state capitals here: https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States
# Sample:
#   state_capitals.write("Alabama, Montgomery\n") - make sure to include the \n as a new line symbol
state_capitals.write("Alabama, Montgomery\n")
state_capitals.write("Alaska, Juneau\n")
state_capitals.write("Arizona, Phoenix\n")

# 5) Close the file
state_capitals.close()

# TODO 6.1 reading data in from a file
print("=" * 10, "Section 6.1 reading data from a file", "=" * 10)
# 1) Assign the variable states_data to open states.txt in read mode
states_data = open("states.txt", "r")
# 2) Read in three lines from the file, assign to the variables below, Remove """   """ to test
line1 = states_data.readline()
line2 = states_data.readline()
line3 = states_data.readline()
 
# 3) Close the file
states_data.close()

# 4) Print the three variables
print(line1, line2, line3, sep="")

# TODO 6.2 Using loops to process files
print("=" * 10, "Section 6.2 use loops to process files", "=" * 10)
# Complete the program below to Read in and Count all of the entries in the states file
# Remove the """ """ before testing
# 1) Open the file in read mode using states_file as the file variable
states_file = open("states.txt", "r")
counter = 0
# 2) Write a for loop to read in all of the lines,
# -- print them on the screen,
# -- and add 1 to counter for each line
print("List of States in the US:")
for line in states_file:
    country = line.strip()  # strip() trims whitespace from string
    if country:  # returns true if country is not blank
        print("  {:15}".format(country), end="")
        counter = counter + 1
        if counter % 5 == 0:
            print()
# 3) Close the file
states_file.close()
print("There are {} states recorded in file.".format(counter))
print()

# Reference: https://stackabuse.com/reading-files-with-python/
# Reference: https://stackoverflow.com/questions/9573244/most-elegant-way-to-check-if-the-string-is-empty-in-python

# TODO 6.3 Processing records
print("=" * 10, "Section 6.3 processing records", "=" * 10)
# You are going to finish the program below to write book information to a file
books = 3      # use this as the number of books to enter

# 1) open the file books.txt for writing, using the variable books_file
books_file = open("books.txt", "w")

# 2) Use a for loop to get a title and author from the user using the range 1, books + 1
# -- get the data from the user in the loop
# -- write the data to the file as a record while in the loop,
#    make sure to include the \n at the end of the line
print("Please enter title and author information: ")
for i in range(books):
    print("Enter information for Book {}:".format(i + 1))
    books_file.write("Book {} \n".format(i + 1))
    books_file.write("Title: " + input("   Title  : ") + "\n")
    books_file.write("Author: " + input("   Author : ") + "\n\n")
    print()
print()

# 3) Close the file
books_file.close()

# TODO 6.4 Exceptions
print("=" * 10, "Section 6.4 exceptions", "=" * 10)
# In this exercise you will try to open a file that does not exist,
# capture the error, and display a custom error message

# 1) Create a try statement
try:
    # 2) Open the file superheros.txt for READING (we are not writing, it would create the file)
    superhero_txt = open("superheros.txt", "r")
    # 3) Close the file
    superhero_txt.close()
except IOError:
    # 4) Create an except IOError, that uses a print statement telling the user that the file doesn't exist
    print("File superheros.txt does not exist.")
