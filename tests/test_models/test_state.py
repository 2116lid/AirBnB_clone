#!/usr/bin/python3
"""Test suite for the State class of the models.state module"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        """Set up method to create an instance of State for testing"""
        self.state = State()

    def test_attrib(self):
        """Test if the state instance has the expected attributes"""
        self.assertTrue(hasattr(self.state, "name"))

    def test_types(self):
        """Test if the attribute types of the state instance are as expected"""
        self.assertIsInstance(self.state.name, str)

    def test_initialization(self):
        """Test if the attributes are initialized as empty strings"""
        self.assertEqual(self.state.name, "")

    def test_state_subclass_basemodel(self):
        self.assertTrue(issubclass(type(self.state), BaseModel))
        

if __name__ == '__main__':
    unittest.main()
