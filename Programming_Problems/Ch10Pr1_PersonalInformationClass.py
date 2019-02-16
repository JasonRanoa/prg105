# Programming Practice 10.1 Personal Information Class
"""
Design a class that holds the following personal data:
name, address, age, and phone number. Write appropriate accessor
and mutator methods (get and set). Write a program that creates
three instances of the class. One instance should hold your
information and the other two should hold your friends or family
members' information.  Just add information, don't get it from the
user.
Print the data from each object, make sure to format the output
for clarity and ease of reading.
"""


class PersonalData:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.age = ""
        self.phone = ""

    # Setters
    def set_name(self, new_name):
        self.name = new_name

    def set_address(self, new_address):
        self.address = new_address

    def set_age(self, new_age):
        self.age = new_age

    def set_phone(self, new_phone):
        self.phone = new_phone

    # Getters
    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone(self):
        return self.phone


def main():
    people = [PersonalData() for _ in range(3)]
    # Note: [PersonalData()] * 3 just creates ONE mutable object
    #       Basically, like three pointers to the same thing
    # Note2: _ is accepted by PEP8 to be a variable that is not used.
    # The iterator for this for-range loop, for example.

    # me
    people[0].set_name("Jason Ranoa")
    people[0].set_address("McHenry, IL 60051")
    people[0].set_age(22)
    people[0].set_phone("REDACTED")

    # Fictional Person 1
    people[1].set_name("Bakugou Katsuki")
    people[1].set_address("Musutafu, Japan")
    people[1].set_age(16)
    people[1].set_phone("REDACTED")

    # Fictional Person 2
    people[2].set_name("Kirishima Eijirou")
    people[2].set_address("Chiba Prefecture, Japan")
    people[2].set_age(15)
    people[2].set_phone("REDACTED")

    for person in people:
        print(
            "Name    : {}\n"
            "Address : {}\n"
            "Age     : {}\n"
            "Phone   : {}\n"
            .format(
                person.get_name(), person.get_address(),
                person.get_age(), person.get_phone()
            )
        )


main()
