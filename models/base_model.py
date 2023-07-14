#!/usr/bin/env python3
""" the base model class"""


import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage
""" nd"""


class BaseModel:
    """
    Base class for other models.
    """
    def __init__(self, *args, my_number=None, name=None, **kwargs):
        """
        Initializes a new instance of the BaseModel.

        Args:
            my_number (int): The number associated with the instance.
            name (str): The name associated with the instance.
            *args: List of arguments
            **kwargs: Dictionary of Key-Value Arguments
        """
        if kwargs: #If kwargs is not empty
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")


                setattr(self, key, value)
            created_at = kwargs.get("created_at")
            updated_at = kwargs.get("updated_at")

            if created_at:
                self.created_at = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.now()
            if updated_at:
                self.updated_at = datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.now()
        else: #if kwargs is empty
            self.my_number = my_number
            self.name = name
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel.

        Returns:
            str: The string representation of the BaseModel.
        """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel.

        Returns:
            dict: A dictionary containing all\
                    keys/values of the BaseModel instance.
        """
        data = {
            '__class__': self.__class__.__name__,
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
        try:
            if self.my_number is not None:
                data['my_number'] = self.my_number
            if self.name is not None:
                data['name'] = self.name
        except Exception:
            pass
        return data
