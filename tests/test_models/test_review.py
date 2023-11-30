#!/usr/bin/python3
""" Review Unittests"""


from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models.user import User
from models.place import Place
from models.base_model import BaseModel
from models import storage


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
