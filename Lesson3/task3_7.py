import math
from numbers import Number
from typing import Self

import numpy as np


class SizeMismatchError(Exception):
    """Defines custom error"""


class Vector:
    """Defines vectors in an n-dimensional space"""

    def __init__(self, *coordinates) -> None:
        """Creates vector with input coordinators"""
        if not coordinates:
            raise ValueError("Vector has to have at least one coordinate")
        for coord in coordinates:
            if not isinstance(coord, Number):
                raise TypeError("Coordinates must be numeric values")

        self.coordinates = np.array(coordinates)

    def __add__(self, other: Self) -> Self:
        """Returns a new vector as the result of vector addition"""
        self._is_vector(other)
        self._is_vectors_same_size(other)
        return Vector(*(self.coordinates + other.coordinates))

    def __radd__(self, other: Self) -> Self:
        """Returns a new vector as the result of vector addition"""
        self._is_vector(other)
        return other.__add__(self)

    def __sub__(self, other: Self) -> Self:
        """Returns a new vector as the result of subtracting two vectors"""
        self._is_vector(other)
        self._is_vectors_same_size(other)
        return Vector(*(self.coordinates - other.coordinates))

    def __rsub__(self, other: Self) -> Self:
        """Returns a new vector as the result of subtracting two vectors"""
        self._is_vector(other)
        return other.__sub__(self)

    def __mul__(self, other: Self) -> np.ndarray:
        """Returns the scalar (dot) product of two vectors"""
        self._is_vector(other)
        self._is_vectors_same_size(other)
        return self.coordinates @ other.coordinates

    def length(self) -> float:
        """Gets the length of vector in an n-dimensional space"""
        return math.sqrt(sum(x * x for x in self.coordinates))

    def __lt__(self, other: Self) -> bool:
        """Returns true if the first input vector less than the second"""
        self._is_vector(other)
        return self.length() < other.length()

    def __eq__(self, other: Self) -> bool:
        """Returns true if coordinates of both input vector are equal"""
        self._is_vector(other)
        return self.length() == other.length()

    def __gt__(self, other: Self) -> bool:
        """Returns true if the first input vector greater than the second"""
        self._is_vector(other)
        return self.length() > other.length()

    def _is_vectors_same_size(self, other: Self) -> None:
        """Checks whether two vectors have the same number of coordinates"""
        if len(self.coordinates) != len(other.coordinates):
            raise SizeMismatchError("Vectors must have the same dimension")

    def _is_vector(self, other: Self) -> None:
        """Checks whether object is an instance of the Vector class"""
        if not isinstance(other, Vector):
            raise TypeError("Objects must be a Vector")

    def __str__(self) -> str:
        """Returns human-readable string representation of an object"""
        return f"Vector with coordinates {self.coordinates.tolist()}"


a = Vector(4, 5, 2, -4)
b = Vector(7, -3, 0, 3)
c = Vector(0, 0, 0, 0)
d = Vector(0.1, 0.2, 2.5, 5)
e = Vector(1, 8)

assert str(a + b) == 'Vector with coordinates [11, 2, 2, -1]'
assert str(a - b) == 'Vector with coordinates [-3, 8, 2, -7]'
assert a * b == 1
assert a * d == -13.6
assert str(b + d) == 'Vector with coordinates [7.1, -2.8, 2.5, 8.0]'
assert c * b == 0
print(a.length(), e.length())
assert a < e

try:
    f = Vector(1, 5.5, '8k')
    assert False
except (ValueError, TypeError) as ex:
    print(ex)

try:
    f = Vector()
    assert False
except (ValueError, TypeError) as ex:
    print(ex)

try:
    a * 5
    assert False
except TypeError as ex:
    print(ex)

try:
    7 + b
    assert False
except TypeError as ex:
    print(ex)

try:
    '7' - c
    assert False
except TypeError as ex:
    print(ex)

try:
    e + d
    assert False
except Exception as ex:
    print(ex)
