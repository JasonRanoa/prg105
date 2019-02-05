"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 7.2 Lists
print("=" * 10, "Section 7.2 lists", "=" * 10)
# 1) Create a list of days of the week, assign it to the variable days, remove """ """ to test
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# 2) Create a list with 5 items, set them all to 0, use the Repetition Operator ( * )
zero_list = [0] * 5
# Reference: https://stackoverflow.com/questions/3459098/create-list-of-single-item-repeated-n-times-in-python/3459131
# 3) Print the contents of your days list using the for operator
print("Task 7.2.3: ", days)
# 4) Print the list item that holds the value Saturday from the days list by using it's index
print("Task 7.2.4:", days[6])
# 5) Create a variable called size to hold the length of the list days using the len function
size = len(days)
# 6) Concatenate the two following lists together, storing the value in list3 - remove the """ """ to test
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = list1 + list2
print(list3)
print()

# TODO 7.3 List Slicing
print("=" * 10, "Section 7.3 list slicing", "=" * 10)
# Slice the list days to select from Monday through Friday, inclusive, and assign the new list to work_days
# Print work_days
work_days = days[1:6]
print("Task 7.3:", work_days)
# Reference: https://stackoverflow.com/questions/509211/understanding-slice-notation
print()

# TODO 7.4 Finding items in Lists with the in Operator
print("=" * 10, "Section 7.4 using the in operator", "=" * 10)
# Test to see if "Tue" is in the list days - display "yes, Tue is in the list" or "no, Tue is not in the list"
if "Tue" in days:
    print("Yes, Tue is in the list.")
else:
    print("No, Tue is not on the list.")
print()

# TODO 7.5 List Methods and Useful Built-in Functions
print("=" * 10, "Section 7.5 list methods and functions", "=" * 10)
# 1) Use append() to append the last three months of the year to the list months.
months = list(["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept"])
months.append("Oct")
months.append("Nov")
months.append("Dec")

# 2) Get the index of "May" from the months list and print it on screen
print(months[months.index("May")])
# 3) Sort list3 from exercise 7.2 and print the results on screen
list3.sort()
print("Task 7.5.3:", list3)
# 4) Reverse the order of list3
list3.reverse()
print("Task 7.5.4:", list3)
# 5) Delete the number 5 from list3 and print the list(remember we reversed the list)
list3.remove(5)
print("Task 7.5.5:", list3)
# 6) Print the maximum value from list 3
print("Task 7.5.6:", list3[0])  # List was sorted in decreasing order prev.
# Note that using the max function also works
print()

# TODO 7.6 Copying Lists
print("=" * 10, "Section 7.6 copying lists", "=" * 10)
# Copy the list months to the variable months_of_the_year
# Print the values in months_of_the_year
months_of_the_year = months[:]
print(months_of_the_year)
print()

# TODO 7.7 Processing lists
print("=" * 10, "Section 7.7 processing lists", "=" * 10)
# 1) Total the values in list3 and print the results
total = 0
for n in list3:
    total = total + n
print("Task 7.7.1:", total)
# 2) Get the average of values in list3 and print the results
print("Task 7.7.2: {:.2f}".format(total / len(list3)))
# 3) Open the file states.txt in read mode,
# -- read the contents of the file into the list states_list
# -- print the contents of states_list on screen
states_file = open("states.txt", "r")
states_list = []
for state in states_file:
    states_list.append(state)
states_file.close()
print("Task 7.7.3:", states_list)  # Special character's still there?
print()

# TODO 7.8 Two-Dimensional Lists
print("=" * 10, "Section 7.8 two-dimensional lists", "=" * 10)
# 1) Create a new two dimensional list that has the months of the year
#     and the days in each month during a non leap year
#     For example, the first entry should be: January, 31
month_data = [
    ["January", 31], ["February", 28], ["March", 31], ["April", 30],
    ["May", 31], ["June", 30], ["July", 31], ["August", 31],
    ["September", 30], ["October", 31], ["November", 30], ["December", 31]
]
# 2) Print the contents of the entire list
print("Task 7.8.2:", month_data)
# 3) Print just the values for index 3,0 and 3,1
print("Task 7.8.3:", month_data[3][0], month_data[3][1])
print()

# TODO 7.9 Tuples
print("=" * 10, "Section 7.9 tuples", "=" * 10)
# Create a tuple using the months list as its data source
months_tuple = tuple(months)
print(months_tuple)
