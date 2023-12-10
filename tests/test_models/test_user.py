"""Test suite for the User class in models.user"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases against the User class"""

    def setUp(self):
        """Set up for the tests"""
        self.user = User()

    def test_initialization(self):
        """Tests for initialization"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_type(self):
        """Tests for the type of the attributes"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_user_is_subclass_basemodel(self):
        u = User()
        self.assertTrue(issubclass(type(u), BaseModel))
