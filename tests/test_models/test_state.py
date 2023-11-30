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
