#!/usr/bin/python3

"""Defines a Magic Class matching exactly a bytecode provided by Holberton."""


import math


class MagicClass:
    """Represents a circle."""

    def __init__(self, radius=0):
        """Initializes a MagicsClass.

        Arg:
        radius (float or int): The radius of the new Magic Class.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the Magic Class."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns The circumference of the Magic Class."""
        return (2 * math.pi * self.__radius)
