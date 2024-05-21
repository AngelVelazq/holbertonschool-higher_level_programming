#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    A class that defines a rectangle by its width and height.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
        """Return the string of the rectangle using the '#' character"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for _ in range(self.__height):
            rect_str += "#" * self.__width + "\n"
        return rect_str.rstrip()

    def __repr__(self):
        """Return a string of the rectangle used to recreate the object."""
        return f"Rectangle({self.__width}, {self.__height})"


# Example Usage
if __name__ == "__main__":
    r1 = Rectangle(3, 4)
    print(r1)
    # Output:
    # ###
    # ###
    # ###
    # ###

    print(r1.area())  # Output: 12
    print(r1.perimeter())  # Output: 14

    r2 = Rectangle(0, 4)
    print(r2)
    # Output:
    # (empty string)

    print(r2.area())  # Output: 0
    print(r2.perimeter())  # Output: 0
