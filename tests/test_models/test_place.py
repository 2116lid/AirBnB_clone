#!/usr/bin/python3
"""Test suite for the Place class of models.place"""
import unittest

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases against the Place class"""

    def setUp(self):
        """Set up for the tests"""
        self.place = Place()

    def test_initialization(self):
        """Tests for initialization"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_type(self):
        """Tests for the type of the attributes"""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_place_subclass_basemodel(self):
        self.assertTrue(issubclass(type(self.place), BaseModel))

if __name__ == '__main__':
    unittest.main()
