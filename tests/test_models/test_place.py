#!/usr/bin/python3
""" Place unittests """


from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models import storage
import os
from sqlalchemy.orm import relationship
from models import storage
from unittest.mock import patch
from os import getenv
from sqlalchemy import String, Column, ForeignKey, Integer, Float, Table


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
    """OLD"""
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

    def setUp(self):
        """Set up the testing environment"""
        self.place = Place()

    def tearDown(self):
        """Tear down the testing environment"""
        storage.close()

    def test_place_inherits_from_base_model(self):
        """Test if Place inherits from BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_has_city_id_attribute(self):
        """Test if Place has 'city_id' attribute"""
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertIsInstance(self.place.city_id, str)

    def test_place_has_user_id_attribute(self):
        """Test if Place has 'user_id' attribute"""
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertIsInstance(self.place.user_id, str)

    def test_place_has_name_attribute(self):
        """Test if Place has 'name' attribute"""
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertIsInstance(self.place.name, str)

    def test_place_has_description_attribute(self):
        """Test if Place has 'description' attribute"""
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertIsInstance(self.place.description, str)

    def test_place_has_number_rooms_attribute(self):
        """Test if Place has 'number_rooms' attribute"""
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertIsInstance(self.place.number_rooms, int)

    def test_place_has_number_bathrooms_attribute(self):
        """Test if Place has 'number_bathrooms' attribute"""
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_place_has_max_guest_attribute(self):
        """Test if Place has 'max_guest' attribute"""
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertIsInstance(self.place.max_guest, int)

    def test_place_has_price_by_night_attribute(self):
        """Test if Place has 'price_by_night' attribute"""
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertIsInstance(self.place.price_by_night, int)

    def test_place_has_latitude_attribute(self):
        """Test if Place has 'latitude' attribute"""
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertIsInstance(self.place.latitude, float)

    def test_place_has_longitude_attribute(self):
        """Test if Place has 'longitude' attribute"""
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertIsInstance(self.place.longitude, float)

    def test_place_has_amenities_relationship(self):
        """Test if Place has a relationship with Amenity"""
        self.assertTrue(hasattr(Place, 'amenities'))
        self.assertIsInstance(Place.amenities.property, relationship)

    def test_place_has_reviews_relationship(self):
        """Test if Place has a relationship with Review"""
        self.assertTrue(hasattr(Place, 'reviews'))
        self.assertIsInstance(Place.reviews.property, relationship)

    @patch('models.storage')
    def test_place_reviews_is_list(self, mock_storage):
        """Test if Place 'reviews' is a list"""
        self.assertTrue(hasattr(self.place, 'reviews'))
        self.assertIsInstance(self.place.reviews, list)

    @patch('models.storage')
    def test_place_amenities_is_list(self, mock_storage):
        """Test if Place 'amenities' is a list"""
        self.assertTrue(hasattr(self.place, 'amenities'))
        self.assertIsInstance(self.place.amenities, list)

    @patch('models.storage')
    def test_place_reviews_property(self, mock_storage):
        """Test Place 'reviews' property"""
        self.place.reviews = [Review()]
        self.assertEqual(len(self.place.reviews), 1)

    @patch('models.storage')
    def test_place_amenities_property(self, mock_storage):
        """Test Place 'amenities' property"""
        self.place.amenities = [Amenity()]
        self.assertEqual(len(self.place.amenities), 1)

    @patch('models.storage')
    def test_place_save_method(self, mock_storage):
        """Test if Place has a 'save' method"""
        self.assertTrue(hasattr(self.place, 'save'))
        self.place.save()
        mock_storage.new.assert_called_once_with(self.place)
        mock_storage.save.assert_called_once()

    @patch('models.storage')
    def test_place_delete_method(self, mock_storage):
        """Test if Place has a 'delete' method"""
        self.assertTrue(hasattr(self.place, 'delete'))
        self.place.delete()
        mock_storage.delete.assert_called_once_with(self.place)
