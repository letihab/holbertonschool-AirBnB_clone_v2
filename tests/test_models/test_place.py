#!/usr/bin/python3
""" """


from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
import os


class test_Place(test_basemodel):
    """ """

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


    #--OLD UNITTESTS--#
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
