#!/usr/bin/python3
""" State Module for HBNB project """
import models
import os
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """
        Getter attribute cities that returns the list of City
        instances with state_id equals to the current
        """
        cities = models.storage.all(City)
        if os.getenv("HBNB_TYPE_STORAGE") == "db":
            return [city for city in cities.values()
                    if city.state_id == self.id]
        else:
            return [city for city in cities.values()
                    if city.state_id == self.id]
