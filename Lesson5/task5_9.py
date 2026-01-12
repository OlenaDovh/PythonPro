from typing import Any


class DynamicProperties:
    """Defines a class that allows dynamic creation of properties"""

    def add_property(self, name: str, default_value: Any) -> None:
        """Adds a property to the class dynamically"""
        private_name = f"_{name}"
        setattr(self, private_name, default_value)

        def getter(instance: "DynamicProperties") -> Any:
            """Returns attribute info"""
            return getattr(instance, private_name)

        def setter(instance: "DynamicProperties", value: Any) -> None:
            """Sets attribute value            """
            setattr(instance, private_name, value)

        prop = property(getter, setter)

        setattr(self.__class__, name, prop)


obj = DynamicProperties()
obj.add_property('name', 'default_name')
print(obj.name)  # default_name
obj.name = "Python"
print(obj.name)  # Python
