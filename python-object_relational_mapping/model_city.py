#!/usr/bin/python3
"""
    This script Contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class to represent a row in the cities table.

    Inherits from Base class which is declared in model_state.py
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
