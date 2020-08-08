"""
beverages.py
This script implements Beverages Model
Its getter and setter methods.
Beverages class has 2 attributes
1. beverages - object containing all the beverage options available with ingredient and quantity
2. time_to_prepare_beverage - time required to create a beverage
"""
from src.exceptions import BeveragesTypeError, FetchBeverageDataError, AddBeverageTypeError


class Beverages:
    def __init__(self, beverages):
        self.beverages = beverages
        self.time_to_prepare_beverage = 0

    def __str__(self):
        return f'''Choose from the following Beverages : {', '.join(self.beverages.keys())}'''

    @property
    def beverages(self):
        return self._beverages

    @beverages.setter
    def beverages(self, beverages):
        if not isinstance(beverages, dict):
            raise BeveragesTypeError
        self._beverages = beverages

    def add(self, beverage_name, ingredients_required, update=False):
        """adds a new beverage to the existing beverages collection or update the existing one with new ingredients"""
        if not isinstance(beverage_name, str) or not isinstance(ingredients_required, dict):
            raise AddBeverageTypeError
        if not update and beverage_name in self.beverages:
            print("Beverage already exist. updating the exiting one...")
        self.beverages[beverage_name] = ingredients_required

    def get_ingredients_required_for_beverage(self, beverage_name):
        try:
            return self.beverages[beverage_name]
        except Exception:
            raise FetchBeverageDataError
