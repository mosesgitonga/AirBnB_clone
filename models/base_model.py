#!/usr/bin/env python3
""" the base model class"""


import uuid
from datetime import datetime
""" nd"""


class BaseModel:
    """
    Base class for other models.
    """
    def __init__(self, my_number=None, name=None):
        """
        Initializes a new instance of the BaseModel.

        Args:
            my_number (int): The number associated with the instance.
            name (str): The name associated with the instance.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.my_number = my_number
        self.name = name

    def __str__(self):
        """
        Returns a string representation of the BaseModel.

        Returns:
            str: The string representation of the BaseModel.
        """
        return "[{}] ({}) {{'my_number': {}, 'name': {}, 'updat\
ed_at': {}, 'id': '{}', 'created_at': {}}}".format(
            self.__class__.__name__,
            self.id,
            self.my_number,
            self.name,
            self.updated_at.strftime("%Y, %m, %d, %H, %M, %S, %f"),
            self.id,
            self.created_at.strftime("%Y, %m, %d, %H, %M, %S, %f")
        )

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime.
        """
        self.updated_at = datetime.now()

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
        if self.my_number is not None:
            data['my_number'] = self.my_number
        if self.name is not None:
            data['name'] = self.name
        return data
