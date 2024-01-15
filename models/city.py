#!/usr/bin/python3
""" City State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent the State class

    Attributes:
        state_id (str): The state id
        name (str): The name of the city
    """
    state_id = ""
    name = ""
