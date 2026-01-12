from typing import Callable, Any


def log_methods(cls: type) -> type:
    """Logs calls to all public methods of a class"""
    for attr_name, attr in cls.__dict__.items():
        if not attr_name.startswith("__"):
            setattr(cls, attr_name, _wrap_method(attr_name, attr))
    return cls


def _wrap_method(name: str, method: Callable) -> Callable:
    """Wraps a class method to log its invocation"""

    def wrapper(*args: Any, **kwargs: Any) -> Callable:
        """Wrapper function that logs the method call"""
        print(f"Logging: {name} called with {args[1:]}")
        return method(*args, **kwargs)

    return wrapper


@log_methods
class MyClass:
    """Defines some test class"""

    def add(self, a: int | float, b: int | float) -> int | float:
        """Returns result of sum operation with 2 input operands"""
        return a + b

    def subtract(self, a: int | float, b: int | float) -> int | float:
        """Returns result of substraction operation with 2 input operands"""
        return a - b


obj = MyClass()
obj.add(5, 3)  # Logging: add called with (5, 3)
obj.subtract(5, 3)  # Logging: subtract called with (5, 3)
