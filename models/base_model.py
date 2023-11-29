#!/usr/bin/python3
"""Base console AirBnB"""


import uuid
from datetime import datetime
import models
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class BaseModel:
    """class BaseModel that defines all common attributes/methods
    for other classes"""

    def __init__(self, *args, **kwargs):
        """initializes an instance of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """prints a representation od the instance"""
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime"""

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of
        the instance"""

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        if obj_dict["_sa_instance_state"]:
            obj_dict.pop('_sa_instance_state', None)
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
                        setattr(instance, key, cls.parse_datetime(value))
                    elif key == "updated_at":
                        setattr(instance, key, cls.parse_datetime(value))
                    elif key != '__class__':
                        setattr(instance, key, value)
                return instance
            else:
                raise ValueError("Invalid '__class__' in the dictionary")
        else:
            raise ValueError("No '__class__' key found in the dictionary")

    def delete(self):
        """Delete the current instance from the file_storage."""
        models.file_storage.delete(self)
