#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""


import json
from models.user import User
from models.city import City
from models.state import State


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            filtered_objects = {k: v for k, v in FileStorage.__objects.items()
                                if isinstance(v, cls)}
        return filtered_objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete object"""
        if obj is not None:
            key = "{}.{}".format(obj.to_dict()['__class__'], obj.id)
            if key in self.__objects:
                self.__objects.pop(key, None)

    def close(self):
        """update object"""
        self.reload()

    #--New unittests--#

    def test_all_with_class_filter(self):
        """Test all method with class filter"""
        new_user = User()
        new_city = City()
        new_state = State()
        self.storage.new(new_user)
        self.storage.new(new_city)
        self.storage.new(new_state)

        filtered_objects_user = self.storage.all(cls=User)
        self.assertEqual(len(filtered_objects_user), 1)
        self.assertIn("User.{}".format(new_user.id), filtered_objects_user)

        filtered_objects_city = self.storage.all(cls=City)
        self.assertEqual(len(filtered_objects_city), 1)
        self.assertIn("City.{}".format(new_city.id), filtered_objects_city)

        filtered_objects_state = self.storage.all(cls=State)
        self.assertEqual(len(filtered_objects_state), 1)
        self.assertIn("State.{}".format(new_state.id), filtered_objects_state)

    def test_new(self):
        """Test new method"""
        new_user = User()
        self.storage.new(new_user)
        key = "User.{}".format(new_user.id)
        self.assertIn(key, self.storage.all())

    def test_save_reload(self):
        """Test save and reload methods"""
        new_user = User()
        self.storage.new(new_user)
        self.storage.save()

        loaded_storage = FileStorage()
        loaded_storage.reload()

        key = "User.{}".format(new_user.id)
        self.assertEqual(loaded_storage.all()[key].to_dict(),
                         new_user.to_dict())

    def test_delete(self):
        """Test delete method"""
        new_user = User()
        self.storage.new(new_user)
        key = "User.{}".format(new_user.id)
        self.assertIn(key, self.storage.all())

        self.storage.delete(new_user)
        self.assertNotIn(key, self.storage.all())

    def test_delete_nonexistent(self):
        """Test delete method with nonexistent object"""
        new_user = User()
        key = "User.{}".format(new_user.id)
        self.assertNotIn(key, self.storage.all())

        self.storage.delete(new_user)
        self.assertNotIn(key, self.storage.all())

    def test_close(self):
        """Test close method"""
        self.storage.close()
        self.assertEqual(len(self.storage.all()), 0)

        # Confirm reloading after close
        loaded_storage = FileStorage()
        loaded_storage.reload()
        self.assertEqual(len(loaded_storage.all()), 0)
