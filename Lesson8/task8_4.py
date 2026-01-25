import math


def is_even(n: int) -> bool:
    """
    Перевіряє, чи є число парним.
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    """
    return n % 2 == 0


def factorial(n: int) -> int:
    """
    Перевіряє значення факторіалу.
    >>> factorial(5)
    120
    >>> factorial(4)
    24
    >>> factorial(3)
    6
    >>> factorial(2)
    2
    >>> factorial(1)
    1
    >>> factorial(0)
    1
    """
    if not isinstance(n, int):
        raise TypeError("Digit must be a numeric value")
    return math.factorial(n)
