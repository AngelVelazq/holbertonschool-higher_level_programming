#!/usr/bin/env python3
"""
Module to serialize and deserialize custom objects
"""
import pickle
"""Module imported - primarily used in serializing
and deserializing a Python object structure."""


class CustomObject:
    """A class representing a custom object with attributes:
    name, age, and is_student."""

    def __init__(self, name, age, is_student):
        """Initializes a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the CustomObject instance.
        """
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """Serialize the CustomObject instance and save it to a file.

        Returns:
            bool: True if serialization is successful, False otherwise."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print("Serialization successful.")
            return True
        except Exception as e:
            print(f"Serialization failed: {e}")
            return False

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject instance from a file.

        Returns:
            CustomObject or None: The deserialized object...
            if successful, None otherwise."""
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            return obj
        except FileNotFoundError:
            print("File not found.")
            return None
        except pickle.UnpicklingError:
            print("Unpickling failed.")
            return None


# Example usage
if __name__ == "__main__":
    # Creating an instance of CustomObject
    obj = CustomObject("John", 25, True)

    # Displaying object attributes
    obj.display()

    # Serializing the object
    obj.serialize("custom_object.pkl")

    # Deserializing the object
    new_obj = CustomObject.deserialize("custom_object.pkl")
    if new_obj:
        print("\nDeserialized object:")
        new_obj.display()
