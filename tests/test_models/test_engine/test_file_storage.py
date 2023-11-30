#!/usr/bin/python3
""" Module for testing file storage"""


import unittest
from models.base_model import BaseModel
from models import storage
import os

from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)

    #---ADD OLD UNITTEST--#

    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        new_user = User()
        self.storage.new(new_user)
        key = "User.{}".format(new_user.id)
        self.assertEqual(self.storage.all()[key], new_user)

    def test_save_reload(self):
        new_user = User()
        self.storage.new(new_user)
        self.storage.save()
        loaded_storage = FileStorage()
        loaded_storage.reload()
        key = "User.{}".format(new_user.id)
        self.assertEqual(loaded_storage.all()[key].to_dict(),
                         new_user.to_dict())

    def tearDown(self):
            try:
                os.remove(FileStorage._FileStorage__file_path)
            except:
                pass

    def delete(self, obj=None):
        """Deletes an object from storage if it exists"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()

    def test_load_multiple_classes(self):
        new_user = User()
        new_city = City()
        new_state = State()
        self.storage.new(new_user)
        self.storage.new(new_city)
        self.storage.new(new_state)
        self.storage.save()
        loaded_storage = FileStorage()
        loaded_storage.reload()
        key_user = "User.{}".format(new_user.id)
        key_city = "City.{}".format(new_city.id)
        key_state = "State.{}".format(new_state.id)
        self.assertEqual(loaded_storage.all()[key_user].to_dict(),
                         new_user.to_dict())
        self.assertEqual(loaded_storage.all()[key_city].to_dict(),
                         new_city.to_dict())
        self.assertEqual(loaded_storage.all()[key_state].to_dict(),
                         new_state.to_dict())

    def test_load_empty_file(self):
        self.storage.save()
        loaded_storage = FileStorage()
        loaded_storage.reload()
        self.assertEqual(len(loaded_storage.all()), len(self.storage.all()))

    def test_load_non_existent_file(self):
        self.storage._FileStorage__file_path = "non_existent_file.json"
        loaded_storage = FileStorage()
        loaded_storage.reload()
        self.assertEqual(len(loaded_storage.all()), len(self.storage.all()))

    def test_save_custom_file_path(self):
        self.storage._FileStorage__file_path = "custom_file.json"
        new_user = User()
        self.storage.new(new_user)
        self.storage.save()
        loaded_storage = FileStorage()
        loaded_storage._FileStorage__file_path = "custom_file.json"
        loaded_storage.reload()
        key = "User.{}".format(new_user.id)
        self.assertEqual(loaded_storage.all()[key].to_dict(),
                         new_user.to_dict())

    def test_duplicate_object_creation(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    """Test Erwan & Nathalie"""

    def test_save(self):
        """Test case for 'save' method"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload(self):
        """Test case for 'reload' method"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage._FileStorage__objects.clear()
        self.storage.reload()
        key = model.__class__.__name__ + "." + model.id
        self.assertIn(key, self.storage.all())

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.storage = FileStorage()
        try:
            os.rename(FileStorage._FileStorage__file_path,
                        "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """Class method to close test's environment"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
            os.rename("test_file.json", FileStorage._FileStorage__file_path)
        except Exception:
            pass

    def test_all(self):
        """Test case for 'all' method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test case for 'new' method"""
        model = BaseModel()
        self.storage.new(model)
        key = model.__class__.__name__ + "." + model.id
        self.assertIn(key, self.storage.all())
