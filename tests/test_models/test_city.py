#!/usr/bin/python3
"""Test suite for the City class of the models.city module"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up for the tests"""
        self.city = City()

    def test_initialization(self):
        """Tests for initialization"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_type_attrib(self):
        """Tests for the type of the attributes"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_city_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.city), BaseModel))

if __name__ == '__main__':
    unittest.main()
