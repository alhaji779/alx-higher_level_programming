#!/usr/bin/python3
""" code to create a new class(table) via orm
"""
from sys import argv
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base, State


class City(Base):
    """ City table
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
