# Programming Practice 3.3 Nested Ifs
"""
A mobile phone service provider has three different subscription
packages for its customers:

Package A:	For $39.99 per month 450 minutes are provided.
            Additional minutes are $0.45 per minute.
Package B:	For $59.99 per month 900 minutes are provided.
            Additional minutes are $0.40 per minute.
Package C:	For $69.99 per month unlimited minutes provided.

Write a program that calculates a customer's monthly bill.
It should ask which package the customer has purchased and
how many minutes were used. It should then display the total amount due.
Use a dollar sign and two decimal places for currency.
"""

# Constants
# Plan A
A_BASE = 39.99
A_MIN_LIMIT = 450  # provided minutes
A_ADD_COST = 0.45  # dollars per minute
# Plan B
B_BASE = 59.99
B_MIN_LIMIT = 900
B_ADD_COST = 0.40
# Plan C
C_BASE = 69.99

print("This program calculates a customer's monthly bill.")
plan = input("Enter customer's subscription package (A, B or C): ")

if plan == "A" or plan == "a":
    cost = A_BASE
    min_num = int(input("Enter number of minutes used: "))
    remainder = min_num - A_MIN_LIMIT
    if remainder > 0:
        cost = cost + remainder * A_ADD_COST
    print("Customer's bill totals up to ${:,.2f}".format(cost))

elif plan == "B" or plan == "b":
    cost = B_BASE
    min_num = int(input("Enter number of minutes used: "))
    remainder = min_num - B_MIN_LIMIT
    if remainder > 0:
        cost = cost + remainder * B_ADD_COST
    print("Customer's bill totals up to ${:,.2f}".format(cost))

elif plan == "C" or plan == "c":
    cost = C_BASE
    print("Customer's bill totals up to ${:,.2f}".format(cost))

else:
    print("Subscription package not found. Please enter A, B, or C next time.")
