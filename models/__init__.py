#!/usr/bin/python3
""" Create a new instance """

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Storage
# =================================================== #

storage = FileStorage()
storage.reload()

# Models classes
# =================================================== #

classes = [
    "BaseModel",
    "User",
    "State",
    "Place",
    "City",
    "Amenity",
    "Review"
]

# Attributs types
# =================================================== #

int_attrs = [
    "number_rooms",
    "number_bathrooms",
    "max_guest",
    "price_by_night"
]

float_attrs = [
    "latitude",
    "longitude"
]
