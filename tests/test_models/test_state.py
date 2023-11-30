#!/usr/bin/python3
""" State unittests """


from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models.city import City
from models.base_model import BaseModel
from models import storage
import os


class test_state(test_basemodel):
    """ State unittests """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    #--New unittests--#

    def test_name(self):
        """ """
        new = State()
        self.assertEqual(type(new.name), str)

    def test_state_cities_relationship(self):
        # Test the relationship between State and City
        state = State(name="California")
        city = City(name="San Francisco", state=state)
        self.assertIn(city, state.state_cities)
