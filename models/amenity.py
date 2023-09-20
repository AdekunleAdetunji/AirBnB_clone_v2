#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Class representing amenities"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenity = relationship(
        "Place", secondary="place_amenity", backref="place_amenity")
