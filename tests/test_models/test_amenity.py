#!/usr/bin/python3
""" """


from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.place import Place
from models.base_model import BaseModel
from models import storage
import os


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    #---OLD UNITTEST--#

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
