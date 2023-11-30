#!/usr/bin/python3
"""This module defines a class User"""


from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel):
    """class defines a user with a various attributes"""
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
