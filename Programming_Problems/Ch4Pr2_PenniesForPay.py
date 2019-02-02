# Programming Practice 4.2 Pennies for Pay
"""
Write a program that calculates the amount of money a person would
earn over a period of time if his or her salary is one penny the
first day, two pennies the second day, and continues to double each day.
The program should ask the user for the number of days.
Display a table showing what the salary was for each day,
and then show the total pay at the end of the period.
The output should be displayed in a dollar amount, not the number of
pennies.
"""

START_PAY = 0.01
COMMON_RATIO = 2  # Salary increases 2x per day
total_pay = 0

num_days = int(input("Enter number of days worked: "))
print("Here's a summary of earnings: ")
for day in range(num_days):
    pay_this_day = START_PAY * (COMMON_RATIO ** day)
    print(
        "  Day {:>2}: \t${:>20,.2f}".format(day + 1, pay_this_day)
    )
    total_pay = total_pay + pay_this_day
print("-" * (13 + 20))
print("Pay Total: \t${:>20,.2f}".format(total_pay))

# Reference: https://docs.python.org/3/library/string.html#formatstrings
