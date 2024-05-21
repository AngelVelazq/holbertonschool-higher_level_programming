#!/usr/bin/python3
class Rectangle:
    """
    A class that defines a rectangle by its width and height.
    """

    number_of_instances = 0  # Public class attribute
    print_symbol = "#"  # Public class attribute

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Incremented during instantiation

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the string of the rectangle using print_symbol character."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for _ in range(self.__height):
            rect_str += str(self.print_symbol) * self.__width + "\n"
        return rect_str.rstrip()

    def __repr__(self):
        """Return a string of the rectangle used to recreate the object."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints the message when an instance of Rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        # Decremented during instance deletion
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)


# Example usage
if __name__ == "__main__":
    r1 = Rectangle(3, 4)
    r2 = Rectangle(2, 5)
    r3 = Rectangle(4, 4)

    print(r1)  # Should print the rectangle using '#'
    print(r2)  # Should print the rectangle using '#'
    print(f"Number of instances: {Rectangle.number_of_instances}")
    # Should print 3

    biggest = Rectangle.bigger_or_equal(r1, r2)
    print(f"The biggest rectangle is: {biggest}")

    biggest = Rectangle.bigger_or_equal(r1, r3)
    print(f"The biggest rectangle is: {biggest}")

    square_r = Rectangle.square(5)
    print(f"A square: {square_r}")

    del r1
    del r2
    del r3
    del square_r
    print(f"Number of instances: {Rectangle.number_of_instances}")
    # Should print 0
