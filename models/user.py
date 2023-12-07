#!/usr/bin/python3
"""this module inherits from base class"""
from models.base_model import BaseModel


class User(BaseModel):
    """represents user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
