#!/usr/bin/python3
"""This creates user profile"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This class would hold user info
    """
email = ""
password = ""
first_name = ""
last_name = ""

