#!/usr/bin/python3
"""
TestDBStorageDocs and TestDBStorage classes
and filestorage
"""
from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pycodestyle
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}
storage_t = os.getenv("HBNB_TYPE_STORAGE")


class TestDBStorage(unittest.TestCase):
    def setUp(self):
        """Initializes an instance of DBStorage"""
        self.db_storage = DBStorage()

    def tearDown(self):
        """Closes the DBStorage session"""
        self.db_storage.close()

    def test_initialization(self):
        """Test DBStorage initialization"""
        self.assertIsNotNone(self.db_storage._DBStorage__engine)
        self.assertIsNotNone(self.db_storage._DBStorage__session)

    def test_all_empty_database(self):
        """Test all() returns an empty dictionary for an empty database"""
        all_objects = self.db_storage.all()
        self.assertEqual(len(all_objects), 0)

    def test_all_objects_added(self):
        """Test all() returns all objects of a specific class"""
        user = User()
        self.db_storage.new(user)
        self.db_storage.save()
        all_users = self.db_storage.all(User)
        self.assertIn('User.{}'.format(user.id), all_users)

    def test_new(self):
        """Test new() adds a new object to the session"""
        state = State()
        self.db_storage.new(state)
        self.assertIn(state, self.db_storage._DBStorage__session.new)

class TestFileStorage(unittest.TestCase):
    """filestorage class"""
    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""