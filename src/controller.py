"""
controller.py
This script implements Controller class which is used to control the CoffeeMachine
This class runs the CoffeeMachine instance to prepare beverage
The Controller class need machine_configuration as input which specifies
- number_of_outlets
- ingredients_container
- beverages
"""
from src.coffee_machine import CoffeeMachine
import threading
import concurrent.futures
import json


class Controller:
    def __init__(self, machine_configuration):
        self.coffee_machine = machine_configuration

    @property
    def coffee_machine(self):
        return self._coffee_machine

    @coffee_machine.setter
    def coffee_machine(self, machine_configuration):
        if not isinstance(machine_configuration, dict):
            raise TypeError("Machine configuration input is required to be in json object format")
        machine_configuration = machine_configuration["machine"]
        self._coffee_machine = CoffeeMachine(number_of_outlets=machine_configuration["outlets"]["count_n"],
                                             ingredients_container=machine_configuration["total_items_quantity"],
                                             beverages=machine_configuration["beverages"])

    def display_coffee_machine(self):
        self.coffee_machine.display_coffee_machine()

    def prepare_beverage(self, selected_beverage):
        output = []
        lock = threading.Lock()
        self.coffee_machine.prepare_beverage(selected_beverage, output, lock)
        return output

    def refill_ingredient_container(self, selected_ingredient):
        self.coffee_machine.refill_ingredients(selected_ingredient)

    def run(self):
        """
        This method runs a CoffeeMachine.
        As CoffeeMachine can have more than one outlet, CoffeeMachine can serve more than one beverage at a time
        This method calls prepare_beverage method with all the beverages using threads.
        threading.Lock() is used to avoid race condition in accessing and modifying data
        """
        output = []
        self.display_coffee_machine()
        lock = threading.Lock()
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.coffee_machine.number_of_outlets) as executor:
            for each_beverage in self.coffee_machine.beverages.beverages.keys():
                executor.submit(self.coffee_machine.prepare_beverage, each_beverage, output, lock)
        print('\n'.join(output))
        self.coffee_machine.check_container()
        self.display_coffee_machine()
        return output


if __name__ == "__main__":
    with open('../test_data/test_input.json') as input_test_json:
        configuration = json.load(input_test_json)
        controller = Controller(configuration)
        controller.run()
