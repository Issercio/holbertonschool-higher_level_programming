#!/usr/bin/env python3
'''pickle
'''


import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance.

        Parameters:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current object and saves it to a file using pickle.

        Parameters:
        filename (str): The name of the file to save the serialized object.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file using pickle.

        Parameters:
        filename (str): The name of the file to load the serialized object from

        Returns:
        CustomObject or None The deserialized object,or None if an error occurs
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError) as e:
            print(
                "Deserialization error: "
                f"{e}"
            )
            return None
