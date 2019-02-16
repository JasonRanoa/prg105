"""
COPIED INSTRUCTIONS
Write an Employee class that keeps data attributes for the
following pieces of information:
    Employee name, Employee number

Next, Write a class named ProductionWorker
that is a subclass of the Employee class.
The ProductionWorker class should keep data attributes for the
following information
    Shift numbered (an integer, such as 1, 2, or 3)
    Hourly pay rate
    The workday is divided into two shifts: day and night.
        The shift attribute will hold an integer value representing
        the shift that the employee works.
        The day shift is shift 1 and the night shift is shift 2.
        Write the appropriate accessor and mutator methods
        (get and set) for each class.

Next, Write a class named ProductionWorker
that is a subclass of the Employee class.
The ProductionWorker class should keep data attributes for the
following information
    Shift numbered (an integer, such as 1, 2, or 3)
    Hourly pay rate
    The workday is divided into two shifts: day and night.
        The shift attribute will hold an integer value representing
        the shift that the employee works.
        The day shift is shift 1 and the night shift is shift 2.
        Write the appropriate accessor and mutator methods
        (get and set) for each class.
"""

"""
Generic Employee Class.
"""


class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def set_name(self, name):
        self.name = name

    def set_number(self, number):
        self.number = number

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number


"""
ProductionWorker class -- derived from Employee
"""


class ProductionWorker(Employee):
    def __init__(self, name, number, shift, pay):
        Employee.__init__(self, name, number)
        self.shift = shift
        self.pay = pay

    def get_shift(self):
        if self.shift == 1:
            return "Day"
        elif self.shift == 2:
            return "Night"
        else:
            return "N/A"

    def get_pay(self):
        return self.pay

    def set_shift(self, shift):
        self.shift = shift

    def set_pay(self, pay):
        self.pay = pay
