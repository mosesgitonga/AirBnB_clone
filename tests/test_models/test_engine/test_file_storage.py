#!/usr/bin/python3
"""
This Script runs several testcases for models/engine/file_storage.py using the unittest framework

Test cases are divided into 2 classes:
    - TestFileStorsge_Instances
    - TestFileStorage_Methods
"""

""" Import the Required Modules for proper functionaliy """

import unittest
import json
import os
import models
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.state import State

""" Unittests """

class TestFileStorage_Instances(unittest.TestCase):
    """ This Class runs tests that cater for FileStorage
    instances.
    """

    def test_create_instance_with_args(self):
        """ The goal is to ensure that the constructor
        correctly handles the arguments
        """
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_create_instance_with_NO_args(self):
        """Verify that an instance can be created without
        passing arguments
        """
        my_instance = FileStorage()
        self.assertEqual(type(my_instance), FileStorage)

    def test_check_file_path_status(self):
        """ This Method Checks if __file_path is private
        and whether it is a string type.
        """
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_check_objects_status(self):
        """ This Method checks if the __objects attribute
        is a private dictionary
        """
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_check_instance_status(self):
        """ This Method confirms that models.storage object
        is cirrectly instantiated as an instance of the
        FileStorage class
        """
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_Methods(unittest.TestCase):
    """This Subclass of unittest.TestCase runs tests that
    cater for FileStorage Methods
    """

    @classmethod
    def set_up_environment(self):
        """ The method is used to perform any necessary
        setup or initialization steps before running each
        test case
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def clean_up_environmets(self):
        """ The method is responsible for cleaning up any
        temporary changes made during the test case
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        """The purpose of this test is to verify that the
        models.storage.all() method returns a dictionary
        object.
        """
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_method_with_args(self):
        """ The purpose of this test is to ensure that the 
        models.storage.all() method does not accept any
        arguments. By passing None as an argument to th
        method, the test expects a TypeError to be raised
        """
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_method(self):
        """The purpose of this test is to verify that the 
        models.storage.new() method correctly adds object
        to the file storage and that they can be retrieved
        using models.storage.all()
        """
        bm = BaseModel()
        usr = User()
        st = State()
        pl = Place()
        amn = Amenity()
        rv = Review()
        cty = City()

        models.storage.new(bm)
        models.storage.new(usr)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(amn)
        models.storage.new(rv)
        models.storage.new(cty)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + usr.id, models.storage.all().keys())
        self.assertIn(usr, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + cty.id, models.storage.all().keys())
        self.assertIn(cty, models.storage.all().values())
        self.assertIn("Amenity." + amn.id, models.storage.all().keys())
        self.assertIn(amn, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())


    def test_new_method_with_args(self):
        """The purpose of this test is to ensure that the 
        models.storage.new() method does not accept an
        additional arguments beyond the object to be stored
        """
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_method_with_None(self):
        """The purpose of this test is to ensure that the
        models.storage.new() method does not accept None
        as an argument. 

        By passing None as an argument to the method, 
        the test expects an AttributeError to be raise
        """
        with self.assertRaises(AttributeError):
            models.storage.new(None)

if __name__ == "__main__":
    unittest.main()
