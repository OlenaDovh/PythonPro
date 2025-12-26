"""
1) Write a function calculate_circle_area(radius) that:
Takes the radius of a circle.
Returns the area of a circle.
Use this function in a program that asks the user for a radius and prints out the area.
"""

import math

circle_radius = int(input("Enter radius of the circle\n"))

def calculate_circle_area(radius: int|float) -> float:
    """
    Returns the area of a circle based on the given radius
    """
    return math.pi * radius**2

print(calculate_circle_area(circle_radius))