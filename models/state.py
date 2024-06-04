#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """getter for list of city instances related to the state"""
        city_list = []
        if models.storage_t == "db":
            all_cities = models.storage.all(City).values()
            for city in all_cities:
                if city.state_id == self.id:
                    city_list.append(city)
        else:
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
        return city_list

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """Returns a dictionary representation of the State instance"""
        dictionary = super().to_dict()
        dictionary["__class__"] = "State"
        dictionary["name"] = self.name
        return dictionary
