#!/usr/bin/python3
"""class State that inherits from BaseModel"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        city_list = []
        from models import storage
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
