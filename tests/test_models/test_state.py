#!/usr/bin/python3
"""Test for class State"""


import unittest
from models.state import State
from models.base_model import BaseModel
from models import storage
import os


class TestState(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
