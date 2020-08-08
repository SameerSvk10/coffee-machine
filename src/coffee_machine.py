""""
coffee_machine.py

This script implements the CoffeeMachine model
CoffeeMachine can have following attributes
1.  number_of_outlets  - outlet from which beverages can be served.
2. ingredients_container - all the available ingredients in the coffee machine container with capacity
2. beverages - list of beverages and ingredients required to prepare that particular beverage and their quantities
"""

from src.beverages import Beverages
from src.container import Container
import time


class CoffeeMachine:
    def __init__(self, number_of_outlets, ingredients_container, beverages):
        self.number_of_outlets = number_of_outlets
        self.ingredients_container = ingredients_container
        self.beverages = beverages

    @property
    def number_of_outlets(self):
        return self._number_of_outlets

    @number_of_outlets.setter
    def number_of_outlets(self, value):
        if not isinstance(value, int):
            raise TypeError('Number of outlets should be an integer')
        if value <= 0:
            raise ValueError("Number of outlets should be positive non-zero integer")
        self._number_of_outlets = value

    @property
    def ingredients_container(self):
        return self._ingredients_container

    @ingredients_container.setter
    def ingredients_container(self, container_object):
        self._ingredients_container = Container(container_object)

    @property
    def beverages(self):
        return self._beverages

    @beverages.setter
    def beverages(self, beverages):
        self._beverages = Beverages(beverages)

    def add_new_beverage(self, beverage_name, ingredients_required):
        self.beverages.add(beverage_name, ingredients_required)

    def update_beverage(self, beverage_name, ingredients_required):
        self.beverages.add(beverage_name, ingredients_required, update=True)

    def display_coffee_machine(self):
        """This method prints the list of beverages available & ingredients in the container with their
        level & capacity"""
        print(f'''Welcome!!!\n{self._beverages}\n{self._ingredients_container}''')

    def refill_ingredients(self, ingredient):
        self._ingredients_container.refill_container(ingredient)

    def check_container(self):
        self.ingredients_container.check_container_level()

    def prepare_beverage(self, selected_beverage, output, lock):
        """
        preparing selected beverage. It gets the list of ingredients required and checks whether all ingredients
        are available or not else outputs a message. Output is an array which keeps track of beverages prepared and
        those which were not available due to insufficient ingredients or non-availability of ingredient
        threading.Lock is used to avoid race condition when checking or decrementing quantity of ingredient
        """
        ingredients_required = self.beverages.get_ingredients_required_for_beverage(selected_beverage)
        insufficient_ingredients = []
        lock.acquire()
        for each_ingredient, quantity in ingredients_required.items():
            if each_ingredient not in self.ingredients_container.ingredients_container:
                output.append(
                    selected_beverage + " cannot be prepared because " + each_ingredient + " is not available")
                return
            else:
                if self.ingredients_container.ingredients_container[each_ingredient]['level'] < quantity:
                    insufficient_ingredients.append(each_ingredient)

        if not insufficient_ingredients:
            for each_ingredient, quantity in ingredients_required.items():
                self.ingredients_container.ingredients_container[each_ingredient]['level'] -= quantity
            lock.release()
            time.sleep(self.beverages.time_to_prepare_beverage)
            output.append(selected_beverage + " is prepared")
        else:
            lock.release()
            output.append(
                selected_beverage + " cannot be prepared because item " + insufficient_ingredients[
                    0] + " is not sufficient")
