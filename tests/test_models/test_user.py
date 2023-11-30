#!/usr/bin/python3
""" """


from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models.base_model import BaseModel
from models import storage
import os


class test_User(test_basemodel):
    """ """

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

    #-- OLD UNITTESTS--#

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

    #--New unittests--#

    def test_user_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_first_name(self):
        """ """
        new = User()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = User()
        self.assertEqual(type(new.last_name), str)

    def test_password(self):
        """ """
        new = User()
        self.assertEqual(type(new.password), str)

    def test_email(self):
        """ """
        new = User()
        self.assertEqual(type(new.email), str)

    def test_email_unique(self):
        # Test that email is unique
        user1 = User(email="test@example.com", password="password")
        user2 = User(email="test@example.com", password="password")
        self.assertNotEqual(user1.email, user2.email)

    def test_password_hashing(self):
        # Test that the password is properly hashed
        password = "secure_password"
        user = User(email="test@example.com", password=password)
        self.assertNotEqual(user.password, password)
        self.assertTrue(user.check_password(password))
