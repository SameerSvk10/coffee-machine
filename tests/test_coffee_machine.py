from src.coffee_machine import CoffeeMachine
from collections import namedtuple
import threading
import pytest
import json
import random


@pytest.fixture()
def create_test_data():
    """create test data for testing"""
    with open("../test_data/test_input.json") as input_test:
        configuration_data = json.load(input_test)
        machine_configuration = configuration_data["machine"]
        number_of_outlets = machine_configuration["outlets"]["count_n"]
        ingredients_container = machine_configuration["total_items_quantity"]
        beverages = machine_configuration["beverages"]
        coffee_machine = CoffeeMachine(number_of_outlets, ingredients_container, beverages)
        return namedtuple('test_data', "number_of_outlets ingredients_container beverages coffee_machine")(
            number_of_outlets, ingredients_container, beverages, coffee_machine)


class TestCoffeeMachine:

    def test_initialization(self, create_test_data):
        """Test CoffeeMachine object"""
        assert create_test_data.coffee_machine

    def test_object_attributes(self, create_test_data):
        """test if the attributes are set properly or not"""
        assert create_test_data.coffee_machine.number_of_outlets == create_test_data.number_of_outlets
        assert set(create_test_data.coffee_machine.beverages.beverages.keys()) == set(create_test_data.beverages.keys())
        hot_water_container_object = create_test_data.ingredients_container["hot_water"]
        assert create_test_data.coffee_machine.ingredients_container.ingredients_container[
                   'hot_water']["capacity"] == hot_water_container_object

    @pytest.mark.parametrize("beverage_name, ingredients_required",
                             [("ginger_tea", {"ginger_syrup": 50, "hot_water": 300}),
                              ("masala_tea", {"tea_leaves_syrup": 60, "ginger_syrup": 50})])
    def test_add_new_beverage(self, create_test_data, beverage_name, ingredients_required):
        """test case for adding new beverage"""
        create_test_data.coffee_machine.add_new_beverage(beverage_name, ingredients_required)
        assert beverage_name in create_test_data.coffee_machine.beverages.beverages

    def test_refill_ingredients(self, create_test_data):
        """test case to check refill functionality"""
        ingredient_name = random.choice(list(create_test_data.ingredients_container.keys()))
        create_test_data.coffee_machine.refill_ingredients(ingredient_name)
        ingredients_container = create_test_data.coffee_machine.ingredients_container.ingredients_container
        assert ingredients_container[ingredient_name]["capacity"] == ingredients_container[ingredient_name]["level"]

    def test_prepare_beverage(self, create_test_data):
        """test case to check prepare beverage"""
        beverage_name = random.choice(list(create_test_data.beverages.keys()))
        output = []
        create_test_data.coffee_machine.prepare_beverage(beverage_name, output, threading.Lock())
        assert output
