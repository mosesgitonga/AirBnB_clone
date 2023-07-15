#!/usr/bin/python3
"""
    This Script Initializes the Package
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
