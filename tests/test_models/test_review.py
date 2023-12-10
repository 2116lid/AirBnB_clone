#!/usr/bin/python3
"""Test suite for Review class in models.review"""
import unittest

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def setUp(self):
        """Set up method to create an instance of Review for testing"""
        self.review = Review()

    def test_review_subclass_basemodel(self):
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_attributes(self):
        """Test if the review instance has the expected attributes"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_a_types(self):
        """Test if the attribute types of review instance are as expected"""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_attrib_initialization(self):
        """Test if the attributes are initialized as empty strings"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")


if __name__ == '__main__':
    unittest.main()
