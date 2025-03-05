#!/usr/bin/python3
"""Contains the class definition of City"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """City class that inherits from Base
    Attributes:
        id (int): The city id
        name (str): The city name
        state_id (int): Foreign Key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)