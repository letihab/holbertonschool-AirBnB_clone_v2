#!/usr/bin/python3
""" unittests amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ unittests amenity """

    def __init__(self, *args, **kwargs):
        """ unittests amenity """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """test_name2 """
        new = self.value()
        self.assertEqual(type(new.name), str)
