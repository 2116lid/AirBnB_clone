#!/usr/bin/python3
"""this module contains review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """represents review class"""
    place_id = ""
    user_id = ""
    text = ""
