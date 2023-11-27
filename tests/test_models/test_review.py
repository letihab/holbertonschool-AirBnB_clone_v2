#!/usr/bin/python3
"""Test for class Review"""


import unittest
from models.review import Review
from models.base_model import BaseModel
from models import storage
import os


class TestReview(unittest.TestCase):
    def test_review_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_in_storage(self):
        review = Review()
        storage.save()
        key = "Review.{}".format(review.id)
        self.assertEqual(key in storage.all(), True)

    def test_review_set_and_get_name(self):
        review = Review()
        review.text = "laval"
        self.assertEqual(review.text, "laval")
        review.text = "paris"
        self.assertEqual(review.text, "paris")

    def test_review_inherits_from(self):
        self.assertTrue(issubclass(Review, BaseModel))

    """Test Erwan & Nathalie"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.review = Review()
        try:
            os.rename("file.json", "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """Class method to close test's environment"""
        try:
            os.remove("file.json")
            os.rename("test_file.json", "file.json")
        except Exception:
            pass

    def test_save_method(self):
        """Test case for 'save' method"""
        datetime_prev = self.review.updated_at
        self.review.save()
        self.assertGreater(self.review.updated_at, datetime_prev)
        self.assertTrue(os.path.exists("file.json"))

    def test_str_method(self):
        """Test case for str instance representation"""
        cls_name = str(self.review.__class__.__name__)
        obj_dict = str(self.review.__dict__)
        obj_str = "[{}] ({}) {}".format(cls_name, self.review.id, obj_dict)
        self.assertEqual(obj_str, self.review.__str__())

    def test_to_dict_method(self):
        """Test case for 'to_dict' method"""
        dict = {
            "id": self.review.id,
            "__class__": self.review.__class__.__name__,
            "created_at": self.review.created_at.isoformat(),
            "updated_at": self.review.updated_at.isoformat()
        }
        self.assertDictEqual(dict, self.review.to_dict())

    def test_instance_creation(self):
        obj = Review()
        self.assertIsInstance(obj, Review)

    def test_str_representation(self):
        obj = Review()
        obj_str = str(obj)
        self.assertTrue("[Review]" in obj_str)
        self.assertTrue(obj.id in obj_str)

    def test_to_dict_method(self):
        obj = Review()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'Review')
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)


if __name__ == "__main__":
    unittest.main()
