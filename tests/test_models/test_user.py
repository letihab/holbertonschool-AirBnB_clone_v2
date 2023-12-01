#!/usr/bin/python3
""" User unittests """


from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models.base_model import BaseModel
from models import storage
import os
from unittest.mock import patch
from sqlalchemy.orm import relationship
from models.review import Review
from models.place import Place


class test_User(test_basemodel):
    """ User unittests """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

    #--New unittests--#
    """OLD"""

    def test_user_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_in_storage(self):
        user = User()
        storage.save()
        key = "User.{}".format(user.id)
        self.assertEqual(key in storage.all(), True)

    def test_review_set_and_get_name(self):
        user = User()
        user.email = "1"
        user.password = "2"
        user.first_name = "3"
        user.last_name = "4"
        self.assertEqual(user.email, "1")
        self.assertEqual(user.password, "2")
        self.assertEqual(user.first_name, "3")
        self.assertEqual(user.last_name, "4")
        user.email = "5"
        user.password = "6"
        user.first_name = "7"
        user.last_name = "8"
        self.assertEqual(user.email, "5")
        self.assertEqual(user.password, "6")
        self.assertEqual(user.first_name, "7")
        self.assertEqual(user.last_name, "8")

    def test_user_inherits_from(self):
        self.assertTrue(issubclass(User, BaseModel))

    """Test Erwan & Nathalie"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.user = User()
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
        datetime_prev = self.user.updated_at
        self.user.save()
        self.assertGreater(self.user.updated_at, datetime_prev)
        self.assertTrue(os.path.exists("file.json"))

    def test_str_method(self):
        """Test case for str instance representation"""
        cls_name = str(self.user.__class__.__name__)
        obj_dict = str(self.user.__dict__)
        obj_str = "[{}] ({}) {}".format(cls_name, self.user.id, obj_dict)
        self.assertEqual(obj_str, self.user.__str__())

    def test_to_dict_method(self):
        """Test case for 'to_dict' method"""
        dict = {
            "id": self.user.id,
            "__class__": self.user.__class__.__name__,
            "created_at": self.user.created_at.isoformat(),
            "updated_at": self.user.updated_at.isoformat()
        }
        self.assertDictEqual(dict, self.user.to_dict())

    def test_instance_creation(self):
        obj = User()
        self.assertIsInstance(obj, User)

    def test_str_representation(self):
        obj = User()
        obj_str = str(obj)
        self.assertTrue("[User]" in obj_str)
        self.assertTrue(obj.id in obj_str)

    def test_to_dict_method(self):
        obj = User()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'User')
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)

    def setUp(self):
        """Set up the testing environment"""
        self.user = User()

    def tearDown(self):
        """Tear down the testing environment"""
        storage.close()

    def test_user_inherits_from_base_model(self):
        """Test if User inherits from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_has_email_attribute(self):
        """Test if User has 'email' attribute"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertIsInstance(self.user.email, str)

    def test_user_has_password_attribute(self):
        """Test if User has 'password' attribute"""
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertIsInstance(self.user.password, str)

    def test_user_has_first_name_attribute(self):
        """Test if User has 'first_name' attribute"""
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertIsInstance(self.user.first_name, str)

    def test_user_has_last_name_attribute(self):
        """Test if User has 'last_name' attribute"""
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertIsInstance(self.user.last_name, str)

    def test_user_has_places_relationship(self):
        """Test if User has a relationship with Place"""
        self.assertTrue(hasattr(User, 'places'))
        self.assertIsInstance(User.places.property, relationship)

    def test_user_has_reviews_relationship(self):
        """Test if User has a relationship with Review"""
        self.assertTrue(hasattr(User, 'reviews'))
        self.assertIsInstance(User.reviews.property, relationship)

    @patch('models.storage')
    def test_user_places_property(self, mock_storage):
        """Test User 'places' property"""
        user_places = self.user.places
        self.assertIsInstance(user_places, list)

    @patch('models.storage')
    def test_user_reviews_property(self, mock_storage):
        """Test User 'reviews' property"""
        user_reviews = self.user.reviews
        self.assertIsInstance(user_reviews, list)

    @patch('models.storage')
    def test_user_places_property_with_places(self, mock_storage):
        """Test User 'places' property with existing places"""
        with patch.dict(storage.all(Place), {'place1': Place(user_id=self.user.id),
                                             'place2': Place(user_id=self.user.id)}):
            user_places = self.user.places
            self.assertEqual(len(user_places), 2)
            self.assertIsInstance(user_places[0], Place)
            self.assertIsInstance(user_places[1], Place)

    @patch('models.storage')
    def test_user_reviews_property_with_reviews(self, mock_storage):
        """Test User 'reviews' property with existing reviews"""
        with patch.dict(storage.all(Review), {'review1': Review(user_id=self.user.id),
                                              'review2': Review(user_id=self.user.id)}):
            user_reviews = self.user.reviews
            self.assertEqual(len(user_reviews), 2)
            self.assertIsInstance(user_reviews[0], Review)
            self.assertIsInstance(user_reviews[1], Review)

    @patch('models.storage')
    def test_user_places_property_empty_list(self, mock_storage):
        """Test User 'places' property with an empty list"""
        user_places = self.user.places
        self.assertEqual(user_places, [])

    @patch('models.storage')
    def test_user_reviews_property_empty_list(self, mock_storage):
        """Test User 'reviews' property with an empty list"""
        user_reviews = self.user.reviews
        self.assertEqual(user_reviews, [])

    @patch('models.storage')
    def test_user_save_method(self, mock_storage):
        """Test if User has a 'save' method"""
        self.assertTrue(hasattr(self.user, 'save'))
        self.user.save()
        mock_storage.new.assert_called_once_with(self.user)
        mock_storage.save.assert_called_once()

    @patch('models.storage')
    def test_user_delete_method(self, mock_storage):
        """Test if User has a 'delete' method"""
        self.assertTrue(hasattr(self.user, 'delete'))
        self.user.delete()
        mock_storage.delete.assert_called_once_with(self.user)
