#!/usr/bin/python3
'''model_class_student
'''


class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If `attrs` is a list of strings, only those attributes are returned.
        Otherwise, all attributes are returned.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes"""
        for key, value in json.items():
            setattr(self, key, value)
