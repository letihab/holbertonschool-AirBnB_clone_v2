#!/usr/bin/python3
""" City Unittests """


from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State
from models import storage
from models.base_model import BaseModel
import os
from models import storage
from unittest.mock import patch
from sqlalchemy.orm import relationship



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
    """OLD"""

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

    def setUp(self):
        """Set up the testing environment"""
        self.city = City()

    def tearDown(self):
        """Tear down the testing environment"""
        storage.close()

    def test_city_inherits_from_base_model(self):
        """Test if City inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_has_name_attribute(self):
        """Test if City has 'name' attribute"""
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertIsInstance(self.city.name, str)

    def test_city_has_state_id_attribute(self):
        """Test if City has 'state_id' attribute"""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertIsInstance(self.city.state_id, str)

    def test_city_has_places_relationship(self):
        """Test if City has a relationship with Place"""
        self.assertTrue(hasattr(City, 'places'))
        self.assertIsInstance(City.places.property, relationship)

    def test_city_name_can_be_set(self):
        """Test if City 'name' can be set"""
        self.city.name = "New York"
        self.assertEqual(self.city.name, "New York")

    def test_city_state_id_can_be_set(self):
        """Test if City 'state_id' can be set"""
        self.city.state_id = "CA"
        self.assertEqual(self.city.state_id, "CA")

    def test_city_name_must_be_string(self):
        """Test if City 'name' must be a string"""
        with self.assertRaises(ValueError):
            self.city.name = 123

    def test_city_name_cannot_be_empty(self):
        """Test if City 'name' cannot be an empty string"""
        with self.assertRaises(ValueError):
            self.city.name = ""

    def test_city_state_id_must_be_string(self):
        """Test if City 'state_id' must be a string"""
        with self.assertRaises(ValueError):
            self.city.state_id = 123

    def test_city_state_id_cannot_be_empty(self):
        """Test if City 'state_id' cannot be an empty string"""
        with self.assertRaises(ValueError):
            self.city.state_id = ""

    def test_city_to_dict_method(self):
        """Test if City has a 'to_dict' method"""
        self.assertTrue(hasattr(self.city, 'to_dict'))
        model_dict = self.city.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'City')
        self.assertEqual(model_dict['name'], self.city.name)
        self.assertEqual(model_dict['state_id'], self.city.state_id)

    @patch('models.storage')
    def test_city_save_method(self, mock_storage):
        """Test if City has a 'save' method"""
        self.assertTrue(hasattr(self.city, 'save'))
        self.city.save()
        mock_storage.new.assert_called_once_with(self.city)
        mock_storage.save.assert_called_once()

    @patch('models.storage')
    def test_city_delete_method(self, mock_storage):
        """Test if City has a 'delete' method"""
        self.assertTrue(hasattr(self.city, 'delete'))
        self.city.delete()
        mock_storage.delete.assert_called_once_with(self.city)
