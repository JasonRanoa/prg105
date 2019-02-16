"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 11.1 Introduction to Inheritance
print("=" * 10, "Section 11.1 inheritance", "=" * 10)
# You are going to create a Dwelling class based on the
# Automobile sample from the chapter

# 1) Create the class Dwelling, the __init__ method should accept number_of_rooms, square_feet, floors


class Dwelling:
    def __init__(self, number_of_rooms, square_feet, floors):
        self.number_of_rooms = number_of_rooms
        self.square_feet = square_feet
        self.floors = floors

    # 2) Add mutators for all of the data attributes (number_of_rooms, square_feet, floors)
    def set_number_of_rooms(self, number_of_rooms):
        self.number_of_rooms = number_of_rooms

    def set_square_feet(self, square_feet):
        self.square_feet = square_feet

    def set_floors(self, floors):
        self.floors = floors

    # 3) Add accessors for all of the data attributes
    def get_number_of_rooms(self):
        return self.number_of_rooms

    def get_square_feet(self):
        return self.square_feet

    def get_floors(self):
        return self.floors


# 4) Create the class Single_family_home as a sub class of Dwelling


class SingleFamilyHome(Dwelling):  # PEP8 requires CamelCase for class names
    # The __init__ method should accept number_of_rooms, square_feet, floors, garage_type, yard_size
    def __init__(self, number_of_rooms, square_feet, floors, garage_type, yard_size):
        # -- Call the __init__ of superclass Dwelling and pass the required arguments, remember to include self
        Dwelling.__init__(self, number_of_rooms, square_feet, floors)
        # -- Initialize the garage_type and yard_size attributes
        self.garage_type = garage_type
        self.yard_size = yard_size

# 5) Create the mutator and accessor methods for the garage_type and yard_size attributes
    def set_garage_type(self, garage_type):
        self.garage_type = garage_type

    def set_yard_size(self, yard_size):
        self.yard_size = yard_size

    def get_garage_type(self):
        return self.garage_type

    def get_yard_size(self):
        return self.yard_size


# 6) Demonstrate the Single_family_home class, no need to import because you are in the same file
# 7) Create an object from the Single_family_home class with the following information:
# 6 rooms, 1200 square feet, 1 floor, single car garage, .25 acres
home = SingleFamilyHome(6, 1200, 1, "Single", .25)

# 8) Display the data using the accessor methods
# 9) Create a main function. Call the main function


def main():
    print(
        "Home Information:",
        "  Number of rooms : {}".format(home.get_number_of_rooms()),
        "  Square feet     : {}".format(home.get_square_feet()),
        "  Floors          : {}".format(home.get_floors()),
        "  Garage Type     : {}".format(home.get_garage_type()),
        "  Acres           : {}".format(home.get_yard_size()),
        sep="\n"
    )
    print()


main()

# TODO 11.2 Polymorphism
print("=" * 10, "Section 11.2 polymorphism", "=" * 10)
# 1) Type in the mammal class from program 11-9, lines 1 - 22
# The Mammal class represents a generic mammal. COPIED FROM TEXT AS INSTRUCTED.


class Mammal:
    # The _ _init_ _ method accepts an argument for\
    # the mammal's species.

    def __init__(self, species):
        self.__species = species

    # The show_species method displays a message
    # indicating the mammal's species.
    def show_species(self):
        print("I am a", self.__species)

    # The make_sound method is the mammal's
    # way of making a generic sound.
    def make_sound(self):
        print("Grrrrr")


# 2) Create a Mouse class as a sub class of the mammal class following the Dog example


class Mouse(Mammal):
    def __init__(self):
        Mammal.__init__(self, "Mouse")

    def make_sound(self):
        print("Squeak! Squeak!")


# 3) Create a Bird class as a sub class of the mammal class following the Cat Example


class Bird(Mammal):  # ... birds are not mammals, though. They have their own phylum.
    def __init__(self):
        Mammal.__init__(self, "Cat")

    def make_sound(self):
        print("Tweet")


# 4) Follow the example in program 11-10 (no need to import, use main2 instead of main
#    because there is already a main on this page) use the Mouse and Bird class that you created


def main2():
    mammal = Mammal("Regular Animal")
    mouse = Mouse()
    bird = Bird()

    print(
        "Here are some animals and the sounds they make:",
        "-" * 20,
        sep="\n"
    )

    show_mammal_info(mammal)
    print()

    show_mammal_info(mouse)
    print()

    show_mammal_info(bird)
    print()


def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()


main2()
