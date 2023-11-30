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

    def test_name(self):
        """ """
        new = Amenity()
        self.assertEqual(type(new.name), str)

    def test_amenity_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_places_relationship(self):
        # Test the relationship between Amenity and Place
        amenity = Amenity(name="Parking")
        place1 = Place(name="House with Parking")
        place2 = Place(name="Apartment with Parking")
        amenity.place_amenities.append(place1)
        amenity.place_amenities.append(place2)
        self.assertIn(place1, amenity.place_amenities)
        self.assertIn(place2, amenity.place_amenities)
