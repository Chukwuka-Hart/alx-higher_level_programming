#!/usr/bin/python3
import json
import csv


class Base:
    """Represent the base model.

    Represents the "base" for the classes used in this project.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base instance.

        Args:
          id (int): The identity of the Base object. If id is passed,
                    it is set to this value. Otherwise, the id is set
                    to the number of instances.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON serialization of a python list of dicts.

        Args:
            list_dictionaries (dict): A list of dictionaries.

        Returns:
            If list_dictionary is empty or None - "[]".
            Otherwise - The JSON string representation of the list.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of Base inherited instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the deserialization of a JSON string.

        Args:
           json_string (str): A JSON str representation of a list of
                             dictionaries.

        Returns:
           If the JSON string is empty or None - an empty list.
           Otherwise - A python list of dictionaries retrieved from
                       json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance instantiated from a dictionary of attributes.

        Args:
           **dictionary (dict): A dictionary containing key/value pair to
                                instantiate an object.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a JSON file.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename) as f:
                json_string = f.read()
                list_dict = Base.from_json_string(json_string)
                list_instances = [cls.create(**d) for d in list_dict]
            return list_instances

        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldname = ["id", "width", "height", "x", "y"]
                else:
                    fieldname = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldname)
                writer.writeheader()
                list_dict = [o.to_dictionary() for o in list_objs]
                for d in list_dict:
                    writer.writerow(d)

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename) as csv_file:
                csv_dict = csv.DictReader(csv_file)
                list_dict = [dict((k, int(v)) for k, v in d.items())
                             for d in csv_dict]
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []
