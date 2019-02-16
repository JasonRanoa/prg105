"""
    Office Furniture Class File
    Intended to be a base class - derived classes include Desk

    INSTRUCTIONS:
    In the first step, you will create a parent class.
    Create a parent class for Office Furniture.
    Set the class variables to be a
        category (desk, chair, filing cabinet would be examples),
        material, length, width, height, and price.
        Include a method that returns a string about the object.
"""


class OfficeFurniture:
    def __init__(self, category, material, length, width, height, price):
        self.category = category
        self.material = material
        self.length = length
        self.width = width
        self.height = height
        self.price = price

    def __str__(self):
        return "{}; {}; {}x{}x{}, ${:,.2f}".format(
            self.category, self.material, self.length, self.width,
            self.height, self.price
        )
