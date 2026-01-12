class MutableClass:
    """Defines a class for dynamic modification of its attributes at runtime"""

    def add_attribute(self, name: str, value: str) -> None:
        """Adds an attribute to the object dynamically"""
        setattr(self, name, value)

    def remove_attribute(self, name: str) -> None:
        """Removes an attribute from the object dynamically """
        delattr(self, name)


obj = MutableClass()

obj.add_attribute("name", "Python")
print(obj.name)  # Python

obj.remove_attribute("name")
print(obj.name)  # Виникне помилка, атрибут видалений
