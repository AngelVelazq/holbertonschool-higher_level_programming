import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file.
        :param filename: The name of the file to save the serialized object.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (IOError, pickle.PickleError) as e:
            print(f"An error occurred while serializing to the file: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an instance from a file.
        :param filename: The name of the file to load the serialized object
        :return: An instance of CustomObject or None if an error occurs."""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (IOError, pickle.PickleError) as e:
            print(f"An error occurred while deserializing from the file: {e}")
            return None


# Sample usage
if __name__ == "__main__":
    # Create an instance of CustomObject
    original_object = CustomObject("John", 25, True)

    # Display the original object
    print("Original Object:")
    original_object.display()

    # Serialize the object to a file
    original_object.serialize('custom_object.pkl')

    # Deserialize the object from the file
    deserialized_object = CustomObject.deserialize('custom_object.pkl')

    # Display the deserialized object
    if deserialized_object:
        print("\nDeserialized Object:")
        deserialized_object.display()
