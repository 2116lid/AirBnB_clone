#!/usr/bin/python3
""" Base model class for other classess """
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ Represents all other classess"""
    def __init__(self, *args, **kwargs):
        """ Initialize the BaseModel class """

        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """ Returns the string representation in the
        format [<class name>] (<self.id>) <self.__dict__> """

        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime"""

        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__
        of the instance"""

        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                val = self.__dict__[key].isoformat()
                dic[key] = val
        return dic
