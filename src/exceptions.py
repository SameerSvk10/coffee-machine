"""
exceptions.py
This script contains custom exceptions related to CoffeeMachine
"""


class BeveragesTypeError(TypeError):
    """"Beverages should be an object with keys as beverage name and their values as ingredient quantities required"""


class AddBeverageTypeError(TypeError):
    """Beverage name should be a string -> 'tea' and Ingredients should be an object with keys as ingredient name
     and value as quantity -> {'water' : 100}"""


class FetchBeverageDataError(Exception):
    """Select beverage from the list of beverage available"""


class ContainerTypeError(TypeError):
    """The container quantities should be an object with key as the name of ingredient and value as quantity"""
