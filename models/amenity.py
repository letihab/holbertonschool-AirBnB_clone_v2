#!/usr/bin/python3
""" amenity class"""


from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)