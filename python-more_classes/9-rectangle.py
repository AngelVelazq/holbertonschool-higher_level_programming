#!/usr/bin/python3
"""Defines a Rectangle class to handle rectangle properties, calculate area
and perimeter, compare instances based on area, and create square instances.
Manages instance lifecycle and custom visual representation."""


class Rectangle:
    """A class Rectangle that defines a rectangle and can also represent squares."""

    number_of_instances = 0  # Class attribute to track the number of instances
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle instance with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment the count of instances

    @property
    def width(self):
        """Retrieves the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the Rectangle.

        Returns:
            int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the Rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the Rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if either dimension is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns the string of the Rectangle using the print_symbol.

        Returns:
            str: The string of the rectangle, or an empty string if
            either dimension is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            line = "".join(str(self.print_symbol) for _ in range(self.__width))
            rect_str.append(line)
        return "\n".join(rect_str)

    def __repr__(self):
        """
        Returns the official string representation of the Rectangle.

        Returns:
            str: The string representation that can recreate the object.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Destructor to print a message when a Rectangle instance is deleted
        and decrement the instance counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement the count of instances

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles and returns the one with the larger area.
        Returns:
            Rectangle: The rectangle with the larger area,or first one if equal

        Raises:
            TypeError: If either is not an instance of Rectangle."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance where width and height are equal.

        Args:
            size (int): The size of the new square.

        Returns:
            Rectangle: A new rectangle instance with equal width and height."""
        return cls(size, size)
