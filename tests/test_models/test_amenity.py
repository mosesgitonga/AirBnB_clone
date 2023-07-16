#!/usr/bin/env python3
import unittest
from models.amenity import Amenity
from datetime import datetime
import models


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
    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))


if __name__ == "__main__":
    unittest.main()
