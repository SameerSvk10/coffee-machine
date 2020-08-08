from src.container import Container
from src.exceptions import ContainerTypeError
from collections import namedtuple
import random
import pytest
import json


@pytest.fixture()
def create_test_data():
    with open("../test_data/test_input.json") as input_test:
        configuration_data = json.load(input_test)
        machine_configuration = configuration_data["machine"]
        ingredients_container = machine_configuration["total_items_quantity"]
        container = Container(ingredients_container)
        return namedtuple('test_data', "container ingredients_container")(container, ingredients_container)


class TestContainer:

    def test_class_initialization(self, create_test_data):
        """Test Container object"""
        assert create_test_data.container
        with pytest.raises(ContainerTypeError):
            Container([])

    def test_object_attributes(self, create_test_data):
        """test initial object attributes"""
        assert isinstance(create_test_data.container.ingredients_container, dict)

    def test_refill_container(self, create_test_data):
        """test case to check refill container functionality"""
        ingredient_name = random.choice(list(create_test_data.ingredients_container.keys()))
        create_test_data.container.refill_container(ingredient_name)
        ingredients_container = create_test_data.container.ingredients_container
        assert ingredients_container[ingredient_name]["capacity"] == ingredients_container[ingredient_name]["level"]
