# Programming Practice 3.1 Days of the Week
"""
Write a program that asks the user for a number in the range of 1
through 7. The program should display the corresponding day of the
week, where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday,
5 = Friday, 6 = Saturday, and 7 = Sunday. The program should display
an error message if the user enters a number that is outside the range
of 1 through 7.
"""
# Program written by Julius Ranoa

day_num = int(input("Enter a number between 1 and 7 (inclusive): "))
if day_num == 1:
    print("Monday")
elif day_num == 2:
    print("Tuesday")
elif day_num == 3:
    print("Wednesday")
elif day_num == 4:
    print("Thursday")
elif day_num == 5:
    print("Friday")
elif day_num == 6:
    print("Saturday")
elif day_num == 7:
    print("Sunday")
else:
    print("Number entered is outside of range.")
