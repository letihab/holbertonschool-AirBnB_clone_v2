#!/usr/bin/python3
"""class State that inherits from BaseModel"""


from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import os
from sqlalchemy.orm import relationship
from city import City


Base = declarative_base()


class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

# Relationship for DBStorage
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")

    # Getter attribute for FileStorage
    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def cities(self):
            from models import storage
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
