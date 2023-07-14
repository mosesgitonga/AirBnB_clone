#!/usr/bin/env python3
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
class User(BaseModel):
    def __init__(self):
        super().__init__(*args, **kwargs)
        self.email = kwargs.get("email", '')
        self.password = kwargs.get("password", '')
        self.first_name = kwargs.get("first_name", '')
        self.last_name = kwwargs.get("last_name", '')

