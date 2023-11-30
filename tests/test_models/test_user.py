#!/usr/bin/python3
""" User unittests """


from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models.base_model import BaseModel
from models import storage


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

    def test_user_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

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
