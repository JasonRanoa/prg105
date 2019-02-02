# Programming Practice 5.2 Automobile Costs
"""
Write a program that asks the user to enter the monthly costs for the
following expenses incurred from operating his or her automobile: loan
payment, insurance, gas, and maintenance. The program should then
display the total monthly cost of these expenses, and the total annual
cost of these expenses.

Assign meaningful names to your functions and variables. Every function
also needs a comment explaining what it does and what other function it
works with.
"""


def main():
    yearly(monthly())


def monthly():
    # Collect monthly costs from user
    print("Enter monthly costs for the ff. expenses.")
    loan_payment = float(input("  Loan Payment: $ "))
    insurance_expense = float(input("  Insurance: $ "))
    gas_expense = float(input("  Gas: $ "))
    maintenance_expense = float(input("  Maintenance: $ "))

    expense_total = loan_payment + insurance_expense + gas_expense \
        + maintenance_expense
    print("Monthly Costs: ${:,.2f}".format(expense_total))
    return expense_total


def yearly(monthly_total):
    # Collect yearly costs from user
    yearly_cost = monthly_total * 12
    print("Yearly Costs: ${:,.2f}".format(yearly_cost))


main()
