#!/usr/bin/python3
""" City Unittests """


from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State
from models import storage
from models.base_model import BaseModel
import os


class test_City(test_basemodel):
    """ City Unittests """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    #--New Unittests--#

    def test_name(self):
        """ """
        new = City()
        self.assertEqual(type(new.name), str)

    def test_city_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_state_relationship(self):
        # Test the relationship between City and State
        state = State(name="New York")
        city = City(name="Albany", state=state)
        self.assertEqual(city.state, state)
