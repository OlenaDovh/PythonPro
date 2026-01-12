from typing import Any


def call_function(obj: object, method_name: str, *args: Any) -> Any:
    """Calls a method of an object by its name"""
    method = getattr(obj, method_name)

    if not callable(method):
        raise TypeError(f"Method '{method_name}' is not callable")
    return method(*args)


class Calculator:
    """Defines class calculator"""

    def add(self, a: int | float, b: int | float) -> int | float:
        """Returns result of sum operation with 2 input operands"""
        return a + b

    def subtract(self, a: int | float, b: int | float) -> int | float:
        """Returns result of substraction operation with 2 input operands"""
        return a - b


calc = Calculator()

print(call_function(calc, "add", 10, 5))  # 15
print(call_function(calc, "subtract", 10, 5))  # 5
