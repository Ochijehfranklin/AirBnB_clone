#!/usr/bin/python3
"""
This would holdmy FileStorage class
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
    This would store, serialize and deserialize data
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the __objects dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        This sets new objects in the __objects dictionary with
        k value = <obj class name>.id
        """
        objClassName = obj.__class__.__name__
        key = f"{objClassName}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        This serializes the objects dictionary to
        JSON format and saves it to file
        """

        all_objs = FileStorage.__objects

        obj_dic = {}

        for obj in all_objs.keys():
            obj_dic[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dic, file)

    def reload(self):
        """
        This would deserialize the JSON file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dic = json.load(file)

                    for key, value in obj_dic.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
