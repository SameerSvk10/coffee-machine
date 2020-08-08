from src.controller import Controller
from src.controller import CoffeeMachine
from collections import namedtuple
import pytest
import json
import random


@pytest.fixture()
def create_test_data():
    """create test data for testing"""
    with open("../test_data/test_input.json") as input_test:
        configuration_data = json.load(input_test)
        controller = Controller(configuration_data)
        machine_configuration = configuration_data["machine"]
        beverages = machine_configuration["beverages"]
        return namedtuple('test_data', "controller beverages")(controller, beverages)


@pytest.fixture()
def output_json():
    with open("../test_data/test_output.json") as test_output:
        output_json = json.load(test_output)
        return output_json


class TestController:

    def test_initialization(self, create_test_data):
        """test Controller object initialization"""
        assert create_test_data.controller

    def test_object_attributes(self, create_test_data):
        """test if Controller has created CoffeeMachine object"""
        assert type(create_test_data.controller.coffee_machine) is CoffeeMachine

    def test_prepare_beverage(self, create_test_data):
        beverage_name = random.choice(list(create_test_data.beverages.keys()))
        assert create_test_data.controller.prepare_beverage(beverage_name)

    def test_run(self, create_test_data, output_json):
        """test if the run method produces the correct output"""
        output = create_test_data.controller.run()
        assert any([set(each_output) == set(output) for each_output in output_json])
