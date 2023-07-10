#!/usr/bin/env python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, my_number=None, name=None):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.my_number = my_number
        self.name = name

    def __str__(self):
        return "[{}] ({}) {{'my_number': {}, 'name': {}, 'updated_at': {}, 'id': '{}', 'created_at': {}}}".format(
                self.__class__.__name__,
                self.id,
                self.my_number,
                self.name,
                self.updated_at,
                self.id,
                self.created_at
                )

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        data = {
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
        if self.my_number is not None:
            data['my_number'] = self.my_number
        if self.name is not None:
            data['name'] = self.name
        return data

