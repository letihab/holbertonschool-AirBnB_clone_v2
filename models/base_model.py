#!/usr/bin/python3
"""Base console AirBnB"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """class BaseModel that defines all common attributes/methods
    for other classes"""

    def __init__(self, *args, **kwargs):
        """initializes an instance of BaseModel"""
        if len(kwargs) < 1:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.id = kwargs.get("id", str(uuid.uuid4()))
            self.created_at = datetime.fromisoformat(kwargs.get("created_at"))
            self.updated_at = datetime.fromisoformat(kwargs.get("updated_at"))

        models.storage.new(self)

    def __str__(self):
        """prints a representation od the instance"""
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime"""

        self.updated_at = datetime.now()
        models.storage.save()
        models.storage.new(self)

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of
        the instance"""

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    @classmethod
    def from_dict(cls, obj_dict):
        """Create a new instance of the class and initialize it from the
        dictionary"""
        if '__class__' in obj_dict:
            class_name = obj_dict['__class__']
            if class_name == cls.__name__:
                instance = cls()
                for key, value in obj_dict.items():
                    if key == "id":
                        setattr(instance, key, value)
                    elif key == "created_at":
                        setattr(instance, key, datetime.fromisoformat(value))
                    elif key == "updated_at":
                        setattr(instance, key, datetime.fromisoformat(value))
                    elif key != '__class__':
                        setattr(instance, key, value)
                return instance
            else:
                raise ValueError("Invalid '__class__' in the dictionary")
        else:
            raise ValueError("No '__class__' key found in the dictionary")
