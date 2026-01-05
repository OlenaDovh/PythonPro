import math
from typing import Self


class Vector:
    """
    Defines vectors and supports operations on them,
    such as addition, subtraction, multiplication, comparison
    """

    def __init__(self, x: int | float, y: int | float) -> None:
        """Creates a new vector using the input parameters numerator, denominator"""
        self.x = x
        self.y = y

    def __add__(self, other: Self) -> Self:
        """Returns a new vector as the sum of two input vectors"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        """Returns a new vector as the result of subtracting two input vectors"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number: int | float) -> Self:
        """Returns a new vector as the result of multiplying two input vectors"""
        return Vector(self.x * number, self.y * number)

    __rmul__ = __mul__

    def __lt__(self, other: Self) -> bool:
        """Returns true if the first input vector less than the second"""
        return self.get_length() < other.get_length()

    def __gt__(self, other: Self) -> bool:
        """Returns true if the first input vector greater than the second"""
        return self.get_length() > other.get_length()

    def __eq__(self, other: Self) -> bool:
        """Returns true if coordinates of both input vector are equal"""
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        """Returns human-readable string representation of an object"""
        return (f"Coordinate x = {self.x}, "
                f"coordinate y = {self.y}, vector length = {self.get_length()}")

    def __repr__(self) -> str:
        """Returns human-readable string representation of an object"""
        return (f"Coordinate x = {self.x}, "
                f"coordinate y = {self.y}, vector length = {self.get_length()}")

    def get_length(self) -> float:
        """Returns length of the input vector"""
        return math.hypot(self.x, self.y)


vector1 = Vector(3, 4)
vector2 = Vector(6, 8)
print(vector1, vector2, sep="\n")
assert (str(vector1)) == "Coordinate x = 3, coordinate y = 4, vector length = 5.0"
assert (str(vector2)) == "Coordinate x = 6, coordinate y = 8, vector length = 10.0"

vector3 = vector1 + vector2
print(vector3)
assert (str(vector3)) == "Coordinate x = 9, coordinate y = 12, vector length = 15.0"

vector4 = vector1 - vector2
print(vector4)
assert (str(vector4)) == "Coordinate x = -3, coordinate y = -4, vector length = 5.0"

vector5 = vector4 * 5
print(vector5)
assert (str(vector5)) == "Coordinate x = -15, coordinate y = -20, vector length = 25.0"

vector6 = Vector(3, 4)
assert vector3 > vector4
assert vector3 != vector4
assert vector1 == vector6
