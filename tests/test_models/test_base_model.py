#!/usr/bin/python3
""" """


from models.base_model import BaseModel
import unittest
import datetime
import json
import os
from models import storage
from unittest.mock import patch


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    #--New unittests--#
    """OLD"""

    def test_instance_creation(self):
        model = BaseModel()
        self.assertTrue(isinstance(model, BaseModel))
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_instance_with_args(self):
        data = {
            'id': 'test_id',
            'created_at': '2023-11-01T12:00:00',
            'updated_at': '2023-11-01T12:30:00'
        }
        model = BaseModel(**data)
        self.assertEqual(model.id, 'test_id')
        self.assertEqual(model.created_at, datetime.fromisoformat
                         ('2023-11-01T12:00:00'))
        self.assertEqual(model.updated_at, datetime.fromisoformat
                         ('2023-11-01T12:30:00'))

    def test_str_representation(self):
        model = BaseModel()
        self.assertIn('BaseModel', str(model))
        self.assertIn(model.id, str(model))

    def test_save_method(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict_method(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'],
                         model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         model.updated_at.isoformat())

    def test_from_dict_method(self):
        data = {
            '__class__': 'BaseModel',
            'id': 'test_id',
            'created_at': '2023-11-01T12:00:00',
            'updated_at': '2023-11-01T12:30:00'
        }
        model = BaseModel.from_dict(data)
        self.assertIsInstance(model, BaseModel)
        self.assertEqual(model.id, 'test_id')
        self.assertEqual(model.created_at, datetime.fromisoformat
                         ('2023-11-01T12:00:00'))
        self.assertEqual(model.updated_at, datetime.fromisoformat
                         ('2023-11-01T12:30:00'))

        """Tests Erwan & Nathalie"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.base_model = BaseModel()
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
        datetime_prev = self.base_model.updated_at
        self.base_model.save()
        self.assertGreater(self.base_model.updated_at, datetime_prev)
        self.assertTrue(os.path.exists("file.json"))

    def test_str_method(self):
        """Test case for str instance representation"""
        cls_name = str(self.base_model.__class__.__name__)
        obj_dict = str(self.base_model.__dict__)
        obj_str = "[{}] ({}) {}".format(cls_name, self.base_model.id, obj_dict)
        self.assertEqual(obj_str, self.base_model.__str__())

    def test_to_dict_method(self):
        """Test case for 'to_dict' method"""
        dict = {
            "id": self.base_model.id,
            "__class__": self.base_model.__class__.__name__,
            "created_at": self.base_model.created_at.isoformat(),
            "updated_at": self.base_model.updated_at.isoformat()
        }
        self.assertDictEqual(dict, self.base_model.to_dict())

    def setUp(self):
        """Set up the testing environment"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Tear down the testing environment"""
        storage.close()

    def test_base_model_inherits_from_sqlalchemy_base(self):
        """Test if BaseModel inherits from sqlalchemy Base"""
        self.assertTrue(issubclass(BaseModel, storage.Base))

    def test_base_model_has_id_attribute(self):
        """Test if BaseModel has 'id' attribute"""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertIsInstance(self.base_model.id, str)

    def test_base_model_has_created_at_attribute(self):
        """Test if BaseModel has 'created_at' attribute"""
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_base_model_has_updated_at_attribute(self):
        """Test if BaseModel has 'updated_at' attribute"""
        self.assertTrue(hasattr(self.base_model, 'updated_at'))
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_base_model_id_is_unique(self):
        """Test if BaseModel 'id' is unique for each instance"""
        new_base_model = BaseModel()
        self.assertNotEqual(self.base_model.id, new_base_model.id)

    def test_base_model_created_at_and_updated_at_are_datetime_objects(self):
        """Test if BaseModel 'created_at' and 'updated_at' are datetime
          objects"""
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_base_model_str_method(self):
        """Test if BaseModel has a '__str__' method"""
        self.assertTrue(hasattr(self.base_model, '__str__'))
        self.assertIsInstance(str(self.base_model), str)

    @patch('models.storage')
    def test_base_model_save_method(self, mock_storage):
        """Test if BaseModel has a 'save' method"""
        self.assertTrue(hasattr(self.base_model, 'save'))
        self.base_model.save()
        mock_storage.new.assert_called_once_with(self.base_model)
        mock_storage.save.assert_called_once()

    def test_base_model_to_dict_method(self):
        """Test if BaseModel has a 'to_dict' method"""
        self.assertTrue(hasattr(self.base_model, 'to_dict'))
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'],
                          self.base_model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                          self.base_model.updated_at.isoformat())

    @patch('models.storage')
    def test_base_model_delete_method(self, mock_storage):
        """Test if BaseModel has a 'delete' method"""
        self.assertTrue(hasattr(self.base_model, 'delete'))
        self.base_model.delete()
        mock_storage.delete.assert_called_once_with(self.base_model)

    """new"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """Test the default instance creation"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test instance creation with kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_str(self):
        """Test the str representation of the instance"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Test the to_dict method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test instance creation with kwargs containing None"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """Test the id attribute"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test the created_at attribute"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test the updated_at attribute"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    @patch('models.storage')
    def test_save_method(self, mock_storage):
        """Test the save method"""
        datetime_prev = new.updated_at
        new.save()
        mock_storage.new.assert_called_once_with(new)
        mock_storage.save.assert_called_once()

    def test_str_method(self):
        """Test the str instance representation"""
        cls_name = str(new.__class__.__name__)
        obj_dict = str(new.__dict__)
        obj_str = "[{}] ({}) {}".format(cls_name, new.id, obj_dict)
        self.assertEqual(obj_str, new.__str__())

    def test_to_dict_method(self):
        """Test the to_dict method"""
        dict = {
            "id": new.id,
            "__class__": new.__class__.__name__,
            "created_at": new.created_at.isoformat(),
            "updated_at": new.updated_at.isoformat()
        }
        self.assertDictEqual(dict, new.to_dict())

    def test_base_model_inherits_from_sqlalchemy_base(self):
        """Test if BaseModel inherits from sqlalchemy Base"""
        self.assertTrue(issubclass(BaseModel, storage.Base))

    def test_base_model_has_id_attribute(self):
        """Test if BaseModel has 'id' attribute"""
        self.assertTrue(hasattr(new, 'id'))
        self.assertIsInstance(new.id, str)

    def test_base_model_has_created_at_attribute(self):
        """Test if BaseModel has 'created_at' attribute"""
        self.assertTrue(hasattr(new, 'created_at'))
        self.assertIsInstance(new.created_at, datetime)

    def test_base_model_has_updated_at_attribute(self):
        """Test if BaseModel has 'updated_at' attribute"""
        self.assertTrue(hasattr(new, 'updated_at'))
        self.assertIsInstance(new.updated_at, datetime)

    def test_base_model_id_is_unique(self):
        """Test if BaseModel 'id' is unique for each instance"""
        new_base_model = BaseModel()
        self.assertNotEqual(new.id, new_base_model.id)

    def test_base_model_created_at_and_updated_at_are_datetime_objects(self):
        """Test if BaseModel 'created_at' and 'updated_at' are datetime
          objects"""
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)

    def test_base_model_str_method(self):
        """Test if BaseModel has a '__str__' method"""
        self.assertTrue(hasattr(new, '__str__'))
        self.assertIsInstance(str(new), str)

    @patch('models.storage')
    def test_base_model_save_method(self, mock_storage):
        """Test if BaseModel has a 'save' method"""
        self.assertTrue(hasattr(new, 'save'))
        new.save()
        mock_storage.new.assert_called_once_with(new)
        mock_storage.save.assert_called_once()

    @patch('models.storage')
    def test_save_method(self, mock_storage):
        """Test the save method"""
        new_instance = self.value()  # Utilisez self.value() pour créer une instance
        datetime_prev = new_instance.updated_at
        new_instance.save()
        mock_storage.new.assert_called_once_with(new_instance)
        mock_storage.save.assert_called_once()

    def test_str_method(self):
        """Test the str instance representation"""
        new_instance = self.value()
        cls_name = str(new_instance.__class__.__name__)
        obj_dict = str(new_instance.__dict__)
        obj_str = "[{}] ({}) {}".format(cls_name, new_instance.id, obj_dict)
        self.assertEqual(obj_str, new_instance.__str__())

    def test_to_dict_method(self):
        """Test the to_dict method"""
        new_instance = self.value()
        model_dict = new_instance.to_dict()
        dict_expected = {
            "id": new_instance.id,
            "__class__": new_instance.__class__.__name__,
            "created_at": new_instance.created_at.isoformat(),
            "updated_at": new_instance.updated_at.isoformat()
        }
        self.assertDictEqual(dict_expected, model_dict)

    @patch('models.storage')
    def test_base_model_save_method(self, mock_storage):
        """Test if BaseModel has a 'save' method"""
        new_instance = self.value()
        self.assertTrue(hasattr(new_instance, 'save'))
        new_instance.save()
        mock_storage.new.assert_called_once_with(new_instance)
        mock_storage.save.assert_called_once()

if __name__ == '__main__':
    unittest.main()
