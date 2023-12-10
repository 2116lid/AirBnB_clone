#!/usr/bin/python3
"""Test suite for Amenity class of the models.amenity module"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up for the tests"""
        self.amenity = Amenity()

    def test_initialization(self):
        """Tests for initialization"""
        self.assertEqual(self.amenity.name, "")

    def test_type_attrib(self):
        """Tests for the type of the attributes"""
        self.assertIsInstance(self.amenity.name, str)

    def test_amenity_subclass_basemodel(self):
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

if __name__ == '__main__':
    unittest.main()
