"""
2) Create a Rectangle class that represents a rectangle.
Class requirements:
Class attributes:
width — the width of the rectangle.
height — the height of the rectangle.
Class methods:
__init__(self, width, height) — a constructor that accepts the width and height of the rectangle.
area(self) — a method that returns the area of the rectangle.
perimeter(self) — a method that returns the perimeter of the rectangle.
is_square(self) — a method that returns True if the rectangle is a square (the width is equal to the height),
otherwise False.
resize(self, new_width, new_height) — a method that changes the width and height of the rectangle.
Create an object of the Rectangle class and test all the methods.
"""


class Rectangle:
    def __init__(self, width: int|float, height: int|float):
        if width <= 0 or height <= 0:
            raise ValueError("Rectangle side cannot be equal to or less than 0")
        self.width = width
        self.height = height

    def area (self) -> int|float:
        """Returns the area of a rectangle by using its width and height"""
        return self.width * self.height

    def perimeter(self) -> int|float:
        """Returns the perimeter of a rectangle by using its width and height"""
        return 2 * (self.width + self.height)

    def is_square(self) -> int|float:
        """Checks whether rectangle is square or not"""
        return self.width == self.height

    def resize(self, new_width: int|float, new_height: int|float):
        """Sets new width and height values"""
        if new_width <= 0 or new_height <= 0:
            raise ValueError("Rectangle side cannot be equal to or less than 0")
        self.width = new_width
        self.height = new_height


try:
    Rectangle(0, 2)
except ValueError as e:
    print(e)

r1 = Rectangle(2, 4)

assert r1.area() == 8, 'Test1'
assert r1.perimeter() == 12, 'Test2'
assert r1.is_square() == False, 'Test3'

try:
    r1.resize(8,0)
except ValueError as e:
    print(e)

assert r1.width == 2 and r1.height == 4, 'Test4'

r1.resize(5, 5)
assert r1.width == 5 and r1.height == 5, 'Test5'
assert r1.is_square() == True, 'Test6'

print("OK")
