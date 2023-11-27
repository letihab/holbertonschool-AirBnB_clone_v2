#!/usr/bin/python3
"""Test for class City"""


import unittest
from models.city import City
from models.base_model import BaseModel
from models import storage
import os


class TestCity(unittest.TestCase):
    def test_city_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_in_storage(self):
        city = City()
        storage.save()
        key = "City.{}".format(city.id)
        self.assertEqual(key in storage.all(), True)

    def test_city_set_and_get_name(self):
        city = City()
        city.name = "laval"
        self.assertEqual(city.name, "laval")
        city.name = "paris"
        self.assertEqual(city.name, "paris")

    def test_city_inherits_from(self):
        self.assertTrue(issubclass(City, BaseModel))

    """Test Erwan & Nathalie"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.city = City()
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
        datetime_prev = self.city.updated_at
        self.city.save()
        self.assertGreater(self.city.updated_at, datetime_prev)
        self.assertTrue(os.path.exists("file.json"))

    def test_str_method(self):
        """Test case for str instance representation"""
        cls_name = str(self.city.__class__.__name__)
        obj_dict = str(self.city.__dict__)
        obj_str = "[{}] ({}) {}".format(cls_name, self.city.id, obj_dict)
        self.assertEqual(obj_str, self.city.__str__())

    def test_to_dict_method(self):
        """Test case for 'to_dict' method"""
        dict = {
            "id": self.city.id,
            "__class__": self.city.__class__.__name__,
            "created_at": self.city.created_at.isoformat(),
            "updated_at": self.city.updated_at.isoformat()
        }
        self.assertDictEqual(dict, self.city.to_dict())

    def test_instance_creation(self):
        obj = City()
        self.assertIsInstance(obj, City)

    def test_str_representation(self):
        obj = City()
        obj_str = str(obj)
        self.assertTrue("[City]" in obj_str)
        self.assertTrue(obj.id in obj_str)

    def test_to_dict_method(self):
        obj = City()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'City')
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)


if __name__ == "__main__":
    unittest.main()
