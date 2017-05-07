from abc import ABCMeta, abstractmethod


class Firearm(object):
    """A firearm on display at Bureau of Alcohol, Tobacco, Firearms and Explosives.

    Attributes:
        caliber: An integer representing the internal diameter of the firearm's barrel in inch.
        s_range: an integer representing the maximum radius within which a shot fired from the firearm is effective.
        capacity: an integer representing the maximum number of bullets the firearm's magazine can hold.
        automacity: The ability or inability of the firearm to fire automatically
        year: The integral year of manufacture of the firearm
    """

    __metaclass__ = ABCMeta

    base_sale_price = 0
    automacity = False

    def __init__(self, caliber, s_range, capacity,  year):
        self.caliber = caliber
        self.s_range = s_range
        self.capacity = capacity
        self.year = year

    def sale_price(self):
        if self.automacity is True:
            if self.capacity > 10:
                return self.base_sale_price + 500 * self.capacity
            else:
                return self.base_sale_price + 200 * self.capacity
        else:
            return self.base_sale_price + 150 * self.capacity

