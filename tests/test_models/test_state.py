#!/usr/bin/python3
""" State unittests """


from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models.city import City
from models.base_model import BaseModel
from models import storage
import os
from unittest.mock import patch


class test_state(test_basemodel):
    """ State unittests """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    #--New unittests--#
    """OLD"""

    def test_state_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_state_in_storage(self):
        state = State()
        storage.save()
        key = "State.{}".format(state.id)
        self.assertEqual(key in storage.all(), True)

    def test_state_set_and_get_name(self):
        state = State()
        state.name = "laval"
        self.assertEqual(state.name, "laval")
        state.name = "paris"
        self.assertEqual(state.name, "paris")

    def test_review_inherits_from(self):
        self.assertTrue(issubclass(State, BaseModel))

    """Tests Erwan & Nathalie"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.state = State()
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
        datetime_prev = self.state.updated_at
        self.state.save()
        self.assertGreater(self.state.updated_at, datetime_prev)
        self.assertTrue(os.path.exists("file.json"))

    def test_str_method(self):
        """Test case for str instance representation"""
        cls_name = str(self.state.__class__.__name__)
        obj_dict = str(self.state.__dict__)
        obj_str = "[{}] ({}) {}".format(cls_name, self.state.id, obj_dict)
        self.assertEqual(obj_str, self.state.__str__())

    def test_to_dict_method(self):
        """Test case for 'to_dict' method"""
        dict = {
            "id": self.state.id,
            "__class__": self.state.__class__.__name__,
            "created_at": self.state.created_at.isoformat(),
            "updated_at": self.state.updated_at.isoformat()
        }
        self.assertDictEqual(dict, self.state.to_dict())

    def test_instance_creation(self):
        obj = State()
        self.assertIsInstance(obj, State)

    def test_str_representation(self):
        obj = State()
        obj_str = str(obj)
        self.assertTrue("[State]" in obj_str)
        self.assertTrue(obj.id in obj_str)

    def test_to_dict_method(self):
        obj = State()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'State')
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)

    def setUp(self):
        """Set up the testing environment"""
        self.state = State()

    def tearDown(self):
        """Tear down the testing environment"""
        storage.close()

    def test_state_inherits_from_base_model(self):
        """Test if State inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_has_name_attribute(self):
        """Test if State has 'name' attribute"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertIsInstance(self.state.name, str)

    @patch('models.storage')
    def test_state_save_method(self, mock_storage):
        """Test if State has a 'save' method"""
        self.assertTrue(hasattr(self.state, 'save'))
        self.state.save()
        mock_storage.new.assert_called_once_with(self.state)
        mock_storage.save.assert_called_once()

    @patch('models.storage')
    def test_state_delete_method(self, mock_storage):
        """Test if State has a 'delete' method"""
        self.assertTrue(hasattr(self.state, 'delete'))
        self.state.delete()
        mock_storage.delete.assert_called_once_with(self.state)

    @patch('models.storage')
    def test_state_cities_property(self, mock_storage):
        """Test State 'cities' property"""
        state_cities = self.state.cities
        self.assertIsInstance(state_cities, list)

    @patch('models.storage')
    def test_state_cities_property_with_cities(self, mock_storage):
        """Test State 'cities' property with existing cities"""
        with patch.dict(storage.all(City), {'city1': City(state_id=self.state.id),
                                           'city2': City(state_id=self.state.id)}):
            state_cities = self.state.cities
            self.assertEqual(len(state_cities), 2)
            self.assertIsInstance(state_cities[0], City)
            self.assertIsInstance(state_cities[1], City)

    @patch('models.storage')
    def test_state_cities_property_empty_list(self, mock_storage):
        """Test State 'cities' property with an empty list"""
        state_cities = self.state.cities
        self.assertEqual(state_cities, [])
