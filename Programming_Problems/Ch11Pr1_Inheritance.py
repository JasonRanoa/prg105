# Programming Practice 11.1 Inheritance
"""
NOTE: See Ch11_ClassFiles for class files.

In the first step, you will create a parent class.
Create a parent class for Office Furniture.
Set the class variables to be a
    category (desk, chair, filing cabinet would be examples),
    material, length, width, height, and price.
    Include a method that returns a string about the object.

In the second step create a subclass for Desk that includes
    location_of_drawers (left, right both are options) and
    number_drawers.
    Override the parents __str__ method to include drawer
    location and count.

Implement each class in a separate file.
Import these into your main program.
Your main program should implement and display an instance of each,
the parent class and the child class.
"""

from ProgrammingPractice.Ch11_ClassFiles import Desk, OfficeFurniture


def main():
    chair = OfficeFurniture.OfficeFurniture(
        "Swivel Chair", "Steel, Polyurethane foam, Polyester",
        "51cm", "65cm", "15cm", 49.99
    )
    desk = Desk.Desk(
        "Particle board, Steel",
        "76cm", "11cm", "111cm", 89.99,
        "Right", 2
    )

    print("Furniture Information: ")
    print("  ", chair)
    print("  ", desk)


main()
