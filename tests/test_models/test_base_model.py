#!/usr/bin/python3
"""
This Script defines unittests for models/base_model.py
"""

""" Import the Required Modules """
import unittest
import models
import os
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

""" Tests for BaseModel Instatiation """

class TestBaseModel_Instatiation(unittest.TestCase):
    """ Class to run test methods """

    def test_no_arguments(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_store_instance(self):
        """Verify if an instance is stored"""
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_check_type_id(self):
        """Checks if the ID of an instance is a str type"""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_attr_type(self):
        """Checks type of attr created_at if datetime"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_Each_id_unique(self):
        """ Verify that two instances have unique ids """
        my_instance_1 = BaseModel()
        my_instance_2 = BaseModel()
        self.assertNotEqual(my_instance_1.id, my_instance_2.id)

    def test_Unique_created_at_attr(self):
        """ Verify that each instance has a different created_at value """
        my_instance_1 = BaseModel()
        sleep(0.06)
        my_instance_2 = BaseModel()
        self.assertLess(my_instance_1.created_at, my_instance_2.created_at)

    def test_is_updated_at_attr_unique(self):
        """Verify that each instance has a unique updated at attr"""
        my_instance_1 = BaseModel()
        sleep(0.06)
        my_instance_2 = BaseModel()
        self.assert(my_instance_1.updated_at, my_instance_2.updated_at)

    def test_the_str_rep(self):
        """Verifies the string representation of an instance"""
        current_datetime = datetime.today()
        current_datetime_rep = repr(current_datetime)
        my_instance_1 = BaseModel()
        my_instance_1.id = "123456"
        my_instance_1.created_at = my_instance_1.updated_at = current_datetime
        my_instance_1_str = my_instance_1.__str__()
        self.assertIn("[BaseModel] (123456)", my_instance_1_str)
        self.assertIn("'id': '123456'", my_instance_1_str)
        self.assertIn("'created_at': ", + current_datetime_rep, my_instance_1_str)
        self.assertIn("'updated_at': ", + current_datetime_rep, my_instance_1_str)

    def test_Single_arg_set_to_none(self):
        """ Ensures the instance does not Store the None attribute """
        my_instance = BaseModel(None)
        self.assertNotIn(None, my_instance.__dict__.values())

    def test_instance_with_kwargs(self):
        """ Ensure the Instance has the right keyworded arg """
        current_datetime = datetime.today()
        current_datetime_iso = current_datetime.isoformat()
        my_instance = BaseModel(id="345", created_at=current_datetime_iso, updated_at=current_datetime_iso)
        self.assertEqual(my_instance.id, "345")
        self.assertEqual(my_instance.created_at, current_datetime)
        self.assertEqual(my_instance.updated_at, current_datetime)

    def test_instance_with_no_kwargs(self):
        """Tests the case when the args are set to none"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instance_with_both_arg_and_kwargs(self):
        """ Test the case when an instance has both positional and keyword arguments """
        current_datetime = datetime.today()
        current_datetime_iso = current_datetime.isoformat()
        myInstance = BaseModel("12", id="345", created_at=current_datetime_iso, updated_at=current_datetime_iso)
        self.assertEqual(myInstance.id)
        self.assertEqual(myInstance.created_at, current_datetime)
        self.assertEqual(myInstance.updated_at, current_datetime

class TestBaseModel_SaveMethod(unittest.TestCase):
    """ The Class Runs tests for the Save Method in models/base_model.py """

    @classmethod
    def set_up_environment(self):
        """sets up the Environment for Testing """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def cleanUp_environment(self):
        """Runs after running Tests.
            Purpose:
                Ensure Testing Environment is clean
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_Save_method_when_called(self)
        """ Ensure The save method updates the updated_at attribute """
        my_instance = BaseModel()
        sleep(0.05)
        first_update = my_instance.updated_at
        my_instance.save()
        self.assertLess(first_update, my_instance.updated_at)

    def test_save_method_when_called_multiple_times(self):
        """Test the save method when called multiple times"""
        my_instance = BaseModel()
        sleep(0.05)
        first_update = my_instance.updated_at
        my_instance.save()
        second_update = my_instance.updated_at
        self.assertLess(first_update, second_update)
        sleep(0.05)
        my_instance.save()
        self.assertLess(second_update, my_instance.updated_at)

    def test_updated_files(self):
        """To Ensure the save method updates the JSON file"""
        myInstance = BaseModel()
        with self.assertRaises(TypeError):
            myInstance.save(None)

    def test_save_updated_files(self):
        myInstance = BaseModel()
        myInstance.save()
        myInstance_id = "BaseModel." + myInstance.id
        with open("file.json", "r") as myfile:
            self.assertIn(myInstance_id, myfile.read())
