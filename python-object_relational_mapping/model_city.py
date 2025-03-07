#!/usr/bin/python3
"""Contains City class and imports Base"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Class representing cities table

    Attributes:
        id (int): city id, primary key
        name (str): city name, max 128 chars
        state_id (int): foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
