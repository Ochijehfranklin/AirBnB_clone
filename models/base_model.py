#!/usr/bin/python3
"""This file defines the BaseModel"""

from datetime import datetime
import uuid


class BaseModel:
    """This is the BaseModel Class"""
    def __init__(self, *args, **kwargs):

        """
        This would initialize basemodel

        Args:

        args (tuple): args passesd to self
        kwargs (dictionary): key, value pai of information
        """

        timeFormat = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "updated_at" or key == "created_at":
                    setattr(self, key, datetime.strptime(value, timeFormat))
                else:
                    setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())

        
    
    def save(self):
        """This updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now() 
    
    def __str__(self):
        """
        return the str representation in a specific format
        """
        className = self.__class__.__name__
        return f"[{className}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
        returns the dictionary conatining all key value of the instance
        """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__   
        dic["updated_at"] = self.updated_at.isoformat()
        dic["created_at"] = self.created_at.isoformat()
        
        return dic
