#!/usr/bin/python3
"""This Script runs the FileStorage """

#Import The Required Modules
import json
import datetime

class FileStorage:
    """ This Class handles Serialization and 
        Deserialization of objects to JSON stings
        and vice versa
    """

    __file_path = "file.json" #Path to the json file
    __objects = {} #Empty Dictionary to store Objs

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
        my_key = "{}.{}".format(type(obj), __name__, obj.id) #Creat the key
        FileStorage.__objects[my_key] = obj #Add the key to the __objects dictionary

    def save(self):
        """ The Method Serializes __objects to the Specified json file path
        """
        