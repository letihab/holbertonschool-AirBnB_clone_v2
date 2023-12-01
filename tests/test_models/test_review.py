#!/usr/bin/python3
""" Review Unittests"""


from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models.user import User
from models.place import Place
from models.base_model import BaseModel
from models import storage
import os
from unittest.mock import patch


class test_review(test_basemodel):
    """ Review unittests """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    #--New unittests--#
    """OLD"""

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

    def setUp(self):
        """Set up the testing environment"""
        self.review = Review()

    def tearDown(self):
        """Tear down the testing environment"""
        storage.close()

    def test_review_inherits_from_base_model(self):
        """Test if Review inherits from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_has_text_attribute(self):
        """Test if Review has 'text' attribute"""
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertIsInstance(self.review.text, str)

    def test_review_has_place_id_attribute(self):
        """Test if Review has 'place_id' attribute"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertIsInstance(self.review.place_id, str)

    def test_review_has_user_id_attribute(self):
        """Test if Review has 'user_id' attribute"""
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertIsInstance(self.review.user_id, str)

    @patch('models.storage')
    def test_review_save_method(self, mock_storage):
        """Test if Review has a 'save' method"""
        self.assertTrue(hasattr(self.review, 'save'))
        self.review.save()
        mock_storage.new.assert_called_once_with(self.review)
        mock_storage.save.assert_called_once()

    @patch('models.storage')
    def test_review_delete_method(self, mock_storage):
        """Test if Review has a 'delete' method"""
        self.assertTrue(hasattr(self.review, 'delete'))
        self.review.delete()
        mock_storage.delete.assert_called_once_with(self.review)

    """ new """

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.rev = Review()
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

    def setUp(self):
        """Set up the testing environment"""
        self.rev = Review()

    def tearDown(self):
        """Tear down the testing environment"""
        storage.close()

    def test_save_method(self):
        """Test case for 'save' method"""
        datetime_prev = self.rev.updated_at
        self.rev.save()
        self.assertGreater(self.rev.updated_at, datetime_prev)
        self.assertTrue(os.path.exists("file.json"))

    def test_str_method(self):
        """Test case for str instance representation"""
        cls_name = str(self.rev.__class__.__name__)
        obj_dict = str(self.rev.__dict__)
        obj_str = "[{}] ({}) {}".format(cls_name, self.rev.id, obj_dict)
        self.assertEqual(obj_str, self.rev.__str__())

    def test_to_dict_method(self):
        """Test case for 'to_dict' method"""
        model_dict = {
            "id": self.rev.id,
            "__class__": self.rev.__class__.__name__,
            "created_at": self.rev.created_at.isoformat(),
            "updated_at": self.rev.updated_at.isoformat()
        }
        self.assertDictEqual(model_dict, self.rev.to_dict())

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

    def test_review_inherits_from_base_model(self):
        """Test if Review inherits from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_has_text_attribute(self):
        """Test if Review has 'text' attribute"""
        self.assertTrue(hasattr(self.rev, 'text'))
        self.assertIsInstance(self.rev.text, str)

    def test_review_has_place_id_attribute(self):
        """Test if Review has 'place_id' attribute"""
        self.assertTrue(hasattr(self.rev, 'place_id'))
        self.assertIsInstance(self.rev.place_id, str)

    def test_review_has_user_id_attribute(self):
        """Test if Review has 'user_id' attribute"""
        self.assertTrue(hasattr(self.rev, 'user_id'))
        self.assertIsInstance(self.rev.user_id, str)

    @patch('models.storage')
    def test_review_save_method(self, mock_storage):
        """Test if Review has a 'save' method"""
        self.assertTrue(hasattr(self.rev, 'save'))
        self.rev.save()
        mock_storage.new.assert_called_once_with(self.rev)
        mock_storage.save.assert_called_once()

    @patch('models.storage')
    def test_review_delete_method(self, mock_storage):
        """Test if Review has a 'delete' method"""
        self.assertTrue(hasattr(self.rev, 'delete'))
        self.rev.delete()
        mock_storage.delete.assert_called_once_with(self.rev)

if __name__ == "__main__":
    test_basemodel.main()
