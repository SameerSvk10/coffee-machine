from src.beverages import Beverages
from src.exceptions import BeveragesTypeError, AddBeverageTypeError, FetchBeverageDataError
import pytest


@pytest.fixture()
def create_beverages():
    beverages = Beverages(beverages={})
    return beverages


class TestBeverages:

    def test_class_initialization(self, create_beverages):
        """Test Beverages object"""
        assert create_beverages
        with pytest.raises(BeveragesTypeError):
            Beverages([])

    def test_object_attributes(self, create_beverages):
        """test initial object attributes"""
        assert create_beverages.time_to_prepare_beverage == 0

    @pytest.mark.parametrize("beverage_name, ingredients_required, expected_output",
                             [("ginger_tea", {"ginger_syrup": 50, "hot_water": 300}, None),
                              ("masala_tea", {"tea_leaves_syrup": 60, "ginger_syrup": 50}, None)])
    def test_add(self, create_beverages, beverage_name, ingredients_required, expected_output):
        """test add beverage"""
        assert create_beverages.add(beverage_name, ingredients_required) == expected_output

    def test_add_raise_exception(self, create_beverages):
        """test case when input data is corrupt"""
        with pytest.raises(AddBeverageTypeError):
            create_beverages.add(1, {})

    def test_get_ingredients_required_for_beverage(self, create_beverages):
        """test get ingredients required to prepare beverage"""
        with pytest.raises(FetchBeverageDataError):
            create_beverages.get_ingredients_required_for_beverage(1)
