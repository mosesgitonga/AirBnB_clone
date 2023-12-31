#!/usr/bin/python3
"""This Script runs the FileStorage """


import json
import datetime
import os


class FileStorage:
    """ This Class handles Serialization and
        Deserialization of objects to JSON stings
        and vice versa
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ This Method returns the __objects dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """ The Method sets obj from __objects with a key

            The Method contructs the key by combinig the
            class name of the object with the object's id
            (<obj class name>.id)
        """
        my_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[my_key] = obj

    def save(self):
        """ The Method Serializes __objects to the Specified json file path
        """
        o = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8')as file:
            json.dump(o, file)

    def reload(self):
        """reloads stored objects in file.json"""

        """ Deserializes the json file """
        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r', encoding='utf-8') as myfile:
            obj_dict = json.load(myfile)
            obj_dict = {
                    k: self.classes()[v["__class__"]](**v)
                    for k, v in obj_dict.items()
                    }

            FileStorage.__objects = obj_dict

    @classmethod
    def classes(cls):
        """This method returns a dictionary of available classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.review import Review
        return {
                "BaseModel": BaseModel,
                "User": User,
                "City": City,
                "Place": Place,
                "State": State,
                "Review": Review,
                "Amenity": Amenity
                }
