import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print("Serialization successful.")
        except Exception as e:
            print(f"Serialization failed: {e}")

    @classmethod
    def deserialize(cls, filename):
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
