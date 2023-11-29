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

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
            del kwargs["__class__"]
            self.__dict__.update(kwargs)

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
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({"__class__":
                          (str(type(self)).split(".")[-1]).split("'")[0]})
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary.keys():
            dictionary.pop("_sa_instance_state")
        return dictionary

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
