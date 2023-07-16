#!/usr/bin/env python3
import unittest
from models.amenity import Amenity
from datetime import datetime
import models
from time import sleep
import os
from models.base_model import BaseModel

class Test_Amenity_instantiates(unittest.TestCase):
    """Test for Amenity instantiation"""
    def test_no_arguments(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_if_in_storage(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_if_id_is_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_if_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_if_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_two_amenities(self):
        a = Amenity()
        b = Amenity()

        self.assertNotEqual(a.id, b.id)

class Test_amenity_to_dict(unittest.TestCase):
    """test for amenity dict"""
    def test_if_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))
    def test_if_to_dict_contains_correct_keys(self):
        a = Amenity()
        self.assertIn("id", a.to_dict())
        self.assertIn("created_at", a.to_dict())
        self.assertIn("updated_at", a.to_dict())
        self.assertIn("__class__", a.to_dict())

    def test_if_to_dict_contains_added_attributes(self):
        a = Amenity()
        a.middle_name = "Holberton"
        a.my_number = 98
        self.assertEqual("Holberton", a.middle_name)
        self.assertIn("my_number", a.to_dict())

    def test_if_to_dict_datetime_is_str(self):
        b = Amenity()
        a = b.to_dict()
        self.assertEqual(str, type(a["id"]))
        self.assertEqual(str, type(a["created_at"]))
        self.assertEqual(str, type(a["updated_at"]))

    def test_if_to_dict_output(self):
        d = datetime.today()
        a = Amenity()
        a.id = "123456"
        a.created_at = a.updated_at = d
        to_dict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': d.isoformat(),
            'updated_at': d.isoformat(),
        }
        self.assertDictEqual(a.to_dict(), to_dict)

    def test_if_contrast_to_dict_ddict(self):
        a = Amenity()
        self.assertNotEqual(a.to_dict(), a.__dict__)

class TestAmenity_save(unittest.TestCase):
    """Unittests Amenity for save."""

    @classmethod
    def setUp(self):
        try:

            os.rename("file.json", "tmp")
        except IOError:

            pass

    def tearDown(self):
        try:

            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_if_one_save(self):
        a = Amenity()
        sleep(0.05)
        first_updated_at = a.updated_at
        a.save()
        self.assertLess(first_updated_at, a.updated_at)

    def test_if_two_saves(self):
        a = Amenity()
        sleep(0.1)
        first_updated_at = a.updated_at
        a.save()
        second_updated_at = a.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.1)
        a.save()
        self.assertLess(second_updated_at, a.updated_at)

    def test_if_save_with_arg(self):
        a = Amenity()
        with self.assertRaises(TypeError):
            a.save(None)

    def test_if_save_updates_file(self):
        a = Amenity()
        a.save()
        amid = "Amenity." + a.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())

if __name__ == "__main__":
    unittest.main()
