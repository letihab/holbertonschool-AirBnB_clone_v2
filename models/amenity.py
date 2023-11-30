#!/usr/bin/python3
""" State Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Attribute for amenity"""

    __tablename__ = 'amenities'
    id = Column(Integer, primary_key=True)

    name = Column(String(128), nullable=False)
    """places = relationship('Place', secondary='place_amenity_association',
                          back_populates='amenities')"""
