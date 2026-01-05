from math import gcd
from typing import Self


class Fraction:
    """Defines fractions and supports arithmetic operations with them"""

    def __init__(self, numerator: int, denominator: int) -> None:
        """Creates a new fraction using the input parameters numerator, denominator"""
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integer")
        if denominator == 0:
            raise ValueError("Denominator cannot be 0")
        g = gcd(numerator, denominator)
        self.numerator = numerator // g
        self.denominator = denominator // g

    def __add__(self, other: Self) -> Self:
        """Returns a new fraction as the sum of two input fractions"""
        denom = self.denominator
        numer1 = self.numerator
        numer2 = other.numerator
        if self.denominator != other.denominator:
            denom = self.denominator * other.denominator
            numer1 *= other.denominator
            numer2 *= self.denominator
        return Fraction(numer1 + numer2, denom)

    def __sub__(self, other: Self) -> Self:
        """Returns a new fraction as the result of subtracting two input fractions"""
        denom = self.denominator
        numer1 = self.numerator
        numer2 = other.numerator
        if self.denominator != other.denominator:
            denom = self.denominator * other.denominator
            numer1 *= other.denominator
            numer2 *= self.denominator
        return Fraction(numer1 - numer2, denom)

    def __mul__(self, other: Self) -> Self:
        """Returns a new fraction as the result of multiplying two input fractions"""
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other: Self) -> Self:
        """Returns a new fraction as the result of dividing two input fractions"""
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __str__(self) -> str:
        """Returns human-readable string representation of an object"""
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self) -> str:
        """Returns human-readable string representation of an object"""
        return f"{self.numerator}/{self.denominator}"


f_a = Fraction(7, 5)
f_b = Fraction(6, 10)
f_c = f_b + f_a
print(f_c)
assert str(f_c) == '2/1'

f_d = f_b * f_a
print(f_d)
assert str(f_d) == '21/25'

f_e = f_a - f_b
print(f_e)
assert str(f_e) == '4/5'

f_f = f_a / f_b
print(f_f)
assert str(f_f) == '7/3'

fraction = [f_f, f_e, f_d, f_c, f_b, f_a]
print(fraction)
assert repr(fraction) == "[7/3, 4/5, 21/25, 2/1, 3/5, 7/5]"

try:
    f_g = Fraction(5, 0)
except ValueError as e:
    print(e)
