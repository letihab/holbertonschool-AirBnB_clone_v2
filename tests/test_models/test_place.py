#!/usr/bin/python3
""" Place unittests """


from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
import os


class test_Place(test_basemodel):
    """ Place unittests """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    #--New unittests--#

    def test_name(self):
        """ """
        new = Place()
        self.assertEqual(type(new.name), str)

    def test_place_attributes(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")

    def test_place_amenities_relationship(self):
        # Test the relationship between Place and Amenity
        place = Place(name="Awesome Apartment")
        amenity1 = Amenity(name="WiFi")
        amenity2 = Amenity(name="Swimming Pool")
        place.amenities.append(amenity1)
        place.amenities.append(amenity2)
        self.assertIn(amenity1, place.amenities)
        self.assertIn(amenity2, place.amenities)
