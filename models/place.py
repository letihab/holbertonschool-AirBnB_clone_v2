#!/usr/bin/python3
""" Place Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.amenity import Amenity


# Définir la table d'association pour la relation many-to-many
place_amenity_association = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', Integer, ForeignKey('amenities.id'), primary_key=True))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    id = Column(String(60), primary_key=True, nullable=False)

    city_id = Column(String(60), ForeignKey('cities_id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users_id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    user = relationship('User', back_populates='places')

    # For DBStorage
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        amenity_ids = []
        amenities = relationship('Amenity', secondary=place_amenity_association,
                                 back_populates='places', viewonly=False)

    # For FileStorage
    else:
        amenity_ids = []

        @property
        def amenities(self):
            """Getter attribute for amenities in FileStorage"""

            from models import storage
            amenity_instances = []
            for amenity_id in self.amenity_ids:
                amenity = storage.get('Amenity', amenity_id)
                if amenity:
                    amenity_instances.append(amenity)
            return amenity_instances

        @amenities.setter
        def amenities(self, amenity_obj):
            """Setter attribute for amenities in FileStorage"""

            if isinstance(amenity_obj, Amenity):
                self.amenity_ids.append(amenity_obj.id)
                self.save()
