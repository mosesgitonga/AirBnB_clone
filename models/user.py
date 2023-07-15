#!/usr/bin/env python3
"""creates module class"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class User(BaseModel):
    """manage user objects"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
