import math

circle_radius = int(input("Enter radius of the circle\n"))


def calculate_circle_area(radius: int | float) -> float:
    """
    Returns the area of a circle based on the given radius
    """
    return math.pi * radius ** 2


