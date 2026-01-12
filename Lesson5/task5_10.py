from typing import Any, Dict


class SingletonMeta(type):
    """Ensures only one instance of a class can be created"""

    _instances = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """
        Returns an instance of the class if it already exists.
        Otherwise, a new instance is created and stored
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """Defines test class that uses SingletonMeta to enforce a single instance"""

    def __init__(self) -> None:
        """Initializes the singleton instance"""
        print("Creating instance")


obj1 = Singleton()  # Creating instance
obj2 = Singleton()
print(obj1 is obj2)  # True
