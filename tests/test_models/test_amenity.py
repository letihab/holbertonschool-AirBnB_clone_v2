#!/usr/bin/python3
""" Amenity unittests """


from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.place import Place
from models.base_model import BaseModel
from models import storage
import os


class test_Amenity(test_basemodel):
    """ Amenity unittests """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    #--New unittests--#
