# Programming Practice 11.2 Production Worker
"""
Once you have written the classes
(see Ch11_ClassFiles for, well, class files)

... write a program that creates an object of the ProductionWorker
class and prompts the user to enter data for each of the object’s
data attributes.
Store the data in the object and then use the object’s accessor
methods to retrieve it and display it on the screen.
"""

from ProgrammingPractice.Ch11_ClassFiles import Employee


def main():
    print("Enter data for employee as prompted: ")

    # No input validation for this one.
    name = input("  Name: ")
    number = input("  Employee Number: ")
    pay = float(input("  Hourly Pay: "))
    shift = int(input("  Shift (Day=1, Night=2): "))
    worker = Employee.ProductionWorker(
        name, number, shift, pay
    )
    print()

    print(
        "Employee Data:",
        "  Name            : {}".format(worker.get_name()),
        "  Employee Number : {}".format(worker.get_number()),
        "  Shift           : {}".format(worker.get_shift()),
        "  Hourly Pay Rate : {}".format(worker.get_pay()),
        sep="\n"
    )


main()
