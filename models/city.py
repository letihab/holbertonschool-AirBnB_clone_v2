#!/usr/bin/python3
"""class City that inherits from BaseModel"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Class city"""
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id', ondelete="CASCADE")
                      , nullable=False)
