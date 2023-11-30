#!/usr/bin/python3
""" """


from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


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

    def test_id_format(self):
        """Test the format of the generated ID."""
        i = self.value()
        self.assertTrue(UUID(i.id, version=4))

    def test_created_at_before_save(self):
        """Test that created_at and updated_at are the same before calling
        save."""
        i = self.value()
        self.assertEqual(i.created_at, i.updated_at)

    def test_updated_at_after_save(self):
        """Test that updated_at changes after calling save."""
        i = self.value()
        original_updated_at = i.updated_at
        i.save()
        self.assertNotEqual(original_updated_at, i.updated_at)

    def test_delete_method(self):
        """Test the delete method."""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j_before_delete = json.load(f)
            self.assertTrue(key in j_before_delete)

        i.delete()

        with open('file.json', 'r') as f:
            j_after_delete = json.load(f)
            self.assertFalse(key in j_after_delete)

    def test_created_at_type(self):
        """Test the type of created_at attribute."""
        i = self.value()
        self.assertIsInstance(i.created_at, datetime.datetime)

    def test_updated_at_type(self):
        """Test the type of updated_at attribute."""
        i = self.value()
        self.assertIsInstance(i.updated_at, datetime.datetime)

    def test_to_dict_with_sa_instance_state(self):
        """Test to_dict method when _sa_instance_state is present."""
        i = self.value()
        i_dict = i.to_dict()
        self.assertNotIn('_sa_instance_state', i_dict)

    def test_from_dict_method(self):
        """Test the from_dict method."""
        data = {
            '__class__': 'BaseModel',
            'id': 'test_id',
            'created_at': '2023-11-01T12:00:00',
            'updated_at': '2023-11-01T12:30:00'
        }
        model = BaseModel.from_dict(data)
        self.assertIsInstance(model, BaseModel)
        self.assertEqual(model.id, 'test_id')
        self.assertEqual(model.created_at,
                         datetime.fromisoformat('2023-11-01T12:00:00'))
        self.assertEqual(model.updated_at,
                         datetime.fromisoformat('2023-11-01T12:30:00'))
