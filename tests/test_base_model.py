#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
from datetime import datetime
import models

class TestBaseModel_instantiation(unittest.TestCase):
    def test_if_args_no_args_instatiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_if_id_is_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_datetme(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_if_BaseModel_in_storage(self):
        self.assertIn(BaseModel(), models.storage.all().values())

if __name__ == "__main__":
    unittest.main()
