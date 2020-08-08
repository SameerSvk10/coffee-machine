"""
container.py
This script implements Container Model and its getter and setter methods
This class has an ingredients_container attribute which tells which ingredients the machine has and their quantities
"""

from src.exceptions import ContainerTypeError


class Container:
    def __init__(self, total_ingredients):
        self.ingredients_container = total_ingredients

    def __str__(self):
        output = f'''Container\n'''
        output += "{:<20} {:<10} {:<10}".format('Ingredient', 'level', 'Capacity') + "\n"
        for each_ingredient, each_quantity in self._ingredients_container.items():
            output += "{:<20} {:<10} {:<10}".format(each_ingredient, each_quantity["level"],
                                                    each_quantity["capacity"]) + "\n"
        return output

    @property
    def ingredients_container(self):
        return self._ingredients_container

    @ingredients_container.setter
    def ingredients_container(self, container_object):
        if not isinstance(container_object, dict):
            raise ContainerTypeError
        self._ingredients_container = {}
        for each_ingredient, capacity in container_object.items():
            self._ingredients_container[each_ingredient] = {"capacity": capacity, "level": capacity}

    def check_container_level(self):
        """checks the each ingredient current level and if the level is less than 10%, it prints running low message"""
        for each_ingredient, quantity in self.ingredients_container.items():
            fill_percentage = (quantity["level"] * 100) / quantity["capacity"]
            if fill_percentage <= 10:
                print(f'''You are running low on {each_ingredient} - {fill_percentage}%''')

    def refill_container(self, ingredient):
        """refill entire specified ingredient's container"""
        self._ingredients_container[ingredient]["level"] = self._ingredients_container[ingredient]["capacity"]
