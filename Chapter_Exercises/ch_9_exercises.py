"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

import pickle

# TODO 9.1 Dictionaries
print("=" * 10, "Section 9.1 dictionaries", "=" * 10)
# 1) Finish creating the following dictionary by adding three more people and birthdays
birthdays = {
    'Meri': 'May 16', 'Kathy': 'July 14',
    "Jason": "Aug 10", "Matt": "Aug 10", "Dan": "June 6"
}
# 2) Print Meri's Birthday
print("Meri's birthday is on:", birthdays["Meri"])
# 3) Create an empty dictionary named registration
registration = {}

# You will use the following dictionary for many of the remaining exercises"
miles_ridden = {'June 1': 25, 'June 2': 20, 'June 3': 38, 'June 4': 12, 'June 5': 30, 'June 7': 25}

# 1) Print the keys and the values of miles_ridden using a for loop
for key in miles_ridden:
    print(key, miles_ridden[key])

# 2) Get the value for June 3 and print it, if not found display 'Entry not found', replace the ""
value = "June 3"
if value in miles_ridden:
    print(miles_ridden[value])
else:
    print("Entry not found.")

# 3) Get the value for June 6 and print it, if not found display 'Entry not found' replace the ""
value2 = "June 6"
if value2 in miles_ridden:
    print(miles_ridden[value2])
else:
    print("Entry not found.")

# 4) Use the items method to print the miles_ridden dictionary
print(miles_ridden.items())

# 5) Use the keys method to print all of the keys in miles_ridden
print(miles_ridden.keys())

# 6) Use the pop method to remove June 4 then print the contents of the dictionary
miles_ridden.pop("June 4")
print(miles_ridden.items())

# 7) Use the values method to print the contents of the miles_ridden dictionary
print(miles_ridden.values())
print()

# TODO 9.2 Sets
print("=" * 10, "Section 9.2 sets", "=" * 10)
# 1) Create an empty set named my_set
my_set = set()  # {} creates an empty dictionary
# 2) Create a set named days that contains the days of the week
days = {
    "Sunday", "Monday", "Tuesday",
    "Wednesday", "Thursday", "Friday", "Saturday"
}
# 3) Get the number of elements from the days set and print it
print(len(days))
# 4) Remove Saturday and Sunday from the days set
days.discard("Sunday")
days.discard("Saturday")
# 5) Determine if 'Mon' is in the days set
if "Mon" in days:
    print("Mon is in the days set.")
else:
    print("Mon is not in the days set.")
print()

# TODO 9.3 Serializing Objects (Pickling)
print("=" * 10, "Section 9.3 serializing objects using the pickle library", "=" * 10)
# Reference (Pickle): https://docs.python.org/3/library/pickle.html#module-pickle
# Reference (Open Flags): https://docs.python.org/3/library/functions.html#open
# 1) Import the pickle library at the top of this file
# 2) Create the output file log and open it for binary writing
log = open("log.bin", "wb")
# 3) Pickle the miles_ridden dictionary and output it to the log file
pickle.dump(miles_ridden, log)
# 4) Close the log file
log.close()
