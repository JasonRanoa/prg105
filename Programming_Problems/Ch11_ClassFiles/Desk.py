from . import OfficeFurniture  # Not sure why import OfficeFurniture doesn't work

"""
    Desk class -- derived from OfficeFurniture
    
    COPIED INSTRUCTIONS:
    In the second step create a subclass for Desk that includes
    location_of_drawers (left, right both are options) and number_drawers.
    Override the parents __str__ method to include drawer
    location and count.
"""


class Desk(OfficeFurniture.OfficeFurniture):
    def __init__(self, material, length, width, height, price,
                 location_of_drawers, number_drawers):
        OfficeFurniture.OfficeFurniture.__init__(
            self, "Desk", material, length, width, height, price
        )
        self.location_of_drawers = location_of_drawers
        self.number_drawers = number_drawers

    def __str__(self):
        return "{}; {}; {}x{}x{}, ${:,.2f}; Drawers: {} on {}".format(
            self.category, self.material, self.length, self.width,
            self.height, self.price, self.number_drawers, self.location_of_drawers
        )
