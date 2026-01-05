from typing import Self


class BinaryNumber:
    """Defines binary number and binary operations"""

    def __init__(self, number: int) -> None:
        """Creates binary number"""
        if not isinstance(number, int):
            raise TypeError("BinaryNumber expects int")
        self.number = number

    def __and__(self, other: Self) -> Self:
        """Returns new binary number as a result of binary operation AND"""
        return BinaryNumber(self.number & other.number)

    def __or__(self, other: Self) -> Self:
        """Returns new binary number as a result of binary operation OR"""
        return BinaryNumber(self.number | other.number)

    def __xor__(self, other: Self) -> Self:
        """Returns new binary number as a result of binary operation XOR"""
        return BinaryNumber(self.number ^ other.number)

    def __invert__(self) -> Self:
        """Returns new binary number as a result of binary operation NOT"""
        return BinaryNumber(~ self.number)

    def __str__(self) -> str:
        """Returns human-readable string representation of an object"""
        return bin(self.number)

    def __repr__(self) -> str:
        """Returns human-readable string representation of an object"""
        return bin(self.number)


binary1 = BinaryNumber(17)
binary2 = BinaryNumber(49)

try:
    binary3 = BinaryNumber("ds1")
except Exception as e:
    print(e)

print(f"binary1: {binary1}")
print(f"binary2: {binary2}")
print(f"AND: {binary1 & binary2}")
print(f"OR:  {binary1 | binary2}")
print(f"XOR: {binary1 ^ binary2}")
print(f"NOT: {~binary1}")

assert str(binary1) == '0b10001'
assert str(binary2) == '0b110001'
assert str(binary1 & binary2) == '0b10001'
assert str(binary1 | binary2) == '0b110001'
assert str(binary1 ^ binary2) == '0b100000'
assert str(~binary1) == '-0b10010'
