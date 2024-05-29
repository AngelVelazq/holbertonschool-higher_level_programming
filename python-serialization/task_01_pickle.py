import pickle
import io  # Import io to use StringIO


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, file_buffer):
        """
        Serialize the current instance to a file-like object.
        :param file_buffer: The file-like object to save the serialized object.
        """
        try:
            pickle.dump(self, file_buffer)
        except (pickle.PickleError) as e:
            print(f"An error occurred while serializing to the buffer: {e}")

    @classmethod
    def deserialize(cls, file_buffer):
        """Deserialize an instance from a file-like object.
        :param file_buffer: The file-like object to load the serialized object
        :return: An instance of CustomObject or None if error occurs."""
        try:
            file_buffer.seek(0)  # Move to the start of the buffer
            return pickle.load(file_buffer)
        except (pickle.PickleError) as e:
            print("An error occurred while deserializing from the buffer: "
                  f"{e}")
        return None


# Sample usage
if __name__ == "__main__":
    # Create an instance of CustomObject
    original_object = CustomObject("John", 25, True)

    # Display the original object
    print("Original Object:")
    original_object.display()

    # Create a StringIO buffer to simulate a file
    buffer = io.BytesIO()  # Use BytesIO to handle binary data

    # Serialize the object to the buffer
    original_object.serialize(buffer)

    # Deserialize the object from the buffer
    deserialized_object = CustomObject.deserialize(buffer)

    # Display the deserialized object
    if deserialized_object:
        print("\nDeserialized Object:")
        deserialized_object.display()
