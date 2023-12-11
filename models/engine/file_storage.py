#!/usr/bin/python3
""" A class that serializes and deserializes json
    file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ A class that serializes and deserializes json
    file to instances
    """

    __file_path = "file.json"
    __objects = {}

    CLASSES1 = {
            "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        """ returns the dictionary __objects """

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id """

        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        with open(self.__file_path, "w") as f:
            dic_storage = {}
            for key, val in self.__objects.items():
                dic_storage[key] = val.to_dict()
            json.dump(dic_storage, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """

        try:
            if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    base = FileStorage.CLASSES1[value["__class__"]](**value)
                    FileStorage.__objects[key] = base
        except FileNotFoundError:
            pass
