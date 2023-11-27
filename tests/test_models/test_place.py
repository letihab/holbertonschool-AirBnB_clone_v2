#!/usr/bin/python3
"""Test for class Place"""


import unittest
from models.place import Place
from models.base_model import BaseModel
from models import storage
import os


class TestPlace(unittest.TestCase):
    def test_place_attributes(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_in_storage(self):
        place = Place()
        storage.save()
        key = "Place.{}".format(place.id)
        self.assertEqual(key in storage.all(), True)

    def test_place_set_and_get_name(self):
        place = Place()
        place.name = "laval"
        self.assertEqual(place.name, "laval")
        place.name = "paris"
        self.assertEqual(place.name, "paris")

    def test_city_inherits_from(self):
        self.assertTrue(issubclass(Place, BaseModel))

    """Test Erwan & Nathalie"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.place = Place()
        try:
            os.rename("file.json", "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """Class method to close test's environment"""
        try:
            os.remove("file.json")
            os.rename("test_file.json", "file.json")
        except Exception:
            pass

    def test_save_method(self):
        """Test case for 'save' method"""
        datetime_prev = self.place.updated_at
        self.place.save()
        self.assertGreater(self.place.updated_at, datetime_prev)
        self.assertTrue(os.path.exists("file.json"))

    def test_str_method(self):
        """Test case for str instance representation"""
        cls_name = str(self.place.__class__.__name__)
        obj_dict = str(self.place.__dict__)
        obj_str = "[{}] ({}) {}".format(cls_name, self.place.id, obj_dict)
        self.assertEqual(obj_str, self.place.__str__())

    def test_to_dict_method(self):
        """Test case for 'to_dict' method"""
        dict = {
            "id": self.place.id,
            "__class__": self.place.__class__.__name__,
            "created_at": self.place.created_at.isoformat(),
            "updated_at": self.place.updated_at.isoformat()
        }
        self.assertDictEqual(dict, self.place.to_dict())

    def test_instance_creation(self):
        obj = Place()
        self.assertIsInstance(obj, Place)

    def test_str_representation(self):
        obj = Place()
        obj_str = str(obj)
        self.assertTrue("[Place]" in obj_str)
        self.assertTrue(obj.id in obj_str)

    def test_to_dict_method(self):
        obj = Place()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'Place')
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)


if __name__ == "__main__":
    unittest.main()
