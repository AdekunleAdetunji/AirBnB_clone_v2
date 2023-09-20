#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state",
                          cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """gets all the cities that belong to the present state instance"""
        return [v for v in models.storage.all(City).values()
                if v.state_id == self.id]
