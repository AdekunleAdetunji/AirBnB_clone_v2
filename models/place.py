#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


place_amenity = Table('place_amenity', Base.metadata,
                      Column("place_id", String(60), ForeignKey(
                          "places.id"), primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity", backref="place_amenities",
                                 secondary=place_amenity, viewonly=False)

        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
    else:
        @property
        def reviews(self):
            "getter for reviews when using file storage"
            all = models.storage.all(Review)
            return [v for v in all.values() if v.place_id == self.id]

        @property
        def amenities(self):
            """getter for amenities in file storage"""
            all = models.storage.all(Amenity)
            return [v for v in all.values() if v.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """adds amenities to a place in file storage mode"""
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append[obj.id]
