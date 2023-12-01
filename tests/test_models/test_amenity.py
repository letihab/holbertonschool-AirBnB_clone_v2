#!/usr/bin/python3
""" Amenity unittests """


from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.place import Place
from models.base_model import BaseModel
from models import storage
import os
from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.orm import relationship


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
    """OLD"""
    def test_amenity_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_in_storage(self):
        amenity = Amenity()
        storage.save()
        key = "Amenity.{}".format(amenity.id)
        self.assertEqual(key in storage.all(), True)

    def test_amenity_set_and_get_name(self):
        amenity = Amenity()
        amenity.name = "shop"
        self.assertEqual(amenity.name, "shop")
        amenity.name = "park"
        self.assertEqual(amenity.name, "park")

    def test_amenity_inherits_from(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    """Test Erwan & Nathalie"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.amenity = Amenity()
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
        datetime_prev = self.amenity.updated_at
        self.amenity.save()
        self.assertGreater(self.amenity.updated_at, datetime_prev)
        self.assertTrue(os.path.exists("file.json"))

    def test_str_method(self):
        """Test case for str instance representation"""
        cls_name = str(self.amenity.__class__.__name__)
        obj_dict = str(self.amenity.__dict__)
        obj_str = "[{}] ({}) {}".format(cls_name, self.amenity.id, obj_dict)
        self.assertEqual(obj_str, self.amenity.__str__())

    def test_to_dict_method(self):
        """Test case for 'to_dict' method"""
        dict = {
            "id": self.amenity.id,
            "__class__": self.amenity.__class__.__name__,
            "created_at": self.amenity.created_at.isoformat(),
            "updated_at": self.amenity.updated_at.isoformat()
        }
        self.assertDictEqual(dict, self.amenity.to_dict())

    def test_instance_creation(self):
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)

    def test_str_representation(self):
        obj = Amenity()
        obj_str = str(obj)
        self.assertTrue("[Amenity]" in obj_str)
        self.assertTrue(obj.id in obj_str)

    def test_to_dict_method(self):
        obj = Amenity()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'Amenity')
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)

    def setUp(self):
        """Set up the testing environment"""
        pass

    def tearDown(self):
        """Tear down the testing environment"""
        pass

    def test_amenity_inherits_from_base_model(self):
        """Test if Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_has_name_attribute(self):
        """Test if Amenity has 'name' attribute"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertIsInstance(amenity.name, str)

    def test_amenity_name_can_be_set(self):
        """Test if Amenity 'name' can be set"""
        amenity = Amenity()
        amenity.name = "WiFi"
        self.assertEqual(amenity.name, "WiFi")

    def test_amenity_name_must_be_string(self):
        """Test if Amenity 'name' must be a string"""
        amenity = Amenity()
        with self.assertRaises(ValueError):
            amenity.name = 123

    def test_amenity_name_cannot_be_empty(self):
        """Test if Amenity 'name' cannot be an empty string"""
        amenity = Amenity()
        with self.assertRaises(ValueError):
            amenity.name = ""

    def test_amenity_has_place_amenity_relationship(self):
        """Test if Amenity has a relationship with PlaceAmenity"""
        self.assertTrue(hasattr(Amenity, 'place_amenities'))
        self.assertIsInstance(Amenity.place_amenities.property, relationship)

    def test_amenity_place_amenities_is_list(self):
        """Test if Amenity 'place_amenities' is a list"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'place_amenities'))
        self.assertIsInstance(amenity.place_amenities, InstrumentedList)

