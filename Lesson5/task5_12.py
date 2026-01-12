from typing import Any


class LoggingMeta(type):
    """Metaclass that automatically logs attribute access and modification."""

    def __new__(mcs, cls_name: str, bases: tuple, dct: dict) -> type:
        """Creates a new class with logging-enabled attribute access."""
        base_getattribute = dct.get("__getattribute__")
        base_setattr = dct.get("__setattr__")

        def __getattribute__(self, attr: str) -> Any:
            """Logs attribute access."""
            if not attr.startswith("_"):
                print(f"Logging: accessed '{attr}'")
            if base_getattribute:
                return base_getattribute(self, attr)
            return super(type(self), self).__getattribute__(attr)

        def __setattr__(self, attr: str, value: Any) -> None:
            """Logs attribute modification."""
            if not attr.startswith("_"):
                print(f"Logging: modified '{attr}'")
            if base_setattr:
                base_setattr(self, attr, value)
            else:
                super(type(self), self).__setattr__(attr, value)

        dct["__getattribute__"] = __getattribute__
        dct["__setattr__"] = __setattr__

        return super().__new__(mcs, cls_name, bases, dct)

class MyClass(metaclass=LoggingMeta):
    """Defines some test class"""

    def __init__(self, name: str) -> None:
        """Initializes the object with some input name"""
        self.name = name


obj = MyClass("Python")
print(obj.name)  # Logging: accessed 'name'
obj.name = "New Python"  # Logging: modified 'name'
