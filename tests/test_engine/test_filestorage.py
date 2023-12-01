#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import os
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        # Nettoyage de la mémoire partagée
        storage._FileStorage__objects = {}
        # Suppression du fichier de stockage s'il existe
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up storage file after tests"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_all_empty(self):
        """Test if __objects is initially empty"""
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """Test if new object is added to __objects"""
        new_obj = BaseModel()
        self.assertIn('BaseModel.' + new_obj.id, storage.all())

    def test_save(self):
        """Test if objects are saved to file"""
        new_obj = BaseModel()
        storage.save()
        with open("file.json", "r") as file:
            data = file.read()
            self.assertTrue(len(data) > 0)
            self.assertIn('BaseModel.' + new_obj.id, data)

    def test_reload(self):
        """Test if objects are loaded from file"""
        new_obj = BaseModel()
        storage.save()
        storage._FileStorage__objects = {}
        storage.reload()
        self.assertIn('BaseModel.' + new_obj.id, storage.all())

    def test_delete(self):
        """Test if object is deleted from __objects"""
        new_obj = BaseModel()
        storage.delete(new_obj)
        self.assertNotIn('BaseModel.' + new_obj.id, storage.all())

    def test_close(self):
        """Test if close method closes the session"""
        storage.close()
        with self.assertRaises(AttributeError):
            storage.reload()

    def test_instance_type(self):
        """Test if storage instance is of FileStorage"""
        self.assertIsInstance(storage, storage.FileStorage)


if __name__ == '__main__':
    unittest.main()
