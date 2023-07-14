#!/usr/bin/python3
"""
    This Script Initializes the Package
"""
from models.engine.file_storage import FileStorage
#Import the FileStorage class from file_storage.py

storage = FileStorage() #
storage.reload()

from models.user import User
from models.base_model import BaseModel
